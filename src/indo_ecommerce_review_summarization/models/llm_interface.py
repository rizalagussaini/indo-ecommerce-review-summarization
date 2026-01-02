"""
LLM Interface for Indonesian Review Summarization
==================================================

Generic interface for working with instruction-tuned LLMs.
"""

from typing import Optional, List, Dict, Any, Union
from abc import ABC, abstractmethod

try:
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
    HAS_TORCH = True
except ImportError:
    HAS_TORCH = False
    torch = None


class LLMInterface(ABC):
    """
    Abstract base class for LLM interfaces.
    """
    
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate text from a prompt.
        
        Args:
            prompt: Input prompt
            **kwargs: Additional generation parameters
            
        Returns:
            Generated text
        """
        pass
    
    @abstractmethod
    def batch_generate(self, prompts: List[str], **kwargs) -> List[str]:
        """
        Generate text from multiple prompts.
        
        Args:
            prompts: List of input prompts
            **kwargs: Additional generation parameters
            
        Returns:
            List of generated texts
        """
        pass


class HuggingFaceLLM(LLMInterface):
    """
    Interface for Hugging Face transformers models.
    """
    
    def __init__(
        self,
        model_name: str,
        device: Optional[str] = None,
        load_in_8bit: bool = False,
        load_in_4bit: bool = False,
        torch_dtype: Optional[Any] = None
    ):
        """
        Initialize the Hugging Face LLM.
        
        Args:
            model_name: Name of the model on Hugging Face Hub
            device: Device to load model on ('cuda', 'cpu', or None for auto)
            load_in_8bit: Load model in 8-bit precision
            load_in_4bit: Load model in 4-bit precision
            torch_dtype: Torch dtype for model weights
        """
        if not HAS_TORCH:
            raise ImportError(
                "PyTorch and transformers are required for HuggingFaceLLM. "
                "Install them with: pip install torch transformers"
            )
        
        self.model_name = model_name
        
        # Determine device
        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device
        
        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        
        # Prepare model loading kwargs
        model_kwargs = {}
        if torch_dtype:
            model_kwargs['torch_dtype'] = torch_dtype
        if load_in_8bit:
            model_kwargs['load_in_8bit'] = True
        elif load_in_4bit:
            model_kwargs['load_in_4bit'] = True
        else:
            model_kwargs['device_map'] = self.device
        
        # Load model
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            **model_kwargs
        )
        
        # Create pipeline
        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=self.device if not (load_in_8bit or load_in_4bit) else None
        )
    
    def generate(
        self,
        prompt: str,
        max_new_tokens: int = 256,
        temperature: float = 0.7,
        top_p: float = 0.9,
        top_k: int = 50,
        do_sample: bool = True,
        **kwargs
    ) -> str:
        """
        Generate text from a prompt.
        
        Args:
            prompt: Input prompt
            max_new_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature
            top_p: Nucleus sampling parameter
            top_k: Top-k sampling parameter
            do_sample: Whether to use sampling
            **kwargs: Additional generation parameters
            
        Returns:
            Generated text
        """
        output = self.pipe(
            prompt,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            do_sample=do_sample,
            return_full_text=False,
            **kwargs
        )
        
        return output[0]['generated_text'].strip()
    
    def batch_generate(
        self,
        prompts: List[str],
        max_new_tokens: int = 256,
        temperature: float = 0.7,
        top_p: float = 0.9,
        top_k: int = 50,
        do_sample: bool = True,
        batch_size: int = 4,
        **kwargs
    ) -> List[str]:
        """
        Generate text from multiple prompts.
        
        Args:
            prompts: List of input prompts
            max_new_tokens: Maximum number of tokens to generate
            temperature: Sampling temperature
            top_p: Nucleus sampling parameter
            top_k: Top-k sampling parameter
            do_sample: Whether to use sampling
            batch_size: Batch size for generation
            **kwargs: Additional generation parameters
            
        Returns:
            List of generated texts
        """
        results = []
        
        for i in range(0, len(prompts), batch_size):
            batch = prompts[i:i+batch_size]
            outputs = self.pipe(
                batch,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                do_sample=do_sample,
                return_full_text=False,
                batch_size=len(batch),
                **kwargs
            )
            
            for output in outputs:
                results.append(output[0]['generated_text'].strip())
        
        return results


def load_model(
    model_name: str,
    model_type: str = "huggingface",
    **kwargs
) -> LLMInterface:
    """
    Load an LLM model.
    
    Args:
        model_name: Name or path of the model
        model_type: Type of model interface ('huggingface')
        **kwargs: Additional arguments for model initialization
        
    Returns:
        LLM interface instance
    """
    if model_type == "huggingface":
        return HuggingFaceLLM(model_name, **kwargs)
    else:
        raise ValueError(f"Unknown model type: {model_type}")

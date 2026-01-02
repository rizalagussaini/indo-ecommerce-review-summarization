"""
Prompt Templates for Indonesian E-commerce Review Summarization
================================================================

Provides prompt templates for instruction-tuned LLMs.
"""

from typing import Dict, Optional, List


# Prompt templates for different models
PROMPT_TEMPLATES = {
    "mistral": {
        "system": "Anda adalah asisten AI yang ahli dalam merangkum ulasan e-commerce dalam Bahasa Indonesia.",
        "instruction": "[INST] {system}\n\n{user_input} [/INST]",
    },
    "llama": {
        "system": "You are a helpful assistant that specializes in summarizing Indonesian e-commerce reviews.",
        "instruction": "<s>[INST] <<SYS>>\n{system}\n<</SYS>>\n\n{user_input} [/INST]",
    },
    "generic": {
        "system": "You are an AI assistant that summarizes Indonesian e-commerce reviews.",
        "instruction": "{system}\n\nUser: {user_input}\nAssistant:",
    },
    "indonesian": {
        "system": "Anda adalah asisten yang membantu merangkum ulasan produk e-commerce dalam Bahasa Indonesia.",
        "instruction": "### Instruksi:\n{system}\n\n### Input:\n{user_input}\n\n### Respon:",
    }
}


def create_summarization_prompt(
    reviews: List[str],
    model_type: str = "mistral",
    custom_instruction: Optional[str] = None,
    max_length: Optional[int] = None
) -> str:
    """
    Create a prompt for summarizing Indonesian e-commerce reviews.
    
    Args:
        reviews: List of review texts to summarize
        model_type: Type of model ('mistral', 'llama', 'generic', 'indonesian')
        custom_instruction: Custom instruction to override default
        max_length: Maximum length of summary in words (optional)
        
    Returns:
        Formatted prompt string
        
    Examples:
        >>> reviews = ["Barang bagus", "Pengiriman cepat"]
        >>> prompt = create_summarization_prompt(reviews, model_type="mistral")
    """
    if model_type not in PROMPT_TEMPLATES:
        raise ValueError(f"Unknown model type: {model_type}. Choose from {list(PROMPT_TEMPLATES.keys())}")
    
    template = PROMPT_TEMPLATES[model_type]
    
    # Create review list text
    if len(reviews) == 1:
        reviews_text = f"Ulasan:\n{reviews[0]}"
    else:
        reviews_text = "Ulasan-ulasan:\n" + "\n".join([f"{i+1}. {rev}" for i, rev in enumerate(reviews)])
    
    # Create instruction
    if custom_instruction:
        instruction = custom_instruction
    else:
        instruction = "Buatlah ringkasan dari ulasan produk berikut dalam Bahasa Indonesia yang natural dan informatif."
        if max_length:
            instruction += f" Ringkasan maksimal {max_length} kata."
    
    # Combine instruction and reviews
    user_input = f"{instruction}\n\n{reviews_text}"
    
    # Format according to template
    prompt = template["instruction"].format(
        system=template["system"],
        user_input=user_input
    )
    
    return prompt


def create_multi_review_prompt(
    reviews: List[str],
    model_type: str = "mistral",
    focus_aspects: Optional[List[str]] = None
) -> str:
    """
    Create a prompt for summarizing multiple reviews with optional focus aspects.
    
    Args:
        reviews: List of review texts
        model_type: Type of model
        focus_aspects: Optional list of aspects to focus on (e.g., ['kualitas', 'pengiriman'])
        
    Returns:
        Formatted prompt string
    """
    if model_type not in PROMPT_TEMPLATES:
        raise ValueError(f"Unknown model type: {model_type}")
    
    template = PROMPT_TEMPLATES[model_type]
    
    # Create instruction
    instruction = "Buatlah ringkasan dari ulasan-ulasan produk berikut dalam Bahasa Indonesia."
    
    if focus_aspects:
        aspects_text = ", ".join(focus_aspects)
        instruction += f" Fokus pada aspek: {aspects_text}."
    
    # Format reviews
    reviews_text = "\n".join([f"Ulasan {i+1}: {rev}" for i, rev in enumerate(reviews)])
    
    user_input = f"{instruction}\n\n{reviews_text}"
    
    prompt = template["instruction"].format(
        system=template["system"],
        user_input=user_input
    )
    
    return prompt


def create_aspect_based_prompt(
    reviews: List[str],
    aspects: List[str],
    model_type: str = "mistral"
) -> str:
    """
    Create a prompt for aspect-based summarization.
    
    Args:
        reviews: List of review texts
        aspects: List of aspects to summarize (e.g., ['kualitas produk', 'harga', 'pengiriman'])
        model_type: Type of model
        
    Returns:
        Formatted prompt string
    """
    if model_type not in PROMPT_TEMPLATES:
        raise ValueError(f"Unknown model type: {model_type}")
    
    template = PROMPT_TEMPLATES[model_type]
    
    aspects_text = ", ".join(aspects)
    instruction = f"Buatlah ringkasan dari ulasan-ulasan berikut untuk setiap aspek: {aspects_text}"
    
    reviews_text = "\n".join([f"Ulasan {i+1}: {rev}" for i, rev in enumerate(reviews)])
    
    user_input = f"{instruction}\n\n{reviews_text}"
    
    prompt = template["instruction"].format(
        system=template["system"],
        user_input=user_input
    )
    
    return prompt

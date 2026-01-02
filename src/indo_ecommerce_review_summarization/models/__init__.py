"""
Models Module
=============

LLM interfaces and prompt templates for instruction-tuned models.
"""

from .llm_interface import LLMInterface
from .prompt_templates import create_summarization_prompt, PROMPT_TEMPLATES

__all__ = [
    "LLMInterface",
    "create_summarization_prompt",
    "PROMPT_TEMPLATES",
]

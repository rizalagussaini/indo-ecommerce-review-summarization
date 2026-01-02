"""
Tests for prompt templates.
"""

import pytest
from indo_ecommerce_review_summarization.models import (
    create_summarization_prompt,
    create_multi_review_prompt,
    PROMPT_TEMPLATES
)


def test_prompt_templates_exist():
    """Test that all prompt templates exist."""
    assert 'mistral' in PROMPT_TEMPLATES
    assert 'llama' in PROMPT_TEMPLATES
    assert 'generic' in PROMPT_TEMPLATES
    assert 'indonesian' in PROMPT_TEMPLATES


def test_create_summarization_prompt_mistral():
    """Test Mistral prompt creation."""
    reviews = ["Barang bagus"]
    prompt = create_summarization_prompt(reviews, model_type="mistral")
    
    assert isinstance(prompt, str)
    assert len(prompt) > 0
    assert "[INST]" in prompt
    assert "Barang bagus" in prompt


def test_create_summarization_prompt_multiple_reviews():
    """Test prompt creation with multiple reviews."""
    reviews = ["Review 1", "Review 2", "Review 3"]
    prompt = create_summarization_prompt(reviews, model_type="mistral")
    
    assert "Review 1" in prompt
    assert "Review 2" in prompt
    assert "Review 3" in prompt


def test_create_summarization_prompt_max_length():
    """Test prompt with max length specification."""
    reviews = ["Barang bagus"]
    prompt = create_summarization_prompt(reviews, model_type="mistral", max_length=50)
    
    assert "50" in prompt


def test_create_summarization_prompt_custom_instruction():
    """Test prompt with custom instruction."""
    reviews = ["Barang bagus"]
    custom = "Ringkas ulasan ini"
    prompt = create_summarization_prompt(
        reviews,
        model_type="mistral",
        custom_instruction=custom
    )
    
    assert custom in prompt


def test_create_multi_review_prompt():
    """Test multi-review prompt creation."""
    reviews = ["Review 1", "Review 2"]
    prompt = create_multi_review_prompt(reviews, model_type="mistral")
    
    assert isinstance(prompt, str)
    assert "Review 1" in prompt
    assert "Review 2" in prompt


def test_create_multi_review_prompt_with_aspects():
    """Test multi-review prompt with focus aspects."""
    reviews = ["Review 1"]
    aspects = ["kualitas", "pengiriman"]
    prompt = create_multi_review_prompt(
        reviews,
        model_type="mistral",
        focus_aspects=aspects
    )
    
    assert "kualitas" in prompt
    assert "pengiriman" in prompt


def test_create_prompt_invalid_model_type():
    """Test error handling for invalid model type."""
    reviews = ["Test"]
    
    with pytest.raises(ValueError):
        create_summarization_prompt(reviews, model_type="invalid_model")

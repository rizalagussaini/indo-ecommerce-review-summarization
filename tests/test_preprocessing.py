"""
Tests for text cleaning and preprocessing utilities.
"""

import pytest
from indo_ecommerce_review_summarization.preprocessing import (
    clean_text,
    normalize_text,
    preprocess_review
)


def test_clean_text_basic():
    """Test basic text cleaning."""
    text = "Barang bagus bgt!!!   "
    result = clean_text(text)
    assert result == "Barang bagus bgt!!!"
    assert result.strip() == result


def test_clean_text_url_removal():
    """Test URL removal."""
    text = "Barang bagus http://example.com"
    result = clean_text(text)
    assert "http://example.com" not in result
    assert "Barang bagus" in result


def test_clean_text_email_removal():
    """Test email removal."""
    text = "Hubungi saya di test@example.com"
    result = clean_text(text)
    assert "test@example.com" not in result


def test_normalize_text_lowercase():
    """Test lowercase normalization."""
    text = "Barang BAGUS Sekali"
    result = normalize_text(text, lowercase=True)
    assert result == "barang bagus sekali"


def test_normalize_text_punctuation():
    """Test punctuation removal."""
    text = "Barang bagus!!!"
    result = normalize_text(text, remove_punctuation=True)
    assert result == "barang bagus"


def test_preprocess_review():
    """Test complete preprocessing pipeline."""
    text = "Barang BAGUS bgt!!! http://example.com"
    result = preprocess_review(text, clean=True, normalize=True, lowercase=True)
    assert "http://example.com" not in result
    assert result.islower()


def test_clean_text_empty():
    """Test cleaning empty text."""
    assert clean_text("") == ""
    assert clean_text(None) == ""


def test_normalize_text_empty():
    """Test normalizing empty text."""
    assert normalize_text("") == ""
    assert normalize_text(None) == ""

"""
Text Cleaning and Normalization for Indonesian E-commerce Reviews
==================================================================

Provides utilities to clean and normalize informal Indonesian text
commonly found in e-commerce reviews.
"""

import re
import html
from typing import Optional


def clean_text(text: str) -> str:
    """
    Clean Indonesian e-commerce review text.
    
    This function performs basic cleaning operations:
    - Decodes HTML entities
    - Removes URLs
    - Removes email addresses
    - Removes excessive whitespace
    - Removes special characters (optional, preserves common punctuation)
    
    Args:
        text: Raw review text
        
    Returns:
        Cleaned text
        
    Examples:
        >>> clean_text("Barang bagus bgt!!!! 😊 http://example.com")
        'Barang bagus bgt!!!! 😊'
    """
    if not text or not isinstance(text, str):
        return ""
    
    # Decode HTML entities
    text = html.unescape(text)
    
    # Remove URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    return text


def normalize_text(text: str, lowercase: bool = True, remove_punctuation: bool = False) -> str:
    """
    Normalize Indonesian text.
    
    Args:
        text: Text to normalize
        lowercase: Convert text to lowercase
        remove_punctuation: Remove punctuation marks
        
    Returns:
        Normalized text
        
    Examples:
        >>> normalize_text("Barang BAGUS sekali!!!")
        'barang bagus sekali!!!'
        >>> normalize_text("Barang BAGUS sekali!!!", remove_punctuation=True)
        'barang bagus sekali'
    """
    if not text or not isinstance(text, str):
        return ""
    
    # Convert to lowercase
    if lowercase:
        text = text.lower()
    
    # Remove punctuation if requested
    if remove_punctuation:
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', ' ', text)
    
    return text.strip()


def preprocess_review(
    text: str,
    clean: bool = True,
    normalize: bool = True,
    lowercase: bool = True,
    remove_punctuation: bool = False
) -> str:
    """
    Complete preprocessing pipeline for a review.
    
    Args:
        text: Raw review text
        clean: Apply cleaning
        normalize: Apply normalization
        lowercase: Convert to lowercase
        remove_punctuation: Remove punctuation marks
        
    Returns:
        Preprocessed text
        
    Examples:
        >>> preprocess_review("Barang BAGUS bgt!!! 😊 http://example.com")
        'barang bagus bgt!!! 😊'
    """
    if clean:
        text = clean_text(text)
    
    if normalize:
        text = normalize_text(text, lowercase=lowercase, remove_punctuation=remove_punctuation)
    
    return text

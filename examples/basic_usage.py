"""
Example Script: Basic Usage of Indonesian E-commerce Review Summarization
==========================================================================

This script demonstrates basic usage of the library without requiring GPU/LLM.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from indo_ecommerce_review_summarization.preprocessing import (
    clean_text,
    normalize_text,
    preprocess_review
)
from indo_ecommerce_review_summarization.models import (
    create_summarization_prompt,
    PROMPT_TEMPLATES
)
from indo_ecommerce_review_summarization.utils import setup_logger


def main():
    # Setup logger
    logger = setup_logger('example', log_file=None)
    logger.info("Starting example script...")
    
    # Example 1: Text Cleaning
    logger.info("\n" + "="*80)
    logger.info("Example 1: Text Cleaning and Normalization")
    logger.info("="*80)
    
    raw_review = """
    Barang bagus bgt!!!! 😊 
    Pengiriman cepet bgt cuma 2 hari. 
    Check website: http://example.com
    Contact: seller@example.com
    """
    
    print(f"\nOriginal Review:\n{raw_review}")
    
    # Clean the text
    cleaned = clean_text(raw_review)
    print(f"\nCleaned Review:\n{cleaned}")
    
    # Normalize
    normalized = normalize_text(cleaned, lowercase=True)
    print(f"\nNormalized Review:\n{normalized}")
    
    # Complete preprocessing
    processed = preprocess_review(raw_review, clean=True, normalize=True, lowercase=True)
    print(f"\nFully Processed Review:\n{processed}")
    
    # Example 2: Prompt Creation
    logger.info("\n" + "="*80)
    logger.info("Example 2: Creating Prompts for Different Models")
    logger.info("="*80)
    
    reviews = [
        "Barang bagus, pengiriman cepat, seller responsif.",
        "Kualitas oke, harga terjangkau.",
    ]
    
    print(f"\nReviews to summarize:")
    for i, review in enumerate(reviews, 1):
        print(f"{i}. {review}")
    
    # Create prompts for different model types
    for model_type in PROMPT_TEMPLATES.keys():
        print(f"\n--- {model_type.upper()} Prompt ---")
        prompt = create_summarization_prompt(
            reviews=reviews,
            model_type=model_type,
            max_length=50
        )
        # Show first 200 chars
        print(prompt[:200] + "..." if len(prompt) > 200 else prompt)
    
    # Example 3: Data Processing Pipeline
    logger.info("\n" + "="*80)
    logger.info("Example 3: Complete Data Processing Pipeline")
    logger.info("="*80)
    
    sample_reviews = [
        "Produk SANGAT BAGUS!!! Pengiriman SUPER CEPAT http://link.com",
        "harga murah, kualitas mantap. recommended!!!",
        "seller responsif, barang ORI. packing rapi bgt 👍",
    ]
    
    print("\nProcessing multiple reviews...")
    processed_reviews = []
    
    for i, review in enumerate(sample_reviews, 1):
        processed = preprocess_review(
            review,
            clean=True,
            normalize=True,
            lowercase=True,
            remove_punctuation=False
        )
        processed_reviews.append(processed)
        print(f"\nReview {i}:")
        print(f"  Original:  {review}")
        print(f"  Processed: {processed}")
    
    # Create a batch prompt
    print("\n--- Creating Batch Prompt ---")
    batch_prompt = create_summarization_prompt(
        reviews=processed_reviews,
        model_type="mistral"
    )
    print(f"Prompt length: {len(batch_prompt)} characters")
    print(f"Ready for model inference!")
    
    logger.info("\n" + "="*80)
    logger.info("Example script completed successfully!")
    logger.info("="*80)
    logger.info("\nNext steps:")
    logger.info("1. Check out the Jupyter notebooks in notebooks/")
    logger.info("2. Try the preprocessing script: python scripts/preprocess_reviews.py")
    logger.info("3. If you have a GPU, try generating summaries with Mistral-7B-Instruct")


if __name__ == "__main__":
    main()

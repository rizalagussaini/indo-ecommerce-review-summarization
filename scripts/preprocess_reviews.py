"""
Preprocessing Script for Indonesian E-commerce Reviews
========================================================

This script demonstrates how to preprocess raw review data.

Usage:
    python preprocess_reviews.py --input data/raw/reviews.json --output data/processed/reviews_clean.json
"""

import sys
import argparse
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from indo_ecommerce_review_summarization.preprocessing import (
    load_reviews,
    save_processed_data,
    preprocess_review
)
from indo_ecommerce_review_summarization.utils import setup_logger


def main():
    parser = argparse.ArgumentParser(description='Preprocess Indonesian e-commerce reviews')
    parser.add_argument('--input', type=str, required=True, help='Input file path')
    parser.add_argument('--output', type=str, required=True, help='Output file path')
    parser.add_argument('--lowercase', action='store_true', help='Convert to lowercase')
    parser.add_argument('--remove-punctuation', action='store_true', help='Remove punctuation')
    parser.add_argument('--format', type=str, default='auto', 
                        choices=['auto', 'json', 'jsonl', 'csv'],
                        help='File format')
    
    args = parser.parse_args()
    
    # Setup logger
    logger = setup_logger('preprocess_reviews')
    
    logger.info(f"Loading reviews from {args.input}")
    reviews = load_reviews(args.input, file_format=args.format)
    logger.info(f"Loaded {len(reviews)} reviews")
    
    # Preprocess reviews
    logger.info("Preprocessing reviews...")
    processed_reviews = []
    
    for review in reviews:
        # Preprocess the review text
        if 'review' in review:
            review['review_original'] = review['review']
            review['review'] = preprocess_review(
                review['review'],
                clean=True,
                normalize=True,
                lowercase=args.lowercase,
                remove_punctuation=args.remove_punctuation
            )
        
        # Also preprocess summary if present
        if 'summary' in review:
            review['summary_original'] = review['summary']
            review['summary'] = preprocess_review(
                review['summary'],
                clean=True,
                normalize=True,
                lowercase=args.lowercase,
                remove_punctuation=args.remove_punctuation
            )
        
        processed_reviews.append(review)
    
    # Save processed data
    logger.info(f"Saving processed reviews to {args.output}")
    save_processed_data(processed_reviews, args.output, file_format=args.format)
    
    logger.info("Preprocessing complete!")
    logger.info(f"Processed {len(processed_reviews)} reviews")


if __name__ == '__main__':
    main()

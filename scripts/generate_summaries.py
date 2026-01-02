"""
Generate Summaries Script
==========================

Generate summaries for Indonesian e-commerce reviews using an LLM.

Usage:
    python generate_summaries.py --input data/reviews.json --output results/summaries.json --model mistralai/Mistral-7B-Instruct-v0.2
"""

import sys
import argparse
from pathlib import Path
from tqdm import tqdm

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from indo_ecommerce_review_summarization.preprocessing import load_reviews
from indo_ecommerce_review_summarization.models import (
    load_model,
    create_summarization_prompt
)
from indo_ecommerce_review_summarization.utils import setup_logger, save_json


def main():
    parser = argparse.ArgumentParser(description='Generate summaries using LLM')
    parser.add_argument('--input', type=str, required=True,
                        help='Input file with reviews')
    parser.add_argument('--output', type=str, required=True,
                        help='Output file for summaries')
    parser.add_argument('--model', type=str, required=True,
                        help='Model name or path')
    parser.add_argument('--model-type', type=str, default='mistral',
                        choices=['mistral', 'llama', 'generic', 'indonesian'],
                        help='Model type for prompt template')
    parser.add_argument('--review-field', type=str, default='review',
                        help='Field name for review text in JSON')
    parser.add_argument('--max-new-tokens', type=int, default=128,
                        help='Maximum tokens to generate')
    parser.add_argument('--temperature', type=float, default=0.7,
                        help='Sampling temperature')
    parser.add_argument('--load-in-4bit', action='store_true',
                        help='Load model in 4-bit quantization')
    parser.add_argument('--load-in-8bit', action='store_true',
                        help='Load model in 8-bit quantization')
    parser.add_argument('--batch-size', type=int, default=4,
                        help='Batch size for generation')
    
    args = parser.parse_args()
    
    # Setup logger
    logger = setup_logger('generate_summaries')
    
    # Load reviews
    logger.info(f"Loading reviews from {args.input}")
    reviews = load_reviews(args.input)
    logger.info(f"Loaded {len(reviews)} reviews")
    
    # Load model
    logger.info(f"Loading model {args.model}")
    model = load_model(
        model_name=args.model,
        model_type='huggingface',
        load_in_4bit=args.load_in_4bit,
        load_in_8bit=args.load_in_8bit
    )
    logger.info("Model loaded successfully!")
    
    # Generate summaries
    logger.info("Generating summaries...")
    results = []
    
    for review_data in tqdm(reviews, desc="Processing reviews"):
        review_text = review_data.get(args.review_field, '')
        
        if not review_text:
            logger.warning(f"Empty review for item {review_data.get('id', 'unknown')}")
            continue
        
        # Create prompt
        prompt = create_summarization_prompt(
            reviews=[review_text],
            model_type=args.model_type
        )
        
        # Generate summary
        summary = model.generate(
            prompt,
            max_new_tokens=args.max_new_tokens,
            temperature=args.temperature
        )
        
        # Store result
        result = {
            **review_data,
            'generated_summary': summary,
            'model': args.model,
            'model_type': args.model_type
        }
        results.append(result)
    
    # Save results
    logger.info(f"Saving results to {args.output}")
    save_json(results, args.output)
    
    logger.info(f"Successfully generated {len(results)} summaries!")


if __name__ == '__main__':
    main()

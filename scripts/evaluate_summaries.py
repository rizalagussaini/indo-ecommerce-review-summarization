"""
Evaluate Summarization Script
==============================

Evaluate generated summaries against reference summaries using ROUGE metrics.

Usage:
    python evaluate_summaries.py --predictions predictions.json --references references.json
"""

import sys
import argparse
import json
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from indo_ecommerce_review_summarization.evaluation import (
    evaluate_predictions,
    format_rouge_scores
)
from indo_ecommerce_review_summarization.utils import setup_logger, load_json


def main():
    parser = argparse.ArgumentParser(description='Evaluate summarization with ROUGE metrics')
    parser.add_argument('--predictions', type=str, required=True, 
                        help='File containing predictions')
    parser.add_argument('--references', type=str, required=True,
                        help='File containing references')
    parser.add_argument('--pred-field', type=str, default='summary',
                        help='Field name for predictions in JSON')
    parser.add_argument('--ref-field', type=str, default='summary',
                        help='Field name for references in JSON')
    parser.add_argument('--output', type=str, default=None,
                        help='Optional output file for results')
    
    args = parser.parse_args()
    
    # Setup logger
    logger = setup_logger('evaluate_summaries')
    
    # Load predictions
    logger.info(f"Loading predictions from {args.predictions}")
    pred_data = load_json(args.predictions)
    
    # Load references
    logger.info(f"Loading references from {args.references}")
    ref_data = load_json(args.references)
    
    # Extract summaries
    if isinstance(pred_data, list):
        predictions = [item[args.pred_field] for item in pred_data]
    else:
        predictions = [pred_data[args.pred_field]]
    
    if isinstance(ref_data, list):
        references = [item[args.ref_field] for item in ref_data]
    else:
        references = [ref_data[args.ref_field]]
    
    logger.info(f"Evaluating {len(predictions)} predictions")
    
    # Evaluate
    scores = evaluate_predictions(predictions, references)
    
    # Display results
    logger.info("Evaluation Results:")
    print("\n" + "="*80)
    print(format_rouge_scores(scores))
    print("="*80 + "\n")
    
    # Save results if output specified
    if args.output:
        logger.info(f"Saving results to {args.output}")
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(scores, f, indent=2, ensure_ascii=False)
    
    logger.info("Evaluation complete!")


if __name__ == '__main__':
    main()

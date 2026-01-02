"""
ROUGE Metrics for Evaluation
=============================

Calculate ROUGE scores for evaluating abstractive summarization.
"""

from typing import Dict, List, Union, Optional
import numpy as np

try:
    from rouge_score import rouge_scorer
    from rouge_score.scoring import BootstrapAggregator
    HAS_ROUGE = True
except ImportError:
    HAS_ROUGE = False


def calculate_rouge(
    predictions: Union[str, List[str]],
    references: Union[str, List[str]],
    rouge_types: Optional[List[str]] = None,
    use_stemmer: bool = False
) -> Dict[str, Dict[str, float]]:
    """
    Calculate ROUGE scores between predictions and references.
    
    Args:
        predictions: Predicted summary/summaries
        references: Reference summary/summaries
        rouge_types: Types of ROUGE to calculate (default: ['rouge1', 'rouge2', 'rougeL'])
        use_stemmer: Whether to use stemming (for English; not applicable for Indonesian)
        
    Returns:
        Dictionary of ROUGE scores with precision, recall, and F1
        
    Examples:
        >>> pred = "Produk bagus dan pengiriman cepat"
        >>> ref = "Barang bagus, pengiriman sangat cepat"
        >>> scores = calculate_rouge(pred, ref)
        >>> print(scores['rouge1']['fmeasure'])
    """
    if not HAS_ROUGE:
        raise ImportError(
            "rouge-score is required for ROUGE evaluation. "
            "Install it with: pip install rouge-score"
        )
    
    if rouge_types is None:
        rouge_types = ['rouge1', 'rouge2', 'rougeL']
    
    # Convert single strings to lists
    if isinstance(predictions, str):
        predictions = [predictions]
    if isinstance(references, str):
        references = [references]
    
    # Ensure equal lengths
    if len(predictions) != len(references):
        raise ValueError("Number of predictions must match number of references")
    
    # Initialize scorer
    scorer = rouge_scorer.RougeScorer(rouge_types, use_stemmer=use_stemmer)
    
    # Calculate scores for each prediction-reference pair
    all_scores = []
    for pred, ref in zip(predictions, references):
        scores = scorer.score(ref, pred)
        all_scores.append(scores)
    
    # Aggregate scores
    if len(all_scores) == 1:
        # Return scores for single example
        result = {}
        for rouge_type in rouge_types:
            score = all_scores[0][rouge_type]
            result[rouge_type] = {
                'precision': score.precision,
                'recall': score.recall,
                'fmeasure': score.fmeasure
            }
        return result
    else:
        # Average scores across multiple examples
        result = {}
        for rouge_type in rouge_types:
            precisions = [s[rouge_type].precision for s in all_scores]
            recalls = [s[rouge_type].recall for s in all_scores]
            fmeasures = [s[rouge_type].fmeasure for s in all_scores]
            
            result[rouge_type] = {
                'precision': np.mean(precisions),
                'recall': np.mean(recalls),
                'fmeasure': np.mean(fmeasures)
            }
        return result


def evaluate_predictions(
    predictions: List[str],
    references: List[str],
    rouge_types: Optional[List[str]] = None,
    aggregate: bool = True
) -> Union[Dict[str, Dict[str, float]], List[Dict[str, Dict[str, float]]]]:
    """
    Evaluate predictions against references using ROUGE metrics.
    
    Args:
        predictions: List of predicted summaries
        references: List of reference summaries
        rouge_types: Types of ROUGE to calculate
        aggregate: Whether to aggregate scores or return per-example scores
        
    Returns:
        Aggregated ROUGE scores or list of per-example scores
    """
    if not HAS_ROUGE:
        raise ImportError(
            "rouge-score is required for ROUGE evaluation. "
            "Install it with: pip install rouge-score"
        )
    
    if rouge_types is None:
        rouge_types = ['rouge1', 'rouge2', 'rougeL']
    
    if len(predictions) != len(references):
        raise ValueError(f"Mismatch: {len(predictions)} predictions vs {len(references)} references")
    
    # Initialize scorer
    scorer = rouge_scorer.RougeScorer(rouge_types, use_stemmer=False)
    
    # Calculate scores for each example
    all_scores = []
    for pred, ref in zip(predictions, references):
        scores = scorer.score(ref, pred)
        score_dict = {}
        for rouge_type in rouge_types:
            score = scores[rouge_type]
            score_dict[rouge_type] = {
                'precision': score.precision,
                'recall': score.recall,
                'fmeasure': score.fmeasure
            }
        all_scores.append(score_dict)
    
    if not aggregate:
        return all_scores
    
    # Aggregate scores
    aggregated = {}
    for rouge_type in rouge_types:
        precisions = [s[rouge_type]['precision'] for s in all_scores]
        recalls = [s[rouge_type]['recall'] for s in all_scores]
        fmeasures = [s[rouge_type]['fmeasure'] for s in all_scores]
        
        aggregated[rouge_type] = {
            'precision': float(np.mean(precisions)),
            'recall': float(np.mean(recalls)),
            'fmeasure': float(np.mean(fmeasures)),
            'std': float(np.std(fmeasures))
        }
    
    return aggregated


def format_rouge_scores(scores: Dict[str, Dict[str, float]], decimals: int = 4) -> str:
    """
    Format ROUGE scores as a readable string.
    
    Args:
        scores: Dictionary of ROUGE scores
        decimals: Number of decimal places
        
    Returns:
        Formatted string
    """
    lines = []
    for rouge_type, metrics in scores.items():
        lines.append(f"{rouge_type.upper()}:")
        for metric_name, value in metrics.items():
            lines.append(f"  {metric_name}: {value:.{decimals}f}")
    return "\n".join(lines)

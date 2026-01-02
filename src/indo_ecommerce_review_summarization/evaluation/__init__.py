"""
Evaluation Module
=================

ROUGE-based evaluation metrics for abstractive summarization.
"""

try:
    from .rouge_metrics import calculate_rouge, evaluate_predictions
    __all__ = [
        "calculate_rouge",
        "evaluate_predictions",
    ]
except ImportError:
    # rouge-score not installed
    __all__ = []

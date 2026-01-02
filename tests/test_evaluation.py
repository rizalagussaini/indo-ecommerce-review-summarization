"""
Tests for ROUGE evaluation metrics.
"""

import pytest
from indo_ecommerce_review_summarization.evaluation import (
    calculate_rouge,
    evaluate_predictions,
    format_rouge_scores
)


def test_calculate_rouge_single():
    """Test ROUGE calculation for single prediction."""
    prediction = "Produk bagus dengan pengiriman cepat"
    reference = "Barang bagus, pengiriman cepat"
    
    scores = calculate_rouge(prediction, reference)
    
    assert 'rouge1' in scores
    assert 'rouge2' in scores
    assert 'rougeL' in scores
    assert 0 <= scores['rouge1']['fmeasure'] <= 1
    assert 0 <= scores['rouge2']['fmeasure'] <= 1
    assert 0 <= scores['rougeL']['fmeasure'] <= 1


def test_calculate_rouge_multiple():
    """Test ROUGE calculation for multiple predictions."""
    predictions = [
        "Produk bagus",
        "Pengiriman cepat"
    ]
    references = [
        "Barang bagus",
        "Kirim cepat"
    ]
    
    scores = calculate_rouge(predictions, references)
    
    assert 'rouge1' in scores
    assert isinstance(scores['rouge1']['fmeasure'], float)


def test_evaluate_predictions():
    """Test prediction evaluation."""
    predictions = ["Produk bagus", "Pengiriman cepat"]
    references = ["Barang bagus", "Kirim cepat"]
    
    scores = evaluate_predictions(predictions, references, aggregate=True)
    
    assert 'rouge1' in scores
    assert 'std' in scores['rouge1']


def test_evaluate_predictions_per_example():
    """Test per-example evaluation."""
    predictions = ["Produk bagus", "Pengiriman cepat"]
    references = ["Barang bagus", "Kirim cepat"]
    
    scores = evaluate_predictions(predictions, references, aggregate=False)
    
    assert isinstance(scores, list)
    assert len(scores) == 2
    assert 'rouge1' in scores[0]


def test_format_rouge_scores():
    """Test ROUGE score formatting."""
    scores = {
        'rouge1': {'precision': 0.5, 'recall': 0.6, 'fmeasure': 0.55},
        'rouge2': {'precision': 0.3, 'recall': 0.4, 'fmeasure': 0.35}
    }
    
    formatted = format_rouge_scores(scores)
    
    assert isinstance(formatted, str)
    assert 'ROUGE1' in formatted
    assert 'ROUGE2' in formatted


def test_calculate_rouge_mismatch():
    """Test error handling for mismatched lengths."""
    predictions = ["Test"]
    references = ["Test", "Test2"]
    
    with pytest.raises(ValueError):
        calculate_rouge(predictions, references)

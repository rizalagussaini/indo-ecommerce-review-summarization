# Quick Start Guide

## Installation

```bash
# Clone the repository
git clone https://github.com/rizalagussaini/indo-ecommerce-review-summarization.git
cd indo-ecommerce-review-summarization

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install package
pip install -e .
```

## Quick Example

```python
from indo_ecommerce_review_summarization.preprocessing import clean_text
from indo_ecommerce_review_summarization.models import create_summarization_prompt

# Clean a review
review = "Barang bagus bgt!!! 😊 Pengiriman cepet"
cleaned = clean_text(review)
print(f"Cleaned: {cleaned}")

# Create a prompt
prompt = create_summarization_prompt([cleaned], model_type="mistral")
print(f"Prompt ready for model")
```

## Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src

# Run specific test file
pytest tests/test_preprocessing.py
```

## Using Notebooks

```bash
# Start Jupyter
jupyter notebook

# Open notebooks/01_mistral_summarization.ipynb
```

## Common Tasks

### Preprocess Reviews
```bash
python scripts/preprocess_reviews.py \
    --input data/samples/sample_reviews.json \
    --output data/processed/clean_reviews.json
```

### Generate Summaries (requires GPU)
```bash
python scripts/generate_summaries.py \
    --input data/samples/sample_reviews.json \
    --output results/summaries.json \
    --model mistralai/Mistral-7B-Instruct-v0.2 \
    --load-in-4bit
```

### Evaluate Results
```bash
python scripts/evaluate_summaries.py \
    --predictions results/summaries.json \
    --references data/samples/sample_reviews.json
```

## Troubleshooting

### Out of Memory
- Use `--load-in-4bit` or `--load-in-8bit` flags
- Reduce batch size
- Use a smaller model

### Import Errors
- Make sure to install with `pip install -e .`
- Check your Python version (3.8+ required)

### CUDA Not Available
- Install PyTorch with CUDA support
- Check your GPU drivers
- Models will fall back to CPU (slower)

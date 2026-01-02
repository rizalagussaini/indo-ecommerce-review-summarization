# Indonesian E-commerce Review Summarization

Abstractive summarization of informal Indonesian e-commerce reviews using instruction-tuned LLMs (e.g., Mistral-7B-Instruct). This project includes preprocessing utilities, evaluation with ROUGE metrics, and example notebooks for multiple models.

## 🎯 Features

- **Clean Python Project Structure**: Well-organized modular codebase
- **Preprocessing Pipeline**: Text cleaning and normalization for Indonesian reviews
- **Multiple LLM Support**: Works with Mistral, LLaMA, and other instruction-tuned models
- **ROUGE Evaluation**: Built-in evaluation metrics for summarization quality
- **Example Notebooks**: Interactive Jupyter notebooks demonstrating usage
- **Easy-to-Use Scripts**: Command-line tools for preprocessing and evaluation
- **Sample Data**: Example Indonesian e-commerce reviews included

## 📁 Project Structure

```
indo-ecommerce-review-summarization/
├── src/
│   └── indo_ecommerce_review_summarization/
│       ├── __init__.py
│       ├── preprocessing/          # Text preprocessing utilities
│       │   ├── __init__.py
│       │   ├── text_cleaner.py    # Text cleaning and normalization
│       │   └── data_loader.py     # Data loading/saving utilities
│       ├── evaluation/             # Evaluation metrics
│       │   ├── __init__.py
│       │   └── rouge_metrics.py   # ROUGE score calculation
│       ├── models/                 # LLM interfaces
│       │   ├── __init__.py
│       │   ├── llm_interface.py   # Model wrappers
│       │   └── prompt_templates.py # Prompt templates
│       └── utils/                  # Common utilities
│           ├── __init__.py
│           ├── file_utils.py      # File I/O utilities
│           └── logging_utils.py   # Logging configuration
├── notebooks/                      # Jupyter notebooks
│   ├── 01_mistral_summarization.ipynb
│   ├── 02_model_comparison.ipynb
│   └── 03_rouge_evaluation.ipynb
├── scripts/                        # Utility scripts
│   ├── preprocess_reviews.py     # Preprocess review data
│   ├── generate_summaries.py     # Generate summaries
│   └── evaluate_summaries.py     # Evaluate predictions
├── data/                          # Data directories
│   ├── samples/                   # Sample data
│   ├── raw/                       # Raw data
│   └── processed/                 # Processed data
├── tests/                         # Unit tests
├── requirements.txt               # Python dependencies
├── pyproject.toml                # Package configuration
└── README.md                     # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- CUDA-capable GPU (recommended for running LLMs)
- 16GB+ RAM recommended

### Installation

1. Clone the repository:
```bash
git clone https://github.com/rizalagussaini/indo-ecommerce-review-summarization.git
cd indo-ecommerce-review-summarization
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install the package in development mode:
```bash
pip install -e .
```

## 📚 Usage

### 1. Using Jupyter Notebooks (Recommended for beginners)

Start Jupyter:
```bash
jupyter notebook
```

Then explore the notebooks in the `notebooks/` directory:
- `01_mistral_summarization.ipynb` - Complete guide to using Mistral-7B-Instruct
- `02_model_comparison.ipynb` - Compare different LLMs
- `03_rouge_evaluation.ipynb` - Evaluate summarization quality

### 2. Using Python Scripts

#### Preprocess Reviews
```bash
python scripts/preprocess_reviews.py \
    --input data/samples/sample_reviews.json \
    --output data/processed/reviews_clean.json \
    --lowercase
```

#### Generate Summaries
```bash
python scripts/generate_summaries.py \
    --input data/samples/sample_reviews.json \
    --output results/summaries.json \
    --model mistralai/Mistral-7B-Instruct-v0.2 \
    --load-in-4bit
```

#### Evaluate Summaries
```bash
python scripts/evaluate_summaries.py \
    --predictions results/summaries.json \
    --references data/samples/sample_reviews.json \
    --pred-field generated_summary \
    --ref-field summary
```

### 3. Using as a Python Library

```python
from indo_ecommerce_review_summarization.preprocessing import clean_text
from indo_ecommerce_review_summarization.models import load_model, create_summarization_prompt
from indo_ecommerce_review_summarization.evaluation import calculate_rouge

# Preprocess a review
review = "Barang bagus bgt!!! Pengiriman cepet 👍"
cleaned = clean_text(review)

# Load model
model = load_model(
    model_name="mistralai/Mistral-7B-Instruct-v0.2",
    load_in_4bit=True
)

# Create prompt and generate summary
prompt = create_summarization_prompt([cleaned], model_type="mistral")
summary = model.generate(prompt, max_new_tokens=128)

# Evaluate
reference = "Produk berkualitas dengan pengiriman cepat."
scores = calculate_rouge(summary, reference)
print(scores)
```

## 🔧 Configuration

### Supported Models

The project supports various instruction-tuned LLMs:
- **Mistral-7B-Instruct** (recommended)
- **LLaMA-2-7B-Chat**
- **LLaMA-2-13B-Chat**
- Other Hugging Face compatible models

### Prompt Templates

Four prompt templates are provided:
- `mistral` - For Mistral models
- `llama` - For LLaMA models
- `indonesian` - Indonesian-focused template
- `generic` - Generic instruction template

## 📊 Evaluation

The project uses ROUGE metrics for evaluation:
- **ROUGE-1**: Unigram overlap
- **ROUGE-2**: Bigram overlap
- **ROUGE-L**: Longest common subsequence

See `notebooks/03_rouge_evaluation.ipynb` for detailed examples.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Hugging Face Transformers library
- ROUGE score implementation
- Indonesian NLP community

## 📧 Contact

Rizal Agus Saini - [GitHub](https://github.com/rizalagussaini)

## 🔗 Related Projects

- [Hugging Face Transformers](https://github.com/huggingface/transformers)
- [ROUGE Score](https://github.com/google-research/google-research/tree/master/rouge)

## 📝 Citation

If you use this project in your research, please cite:

```bibtex
@software{indo_ecommerce_review_summarization,
  title = {Indonesian E-commerce Review Summarization},
  author = {Saini, Rizal Agus},
  year = {2026},
  url = {https://github.com/rizalagussaini/indo-ecommerce-review-summarization}
}
```

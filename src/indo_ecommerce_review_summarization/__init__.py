"""
Indo E-commerce Review Summarization
=====================================

Abstractive summarization of informal Indonesian e-commerce reviews 
using instruction-tuned LLMs.

Modules:
    - preprocessing: Text preprocessing and cleaning utilities
    - evaluation: ROUGE-based evaluation metrics
    - models: LLM interfaces and wrappers
    - utils: Common utilities
"""

__version__ = "0.1.0"
__author__ = "Rizal Agus Saini"

from . import preprocessing
from . import evaluation
from . import models
from . import utils

__all__ = ["preprocessing", "evaluation", "models", "utils"]

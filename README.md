# Indonesian E‑Commerce Review Summarization

This repository contains code and notebooks for our project on abstractive
summarization of informal Indonesian e‑commerce reviews using instruction‑tuned
Large Language Models (LLMs). The goal is to help business teams quickly
understand customer feedback without reading thousands of long reviews.

## Colab Notebooks

You can run each model directly in Google Colab:

- **mistralai/Mistral-7B-Instruct-v0.2**  
  https://colab.research.google.com/drive/1ibPbqfPbVQjspH7w9Cv9JajuQ1P8vaO6?usp=sharing  

- **NousResearch/Nous-Hermes-llama-2-7b**  
  https://colab.research.google.com/drive/1rdcq5RdokH_GzFHmyQvdb07hEAlANY_p?usp=sharing  

- **microsoft/phi-2**  
  https://colab.research.google.com/drive/1oGbWolGSYFui386JBQJrqDi2pPS1ksXG?usp=sharing  

- **TheBloke/vicuna-7b-1.1-HF**  
  https://colab.research.google.com/drive/1bump3anc0DHAQXnUOtPwmO2vX5tuZKPE?usp=sharing  

Each notebook follows a similar pipeline:
data loading, preprocessing (including slang normalization), prompting,
generation, and ROUGE-based evaluation. [file:145]

## Project Status

We are still improving evaluation and integration with real e‑commerce
analytics workflows. Feedback and suggestions are very welcome.

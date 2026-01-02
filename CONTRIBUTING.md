# Contributing to Indonesian E-commerce Review Summarization

Thank you for considering contributing to this project! We welcome contributions from everyone.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. Check if the issue already exists in the [issue tracker](https://github.com/rizalagussaini/indo-ecommerce-review-summarization/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment details (Python version, OS, etc.)

### Contributing Code

1. **Fork the repository**
   ```bash
   git clone https://github.com/your-username/indo-ecommerce-review-summarization.git
   cd indo-ecommerce-review-summarization
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   pip install -e .
   ```

3. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**
   - Write clean, readable code
   - Follow the existing code style
   - Add docstrings to functions and classes
   - Update documentation if needed

5. **Add tests**
   ```bash
   # Write tests in tests/ directory
   pytest tests/test_your_feature.py
   ```

6. **Run all tests**
   ```bash
   pytest tests/
   ```

7. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```

8. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

9. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Describe your changes clearly

## Code Style Guidelines

- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Add type hints where appropriate
- Keep functions focused and small
- Write docstrings for all public functions/classes

Example:
```python
def process_review(text: str, lowercase: bool = True) -> str:
    """
    Process an Indonesian e-commerce review.
    
    Args:
        text: Raw review text
        lowercase: Convert to lowercase if True
        
    Returns:
        Processed review text
        
    Examples:
        >>> process_review("Barang BAGUS")
        'barang bagus'
    """
    # Implementation
    pass
```

## Testing Guidelines

- Write unit tests for new features
- Ensure all tests pass before submitting PR
- Aim for high test coverage
- Test edge cases and error conditions

## Documentation

- Update README.md if you add new features
- Add examples to notebooks if appropriate
- Update docstrings
- Keep QUICKSTART.md in sync

## Areas for Contribution

We welcome contributions in these areas:

### Code Improvements
- Add support for more LLM models
- Improve preprocessing for Indonesian text
- Add more evaluation metrics (BLEU, METEOR, BERTScore)
- Optimize performance
- Add caching mechanisms

### Documentation
- Improve README and guides
- Add more examples and tutorials
- Translate documentation to Indonesian
- Create video tutorials

### Testing
- Increase test coverage
- Add integration tests
- Add performance benchmarks

### Features
- Add fine-tuning capabilities
- Add dataset collection tools
- Add web interface/API
- Add aspect-based summarization
- Add sentiment analysis

## Code Review Process

1. Maintainers will review your PR
2. They may request changes
3. Make requested changes and push updates
4. Once approved, your PR will be merged

## Questions?

- Open an issue for questions
- Tag it with "question" label
- We'll respond as soon as possible

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Thank You!

Your contributions help make this project better for everyone. We appreciate your time and effort! 🙏

"""
Data Loading and Saving Utilities
==================================

Utilities for loading and saving review data in various formats.
"""

import json
import csv
from pathlib import Path
from typing import List, Dict, Any, Optional
import pandas as pd


def load_reviews(file_path: str, file_format: str = "auto") -> List[Dict[str, Any]]:
    """
    Load reviews from a file.
    
    Supports JSON, JSONL, and CSV formats.
    
    Args:
        file_path: Path to the file
        file_format: Format of the file ('json', 'jsonl', 'csv', or 'auto')
        
    Returns:
        List of review dictionaries
        
    Raises:
        ValueError: If file format is not supported
        FileNotFoundError: If file does not exist
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Auto-detect format from extension
    if file_format == "auto":
        suffix = path.suffix.lower()
        if suffix == ".json":
            file_format = "json"
        elif suffix == ".jsonl":
            file_format = "jsonl"
        elif suffix == ".csv":
            file_format = "csv"
        else:
            raise ValueError(f"Cannot auto-detect format for {suffix} files")
    
    # Load based on format
    if file_format == "json":
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Handle both list and single object
            if isinstance(data, dict):
                return [data]
            return data
    
    elif file_format == "jsonl":
        reviews = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    reviews.append(json.loads(line))
        return reviews
    
    elif file_format == "csv":
        df = pd.read_csv(file_path)
        return df.to_dict('records')
    
    else:
        raise ValueError(f"Unsupported file format: {file_format}")


def save_processed_data(
    data: List[Dict[str, Any]],
    output_path: str,
    file_format: str = "auto"
) -> None:
    """
    Save processed data to a file.
    
    Args:
        data: List of data dictionaries
        output_path: Path to save the file
        file_format: Format to save ('json', 'jsonl', 'csv', or 'auto')
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    # Auto-detect format from extension
    if file_format == "auto":
        suffix = path.suffix.lower()
        if suffix == ".json":
            file_format = "json"
        elif suffix == ".jsonl":
            file_format = "jsonl"
        elif suffix == ".csv":
            file_format = "csv"
        else:
            raise ValueError(f"Cannot auto-detect format for {suffix} files")
    
    # Save based on format
    if file_format == "json":
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    elif file_format == "jsonl":
        with open(output_path, 'w', encoding='utf-8') as f:
            for item in data:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
    
    elif file_format == "csv":
        df = pd.DataFrame(data)
        df.to_csv(output_path, index=False, encoding='utf-8')
    
    else:
        raise ValueError(f"Unsupported file format: {file_format}")


def load_dataset_splits(
    data_dir: str,
    splits: Optional[List[str]] = None
) -> Dict[str, List[Dict[str, Any]]]:
    """
    Load dataset splits (train, validation, test) from a directory.
    
    Args:
        data_dir: Directory containing split files
        splits: List of split names (default: ['train', 'val', 'test'])
        
    Returns:
        Dictionary mapping split names to data
    """
    if splits is None:
        splits = ['train', 'val', 'test']
    
    data_path = Path(data_dir)
    datasets = {}
    
    for split in splits:
        # Try common file extensions
        for ext in ['.json', '.jsonl', '.csv']:
            file_path = data_path / f"{split}{ext}"
            if file_path.exists():
                datasets[split] = load_reviews(str(file_path))
                break
    
    return datasets

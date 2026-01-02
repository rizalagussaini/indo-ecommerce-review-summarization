"""
Tests for file utilities.
"""

import pytest
import tempfile
import json
import os
from pathlib import Path

from indo_ecommerce_review_summarization.utils import (
    load_json,
    save_json,
    load_csv,
    save_csv
)


def test_save_and_load_json():
    """Test JSON save and load."""
    data = {"key": "value", "list": [1, 2, 3]}
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        temp_path = f.name
    
    try:
        save_json(data, temp_path)
        loaded = load_json(temp_path)
        assert loaded == data
    finally:
        os.unlink(temp_path)


def test_save_json_creates_directory():
    """Test that save_json creates parent directories."""
    with tempfile.TemporaryDirectory() as temp_dir:
        path = os.path.join(temp_dir, "subdir", "test.json")
        data = {"test": "data"}
        
        save_json(data, path)
        assert os.path.exists(path)
        
        loaded = load_json(path)
        assert loaded == data


def test_save_and_load_csv():
    """Test CSV save and load."""
    data = [
        {"name": "Item1", "price": 100},
        {"name": "Item2", "price": 200}
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
        temp_path = f.name
    
    try:
        save_csv(data, temp_path)
        loaded = load_csv(temp_path)
        
        assert len(loaded) == 2
        assert loaded[0]["name"] == "Item1"
        assert loaded[1]["name"] == "Item2"
    finally:
        os.unlink(temp_path)


def test_save_csv_empty():
    """Test saving empty CSV."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
        temp_path = f.name
    
    try:
        save_csv([], temp_path)
        # Should not raise an error
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)

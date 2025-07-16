# test_neuralalchemy.py
"""
Tests for NeuralAlchemy module.
"""

import unittest
from neuralalchemy import NeuralAlchemy

class TestNeuralAlchemy(unittest.TestCase):
    """Test cases for NeuralAlchemy class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeuralAlchemy()
        self.assertIsInstance(instance, NeuralAlchemy)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeuralAlchemy()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

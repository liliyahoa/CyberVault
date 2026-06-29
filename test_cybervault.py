# test_cybervault.py
"""
Tests for CyberVault module.
"""

import unittest
from cybervault import CyberVault

class TestCyberVault(unittest.TestCase):
    """Test cases for CyberVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CyberVault()
        self.assertIsInstance(instance, CyberVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CyberVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

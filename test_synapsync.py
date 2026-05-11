# test_synapsync.py
"""
Tests for SynapSync module.
"""

import unittest
from synapsync import SynapSync

class TestSynapSync(unittest.TestCase):
    """Test cases for SynapSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SynapSync()
        self.assertIsInstance(instance, SynapSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SynapSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

# test_yellowsun.py
"""
Tests for YellowSun module.
"""

import unittest
from yellowsun import YellowSun

class TestYellowSun(unittest.TestCase):
    """Test cases for YellowSun class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = YellowSun()
        self.assertIsInstance(instance, YellowSun)
        
    def test_run_method(self):
        """Test the run method."""
        instance = YellowSun()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

# test_governancedao.py
"""
Tests for GovernanceDAO module.
"""

import unittest
from governancedao import GovernanceDAO

class TestGovernanceDAO(unittest.TestCase):
    """Test cases for GovernanceDAO class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GovernanceDAO()
        self.assertIsInstance(instance, GovernanceDAO)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GovernanceDAO()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

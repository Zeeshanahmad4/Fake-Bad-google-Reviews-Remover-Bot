import unittest
from unittest.mock import patch
from src.vpn_manager import change_vpn

class TestVPNManager(unittest.TestCase):
    @patch('src.vpn_manager.subprocess.run')
    def test_change_vpn_success(self, mock_subprocess_run):
        """Test changing VPN connection successfully."""
        # Configure the mock to simulate a successful VPN change command
        mock_subprocess_run.return_value.returncode = 0
        
        result = change_vpn()
        self.assertIn('Successfully connected', result, "The result should indicate a successful connection change.")
        
    @patch('src.vpn_manager.subprocess.run')
    def test_change_vpn_failure(self, mock_subprocess_run):
        """Test handling of a failed VPN change command."""
        # Configure the mock to simulate a failed VPN change command by raising an exception
        mock_subprocess_run.side_effect = Exception("VPN change failed")
        
        result = change_vpn()
        self.assertIn('Failed to connect', result, "The result should indicate a failure to change the connection.")

if __name__ == '__main__':
    unittest.main()
# Tests for the VPN manager module

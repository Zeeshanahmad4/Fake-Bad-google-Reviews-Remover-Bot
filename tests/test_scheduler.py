import unittest
from unittest.mock import patch, MagicMock
from src.scheduler import schedule_task

class TestScheduler(unittest.TestCase):
    @patch('src.scheduler.schedule.every')
    def test_schedule_task(self, mock_schedule_every):
        """Test that a task is scheduled at the correct interval."""
        mock_interval = MagicMock()
        mock_schedule_every.return_value = mock_interval
        
        interval_minutes = 10
        test_task = lambda: print("This is a test task.")
        
        schedule_task(test_task, interval_minutes)

        # Check if `schedule.every()` was called with the correct interval
        mock_schedule_every.assert_called_once_with(interval_minutes)
        # Check if `.minutes.do()` was called on the resulting object with the correct task
        mock_interval.minutes.do.assert_called_once_with(test_task)

if __name__ == '__main__':
    unittest.main()
# Tests for the scheduler module

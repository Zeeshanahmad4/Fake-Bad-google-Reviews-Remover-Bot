# test_scheduler.py

import unittest
from src.scheduler.scheduler import schedule_reports
from apscheduler.schedulers.background import BackgroundScheduler

class TestScheduler(unittest.TestCase):
    """
    This class contains unit tests for the scheduler module.
    """

    def test_schedule_reports_initialization(self):
        """
        Test if the schedule_reports function initializes the scheduler correctly.
        """
        # Call the schedule_reports function with a test interval
        test_interval_minutes = 1  # Short interval for testing
        scheduler = schedule_reports(test_interval_minutes)

        # Check if the scheduler is an instance of BackgroundScheduler
        self.assertIsInstance(scheduler, BackgroundScheduler)

        # Check if the scheduler has jobs scheduled (assuming at least one job is scheduled)
        self.assertTrue(len(scheduler.get_jobs()) > 0)

    # Additional tests can be added to test specific scheduling behaviors or configurations

if __name__ == '__main__':
    unittest.main()


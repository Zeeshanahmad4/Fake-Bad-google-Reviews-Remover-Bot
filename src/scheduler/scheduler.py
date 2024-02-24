# scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from src.reporter.reporter import submit_report
import time

def schedule_reports(interval_minutes):
    """
    Schedules the submission of reports at regular intervals.

    :param interval_minutes: The interval in minutes for report submission
    """
    scheduler = BackgroundScheduler()

    # Schedule the report submission task
    scheduler.add_job(submit_report, 'interval', minutes=interval_minutes)

    # Start the scheduler
    scheduler.start()

    try:
        # To keep the script running
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        # Shut down the scheduler when exiting the app
        scheduler.shutdown()

def example_report_function():
    """
    An example function that would be called by the scheduler.
    Replace this with the actual function you intend to schedule.
    """
    print("Report function executed")

if __name__ == "__main__":
    # Example usage
    schedule_reports(interval_minutes=30)


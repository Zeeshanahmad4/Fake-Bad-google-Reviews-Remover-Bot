import schedule
import time

def job():
    print("Executing scheduled task...")

def schedule_task(interval_minutes):
    """
    Schedules a task to be executed at regular intervals.

    Parameters:
    - interval_minutes (int): The interval in minutes at which the task should be repeated.
    """
    schedule.every(interval_minutes).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Example: Schedule the 'job' function to run every 30 minutes
    print("Scheduling a task to run every 30 minutes...")
    schedule_task(30)
# Handles scheduling of report submissions

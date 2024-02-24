# main.py

from interfaces.interface import main as start_interface
from utils.utils import setup_logging
from config.settings import LOGGING_SETTINGS

def main():
    """
    Main function to initiate the FakeReviewReporter application.
    """

    # Setup logging
    log_file_path = LOGGING_SETTINGS['log_file']
    setup_logging(log_file_path)

    # Starting the user interface
    print("Starting FakeReviewReporter...")
    start_interface()

if __name__ == "__main__":
    main()


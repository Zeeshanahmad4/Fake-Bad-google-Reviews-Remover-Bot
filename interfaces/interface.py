# interface.py

import sys
from src.reporter import submit_report
from src.scheduler import schedule_reports
from src.vpn_manager import connect_vpn, disconnect_vpn

def display_menu():
    """
    Displays the main menu of the application.
    """
    print("\nFake Review Reporter Interface")
    print("1. Submit a single report")
    print("2. Schedule regular report submission")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")
    return choice

def handle_choice(choice):
    """
    Handles the user's choice from the main menu.
    """
    if choice == '1':
        # Code to submit a single report
        review_url = input("Enter the review URL or ID to report: ")
        connect_vpn()  # Connect to VPN if needed
        submit_report(review_url)
        disconnect_vpn()  # Disconnect VPN after submission

    elif choice == '2':
        # Code to schedule regular reports
        schedule_reports()

    elif choice == '3':
        # Exit the application
        sys.exit("Exiting the application.")

def main():
    """
    The main function to run the interface.
    """
    while True:
        choice = display_menu()
        handle_choice(choice)

if __name__ == "__main__":
    main()


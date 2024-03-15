from scheduler import schedule_task
from report_generator import report_review
from vpn_manager import change_vpn
from user_interface import ui

def main():
    print("Initializing Automated Reporting System...")
    
    # Example: Initialize VPN change (this would be more complex in reality, with scheduled VPN changes)
    print("Establishing initial VPN connection...")
    change_vpn()

    # Display the user interface (assuming a CLI-based interface as previously described)
    ui.main_menu()

    # Example of scheduling a task (you would replace this with actual functionality)
    print("Scheduling regular report submissions...")
    schedule_task(report_review, interval=30)  # This assumes you have a function to schedule tasks
    
    print("Automated Reporting System initialized successfully. The UI is now available for interactions.")

if __name__ == "__main__":
    main()
# Main application entry point

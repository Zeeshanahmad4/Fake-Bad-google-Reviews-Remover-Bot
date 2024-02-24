# settings.py

# This file contains configuration settings for the FakeReviewReporter project.

# VPN Settings
VPN_SETTINGS = {
    'provider': 'YOUR_VPN_PROVIDER',  # Replace with your VPN provider
    'api_key': 'YOUR_VPN_API_KEY',    # Replace with your VPN API key
    # Add other VPN related settings here
}

# Google Review Reporting Settings
GOOGLE_REPORT_SETTINGS = {
    'api_endpoint': 'https://googleapis.com/review/report',  # Replace with actual Google API endpoint if available
    'api_key': 'YOUR_GOOGLE_API_KEY',                         # Replace with your Google API key
    # Add other settings related to Google reporting here
}

# Scheduler Settings
SCHEDULER_SETTINGS = {
    'interval_minutes': 30,  # Interval in minutes for running the reporting task
    # Add other scheduling related settings here
}

# Logging Settings
LOGGING_SETTINGS = {
    'log_file': 'logs/reporter.log',  # Path to the log file
    # Add other logging related settings here
}

# Add any other global settings that might be needed for your application


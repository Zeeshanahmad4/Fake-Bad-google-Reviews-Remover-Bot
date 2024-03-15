# settings.py - Configuration settings for the Automated Reporting System

# Google API settings
GOOGLE_API_KEY = "your_google_api_key_here"
REPORT_SUBMISSION_ENDPOINT = "https://googleapis.com/reviews/report"

# Scheduler settings
REPORT_SUBMISSION_INTERVAL_MINUTES = 30  # Interval in minutes for submitting reports

# VPN Service settings
VPN_SERVICE_API_KEY = "your_vpn_service_api_key_here"
VPN_ROTATION_INTERVAL_MINUTES = 10  # Interval in minutes for rotating VPN IP addresses

# Logging settings
LOG_FILE_PATH = "logs/reporting_system.log"
LOG_LEVEL = "INFO"  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL

# Email settings for notifications (Optional)
EMAIL_HOST = "smtp.yourmailprovider.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "your_email_address@example.com"
EMAIL_HOST_PASSWORD = "your_email_password"
EMAIL_USE_TLS = True
EMAIL_RECEIVERS = ["notify@example.com"]  # List of email addresses to receive notifications

# Add more configurations as needed
# Application settings and configurations

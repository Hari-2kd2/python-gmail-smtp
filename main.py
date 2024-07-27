import time
import schedule
from tasks import process_emails, process_today_emails

# Schedule the process_emails function to run every 10 minutes
# schedule.every(1).minutes.do(process_emails)

# Schedule the process_today_emails function to run every 10 minutes
schedule.every(1).minutes.do(process_today_emails)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)

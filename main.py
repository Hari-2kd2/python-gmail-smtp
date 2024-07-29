import gmeet_scheduler
import time
import schedule
from tasks import process_today_emails


# Define job functions
def job_today_emails():
    """
    Executes the process_today_emails function.
    """
    process_today_emails()


# Schedule the job to run every 1 minute
schedule.every(5).minutes.do(job_today_emails)


# Keep the script running
def main():
    """
    Main function to keep the scheduler running.
    """
    try:
        print("Scheduler started. Press Ctrl+C to stop.")
        while True:
            schedule.run_pending()
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()

Here’s the complete `README.md` for your project with the additional details included:

```markdown
# Email Forwarding and Google Meet Scheduling Script

This project is a Python script designed to check for unread emails in a Gmail account, look for specific keywords, forward those emails to a specified recipient, and schedule Google Meet meetings for them. It runs periodically using the `schedule` library.

## Features

- Connects to a Gmail account using IMAP.
- Searches for unread emails in the inbox.
- Checks the body of each email for specified keywords.
- Forwards emails containing any of the keywords to a specified recipient.
- Schedules Google Meet meetings for emails containing specified keywords.
- Scheduled to run every 10 minutes.

## Prerequisites

- Python 3.x
- Gmail account with IMAP access enabled.
- Google Cloud project with Calendar API enabled.
- Environment variables set up for Gmail credentials and keywords.
- `credentials.json` file for Google API credentials.
```
## Installation

### 1. Clone the Repository

```sh
git clone https://github.com/Hari-2kd2/python-gmail-smtp.git
cd python-gmail-smtp
```

### 2. Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```plaintext
GMAIL_ADDRESS=your-email@gmail.com
GMAIL_PASSWORD=your-email-app-password
KEYWORDS=keyword1,keyword2,keyword3
FORWARD_TO=your-forward-email@gmail.com
```

### 5. Configure Google API Credentials

Place your Google API credentials file in the root directory and name it `credentials.json`.

### 6. Run the Script

```sh
python main.py
```

## File Descriptions

- **`main.py`**: The entry point of the script. It runs the main functions to process emails and schedule Google Meet events.
- **`email_checker.py`**: Contains functions to check for unread emails and process them based on keywords.
- **`check_current_date_mail.py`**: Contains functions to process emails received today and create Google Meet events.
- **`email_forwarder.py`**: Contains functions to forward emails to a specified recipient.
- **`gmeet_scheduler.py`**: Contains functions to create Google Meet events using the Google Calendar API.
- **`login.py`**: Contains functions to log into the IMAP server using credentials from environment variables.
- **`logout.py`**: Contains functions to log out from the IMAP server.
- **`random_string.py`**: Contains functions to generate random strings, used for creating unique Google Meet event IDs.
- **`env_setup.py`**: Contains functions to load environment variables from the `.env` file.

## Seen Handler

The provided script includes functionality to mark all unread messages as read in your inbox. This ensures that processed emails are not handled again in subsequent runs.

## Troubleshooting

- **IMAP Connection Issues**: Ensure that IMAP is enabled in your Gmail settings and that the credentials are correct.
- **Google Meet Scheduling Errors**: Verify that `credentials.json` is correctly set up and that the Google Calendar API is enabled in your Google Cloud project. Ensure the Google Meet link is generated and accessible by checking the printed link after running the script.

For further assistance, please check the [Google Calendar API documentation](https://developers.google.com/calendar) and the [IMAPClient documentation](https://imapclient.readthedocs.io/en/latest/).

##
This README provides a clear guide for setting up and running the project, with additional explanations for each file’s purpose and troubleshooting tips.
Certainly! Here's the updated `README.md` with logic changes and necessary updates, including OAuth setup and troubleshooting:

```markdown
# Email Forwarding and Google Meet Scheduling Script

This project is a Python script designed to check for unread emails in a Gmail account, look for specific keywords, forward those emails to a specified recipient, and schedule Google Meet meetings for them. It runs periodically using the `schedule` library.

## Features

- Connects to a Gmail account using OAuth 2.0.
- Searches for unread emails in the inbox.
- Checks the body of each email for specified keywords.
- Forwards emails containing any of the keywords to a specified recipient.
- Schedules Google Meet meetings for emails containing specified keywords.
- Scheduled to run every 10 minutes.

## Prerequisites

- Python 3.x
- Gmail account with OAuth 2.0 access enabled.
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

1. **Go to Google Cloud Console:**
   - Visit the [Google Cloud Console](https://console.cloud.google.com/).

2. **Create OAuth 2.0 Credentials:**
   - Click on **APIs & Services** > **Credentials**.
   - Click on **Create Credentials** and select **OAuth 2.0 Client IDs**.
   - Choose **Desktop app** as the application type.
   - Download the `credentials.json` file and place it in the root directory of the project.

3. **Set Up OAuth 2.0 Consent Screen:**
   - Go to **APIs & Services** > **OAuth consent screen**.
   - Enter your application details and save.

4. **Request Verification (if needed):**
   - If using sensitive scopes, you may need to submit your app for verification. Follow [Google’s verification guide](https://support.google.com/cloud/answer/9110914).

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

### OAuth 2.0 Verification

- **Access Blocked**: Ensure your app is verified if using sensitive scopes. Follow the [verification process](https://support.google.com/cloud/answer/9110914).
- **App Passwords**: If verification is not feasible, you can use app passwords for Gmail with less secure apps enabled.

### Google Meet Scheduling Errors

- **Invalid Conference Type**: Ensure that your Google API credentials are configured correctly and that the `credentials.json` file is valid. Check that the Calendar API is enabled and that your OAuth 2.0 credentials have the necessary permissions.
- **Calendar Permissions**: Ensure that the service account email or OAuth 2.0 client has the necessary permissions to create events in your Google Calendar.

### IMAP Connection Issues

- **IMAP Access**: Ensure that IMAP is enabled in your Gmail settings and that the credentials are correct. Verify that the `credentials.json` file and environment variables are correctly set up.

For further assistance, please check the [Google Calendar API documentation](https://developers.google.com/calendar) and the [IMAPClient documentation](https://imapclient.readthedocs.io/en/latest/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This `README.md` includes updated instructions for setting up OAuth 2.0 credentials, troubleshooting verification issues, and other necessary configurations. Adjust the file paths and names as needed based on your project structure.
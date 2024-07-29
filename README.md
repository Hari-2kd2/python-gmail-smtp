Here is the updated `README.md` file with the necessary changes for setting up OAuth 2.0, including instructions for dealing with verification issues:

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

## Setup

### 1. Clone the Repository

```sh
git clone https://github.com/Hari-2kd2/python-gmail-smtp.git
cd python-gmail-smtp
```

### 2. Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Set Up OAuth 2.0 Credentials

1. **Go to Google Cloud Console:**
   - Visit the [Google Cloud Console](https://console.cloud.google.com/).

2. **Navigate to OAuth Consent Screen:**
   - Click on **APIs & Services** > **OAuth consent screen**.
   - Configure the consent screen by entering your application name, support email, and scopes.
   - Save your changes.

3. **Create OAuth 2.0 Credentials:**
   - Click on **APIs & Services** > **Credentials**.
   - Click on **Create Credentials** and select **OAuth 2.0 Client IDs**.
   - Choose the appropriate application type (e.g., Desktop app for a script).
   - Download the `credentials.json` file.

4. **Set Up Redirect URIs (if applicable):**
   - For desktop apps, you typically don’t need to set redirect URIs.
   - For web apps, specify redirect URIs and authorized domains.

5. **Request Verification (if needed):**
   - If using sensitive or restricted scopes, you may need to submit your app for verification.
   - Go to [OAuth App Verification](https://support.google.com/cloud/answer/9110914) and follow the instructions.

### 5. Set Up Environment Variables

Create a `.env` file in the project root with the following content:

```plaintext
GMAIL_ADDRESS=your-email@gmail.com
GMAIL_PASSWORD=your-email-app-password
KEYWORDS=keyword1,keyword2,keyword3
FORWARD_TO=your-forward-email@gmail.com
```

### 6. Run the Script

```sh
python main.py
```

## Troubleshooting

### 1. Verification Issues

If you encounter issues with OAuth 2.0 verification:

- **Access Blocked**: Ensure your app is verified if using sensitive scopes. Follow the [verification process](https://support.google.com/cloud/answer/9110914).
- **App Passwords**: If verification is not feasible, you can use app passwords for Gmail with less secure apps enabled.

### 2. Creating Google Meet Links

If you face issues with Google Meet link creation:

- Ensure you have the correct API credentials and permissions.
- Verify that the `credentials.json` file is configured correctly and has the necessary permissions.

## Files and Functions

- **`main.py`**: Main script that handles email checking, forwarding, and scheduling Google Meet meetings.
- **`gmeet_scheduler.py`**: Contains functions to create Google Meet events using Google Calendar API.
- **`env_setup.py`**: Loads environment variables from the `.env` file.
- **`requirements.txt`**: Lists the required Python libraries for the project.

## License
```plaintext
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Summary of Changes

1. **OAuth 2.0 Setup Instructions**: Added detailed steps for setting up OAuth 2.0 credentials, including the consent screen, credentials creation, and verification process.
2. **Troubleshooting Section**: Included troubleshooting tips for verification issues and Google Meet link creation.
3. **File and Function Descriptions**: Added descriptions of the key files and their functions.

Feel free to adjust any details according to your specific needs or additional instructions.
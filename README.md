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

## Seen Handler

- Just use that function to make all messages as read from your inbox

## Setup

## 1. Clone the repository

```sh
git clone https://github.com/Hari-2kd2/python-gmail-smtp.git
cd python-gmail-smtp
```
## 2. Create a virtual environment
```sh
python -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
```
## 3. Install dependencies
```sh
pip install -r requirements.txt
```

## 4. Set up environment variables

```sh
mkdir .env
```
```sh
GMAIL_ADDRESS=your-email@gmail.com
GMAIL_PASSWORD=your-email-app-password
KEYWORDS=keyword1,keyword2,keyword3
FORWARD_TO=your-forward-emain@gmail.com
```

## 5. Run the script
```sh
python main.py
```

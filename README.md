# Bookings RPA Bot

This bot reads a Firebase Firestore containing booking information and sends an email compiling the bookings in a given date range.

## Requirements

The bot runs on Power Automate Desktop (PAD) (Windows required). If it's not installed, you can follow the instructions 

[here]: https://learn.microsoft.com/en-us/power-automate/desktop-flows/install

Microsoft Outlook is also required for this flow.

You must already have a Firebase Firestore setup and service provider credentials (alternative authentication methods are okay, but main.py should be adjusted accordingly). Refer 

[here]: https://firebase.google.com/docs/firestore/quickstart

to setup your Firestore and service provider credentials. The data should have a "start" timestamp field storing the booking start datetime and an "end" timestamp field storing the booking end datetime.

## Getting Started

### Loading Power Automate Flow

1) With PAD open, create a new flow.
2) Copy over main_PAD.txt, and paste it in the main flow.
3) Create a subflow named read_config. Copy over read_config.txt and paste it in the subflow.
4) In the variables section, change ProjectFolder variable to your project folder path.
5) Save changes.

### Create venv

PAD doesn't work very well with imported modules, so venv is required.

1. Create venv

   `python -m venv booking-env`

2. Activate venv

   `booking-env\Scripts\activate`

3. Install requirements (cd into project folder first)

   `pip install -r requirements.txt`

### Update Config and main.py

1. Open config,xlsx and update information, if required.
2. Open main.py, and update the certificate path and collection name (database storing bookings)

### Run Flow

Test the flow by running it via the PAD editor or PAD home panel. On success, the bot should send out an email to the recipient address.

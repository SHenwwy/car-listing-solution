"""
This module is responsible for sending the final car listing data via email.
It uses Python's built-in smtplib and email libraries to construct and
send a multipart email with the JSON data and the car image as attachments.
"""

import os
import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_car_listing_email(json_data: dict, image_path: str):
    """
    Constructs and sends an email with the car data and image.

    Args:
        json_data (dict): The structured car data in dictionary format.
        image_path (str): The file path to the car image to be attached.
    
    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    try:
        sender_email = os.getenv("GMAIL_SENDER_EMAIL")
        app_password = os.getenv("GMAIL_APP_PASSWORD")
        recipient_email = os.getenv("RECIPIENT_EMAIL")

        if not all([sender_email, app_password, recipient_email]):
            print("ERROR: Email credentials are not fully configured in the .env file.")
            return False

        msg = MIMEMultipart()
        msg['Subject'] = f"New Car Listing Submitted: {json_data.get('brand', '')} {json_data.get('model', '')}"
        msg['From'] = sender_email
        msg['To'] = recipient_email

        body = f"A new car listing has been submitted.\n\nDetails:\n\n{json.dumps(json_data, indent=4)}"
        msg.attach(MIMEText(body, 'plain'))

        with open(image_path, 'rb') as f:
            part = MIMEApplication(f.read(), Name=os.path.basename(image_path))
        
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(image_path)}"'
        msg.attach(part)

        print(f"INFO: Connecting to Gmail SMTP server to send email to {recipient_email}...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)
        
        print("INFO: Email sent successfully!")
        return True

    except FileNotFoundError:
        print(f"ERROR: Image file not found at path: {image_path}")
        return False
    except smtplib.SMTPAuthenticationError:
        print("ERROR: SMTP Authentication failed. Check your GMAIL_SENDER_EMAIL and GMAIL_APP_PASSWORD.")
        return False
    except Exception as e:
        print(f"ERROR: An unexpected error occurred while sending the email: {e}")
        return False


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from settings.config import settings
import logging


class SMTPClient:
    def __init__(self, server: str, port: int, username: str, password: str):
        self.server = server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, subject: str, html_content: str, recipient: str):
        """
        Sends an email using the provided SMTP server credentials.

        Args:
            subject (str): Email subject.
            html_content (str): HTML content for the email body.
            recipient (str): Recipient's email address.

        Raises:
            SMTPException: For errors related to the SMTP server.
            Exception: For any unexpected errors.
        """
        try:
            # Create the email message
            message = MIMEMultipart('alternative')
            message['Subject'] = subject
            message['From'] = self.username
            message['To'] = recipient
            message.attach(MIMEText(html_content, 'html'))

            # Connect to the SMTP server
            with smtplib.SMTP(self.server, self.port) as server:
                logging.info(f"Connecting to SMTP server {self.server}:{self.port}")
                server.ehlo()  # Identify with the server
                server.starttls()  # Upgrade to a secure connection
                server.ehlo()  # Re-identify after TLS upgrade
                server.login(self.username, self.password)
                logging.info("SMTP server login successful")
                server.sendmail(self.username, recipient, message.as_string())
                logging.info(f"Email successfully sent to {recipient}")

        except smtplib.SMTPException as smtp_error:
            logging.error(f"SMTP error occurred: {smtp_error}")
            raise
        except Exception as e:
            logging.error(f"Failed to send email: {str(e)}")
            raise

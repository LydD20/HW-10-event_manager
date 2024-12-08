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
        """
        try:
            # Create the email
            message = MIMEMultipart('alternative')
            message['Subject'] = subject
            message['From'] = self.username
            message['To'] = recipient
            message.attach(MIMEText(html_content, 'html'))

            # Connect to the SMTP server
            with smtplib.SMTP(self.server, self.port) as server:
                server.ehlo()  # Identify with the SMTP server
                server.starttls()  # Upgrade the connection to TLS
                server.ehlo()  # Re-identify after upgrading
                server.login(self.username, self.password)
                server.sendmail(self.username, recipient, message.as_string())

            logging.info(f"Email successfully sent to {recipient}")

        except smtplib.SMTPException as smtp_error:
            logging.error(f"SMTP error occurred: {str(smtp_error)}")
            raise
        except Exception as e:
            logging.error(f"Failed to send email: {str(e)}")
            raise


# Usage example (e.g., in a FastAPI or Flask service)
if __name__ == "__main__":
    smtp_client = SMTPClient(
        server="localhost",
        port=1025,
        username="user@example.com",
        password="securepassword"
    )
    try:
        smtp_client.send_email(
            subject="Test Email",
            html_content="<h1>This is a test email</h1>",
            recipient="recipient@example.com"
        )
    except Exception as e:
        logging.error(f"Error sending email: {e}")

import pytest
from app.services.email_service import EmailService
from app.utils.template_manager import TemplateManager

    
@pytest.mark.asyncio
async def test_send_markdown_email(mock_smtp, email_service):
    user_data = {
        "email": "test@example.com",
        "name": "Test User",
        "verification_url": "http://example.com/verify?token=abc123",
    }
    await email_service.send_user_email(user_data, 'email_verification')

    # Assert the email was "sent"
    mock_smtp.send_email.assert_called_once_with(
        "Email Verification", "<html>Email content here</html>", "test@example.com"
    )

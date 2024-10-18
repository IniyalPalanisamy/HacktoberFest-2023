import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

# Read Excel data
df = pd.read_excel('hzshashwat.xlsx')

# Email configuration
smtp_server = 'smtp.example.com'  # Replace with your SMTP server
smtp_port = 587  # Change to your SMTP port
smtp_username = 'your_email@example.com'  # Replace with your email
smtp_password = 'your_password'  # Replace with your email password
sender_email = smtp_username
subject = 'Congratulations!'

# Read the email template
template_path = 'template/index.html'
if not os.path.exists(template_path):
    raise FileNotFoundError(f"Email template not found at {template_path}")

with open(template_path, 'r') as template_file:
    email_template = template_file.read()

# Initialize SMTP server
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Loop through recipients and send emails
    for index, row in df.iterrows():
        recipient_email = row['Email']
        recipient_name = row['Name']

        # Create email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Inject recipient-specific data into the email template
        email_content = email_template.replace('{name}', recipient_name)

        # Attach HTML content to the email
        message.attach(MIMEText(email_content, 'html'))

        # Send email
        server.sendmail(sender_email, recipient_email, message.as_string())
        print(f"Email sent to {recipient_name} at {recipient_email}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the SMTP server
    server.quit()

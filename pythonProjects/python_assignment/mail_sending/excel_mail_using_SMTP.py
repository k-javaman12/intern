import smtplib
import openpyxl
from email.mime.text import MIMEText

def send_email(name, recipient_email, subject, body):
    sender_email = "zizon1434243@naver.com"  # Your email
    password = ""

    msg = MIMEText(body.replace("{name}", name))
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    try:
        server = smtplib.SMTP('smtp.naver.com', 587)  # Use your SMTP server
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

wb = openpyxl.load_workbook('../email_list.xlsx')
sheet = wb.active

for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip the header
    name = row[0]
    email = row[1]
    subject = "Hello {name}!"  # You can customize this
    body = "Dear {name},\n\nThis is a test email."  # You can customize this

    if send_email(name, email, subject, body):
        print(f"Email sent successfully to {name} ({email})")
    else:
        print(f"Failed to send email to {name} ({email})")


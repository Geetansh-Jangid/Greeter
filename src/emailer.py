class Emailer:
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.smtp = None

    def setup_smtp(self):
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        self.smtp = smtplib.SMTP(self.smtp_server, self.smtp_port)
        self.smtp.starttls()
        self.smtp.login(self.username, self.password)

    def send_email(self, recipient, subject, body):
        if self.smtp is None:
            raise Exception("SMTP server not set up. Call setup_smtp() first.")

        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        self.smtp.send_message(msg)
        del msg

    def close(self):
        if self.smtp is not None:
            self.smtp.quit()
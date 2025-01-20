# 👁️ **ScreenLogger** - PYTHON

A **Simple ScreenLogger** built with **Python** that sends **Screenshots** to your email.

## 📚 About

This project was created for a school assignment and is based on other open-source projects found on GitHub. It was developed entirely for educational purposes.

## 🔧 Features

- **Send Screenshots via Email**: Capture and send screenshots of your PC, along with **Hostname, System, User, and IP** information.
- **Customizable Settings**: Adjustable variables are now loaded from a `.env` file, making customization easier.
- **Auto Startup Integration**: Once converted into an **executable**, the program will automatically add itself to the **Startup folder** of Windows.

## 🛠️ **Main Functions**
![Main Functions](https://github.com/user-attachments/assets/54deb6db-15dd-4f27-bb21-49e410000769)

- ✅ **Screenshot Capture**
- ✅ **Hostname Retrieval**
- ✅ **User Information**
- ✅ **IP Address**
- ✅ **Auto Startup Integration**

## ⚙️ **Default Settings**

Settings are now loaded from a `.env` file. Examples of adjustable variables include:

- `EMAIL_SENDER`: Sender email address.
- `EMAIL_RECEIVER`: Receiver email address.
- `EMAIL_PASSWORD`: App password for the email.
- `IMAGES_DIR`: Directory where screenshots will be saved.
- `SMTP_SERVER`: SMTP server for sending emails.
- `SMTP_PORT`: Port for the SMTP server.

Example of `.env` file content:
```env
EMAIL_SENDER=emailsender@example.com
EMAIL_RECEIVER=emailreceiver@example.com
EMAIL_PASSWORD=yourapppassword
IMAGES_DIR=C:\IMAGES
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

## 🛡️ **AntiVirus Tests**

![Antivirus Test 1](https://github.com/user-attachments/assets/9bddf949-9f72-4810-b819-be4c866aee9e)  
![Antivirus Test 2](https://github.com/user-attachments/assets/e5bb72a7-e698-4806-9774-933af345e2e6)

## 💾 **How to Create the Executable (EXE)**

If you want to run **ScreenLogger** as an executable, you can use the library [AutoPyToExe](https://pypi.org/project/auto-py-to-exe/).

Once you have the **.exe file**, ensure that the file name is correct in your script and that the file will be copied to the **Startup folder** of Windows, guaranteeing execution on boot.

## 👨‍💻 **Credits**

This project is based on contributions from other open-source projects. If you're the original creator of any used code, please reach out for proper credit.


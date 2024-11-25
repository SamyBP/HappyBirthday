import pywhatkit

from utils import logs


@logs(message="Sending wapp message")
def send_whatsapp_message(phone_no: str, message: str):
    pywhatkit.sendwhatmsg_instantly(phone_no=phone_no, message=message)

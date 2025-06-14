# relatorios/enviar_email.py

import smtplib
from email.message import EmailMessage
from config.settings import EMAIL_REMETENTE, EMAIL_SENHA, EMAIL_DESTINATARIO

def enviar_email(anexo_path):
    msg = EmailMessage()
    msg['Subject'] = 'Relatório Automático Ipeadata'
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = EMAIL_DESTINATARIO
    msg.set_content('Segue em anexo o relatório gerado automaticamente a partir do Ipeadata.')

    with open(anexo_path, 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=anexo_path)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_REMETENTE, EMAIL_SENHA)
        smtp.send_message(msg)

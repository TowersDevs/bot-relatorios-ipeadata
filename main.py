# main.py

from relatorios.gerar_relatorio import gerar_relatorio
from relatorios.enviar_email import enviar_email

if __name__ == '__main__':
    caminho_pdf = gerar_relatorio()
    enviar_email(caminho_pdf)

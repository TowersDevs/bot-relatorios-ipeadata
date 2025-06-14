# relatorios/gerar_relatorio.py

from ipeadatapy import timeseries
import matplotlib.pyplot as plt
from fpdf import FPDF
import os
from datetime import datetime
from config.settings import CODIGO_SERIE

def gerar_relatorio():
    dados = timeseries(CODIGO_SERIE)

    data_atual = datetime.now().strftime('%Y-%m-%d')
    nome_base = f'relatorio_{CODIGO_SERIE}_{data_atual}'
    grafico_path = os.path.join('relatorios', f'{nome_base}.png')
    pdf_path = os.path.join('relatorios', f'{nome_base}.pdf')

    plt.figure(figsize=(10, 6))
    plt.plot(dados.index, dados[dados.columns[-1]], label='Valor')
    plt.title(f'Série: {CODIGO_SERIE}')
    plt.xlabel('Data')
    plt.ylabel('Valor')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(grafico_path)
    plt.close()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, f'Relatório: Taxa SELIC', ln=True, align='C')
    pdf.image(grafico_path, x=10, y=30, w=190)
    pdf.output(pdf_path)

    return pdf_path

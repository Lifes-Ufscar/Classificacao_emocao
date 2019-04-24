
import xlsxwriter
import time

class Amostra():
    usuario = None
    sessao_id = None
    workbook = None
    planilha = None
    coluna = 0

    def __init__(self, usuario, sessao_id):
        self.usuario = usuario
        self.sessao_id = sessao_id

        self.workbook = xlsxwriter.Workbook("amostras/amostra_" + self.usuario + "_" + self.sessao_id + ".xlsx")
        self.planilha = self.workbook.add_worksheet()
        bold = self.workbook.add_format({'bold': True})

        self.planilha.write('A1', 'Tempo', bold)
        self.planilha.write('B1', 'Contador', bold)
        self.planilha.write('C1', 'Atencao', bold)
        self.planilha.write('D1', 'Meditacao', bold)
        self.planilha.write('E1', 'Raw Value', bold)
        self.planilha.write('F1', 'Delta', bold)
        self.planilha.write('G1', 'Theta', bold)
        self.planilha.write('H1', 'Low Alpha', bold)
        self.planilha.write('I1', 'High Alpha', bold)
        self.planilha.write('J1', 'Low Beta', bold)
        self.planilha.write('K1', 'High Beta', bold)
        self.planilha.write('L1', 'Low Gamma', bold)
        self.planilha.write('M1', 'Mid Gamma', bold)
        self.planilha.write('N1', 'Poor Signal', bold)
        self.planilha.write('O1', 'Blink Strength', bold)
        self.planilha.write('P1', 'GSR', bold)
        self.planilha.write('Q1', 'ECG', bold)

        print(u'\u2713'.encode('utf8') + " Planilha criada com sucesso\n")
        time.sleep(1)

    def escrita_xlsx(self, linha, tempo, contador, mindwave, gsr, ecg):
        # Escrita dos sinais fisiologicos na planilha
        self.planilha.write(linha, self.coluna,      tempo)
        self.planilha.write(linha, self.coluna + 1,  contador)
        self.planilha.write(linha, self.coluna + 2,  mindwave.attention)
        self.planilha.write(linha, self.coluna + 3,  mindwave.meditation)
        self.planilha.write(linha, self.coluna + 4,  mindwave.rawValue)
        self.planilha.write(linha, self.coluna + 5,  mindwave.delta)
        self.planilha.write(linha, self.coluna + 6,  mindwave.theta)
        self.planilha.write(linha, self.coluna + 7,  mindwave.lowAlpha)
        self.planilha.write(linha, self.coluna + 8,  mindwave.highAlpha)
        self.planilha.write(linha, self.coluna + 9,  mindwave.lowBeta)
        self.planilha.write(linha, self.coluna + 10, mindwave.highBeta)
        self.planilha.write(linha, self.coluna + 11, mindwave.lowGamma)
        self.planilha.write(linha, self.coluna + 12, mindwave.midGamma)
        self.planilha.write(linha, self.coluna + 13, mindwave.poorSignal)
        self.planilha.write(linha, self.coluna + 14, mindwave.blinkStrength)
        self.planilha.write(linha, self.coluna + 15, gsr)
        self.planilha.write(linha, self.coluna + 16, ecg)

    def fecha_xlsx(self):
        self.workbook.close()

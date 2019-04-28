
import xlsxwriter
import time

class Amostra():
    usuario   = None
    sessao_id = None
    workbook  = None
    planilha  = None
    filme = None
    linha = 0

    def __init__(self, usuario, sessao_id):
        self.usuario   = usuario
        self.sessao_id = sessao_id
        #self.filme = filme

        #self.workbook = xlsxwriter.Workbook("amostras/amostra_" + self.usuario + "_" + self.sessao_id + "_" + self.filme + ".xlsx")
        self.workbook = xlsxwriter.Workbook("amostras/amostra_" + self.usuario + "_" + self.sessao_id + ".xlsx")
        self.planilha = self.workbook.add_worksheet()
        bold = self.workbook.add_format({'bold': True})

        self.planilha.write('A1', 'Contador',        bold)
        self.planilha.write('A2', 'Tempo',           bold)
        self.planilha.write('A3', 'Atencao',         bold)
        self.planilha.write('A4', 'Meditacao',       bold)
        self.planilha.write('A5', 'Raw Value',       bold)
        self.planilha.write('A6', 'Delta',           bold)
        self.planilha.write('A7', 'Theta',           bold)
        self.planilha.write('A8', 'Low Alpha',       bold)
        self.planilha.write('A9', 'High Alpha',      bold)
        self.planilha.write('A10', 'Low Beta',       bold)
        self.planilha.write('A11', 'High Beta',      bold)
        self.planilha.write('A12', 'Low Gamma',      bold)
        self.planilha.write('A13', 'Mid Gamma',      bold)
        self.planilha.write('A14', 'Poor Signal',    bold)
        self.planilha.write('A15', 'Blink Strength', bold)
        self.planilha.write('A16', 'GSR',            bold)
        self.planilha.write('A17', 'ECG',            bold)

        print("- Planilha criada com sucesso\n")

    def escrita_xlsx(self, coluna, tempo, contador, mindwave, gsr, ecg):
        # Escrita dos sinais fisiologicos na planilha
        self.planilha.write(self.linha,      coluna, contador)
        self.planilha.write(self.linha + 1,  coluna, tempo)
        self.planilha.write(self.linha + 2,  coluna, mindwave.attention)
        self.planilha.write(self.linha + 3,  coluna, mindwave.meditation)
        self.planilha.write(self.linha + 4,  coluna, mindwave.rawValue)
        self.planilha.write(self.linha + 5,  coluna, mindwave.delta)
        self.planilha.write(self.linha + 6,  coluna, mindwave.theta)
        self.planilha.write(self.linha + 7,  coluna, mindwave.lowAlpha)
        self.planilha.write(self.linha + 8,  coluna, mindwave.highAlpha)
        self.planilha.write(self.linha + 9,  coluna, mindwave.lowBeta)
        self.planilha.write(self.linha + 10, coluna, mindwave.highBeta)
        self.planilha.write(self.linha + 11, coluna, mindwave.lowGamma)
        self.planilha.write(self.linha + 12, coluna, mindwave.midGamma)
        self.planilha.write(self.linha + 13, coluna, mindwave.poorSignal)
        self.planilha.write(self.linha + 14, coluna, mindwave.blinkStrength)
        self.planilha.write(self.linha + 15, coluna, gsr)
        self.planilha.write(self.linha + 16, coluna, ecg)

    def fecha_xlsx(self):
        self.workbook.close()

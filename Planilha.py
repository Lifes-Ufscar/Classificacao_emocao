
import xlsxwriter

class Planilha():

    def __init__(self, usuario, sessao_id):
        self.usuario   = usuario
        self.sessao_id = sessao_id

    def criar_xlsx(self):
        self.workbook = xlsxwriter.Workbook("amostras/amostra_" + self.usuario + "_sd" + self.sessao_id + ".xlsx")
        self.planilha = self.workbook.add_worksheet()
        formato = self.workbook.add_format({"bold": True})

        self.planilha.write('A1', 'Contador',        formato)
        self.planilha.write('A2', 'Tempo',           formato)
        self.planilha.write('A3', 'Atencao',         formato)
        self.planilha.write('A4', 'Meditacao',       formato)
        self.planilha.write('A5', 'Raw Value',       formato)
        self.planilha.write('A6', 'Delta',           formato)
        self.planilha.write('A7', 'Theta',           formato)
        self.planilha.write('A8', 'Low Alpha',       formato)
        self.planilha.write('A9', 'High Alpha',      formato)
        self.planilha.write('A10', 'Low Beta',       formato)
        self.planilha.write('A11', 'High Beta',      formato)
        self.planilha.write('A12', 'Low Gamma',      formato)
        self.planilha.write('A13', 'Mid Gamma',      formato)
        self.planilha.write('A14', 'Poor Signal',    formato)
        self.planilha.write('A15', 'Blink Strength', formato)
        self.planilha.write('A16', 'GSR',            formato)
        self.planilha.write('A17', 'ECG',            formato)

    def escrever_xlsx(self, coluna, contador, tempo, mindwave, gsr, ecg):
        self.planilha.write(0,  coluna, contador)
        self.planilha.write(1,  coluna, tempo)
        self.planilha.write(2,  coluna, mindwave.attention)
        self.planilha.write(3,  coluna, mindwave.meditation)
        self.planilha.write(4,  coluna, mindwave.rawValue)
        self.planilha.write(5,  coluna, mindwave.delta)
        self.planilha.write(6,  coluna, mindwave.theta)
        self.planilha.write(7,  coluna, mindwave.lowAlpha)
        self.planilha.write(8,  coluna, mindwave.highAlpha)
        self.planilha.write(9,  coluna, mindwave.lowBeta)
        self.planilha.write(10, coluna, mindwave.highBeta)
        self.planilha.write(11, coluna, mindwave.lowGamma)
        self.planilha.write(12, coluna, mindwave.midGamma)
        self.planilha.write(13, coluna, mindwave.poorSignal)
        self.planilha.write(14, coluna, mindwave.blinkStrength)
        self.planilha.write(15, coluna, gsr)
        self.planilha.write(16, coluna, ecg)

    def fechar_xlsx(self):
        self.workbook.close()
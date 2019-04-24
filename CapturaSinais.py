
from NeuroPy import NeuroPy
from Planilha import Amostra
import serial
import time
import datetime


class CapturaSinais():

    comNeuro   = " "
    mindWave   = " "
    comArduino = " "
    velArduino = " "  # Velocidade bits/seg
    conArduino = " "  # Conexao serial do Arduino

    def __init__(self, comNeuro, comArduino, velArduino):
        self.comNeuro   = comNeuro
        self.comArduino = comArduino
        self.velArduino = velArduino

        # Porta COM do MindWave USB Adapter
        self.mindWave = NeuroPy(self.comNeuro)
        self.mindWave.start()
        print("\n" + u'\u2713'.encode("utf8") + " NeuroPY inicializado")
        time.sleep(1)

        # Porta COM do Arduino
        self.conArduino = serial.Serial(self.comArduino, self.velArduino)  # Abre porta serial
        print(u'\u2713'.encode("utf8") + " Porta serial aberta")
        time.sleep(1)

    def captura_sensores(self, usuario, sessao_id):

        # Setagem de intervalo de captura
        delay = 36 * 1  # 1 loop de 36 segundos
        duracao = time.time() + delay

        ecg = " "
        gsr = " "
        contador = 0

        planilha = Amostra(usuario, sessao_id)

        # Variaveis para a planilha
        linha   = 1

        print("Captura vai comecar\n")
        time.sleep(1)
        while (time.time() < duracao):
            tempo = datetime.datetime.now().strftime("%H:%M:%S.%f")
            sinaisArduino = self.conArduino.readline()  # Leitura de dois sensores: GSR e ECG
            contador += 1

            # Separar os dados dos dois sensores (GSR e ECG)
            if "GSR" in sinaisArduino:
                gsr = sinaisArduino
            else:
                ecg = sinaisArduino

            print(tempo,
                  contador,
                  usuario,
                  sessao_id,
                  self.mindWave.attention,
                  self.mindWave.meditation,
                  self.mindWave.rawValue,
                  self.mindWave.delta,
                  self.mindWave.theta,
                  self.mindWave.lowAlpha,
                  self.mindWave.highAlpha,
                  self.mindWave.lowBeta,
                  self.mindWave.highBeta,
                  self.mindWave.lowGamma,
                  self.mindWave.midGamma,
                  self.mindWave.poorSignal,
                  self.mindWave.blinkStrength,
                  gsr,
                  ecg)
            planilha.escrita_xlsx(linha, tempo, contador, self.mindWave, gsr, ecg)
            linha += 1

        planilha.fecha_xlsx()
        return contador
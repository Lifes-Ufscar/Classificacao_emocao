
from NeuroPy import NeuroPy
from Planilha import Amostra
import serial
import time
import datetime

class CapturaSinais():

    def __init__(self):
        # Porta COM do MindWave USB Adapter
        self.mindWave = NeuroPy("COM13")
        self.mindWave.start()
        #print("\n" + "\33[42m" + "- NeuroPY inicializado")
        print("\n- NeuroPY inicializado")
        time.sleep(1)

        # Porta COM do Arduino
        # Abre porta serial
        self.arduino = serial.Serial("COM15", "9600")
        #print("- Porta serial aberta" + "\33[0m")
        print("- Porta serial aberta")
        time.sleep(1)

    def captura_sensores(self, usuario, sessao_id, filme_id):
        ecg = " "
        gsr = " "
        contador = 1
        coluna = 1

        #planilha = Amostra(usuario, sessao_id)
        planilha = Amostra(usuario, sessao_id, filme_id)

        # Setagem de intervalo de captura
        #t = input("Tempo do video [em s]: ")
        delay = 100 * 1  # 1 loop de 10 segundos
        duracao = time.time() + delay

        print("Captura do usuario " + usuario.upper() + " vai comecar em 1 segundo\n")
        time.sleep(1)
        while (time.time() < duracao):
            tempo = datetime.datetime.now().strftime("%H:%M:%S.%f")
            serial = self.arduino.readline()  # Leitura de dois sensores: GSR e ECG

            # Separar os dados dos dois sensores (GSR e ECG)
            if "GSR" in serial:
                aux = serial
                gsr = aux.replace("GSR", "")
            else:
                aux = serial
                ecg = aux.replace("ECG", "")

            print(contador,
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
                  ecg,
                  tempo)

            planilha.escrita_xlsx(coluna, contador, self.mindWave, gsr, ecg, tempo)

            coluna += 1
            contador += 1

        planilha.fecha_xlsx()
        return contador
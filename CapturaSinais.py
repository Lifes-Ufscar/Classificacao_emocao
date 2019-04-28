
from NeuroPy  import NeuroPy
from Planilha import Amostra
import serial
import time
import datetime


class CapturaSinais():

    def __init__(self):
        # Porta COM do MindWave USB Adapter
        self.mindWave = NeuroPy("COM13")
        self.mindWave.start()
        print("\n- NeuroPY inicializado")

        # Porta COM do Arduino
        self.arduino = serial.Serial("COM15", "9600")  # Abre porta serial
        print("- Porta serial aberta")

    def captura_sensores(self, usuario, sessao_id):
        ecg = " "
        gsr = " "
        contador = 0
        coluna   = 1

        planilha = Amostra(usuario, sessao_id)

        # Setagem de intervalo de captura
        delay   = 10 * 1  # 1 loop de 10 segundos
        duracao = time.time() + delay

        print("Captura vai comecar\n")
        time.sleep(1)
        while (time.time() < duracao):
            tempo = datetime.datetime.now().strftime("%H:%M:%S.%f")
            serial = self.arduino.readline()  # Leitura de dois sensores: GSR e ECG
            contador += 1

            # Separar os dados dos dois sensores (GSR e ECG)
            if "GSR" in serial:
                aux = serial
                gsr = aux.replace("GSR", "")
            else:
                aux = serial
                ecg = aux.replace("ECG", "")

            print(contador,
                  tempo,
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
            planilha.escrita_xlsx(coluna, tempo, contador, self.mindWave, gsr, ecg)
            coluna += 1

        planilha.fecha_xlsx()
        return contador
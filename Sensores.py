
from NeuroPy import NeuroPy
import serial
import time
import datetime

class Sensores():

    def __init__(self, arduino = "COM15", mindwave = "COM13"):
        self.ecg = " "
        self.gsr = " "

        if(isinstance(arduino, str)):
            self.set_arduino(arduino)
        
        if(isinstance(mindwave, str)):
            self.set_mindwave(mindwave)

    # Seta porta COM do Arduino e abre a porta serial
    def set_arduino(self, porta):
        self.arduino = serial.Serial(porta, "9600")  
        print("- Porta serial aberta")

    # Retorna arduino
    def get_arduino(self):
        return self.arduino

    # Seta porta COM do MindWave e o inicializa
    def set_mindwave(self, porta):
        self.mindWave = NeuroPy(porta)
        self.mindWave.start()
        print("- NeuroPY inicializado")

    # Retorna MindWave
    def get_mindwave(self):
        return self.mindWave

    # Retorna sinal GSR
    def get_gsr(self):
        return self.gsr
    
    # Retorna sinal ECG
    def get_ecg(self):
        return self.ecg

    def print_sinais(self, contador, tempo, usuario, id_sessao):
        print(contador,
              tempo,
              usuario,
              id_sessao,
              self.get_mindwave().attention,
              self.get_mindwave().meditation,
              self.get_mindwave().rawValue,
              self.get_mindwave().delta,
              self.get_mindwave().theta,
              self.get_mindwave().lowAlpha,
              self.get_mindwave().highAlpha,
              self.get_mindwave().lowBeta,
              self.get_mindwave().highBeta,
              self.get_mindwave().lowGamma,
              self.get_mindwave().midGamma,
              self.get_mindwave().poorSignal,
              self.get_mindwave().blinkStrength,
              self.get_gsr(),
              self.get_ecg())

    # Leitura dos sensores do arduino e do MindWave
    def leitura_sinais(self, usuario, id_sessao, planilha):
        contador = 1
        coluna   = 1

        # Intervalo de captura
        delay = 10 * 1  # 1 loop de 10 segundos
        tempo = time.time() + delay

        time.sleep(1)
        while(time.time() < tempo):
            tempo  = datetime.datetime.now().strftime("%H:%M:%S.%f")
            serial = self.get_arduino().readline()  # Leitura de dois sensores: GSR e ECG

            # Separa os dados dos sensores GSR e ECG
            if("GSR" in serial):
                aux = serial
                self.gsr = aux.replace("GSR", "")
            else:
                aux = serial
                self.ecg = aux.replace("ECG", "")

            self.print_sinais(contador, tempo, usuario, id_sessao)

            planilha.escrever_xlsx(coluna, contador, tempo, self.get_mindwave(), self.get_gsr(), self.get_ecg())
            coluna += 1
            contador += 1

        return contador
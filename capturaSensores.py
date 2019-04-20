# -*- coding: utf-8 -*-
# #!/usr/bin/env python
#
# Sequência: Inicializações -> Servidor -> Função capturaSensores (loop) -> (Possível) Servidor
#


from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse       import OptionParser
from NeuroPy        import NeuroPy
import serial
import time
import datetime
import xlsxwriter
import sys


#  -------------------------------------------------
# |                 Inicializações                 |
#  ------------------------------------------------
# Porta COM do MindWave USB Adapter
mindwave = NeuroPy("COM13")
mindwave.start()
print("\nNEUROPY INICIALIZADO\n")

# Porta COM do Arduino
conexao = serial.Serial("COM15", 9600)  # Abre porta serial
print("PORTA SERIAL ABERTA\n")

# Para resolver o seguinte problema:
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 10: ordinal not in range(128)
reload(sys)
sys.setdefaultencoding('utf-8')


#  -------------------------------------------------
# |               Captura de sinais                |
#  ------------------------------------------------
def capturaSensores(user, session_id, planilha, bold):
    
    # Variáveis para a planilha
    col = 0
    row = 1
    
    # Setagem de intervalo de captura
    delay = 30 * 1
    duracao = time.time() + delay

    ecg = " "
    gsr = " "
    contador = 0
    
    print("CAPTURA INICIALIZADA\n")
    while(time.time() < duracao):
        tempo = datetime.datetime.now().strftime("%H:%M:%S.%f")
        leitura = conexao.readline()  # Leitura de dois sensores: GSR e ECG
        contador += 1

        # Separar os dados dos dois sensores (GSR e ECG)
        if "GSR" in leitura:
            gsr = leitura
        else:
            ecg = leitura

        print(tempo,
              contador,
              user,
              session_id,
              mindwave.attention,
              mindwave.meditation,
              mindwave.rawValue,
              mindwave.delta,
              mindwave.theta,
              mindwave.lowAlpha,
              mindwave.highAlpha,
              mindwave.lowBeta,
              mindwave.highBeta,
              mindwave.lowGamma,
              mindwave.midGamma,
              mindwave.poorSignal,
              mindwave.blinkStrength,
              gsr,
              ecg)

        # Escrita dos sinais fisiológicos na planilha
        planilha.write(row, col,      tempo)
        planilha.write(row, col + 1,  contador)
        planilha.write(row, col + 2,  user)
        planilha.write(row, col + 3,  session_id)
        planilha.write(row, col + 4,  mindwave.attention)
        planilha.write(row, col + 5,  mindwave.meditation)
        planilha.write(row, col + 6,  mindwave.rawValue)
        planilha.write(row, col + 7,  mindwave.delta)
        planilha.write(row, col + 8,  mindwave.theta)
        planilha.write(row, col + 9,  mindwave.lowAlpha)
        planilha.write(row, col + 10, mindwave.highAlpha)
        planilha.write(row, col + 11, mindwave.lowBeta)
        planilha.write(row, col + 12, mindwave.highBeta)
        planilha.write(row, col + 13, mindwave.lowGamma)
        planilha.write(row, col + 14, mindwave.midGamma)
        planilha.write(row, col + 15, mindwave.poorSignal)
        planilha.write(row, col + 16, mindwave.blinkStrength)
        planilha.write(row, col + 17, gsr)
        planilha.write(row, col + 18, ecg)
        row += 1


# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
# Written by Nathan Hamiel (2010)
class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")


    def do_POST(self):
        request_path = self.path

        print("\n----- Request Start ----->\n")
        print(request_path)

        request_headers = self.headers

        user = request_headers.getheaders('user')
        session_id = request_headers.getheaders('session_id')

        user = str(user)
        user = user.replace("['", "")
        user = user.replace("']", "")

        session_id = str(session_id)
        session_id = session_id.replace("['", "")
        session_id = session_id.replace("']", "")

        # Planilha
        workbook = xlsxwriter.Workbook("amostras/amostra_"+ user + "_" +session_id + ".xlsx")
        planilha = workbook.add_worksheet()

        # Destacar texto de células das categorias
        bold = workbook.add_format({'bold': True})

        # Categorias de células
        planilha.write('A1', 'Tempo', bold)
        planilha.write('B1', 'Contador', bold)
        planilha.write('C1', 'Usuário', bold)
        planilha.write('D1', 'ID Sessão', bold)
        planilha.write('E1', 'Atenção', bold)
        planilha.write('F1', 'Meditação', bold)
        planilha.write('G1', 'Raw Value', bold)
        planilha.write('H1', 'Delta', bold)
        planilha.write('I1', 'Theta', bold)
        planilha.write('J1', 'Low Alpha', bold)
        planilha.write('K1', 'High Alpha', bold)
        planilha.write('L1', 'Low Beta', bold)
        planilha.write('M1', 'High Beta', bold)
        planilha.write('N1', 'Low Gamma', bold)
        planilha.write('O1', 'Mid Gamma', bold)
        planilha.write('P1', 'Poor Signal', bold)
        planilha.write('Q1', 'Blink Strength', bold)
        planilha.write('R1', 'GSR', bold)
        planilha.write('S1', 'ECG', bold)
        print("\nPLANILHA CRIADA COM SUCESSO\n")

        # Chama a função de captura de sinais
        capturaSensores(user, session_id, planilha, bold)

        # Fecha e salva a planilha
        workbook.close()
        
        # length = int(content_length[0]) if content_length else 0

        print("\n<----- Request End -----\n")

        self.send_response(200)

    do_PUT = do_POST
    do_DELETE = do_GET


def main():
    port = 8080
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will echo out any GET or POST parameters\n"
                    "Run:\n\n"
                    "   reflect")
    (options, args) = parser.parse_args()

    main()
# -*- coding: utf-8 -*-
# #!/usr/bin/env python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse       import OptionParser
from NeuroPy        import NeuroPy
import serial
import datetime


'''- - - - - - - - - - - - - 
| Inicializações             |
| (Formato para Windows)     |
 - - - - - - - - - - - - - '''
# Porta COM do MindWave USB Adapter
mindwave = NeuroPy("COM13")
mindwave.start()
print("\nNeuroPY inicializado\n")

# Porta COM do Arduino
conexao = serial.Serial("COM11", 9600)  # Abre porta serial
print("Portal serial aberta\n")


def capturaSensores(user, session_id):
    print ("\nCaptura iniciada\n")

    ecg = " "
    gsr = " "
    contador = 0
    
    print("Início da captura:", datetime.datetime.now().strftime("%H:%M:%S.%f"))

    while(True):
        #tempo    = datetime.datetime.now().strftime("%H:%M:%S")
        tempo    = datetime.datetime.now().strftime("%H:%M:%S.%f")
        contador = contador + 1
        leituras = conexao.readline()  # Leitura de dois sensores: GSR e ECG

        # Separar os dados dos dois sensores
        if 'GSR' in leituras:
            gsr = leituras
        else:
            ecg = leituras

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
        '''
        ID_sessao     = session_id
        ID_usuario    = datas_user
        attention     = mindwave.attention
        meditation    = mindwave.meditation
        rawValue      = mindwave.rawValue
        theta         = mindwave.theta
        delta         = mindwave.delta
        lowAlpha      = mindwave.lowAlpha
        highAlpha     = mindwave.highAlpha
        lowBeta       = mindwave.lowBeta
        highBeta      = mindwave.highBeta
        lowGamma      = mindwave.lowGamma
        midGamma      = mindwave.midGamma
        poorSignal    = mindwave.poorSignal
        blinkStrength = mindwave.blinkStrength

        con = connector.Connect(user='root', password='', database='emobd10', host='localhost')
        cur = con.cursor()

        sql = 'insert into dados_sensores (horas, cont, ID_filmes, ID_sessao, ID_usuario, attention, meditation, rawValue, theta, delta,' \
              'lowAlpha, highAlpha, lowBeta, highBeta, lowGamma, midGamma, poorSignal, blinkStrength, gsr, ecg) values (%s, %s, %s, %s, %s, %s, %s, %s' \
              ', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

        cur.execute("""insert into pessoa (Nome, Sobrenome, Idade, Profissao) values (Nome, Sobrenome, Idade, Profissao);""")
        cur.execute(sql, dados)
        con.commit()
        con.close()

        # Comentar ate aqui

        cnx = mysql.connector.connect(user='root', host='localhost', database='emmoweb')
        cursor = cnx.cursor()

        cursor.execute("INSERT INTO sensors (id, user_id, movie_name, start_time, session_id, attention, meditation, rawValue, delta, theta, lowAlpha, highAlpha, lowBeta, highBeta, lowGamma, midGamma, poorSignal, blinkStrength, gsr, ecg) VALUES ('3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1')")
        cursor.execute('INSERT INTO TABELA (CAMPO1, CAMPO2, CAMPO3) VALUES (?,?,?)', (valor1, valor2, valor3))

        cnx.close()
        '''

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
        # start_time = request_headers.getheaders('start_time')
        # movie_name = request_headers.getheaders('movie_name')

        user = str(user)
        user = user.replace("['", "")
        user = user.replace("']", "")

        session_id = str(session_id)
        session_id = session_id.replace("['", "")
        session_id = session_id.replace("']", "")

        '''
        start_time = str(start_time)
        start_time = start_time.replace("['", "")
        start_time = start_time.replace("']", "")

        movie_name = str(movie_name)
        movie_name = movie_name.replace("['", "")
        movie_name = movie_name.replace("']", "")
        '''

        capturaSensores(user, session_id)

        # length = int(content_length[0]) if content_length else 0

        print("<----- Request End -----\n")

        self.send_response(200)

    do_PUT = do_POST
    do_DELETE = do_GET


def main():
    port = 8081
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
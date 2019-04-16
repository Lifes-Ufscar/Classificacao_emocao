# -*- coding: utf-8 -*-
# #!/usr/bin/env python

from NeuroPy import NeuroPy
import serial
import datetime
#import xlsxwriter  # Para escrita dos dados em uma planilha


#  --------------------------------------------------
# |          Inicializações (para Windows)          |
#  -------------------------------------------------
# Porta COM do MindWave USB Adapter
mindwave = NeuroPy("COM13")
mindwave.start()
print("\nNEUROPY INICIALIZADO\n")

# Porta COM do Arduino
conexao = serial.Serial("COM11", 9600)  # Abre porta serial
print("PORTA SERIAL ABERTA\n")


#  --------------------------------------------------
# |                Captura de sinais                |
#  -------------------------------------------------
def capturaSensores(user, session_id):
    print ("\nCAPTURA INICIALIZADA\n")

    ecg = " "
    gsr = " "
    contador = 0
    
    print("INÍCIO CAPTURA:", datetime.datetime.now().strftime("%H:%M:%S.%f"))

    while(True):
        #tempo    = datetime.datetime.now().strftime("%H:%M:%S")
        tempo    = datetime.datetime.now().strftime("%H:%M:%S.%f")
        contador = contador + 1
        leituras = conexao.readline()  # Leitura de dois sensores: GSR e ECG

        # Separar os dados dos dois sensores
        if "GSR" in leituras:
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
        
#        # Escrita (e criação) em um arquivo excel
#        wbook = xlsxwriter.Workbook("amostras_GSR.xlsx")
#        sheet = wbook.add_worksheet()
#         
#        sheet.write("A1", "Planilha teste")
#        
#        wbook.close()
        
#        # Armazenamento no banco de dados
#        ID_sessao     = session_id
#        ID_usuario    = datas_user
#        attention     = mindwave.attention
#        meditation    = mindwave.meditation
#        rawValue      = mindwave.rawValue
#        theta         = mindwave.theta
#        delta         = mindwave.delta
#        lowAlpha      = mindwave.lowAlpha
#        highAlpha     = mindwave.highAlpha
#        lowBeta       = mindwave.lowBeta
#        highBeta      = mindwave.highBeta
#        lowGamma      = mindwave.lowGamma
#        midGamma      = mindwave.midGamma
#        poorSignal    = mindwave.poorSignal
#        blinkStrength = mindwave.blinkStrength
#
#        con = connector.Connect(user='root', password='', database='emobd10', host='localhost')
#        cur = con.cursor()
#
#        sql = 'INSERT INTO dados_sensores (horas, cont, ID_filmes, ID_sessao, ID_usuario, attention, meditation, rawValue, theta, delta,' \
#              'lowAlpha, highAlpha, lowBeta, highBeta, lowGamma, midGamma, poorSignal, blinkStrength, gsr, ecg) ' \ 
#              'VALUES ' \ 
#              '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
#
#        cur.execute("""INSERT INTO pessoa (Nome, Sobrenome, Idade, Profissao) VALUES (Nome, Sobrenome, Idade, Profissao);""")
#        cur.execute(sql, dados)
#        con.commit()
#        con.close()
#        # Comentar ate aqui
#
#        cnx = mysql.connector.connect(user='root', host='localhost', database='emmoweb')
#        cursor = cnx.cursor()
#
#        insert = 'INSERT INTO sensors(id, user_id, movie_name, start_time, session_id, attention, meditation, rawValue, delta, theta, lowAlpha, highAlpha,' \ 
#                                     'lowBeta, highBeta, lowGamma, midGamma, poorSignal, blinkStrength, gsr, ecg) ' \
#                                     'VALUES ' \  
#                                     '('3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1')'
#        cursor.execute(insert)
#        cursor.execute('INSERT INTO TABELA (CAMPO1, CAMPO2, CAMPO3) VALUES (?,?,?)', (valor1, valor2, valor3))
#
#        cnx.close()
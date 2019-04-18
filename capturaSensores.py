# -*- coding: utf-8 -*-
# #!/usr/bin/env python

from NeuroPy import NeuroPy
import serial
import datetime
import xlsxwriter  # Para escrita dos dados em uma planilha


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
    
    # Propósito de testes
    user = "u1"
    session_id = "sid1"
    
    # Escrita (e criação) em um arquivo excel
    # TODA VEZ QUE EXECUTA, O ARQUIVO ANTERIOR COM MESMO
    # NOME SERÁ SOBRESCRITO, OU SEJA, SERÁ(ÃO) PERDIDO(S)
    # O(S) DADO(S) QUE TINHAM ANTERIORMENTE!
    titulo   = "amostras_" + user + "_" + session_id + ".xlsx"
    workbook = xlsxwriter.Workbook(titulo)
    planilha = workbook.add_worksheet()
    
    # Destacar texto de células das categorias
    bold = workbook.add_format({'bold': True})
    
    # Variáveis para a planilha
    col = 0
    row = 1
    valor = 0
    
#    # Categorias de células
#    planilha.write('A1', 'Tempo',          bold)
#    planilha.write('B1', 'Contador',       bold)
#    planilha.write('C1', 'Usuário',        bold)
#    planilha.write('D1', 'ID Sessão',      bold)
#    planilha.write('E1', 'Atenção',        bold)
#    planilha.write('F1', 'Meditação',      bold)
#    planilha.write('G1', 'Raw Value',      bold)
#    planilha.write('H1', 'Delta',          bold)
#    planilha.write('I1', 'Theta',          bold)
#    planilha.write('J1', 'Low Alpha',      bold)
#    planilha.write('K1', 'High Alpha',     bold)
#    planilha.write('L1', 'Low Beta',       bold)
#    planilha.write('M1', 'High Beta',      bold)
#    planilha.write('N1', 'Low Gamma',      bold)
#    planilha.write('O1', 'Mid Gamma',      bold)
#    planilha.write('P1', 'Poor Signal',    bold)
#    planilha.write('Q1', 'Blink Strength', bold)
#    planilha.write('R1', 'GSR',            bold)
#    planilha.write('S1', 'ECG',            bold)
    
    # Propósito de testes
    # Categorias de células (sem 'Usuário' e 'ID Sessão')
    planilha.write('A1', 'Tempo',          bold)
    planilha.write('B1', 'Contador',       bold)
    planilha.write('C1', 'Atenção',        bold)
    planilha.write('D1', 'Meditação',      bold)
    planilha.write('E1', 'Raw Value',      bold)
    planilha.write('F1', 'Delta',          bold)
    planilha.write('G1', 'Theta',          bold)
    planilha.write('H1', 'Low Alpha',      bold)
    planilha.write('I1', 'High Alpha',     bold)
    planilha.write('J1', 'Low Beta',       bold)
    planilha.write('K1', 'High Beta',      bold)
    planilha.write('L1', 'Low Gamma',      bold)
    planilha.write('M1', 'Mid Gamma',      bold)
    planilha.write('N1', 'Poor Signal',    bold)
    planilha.write('O1', 'Blink Strength', bold)
    planilha.write('P1', 'GSR',            bold)
    planilha.write('Q1', 'ECG',            bold)
    
    print("INÍCIO CAPTURA:", datetime.datetime.now().strftime("%H:%M:%S.%f"))

    while(True):
        #tempo    = datetime.datetime.now().strftime("%H:%M:%S")
        tempo    = datetime.datetime.now().strftime("%H:%M:%S.%f")
        leitura  = conexao.readline()  # Leitura de dois sensores: GSR e ECG
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
        
#        # Propósito de testes
#        # Print sem 'user' e 'session ID', pois são salvos
#        # no nome do arquivo da planilha.
#        print(tempo,
#              contador,
#              mindwave.attention,
#              mindwave.meditation,
#              mindwave.rawValue,
#              mindwave.delta,
#              mindwave.theta,
#              mindwave.lowAlpha,
#              mindwave.highAlpha,
#              mindwave.lowBeta,
#              mindwave.highBeta,
#              mindwave.lowGamma,
#              mindwave.midGamma,
#              mindwave.poorSignal,
#              mindwave.blinkStrength,
#              gsr,
#              ecg)
#        
#        # Escrita dos sinais fisiológicos na planilha
#        planilha.write(row, col,      tempo)
#        planilha.write(row, col + 1,  contador)
#        planilha.write(row, col + 2,  user)
#        planilha.write(row, col + 3,  session_id)
#        planilha.write(row, col + 4,  mindwave.attention)
#        planilha.write(row, col + 5,  mindwave.meditation)
#        planilha.write(row, col + 6,  mindwave.rawValue)
#        planilha.write(row, col + 7,  mindwave.delta)
#        planilha.write(row, col + 8,  mindwave.theta)
#        planilha.write(row, col + 9,  mindwave.lowAlpha)
#        planilha.write(row, col + 10, mindwave.highAlpha)
#        planilha.write(row, col + 11, mindwave.lowBeta)
#        planilha.write(row, col + 12, mindwave.highBeta)
#        planilha.write(row, col + 13, mindwave.lowGamma)
#        planilha.write(row, col + 14, mindwave.midGamma)
#        planilha.write(row, col + 15, mindwave.poorSignal)
#        planilha.write(row, col + 16, mindwave.blinkStrength)
#        planilha.write(row, col + 17, gsr)
#        planilha.write(row, col + 18, ecg)
#        row += 1
    
    # Propósito de testes
    # Teste para escrita na planilha (sem 'Usuário' e 'ID Sessão')
    print("INÍCIO ESCRITA EXCEL:", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    for i in range(0, 99999):
        planilha.write(row, col,      valor)
        planilha.write(row, col + 1,  valor)
        planilha.write(row, col + 2,  valor)
        planilha.write(row, col + 3,  valor)
        planilha.write(row, col + 4,  valor)
        planilha.write(row, col + 5,  valor)
        planilha.write(row, col + 6,  valor)
        planilha.write(row, col + 7,  valor)
        planilha.write(row, col + 8,  valor)
        planilha.write(row, col + 9,  valor)
        planilha.write(row, col + 10, valor)
        planilha.write(row, col + 11, valor)
        planilha.write(row, col + 12, valor)
        planilha.write(row, col + 13, valor)
        planilha.write(row, col + 14, valor)
        planilha.write(row, col + 15, valor)
        planilha.write(row, col + 16, valor)
        row += 1
        valor += 1.1
    print("FIM ESCRITA EXCEL:", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    workbook.close()
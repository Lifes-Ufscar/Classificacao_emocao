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
    
    # Escrita (e criação) em um arquivo excel
    # TODA VEZ QUE EXECUTA, O ARQUIVO ANTERIOR COM MESMO
    # NOME SERÁ SOBRESCRITO, OU SEJA, SERÁ(ÃO) PERDIDO(S)
    # O(S) DADO(S) QUE TINHAM ANTERIORMENTE!
    workbook = xlsxwriter.Workbook("amostras_teste.xlsx")
    worksheet = workbook.add_worksheet()
    
    # Destacar texto de células das categorias
    bold = workbook.add_format({'bold': True})
    
    # Variáveis para a planilha
    col = 0
    row = 1
    valor = 0
    
    # Categorias de células
    worksheet.write('A1', 'Tempo',          bold)
    worksheet.write('B1', 'Contador',       bold)
    worksheet.write('C1', 'Usuário',        bold)
    worksheet.write('D1', 'ID Sessão',      bold)
    worksheet.write('E1', 'Atenção',        bold)
    worksheet.write('F1', 'Meditação',      bold)
    worksheet.write('G1', 'Raw Value',      bold)
    worksheet.write('H1', 'Delta',          bold)
    worksheet.write('I1', 'Theta',          bold)
    worksheet.write('J1', 'Low Alpha',      bold)
    worksheet.write('K1', 'High Alpha',     bold)
    worksheet.write('L1', 'Low Beta',       bold)
    worksheet.write('M1', 'High Beta',      bold)
    worksheet.write('N1', 'Low Gamma',      bold)
    worksheet.write('O1', 'Mid Gamma',      bold)
    worksheet.write('P1', 'Poor Signal',    bold)
    worksheet.write('Q1', 'Blink Strength', bold)
    worksheet.write('R1', 'GSR',            bold)
    worksheet.write('S1', 'ECG',            bold)
    
    print("INÍCIO CAPTURA:", datetime.datetime.now().strftime("%H:%M:%S.%f"))

    while(True):
        #tempo    = datetime.datetime.now().strftime("%H:%M:%S")
        tempo    = datetime.datetime.now().strftime("%H:%M:%S.%f")
        contador += 1
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
        
    # Teste para escrita em um arquivo excel
    # Para 100 mil "amostras" leva cerca de 9 segundos
    print("INÍCIO ESCRITA EXCEL:", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    for i in range(0, 99999):
        worksheet.write(row, col,      valor)
        worksheet.write(row, col + 1,  valor)
        worksheet.write(row, col + 2,  valor)
        worksheet.write(row, col + 3,  valor)
        worksheet.write(row, col + 4,  valor)
        worksheet.write(row, col + 5,  valor)
        worksheet.write(row, col + 6,  valor)
        worksheet.write(row, col + 7,  valor)
        worksheet.write(row, col + 8,  valor)
        worksheet.write(row, col + 9,  valor)
        worksheet.write(row, col + 10, valor)
        worksheet.write(row, col + 11, valor)
        worksheet.write(row, col + 12, valor)
        worksheet.write(row, col + 13, valor)
        worksheet.write(row, col + 14, valor)
        worksheet.write(row, col + 15, valor)
        worksheet.write(row, col + 16, valor)
        worksheet.write(row, col + 17, valor)
        worksheet.write(row, col + 18, valor)
        row += 1
        valor += 1.1
    print("FIM ESCRITA EXCEL:", datetime.datetime.now().strftime("%H:%M:%S.%f"))
    workbook.close()
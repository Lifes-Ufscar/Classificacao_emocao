# -*- coding: utf-8 -*-

import datetime
from mysql import connector

ID_Site = '1'
ID_Sessao = '1'
ID_Usuario = '1'
start_time = '1'


attention = '1001'
meditation = '1002'
rawValue = '1003'
theta = '1004'
delta = '1005'
lowAlpha = '1006'
highAlpha = '1007'
lowBeta = '1008'
highBeta = '1009'
lowGamma = '1010'
midGamma = '1011'
poorSignal = '1012'
blinkStrength = '1013'




cont = 0
ecg = 2000
gsr = 2000

while True:
        #sleep(1)
    cont = cont + 1
    
    Horas =  datetime.datetime.now().strftime("%H:%M:%S.%f")
    #horas = time.strftime('%H:%M:%S')
    #current_time = datetime.datetime().now()
    #leitura1 = conexao.readline()
    #leitura2 = conexao.readline()
    '''
    if 'GSR' in leitura1:
        gsr = leitura1
    
    else:
        ecg = leitura1
    
    '''
    #send_datas(datas_user,neuropy.attention)
    
    print(Horas,
          cont,
          ID_Site,
          ID_Sessao,
          ID_Usuario,
          attention,
          meditation,
          rawValue,
          delta,
          theta,
          lowAlpha,
          highAlpha,
          lowBeta,
          highBeta,
          lowGamma,
          midGamma,
          poorSignal,
          blinkStrength,
          gsr,
          ecg)
    
    dados = (Horas, cont, ID_Site, ID_Sessao, ID_Usuario, attention, meditation, rawValue, delta, theta, lowAlpha, highAlpha, lowBeta, highBeta, lowGamma, midGamma, poorSignal, blinkStrength, gsr,ecg)
    
    cnx = connector.Connect(user='root', password='', database='teste_emoweb', host='localhost')    
    
    cursor = cnx.cursor()
    
    sql = 'INSERT INTO dados_sensores (Horas, Cont, ID_Site, ID_Sessao, ID_Usuario, attention, meditation, rawValue, theta, delta, lowAlpha, highAlpha, lowBeta, highBeta, lowGamma, midGamma, poorSignal, blinkStrength, gsr, ecg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
   
    
    
    cursor.execute(sql, dados)
    
    cnx.commit()
    
    cnx.close()
    
    print("\n aqui")
    
    ######################

    
    
    
    
    
    
    
    
    
    
        

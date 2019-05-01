# -*- coding: utf-8 -*-

# Bibliotecas
from pandas import read_excel
import numpy as np
from classificadorGSR import ClassificadorGSR  # LDA e Classificador GSR
from classificadorECG import ClassificadorECG  # LDA e Classificador ECG
from classificadorEEG import ClassificadorEEG  # LDA e Classificador EEG
import pickle


#  ----------------------------------
# |               ECG EEG GSR               |
#  ---------------------------------
# Leitura das amostras
df = read_excel('amostras//amostra_Bareta_sid2_f3.xlsx', sheet_name = 'Sheet1')

dfgsr = df.iloc[13:14, 1:]
dfecg = df.iloc[14:15, 2:]
dfeeg = df.iloc[0:13, 1:] 

tamanhoamostragsr = dfgsr.size
a = 3000
i = 0
ecga = 1020
ecgi = 0
intervalo = 0

print("\nTESTE INICIADO\n")
while a <= tamanhoamostragsr :
     
    print("\nIntervalo", intervalo)
#####GSR###      
    amostrasgsr = dfgsr.iloc[: , i:a].values  
     
    classeGSR = ClassificadorGSR(amostrasgsr)
    GSR = classeGSR.classificador_gsr()
        
    print("Resultado GSR###:", GSR)
####ECG###         
           
    amostrasecg = dfecg.iloc[: , ecgi:ecga].values  
    #print("i --", i)
    #print("a --", a)
    #print("Intervalo", amostrasgsr.size)
    classeECG = ClassificadorECG(amostrasecg)
    ECG = classeECG.classificador_ecg()
    
    print("Resultado ECG###:", ECG)  
          
###EEG###          
    sinaldelta = dfeeg.iloc[3:4, i:a].values
    sinaltheta = dfeeg.iloc[4:5, i:a].values
    sinallowAlpha = dfeeg.iloc[5:6, i:a].values
    sinalhighAlpha = dfeeg.iloc[6:7, i:a].values
    sinallowBeta = dfeeg.iloc[7:8, i:a].values
    sinalhighBeta = dfeeg.iloc[8:9, i:a].values
    sinallowGamma = dfeeg.iloc[9:10, i:a].values
    sinalmidGamma = dfeeg.iloc[10:11, i:a].values  
    
    classeEEG = ClassificadorEEG(sinaldelta, 
                                 sinalhighAlpha, sinalhighBeta,
                                 sinallowAlpha,  sinallowBeta,
                                 sinallowGamma,  sinalmidGamma,
                                 sinaltheta)
    EEG = classeEEG.classificador_eeg()
     
    print("Resultado EEG###:", EEG)

          
    
    i= i+500
    a = a+500
    ecgi= ecgi+500
    ecga = ecga+500
    intervalo = intervalo +1 
    
    


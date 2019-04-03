# -*- coding: utf-8 -*-

'''
    Autor: Isaque Elcio

    Descrição:
        
'''

# Bibliotecas
from pandas import read_excel
#import numpy  as np
#import pickle
#from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


#  -----------------------------
# |             GSR             |
#  -----------------------------

# Dados teste GSR
df = read_excel('dadosGSR//amostras_GSR.xlsx', sheet_name='Planilha1')
x  = df.values

# LDA e Classificador GSR
from classificadorGSR import ClassificadorGSR
# Teste com amostras
for i in range(0,4):
    teste = [x[i]]
    classeGSR = ClassificadorGSR(teste)
    GSR = classeGSR.classificador_gsr()
    print("i:", i)
    print("Resulado GSR:", GSR)


#  -----------------------------
# |             ECG             |
#  -----------------------------

# Dados teste ECG
df = read_excel('dadosECG//amostras_ECG.xlsx', sheet_name='Planilha1')
x  = df.values

# LDA e Classificador ECG
from classificadorECG import ClassificadorECG
# Teste com amostras
for i in range(0, 4):
    teste = [x[i]]
    classeECG = ClassificadorECG(teste)
    ECG = classeECG.classificador_ecg()
    print("i:", i)
    print("Resulado ECG:", ECG)
 
    
#  -----------------------------
# |             EEG             |
#  -----------------------------
    
# Dados teste EEG
delta = read_excel('dadosEEG//amostras_delta.xlsx', sheet_name='Sheet1')
delta = delta.values

highAlpha = read_excel('dadosEEG//amostras_highAlpha.xlsx', sheet_name='Sheet1')
highAlpha = highAlpha.values

highBeta = read_excel('dadosEEG//amostras_highBeta.xlsx', sheet_name='Sheet1')
highBeta = highBeta.values

lowAlpha = read_excel('dadosEEG//amostras_lowAlpha.xlsx', sheet_name='Sheet1')
lowAlpha = lowAlpha.values

lowBeta = read_excel('dadosEEG//amostras_lowBeta.xlsx', sheet_name='Sheet1')
lowBeta = lowBeta.values

lowGamma = read_excel('dadosEEG//amostras_lowGamma.xlsx', sheet_name='Sheet1')
lowGamma = lowGamma.values

midGamma = read_excel('dadosEEG//amostras_midGamma.xlsx', sheet_name='Sheet1')
midGamma = midGamma.values

theta = read_excel('dadosEEG//amostras_theta.xlsx', sheet_name='Sheet1')
theta = theta.values

# LDA e Classificador EEG
from classificadorEEG import ClassificadorEEG
# Teste com amostras
print("\nTESTE EEG")
for i in range(0, 4):
    sinaldelta     = [delta[i]]  
    sinalhighAlpha = [highAlpha[i]] 
    sinalhighBeta  = [highBeta[i]]  
    sinallowAlpha  = [lowAlpha[i]]  
    sinallowBeta   = [lowBeta[i]]  
    sinallowGamma  = [lowGamma[i]]  
    sinalmidGamma  = [midGamma[i]] 
    sinaltheta     = [theta[i]] 
    
    classeEEG = ClassificadorEEG(sinaldelta, 
                                 sinalhighAlpha, sinalhighBeta,
                                 sinallowAlpha,  sinallowBeta,
                                 sinallowGamma,  sinalmidGamma,
                                 sinaltheta)
    EEG = classeEEG.classificador_eeg()
    print("i:", i)
    print("Resulado EEG:", EEG)
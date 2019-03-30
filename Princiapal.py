# -*- coding: utf-8 -*-
#bibliotecas
import pandas as pd
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import pickle

#********Dados teste GSR
df = pd.read_excel('dadosGSR//amostras_GSR.xlsx', sheet_name='Planilha1')
x = df.values
#************************
#**********LDA e Classificador GSR *********
from classificadorGSR import ClassificadorGSR
#********teste com amostras******
for i in range(0,4):
    teste = [x[i]]
    ClasseGSR = ClassificadorGSR(teste)
    GSR = ClasseGSR.classificador_gsr()
    print("i", i)
    print("Resulado GSR",GSR)
#*******************************,

#********Dados teste ECG
df = pd.read_excel('dadosECG//amostras_ECG.xlsx', sheet_name='Planilha1')
x = df.values
#************************



#**********LDA e Classificador ECG *********
from classificadorECG import ClassificadorECG
#********teste com amostras******
for i in range(0, 4):
    teste = [x[i]]
    ClasseECG = ClassificadorECG(teste)
    ECG = ClasseECG.classificador_ecg()
    print("i", i)
    print("Resulado ECG", ECG)
    
#*******************************


#********Dados teste EEG
delta = pd.read_excel('dadosEEG//amostras_delta.xlsx', sheet_name='Sheet1')
delta = delta.values

highAlpha = pd.read_excel('dadosEEG//amostras_highAlpha.xlsx', sheet_name='Sheet1')
highAlpha = highAlpha.values

highBeta = pd.read_excel('dadosEEG//amostras_highBeta.xlsx', sheet_name='Sheet1')
highBeta = highBeta.values

lowAlpha = pd.read_excel('dadosEEG//amostras_lowAlpha.xlsx', sheet_name='Sheet1')
lowAlpha = lowAlpha.values

lowBeta = pd.read_excel('dadosEEG//amostras_lowBeta.xlsx', sheet_name='Sheet1')
lowBeta = lowBeta.values

lowGamma = pd.read_excel('dadosEEG//amostras_lowGamma.xlsx', sheet_name='Sheet1')
lowGamma = lowGamma.values

midGamma = pd.read_excel('dadosEEG//amostras_midGamma.xlsx', sheet_name='Sheet1')
midGamma = midGamma.values

theta = pd.read_excel('dadosEEG//amostras_theta.xlsx', sheet_name='Sheet1')
theta = theta.values


#************************

#**********LDA e Classificador EEG *********
from classificadorEEG import ClassificadorEEG
#********teste com amostras******
for i in range(0, 4):
    
    sinaldelta = [delta[i]]  
    sinalhighAlpha = [highAlpha[i]] 
    sinalhighBeta = [highBeta[i]]  
    sinallowAlpha = [lowAlpha[i]]  
    sinallowBeta = [lowBeta[i]]  
    sinallowGamma = [lowGamma[i]]  
    sinalmidGamma = [midGamma[i]] 
    sinaltheta = [theta[i]] 
    
    
    ClasseEEG = ClassificadorEEG(sinaldelta, sinalhighAlpha, sinalhighBeta, sinallowAlpha, sinallowBeta,
        sinallowGamma, sinalmidGamma, sinaltheta)
    EEG = ClasseEEG.classificador_eeg()
    print("i", i)
    print("Resulado EEG", EEG)

#*******************************


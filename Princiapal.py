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





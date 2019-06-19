# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
import pickle



dfeeg = pd.read_excel('Amostras//amostra_ID1_VD1_UI3.xlsx', sheet_name = 'Sheet1')

#####Delta
lda_deltaa = pickle.load(open('dados_classifica//lda_deltaa.sav', 'rb'))
delta_classificador = pickle.load(open('dados_classifica//delta_classificador.sav', 'rb'))
#####Final Delta

#####highAlpha
lda_highAlphaa = pickle.load(open('dados_classifica//lda_highAlphaa.sav', 'rb'))
highAlpha_classificador = pickle.load(open('dados_classifica//highAlpha_classificador.sav', 'rb'))
#####Final highAlpha

########highBeta
lda_highBetaa = pickle.load(open('dados_classifica//lda_highBetaa.sav', 'rb'))
highBeta_classificador = pickle.load(open('dados_classifica//highBeta_classificador.sav', 'rb'))

#######Fim highBeta

###########lda_lowAlpha
lda_lowAlphaa = pickle.load(open('dados_classifica//lda_lowAlphaa.sav', 'rb'))
lowAlpha_classificador = pickle.load(open('dados_classifica//lowAlpha_classificador.sav', 'rb'))

##########lda_lowAlpha fim

#################lowBeta
lda_lowBetaa = pickle.load(open('dados_classifica//lda_lowBetaa.sav', 'rb'))
lowBeta_classificador = pickle.load(open('dados_classifica//lowBeta_classificador.sav', 'rb'))
#################lowBeta fim
'''
#################lowGamma
lda_lowGamma = pickle.load(open('dados_classifica//lda_lowGamma.sav', 'rb'))
lowGamma_classificador = pickle.load(open('dados_classifica//lowGamma_classificador.sav', 'rb'))
#################lowGamma

################ midGamma
lda_midGamma = pickle.load(open('dados_classifica//lda_midGamma.sav', 'rb'))
midGamma_classificador = pickle.load(open('dados_classifica//midGamma_classificador.sav', 'rb'))
################# fim midGamma 
'''




sinaldeltat = dfeeg.iloc[3:4, 2:]

tamanhoamostra = sinaldeltat.size

dfeeg = dfeeg.iloc[:, 2:]

aa = 800
i = 0
print("\nTESTE EEG INICIADO\n")
while aa <= tamanhoamostra:
    #Delta
    sinaldelta = dfeeg.iloc[3:4, i:aa]
    sinaldelta = sinaldelta.div(sinaldelta.max(axis=1), axis=0)
    sinaldelta = sinaldelta.values
    sinaldelta = sinaldelta.astype(float)
    
    delta = lda_deltaa.transform(sinaldelta)
    
    previsoesdelta = delta_classificador.predict(delta)
    #Final delta
    
    sinalhighAlpha = dfeeg.iloc[6:7, i:aa]
    sinalhighAlpha = sinalhighAlpha.div(sinalhighAlpha.max(axis=1), axis=0)
    sinalhighAlpha = sinalhighAlpha.values
    sinalhighAlpha = sinalhighAlpha.astype(float)
    
    highAlpha = lda_highAlphaa.transform(sinalhighAlpha)
    previsoeshighAlpha = highAlpha_classificador.predict(highAlpha)
    
    #highBeta
    sinalhighBeta = dfeeg.iloc[8:9, i:aa]
    sinalhighBeta = sinalhighBeta.div(sinalhighBeta.max(axis=1), axis=0)
    sinalhighBeta = sinalhighBeta.values
    sinalhighBeta = sinalhighBeta.astype(float)
    
    highBeta = lda_highBetaa.transform(sinalhighBeta)
    previsoeshighBeta = highBeta_classificador.predict(highBeta)
    #highBeta fim
    
    #lowAlpha
    sinallowAlpha = dfeeg.iloc[5:6, i:aa]
    sinallowAlpha = sinallowAlpha.div(sinallowAlpha.max(axis=1), axis=0)
    sinallowAlpha = sinallowAlpha.values
    sinallowAlpha = sinallowAlpha.astype(float)
    
    lowAlpha = lda_lowAlphaa.transform(sinallowAlpha)
    previsoeslowAlpha = lowAlpha_classificador.predict(lowAlpha)
    
    #lowAlpha fim
    
    #lowBeta
    sinallowBeta = dfeeg.iloc[7:8, i:aa]
    sinallowBeta = sinallowBeta.div(sinallowBeta.max(axis=1), axis=0)
    sinallowBeta = sinallowBeta.values
    sinallowBeta = sinallowBeta.astype(float)
    
    lowBeta = lda_lowBetaa.transform(sinallowBeta)
    previsoeslowBeta = lowBeta_classificador.predict(lowBeta)
    
    #lowBeta fim
    
    
    
    
    
    total = (previsoesdelta + previsoeshighAlpha + previsoeshighBeta + previsoeslowAlpha + previsoeslowBeta) / 5
    
    print("delta", previsoesdelta ,"highAlpha", previsoeshighAlpha, "highBeta", previsoeshighBeta, "lowAlpha", previsoeslowAlpha,"lowBeta", previsoeslowBeta)
    
    i= i+50
    aa = aa+50
    total = 0
    
print("\nTESTE EEG FIM\n")
    





 
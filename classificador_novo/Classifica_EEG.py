# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
import pickle



dfeeg = pd.read_excel('Amostras//amostra_ID2_VD1_UI3.xlsx', sheet_name = 'Sheet1')

#####Delta
lda_delta = pickle.load(open('dados_classifica//lda_delta.sav', 'rb'))
delta_classificador = pickle.load(open('dados_classifica//delta_classificador.sav', 'rb'))
#####Final Delta

#####highAlpha
lda_highAlpha = pickle.load(open('dados_classifica//lda_highAlpha.sav', 'rb'))
highAlpha_classificador = pickle.load(open('dados_classifica//highAlpha_classificador.sav', 'rb'))
#####Final highAlpha

########highBeta
lda_highBeta = pickle.load(open('dados_classifica//lda_highBeta.sav', 'rb'))
highBeta_classificador = pickle.load(open('dados_classifica//highBeta_classificador.sav', 'rb'))

#######Fim highBeta

###########lda_lowAlpha
lda_lowAlpha = pickle.load(open('dados_classifica//lda_lowAlpha.sav', 'rb'))
lowAlpha_classificador = pickle.load(open('dados_classifica//lowAlpha_classificador.sav', 'rb'))

##########lda_lowAlpha fim

#################lowBeta
lda_lowBeta = pickle.load(open('dados_classifica//lda_lowBeta.sav', 'rb'))
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

aa = 3000
i = 0
print("\nTESTE EEG INICIADO\n")
while aa <= tamanhoamostra:
    #Delta
    sinaldelta = dfeeg.iloc[3:4, i:aa]
    sinaldelta = sinaldelta.div(sinaldelta.max(axis=1), axis=0)
    sinaldelta = sinaldelta.values
    sinaldelta = sinaldelta.astype(float)
    
    delta = lda_delta.transform(sinaldelta)
    
    previsoesdelta = delta_classificador.predict(delta)
    #Final delta
    
    sinalhighAlpha = dfeeg.iloc[6:7, i:aa]
    sinalhighAlpha = sinalhighAlpha.div(sinalhighAlpha.max(axis=1), axis=0)
    sinalhighAlpha = sinalhighAlpha.values
    sinalhighAlpha = sinalhighAlpha.astype(float)
    
    highAlpha = lda_highAlpha.transform(sinalhighAlpha)
    previsoeshighAlpha = highAlpha_classificador.predict(highAlpha)
    
    #highBeta
    sinalhighBeta = dfeeg.iloc[8:9, i:aa]
    sinalhighBeta = sinalhighBeta.div(sinalhighBeta.max(axis=1), axis=0)
    sinalhighBeta = sinalhighBeta.values
    sinalhighBeta = sinalhighBeta.astype(float)
    
    highBeta = lda_highBeta.transform(sinalhighBeta)
    previsoeshighBeta = highBeta_classificador.predict(highBeta)
    #highBeta fim
    
    #lowAlpha
    sinallowAlpha = dfeeg.iloc[5:6, i:aa]
    sinallowAlpha = sinallowAlpha.div(sinallowAlpha.max(axis=1), axis=0)
    sinallowAlpha = sinallowAlpha.values
    sinallowAlpha = sinallowAlpha.astype(float)
    
    lowAlpha = lda_lowAlpha.transform(sinallowAlpha)
    previsoeslowAlpha = lowAlpha_classificador.predict(lowAlpha)
    
    #lowAlpha fim
    
    #lowBeta
    sinallowBeta = dfeeg.iloc[7:8, i:aa]
    sinallowBeta = sinallowBeta.div(sinallowBeta.max(axis=1), axis=0)
    sinallowBeta = sinallowBeta.values
    sinallowBeta = sinallowBeta.astype(float)
    
    lowBeta = lda_lowBeta.transform(sinallowBeta)
    previsoeslowBeta = lowBeta_classificador.predict(lowBeta)
    
    #lowBeta fim
    
    
    
    
    
    total = (previsoesdelta + previsoeshighAlpha + previsoeshighBeta + previsoeslowAlpha + previsoeslowBeta) / 5
    
    print("delta", previsoesdelta ,"highAlpha", previsoeshighAlpha, "highBeta", previsoeshighBeta, "lowAlpha", previsoeslowAlpha,"lowBeta", previsoeslowBeta)
    
    i= i+500
    aa = aa+500
    total = 0
    
print("\nTESTE EEG FIM\n")
    





 
# -*- coding: utf-8 -*-

'''
    Autor: Isaque Elcio

    Descrição: 
        Classificação dos dados presentes em planilhas excel de amostras para os sinais fisiológico GSR, EEG, ECG.
        
        Cada um dos sinais significa:
            - EEG (eletroencefalograma): mede a atividade cerebral informando a produção de ondas beta, alfa e teta;
        
            - ECG (eletrocardiograma): mede a atividade elétrica do coração;
        
            - GSR (resposta galvânica da pele): mede a atividade elétrica das glândulas que produzem suor nas palmas
                                                das mãos e pontas dos dedos, mais sensíveis às emoções e pensamentos.
'''

# Bibliotecas
from pandas import read_excel
from classificadorGSR import ClassificadorGSR  # LDA e Classificador GSR
from classificadorECG import ClassificadorECG  # LDA e Classificador ECG
from classificadorEEG import ClassificadorEEG  # LDA e Classificador EEG


#  ----------------------------------
# |               GSR               |
#  ---------------------------------
# Leitura das amostras
df = read_excel("dadosGSR//amostras_GSR.xlsx", sheet_name = "Planilha1")
x  = df.values

# Teste
print("\nTESTE GSR INICIADO\n")
for i in range(0, 4):
    teste = [x[i]]
    classeGSR = ClassificadorGSR(teste)
    GSR = classeGSR.classificador_gsr()
    print("i:", i)
    print("Resultado GSR:", GSR)
print("\nTESTE GSR FINALIZADO\n")


#  ----------------------------------
# |               ECG               |
#  ---------------------------------
# Leitura das amostras
df = read_excel("dadosECG//amostras_ECG.xlsx", sheet_name = "Planilha1")
x  = df.values

# Teste
print("\nTESTE ECG INICIADO\n")
for i in range(0, 4):
    teste = [x[i]]
    classeECG = ClassificadorECG(teste)
    ECG = classeECG.classificador_ecg()
    print("i:", i)
    print("Resultado ECG:", ECG)
print("\nTESTE ECG FINALIZADO\n")

 
#  ----------------------------------
# |               EEG               |
#  ---------------------------------
# Leitura das amostras
delta = read_excel("dadosEEG//amostras_delta.xlsx", sheet_name = "Sheet1")
delta = delta.values

highAlpha = read_excel("dadosEEG//amostras_highAlpha.xlsx", sheet_name = "Sheet1")
highAlpha = highAlpha.values

highBeta = read_excel("dadosEEG//amostras_highBeta.xlsx", sheet_name = "Sheet1")
highBeta = highBeta.values

lowAlpha = read_excel("dadosEEG//amostras_lowAlpha.xlsx", sheet_name = "Sheet1")
lowAlpha = lowAlpha.values

lowBeta = read_excel("dadosEEG//amostras_lowBeta.xlsx", sheet_name = "Sheet1")
lowBeta = lowBeta.values

lowGamma = read_excel("dadosEEG//amostras_lowGamma.xlsx", sheet_name = "Sheet1")
lowGamma = lowGamma.values

midGamma = read_excel("dadosEEG//amostras_midGamma.xlsx", sheet_name = "Sheet1")
midGamma = midGamma.values

theta = read_excel("dadosEEG//amostras_theta.xlsx", sheet_name = "Sheet1")
theta = theta.values

# Teste
print("\nTESTE EEG INICIADO\n")
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
    print("Resultado EEG:", EEG)
print("\nTESTE EEG FINALIZADO\n")
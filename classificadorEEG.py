class ClassificadorEEG():

        
    def __init__(self, sinaldelta, sinalhighAlpha, sinalhighBeta, sinallowAlpha, sinallowBeta,
                 sinallowGamma, sinalmidGamma, sinaltheta):
       
        
        self.sinaldelta = sinaldelta
        self.sinalhighAlpha = sinalhighAlpha
        self.sinalhighBeta = sinalhighBeta
        self.sinallowAlpha = sinallowAlpha
        self.sinallowBeta = sinallowBeta
        self.sinallowGamma = sinallowGamma
        self.sinalmidGamma = sinalmidGamma
        self.sinaltheta = sinaltheta
         
    def classificador_eeg(self):

        import pickle
        import numpy as np 
        #import
        ##LDA delta
        lda_eeg_delta = pickle.load(open('dadosEEG//lda_eeg_delta.sav', 'rb'))
        ##LDA highAlpha
        lda_eeg_highAlpha = pickle.load(open('dadosEEG//lda_eeg_highAlpha.sav', 'rb'))
        ##LDA highBeta
        lda_eeg_highBeta = pickle.load(open('dadosEEG//lda_eeg_highBeta.sav', 'rb'))
        ##LDA lowAlpha
        lda_eeg_lowAlpha = pickle.load(open('dadosEEG//lda_eeg_lowAlpha.sav', 'rb'))
        ##LDA lowBeta
        lda_eeg_lowBeta = pickle.load(open('dadosEEG//lda_eeg_lowBeta.sav', 'rb'))
        ##LDA lowGamma
        lda_eeg_lowGamma = pickle.load(open('dadosEEG//lda_eeg_lowGamma.sav', 'rb'))
        ##LDA midGamma
        lda_eeg_midGamma = pickle.load(open('dadosEEG//lda_eeg_midGamma.sav', 'rb'))
        ##LDA theta
        lda_eeg_theta = pickle.load(open('dadosEEG//lda_eeg_theta.sav', 'rb'))
        #Classificador 
        classificador_svm_eeg = pickle.load(open('dadosEEG//svm_eeg_sinais.sav', 'rb'))
        
        a = lda_eeg_delta.transform(self.sinaldelta)
        b = lda_eeg_highAlpha.transform(self.sinalhighAlpha)
        c = lda_eeg_highBeta.transform(self.sinalhighBeta)
        d = lda_eeg_lowAlpha.transform(self.sinallowAlpha)
        e = lda_eeg_lowBeta.transform(self.sinallowBeta)
        f = lda_eeg_lowGamma.transform(self.sinallowGamma)
        g = lda_eeg_midGamma.transform(self.sinalmidGamma)
        h = lda_eeg_theta.transform(self.sinaltheta)

        dfc = a
        dfc = [np.append(dfc, b)]
        dfc = [np.append(dfc, c)]
        dfc = [np.append(dfc, d)]
        dfc = [np.append(dfc, e)]
        dfc = [np.append(dfc, f)]
        dfc = [np.append(dfc, g)]
        dfc = [np.append(dfc, h)]

      
        resultados = classificador_svm_eeg.predict(dfc)
        return resultados


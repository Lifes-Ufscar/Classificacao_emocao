# -*- coding: utf-8 -*-

class ClassificadorGSR(object):

    def __init__(self, sinalGSR):
        self.sinalGSR = sinalGSR

        print("teste1", sinalGSR)

    def classificador_gsr(self):

        import pickle
        lda = pickle.load(open('dadosGSR//lda_gsr.sav', 'rb'))
        ##Classificador
        nb_gsr = pickle.load(open('dadosGSR//nb_gsr.sav', 'rb'))

        print("teste2", self.sinalGSR)
        #resultados = self.sinalGSR
        #novo_registro = np.asarray(sinalGSR)
        novo_registro = lda.transform(self.sinalGSR)
        resultados = nb_gsr.predict(novo_registro)
        return resultados

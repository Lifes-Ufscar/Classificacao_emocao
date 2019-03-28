class ClassificadorECG():
    
    def __init__(self, sinalECG):
        self.sinalECG = sinalECG

        print("teste1", sinalECG)

    def classificador_ecg(self):
        print("inicio")
        import pickle
        lda = pickle.load(open('dadosECG//lda_ecg.sav', 'rb'))
        ##Classificador
        nb_ecg = pickle.load(open('dadosECG//nb_ecg.sav', 'rb'))

        print("teste2", self.sinalECG)
        #resultados = self.sinalGSR
        #novo_registro = np.asarray(sinalGSR)
        novo_registro = lda.transform(self.sinalECG)
        resultados = nb_ecg.predict(novo_registro)
        return resultados
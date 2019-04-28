
from Planilha import Planilha
from Sensores import Sensores

def main():
    key = raw_input("\nDeseja iniciar a captura? [S/n]: ")

    if(key == "sim" or key == "Sim" or key == "S" or key == "s"):
        # Recebe e verifica o nome do usuario
        usuario = raw_input("\nNome do usuario: ")
        while(not usuario):
            print("Sem nome de usuario!")
            usuario = raw_input("\nNome do usuario: ")

        # Recebe e verifica o ID da sessao
        id_sessao = raw_input("ID da sessao: ")
        while(not id_sessao.isdigit()):
            print("\nSessao deve ser numero!")
            id_sessao = raw_input("ID da sessao: ")

        # Inicializacao da panilha de amostras
        amostra = Planilha(usuario, id_sessao)
        amostra.criar_xlsx()

        # Inicializacao dos sensores
        # Valores de porta default sao (Arduino: COM15) e (MindWave: COM13)
        # Pode passar pelo construtor de sensores outros valores de portas COM
        sensores  = Sensores()
        iteracoes = sensores.leitura_sinais(usuario, id_sessao, amostra)

        amostra.fechar_xlsx()

        print("Captura realizada em %s iteracoes" % iteracoes)

if __name__ == "__main__":
    main()
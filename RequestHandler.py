
from BaseHTTPServer import BaseHTTPRequestHandler
from CapturaSinais  import CapturaSinais
import winsound

# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
# Written by Nathan Hamiel (2010)
class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")

    def do_POST(self):
        duracao = 300  # Milissegundos
        frequencia = 440 # Hz

        request_path = self.path

        print("\n----- Request Start ----->\n")
        print(request_path)

        request_headers = self.headers

        usuario   = request_headers.getheaders('usuario')
        sessao_id = request_headers.getheaders('sessao_id')
        filme = request_headers.getheaders('filme')

        usuario = str(usuario)
        usuario = usuario.replace("['", "")
        usuario = usuario.replace("']", "")

        sessao_id = str(sessao_id)
        sessao_id = sessao_id.replace("['", "")
        sessao_id = sessao_id.replace("']", "")

        #filme = str(filme)
        #filme = filme.replace("['", "")
        #filme = filme.replace("']", "")

        # Chama a funcao de captura de sinais
        # Parametros: Porta COM do MindWave, Porta COM do Arduino, Velocidade bits/s do Arduino
        captura = CapturaSinais()
        #iteracoes = captura.captura_sensores(usuario, sessao_id, filme)
        iteracoes = captura.captura_sensores(usuario, sessao_id)

        # length = int(content_length[0]) if content_length else 0

        print("\nCaptura finalizada com %d iteracoes" % iteracoes)
        print("\n<----- Request End -----\n")

        self.send_response(200)

    do_PUT = do_POST
    do_DELETE = do_GET
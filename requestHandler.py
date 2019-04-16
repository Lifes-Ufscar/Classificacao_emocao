# -*- coding: utf-8 -*-
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
# Written by Nathan Hamiel (2010)

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse       import OptionParser
import capturaSensores

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")


    def do_POST(self):
        request_path = self.path

        print("\n----- Request Start ----->\n")
        print(request_path)

        request_headers = self.headers

        user = request_headers.getheaders('user')
        session_id = request_headers.getheaders('session_id')
        # start_time = request_headers.getheaders('start_time')
        # movie_name = request_headers.getheaders('movie_name')

        user = str(user)
        user = user.replace("['", "")
        user = user.replace("']", "")

        session_id = str(session_id)
        session_id = session_id.replace("['", "")
        session_id = session_id.replace("']", "")

#        start_time = str(start_time)
#        start_time = start_time.replace("['", "")
#        start_time = start_time.replace("']", "")
#
#        movie_name = str(movie_name)
#        movie_name = movie_name.replace("['", "")
#        movie_name = movie_name.replace("']", "")

        capturaSensores(user, session_id)

        # length = int(content_length[0]) if content_length else 0

        print("<----- Request End -----\n")

        self.send_response(200)

    do_PUT = do_POST
    do_DELETE = do_GET


def main():
    port = 8081
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will echo out any GET or POST parameters\n"
                    "Run:\n\n"
                    "   reflect")
    (options, args) = parser.parse_args()

    main()
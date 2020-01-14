# TODO: D E P R E C A D O - no funcionará - migrar
# https://dev.to/petercour/get-http-response-codes-with-python-181h
from threading import Thread
import urllib.request
import urllib.parse
import time
import ssl
import json

class GetUrlThread(Thread):
    def __init__(self, url):
        self.url = url
        self.code = 0
        super(GetUrlThread, self).__init__()

    def run(self):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        request = urllib.request.Request(self.url)
        request.add_header('User-Agent', 'Mozilla')
        try:
            response = urllib.request.urlopen(request, context=ctx)
            self.code = response.getcode()
        except:
            self.code = 403


class Repositorio:
    #COLUMNAS = ['CATEGORÍA', 'DESCRIPCIÓN', 'LINK', 'CONTRASEÑA', 'F. INC.', 'F. REV.']
    PRIMERA_FILA = 2

    def __get(self):
        sheet = self.GOOGLE_CLIENT.open('repositorio').sheet1.get_all_values()
        return sheet[self.PRIMERA_FILA:]

    def __get_col_categoria(self, row):
        return row[0]
    def __get_col_descripcion(self, row):
        return row[1]
    def __get_col_link(self, row):
        return row[2]
    def __get_col_contrasena(self, row):
        return row[3]
    def __get_col_fecha_inclusion(self, row):
        return row[4]
    def __get_col_fecha_revision(self, row):
        return row[5]


    def get_links(self):
        rows = self.__get()
        return [self.__get_col_link(row) for row in rows]


    def check_links(self):
        threads = []
        start = time.time()
        for link in self.get_links():
            t = GetUrlThread(link)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        for t in threads:
            check_lst = []
            if (t.code != 200):
                check_lst.append(t.url)
                print(t.url)
            elif "mega.nz" in t.url:
                status = 0
                try:
                    data = json.dumps({"a": "g", "g": 1, "ssl": 0, "p": self.url.split("!")[1]}).encode('utf-8')
                    request = urllib.request.Request("https://eu.api.mega.co.nz/")
                    request.add_header('Content-Type', 'application/json; charset=utf-8')
                    request.add_header('Content-Length', len(data))
                    status = urllib.request.urlopen(request, data).read().decode()
                except:
                    status = -100

                if status == -9 or status == -100:
                    check_lst.append(t.url)
                    print(t.url, status)
        print("Elapsed time: %s" % (time.time() - start))

        return check_lst


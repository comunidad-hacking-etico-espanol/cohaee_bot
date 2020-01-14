from google_sheet import GoogleSheet

class PreguntaDiaria():
    __ESTADOS = {'disponible', 'preguntanda', 'pendiente', 'respondida'}

    def __init__(self):
        self.google_sheet = GoogleSheet(file='pregunta_diaria', norm=self.__norm)

    @staticmethod
    def __norm(row):
        return {'id': row[0], 'fecha': row[1], 'pregunta': row[3], 'usuario': row[4], 'estado': row[5]}

    def __get_preguntas(self):
        preguntas = self.google_sheet.get_data()
        preguntas.pop(0)  # quito los encabezados
        return preguntas

    def __get_pregunta_formateada(self, p):
        return "*Pregunta del día:* {} \n\n" \
               "El horario de respuesta y comentarios se abre mañana a las 22:00h \(UTC\+1\)\. " \
               "Responder con el hashtag *\#PDD\_ID{}*".format(p["pregunta"], p["id"], p["usuario"])

    def get_pregunta_diaria(self):
        #TODO hacer que tome la siguiente pregunta disponible y marque la pendiente como respondida
        preguntas = self.__get_preguntas()
        pendientes = [p for p in preguntas if p["estado"] == 'pendiente']
        disponibles = [p for p in preguntas if p["estado"] == 'disponible']

        if len(pendientes) == 1:
            return self.__get_pregunta_formateada(pendientes.pop(0))
        elif len(pendientes) > 1:
            return "Error: pendientes > 1 - @jarriagada"

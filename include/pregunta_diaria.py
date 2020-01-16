class PreguntaDiaria:
    from models.pregunta import Pregunta
    __collection = "pregunta_diaria"
    __model = Pregunta

    def __init__(self, firebase):
        self.__firebase = firebase

    def __get_db(self):
        self.__firebase.collection = self.__collection
        self.__firebase.model = self.__model
        return self.__firebase

    def __get_pregunta_formateada(self, p):
        return "*Pregunta del día:* {} \n\n" \
               "El horario de respuesta y comentarios se abre mañana a las 22:00h \(UTC\+1\)\. " \
               "Responder con el hashtag *\#PDD\_{}*".format(p.pregunta, p.document)

    def get_pregunta_diaria(self):
        lst_pendientes = self.__get_db().where('pendiente', '==', True)

        if len(lst_pendientes) == 1:
            return self.__get_pregunta_formateada(lst_pendientes.pop(0))
        elif len(lst_pendientes) > 1:
            return "Error: pendientes > 1 - @jarriagada"

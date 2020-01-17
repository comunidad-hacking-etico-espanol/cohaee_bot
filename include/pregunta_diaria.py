from include.firebase import Database


class PreguntaDiaria(Database):
    from telegram.ext import CallbackContext

    def __init__(self, firestore):
        from models.pregunta import Pregunta
        super().__init__(firestore=firestore, collection='pregunta_diaria', model=Pregunta)

    def job_callback(self, context: CallbackContext):
        pass

    def __get_pregunta_formateada(self, p):
        return "*Pregunta del día:* {} \n\n" \
               "El horario de respuesta y comentarios se abre mañana a las 22:00h \(UTC\+1\)\. " \
               "Responder con el hashtag *\#PDD\_{}*".format(p.pregunta, p.document)

    def get_pregunta_diaria(self):
        lst_pendientes = self._db().where('pendiente', '==', True)

        if len(lst_pendientes) == 1:
            return self.__get_pregunta_formateada(lst_pendientes.pop(0))
        elif len(lst_pendientes) > 1:
            return "Error: pendientes > 1 - @jarriagada"

        return None

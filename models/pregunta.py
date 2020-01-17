class Pregunta(object):
    def __init__(self, pregunta, user, fecha=None, disponible=True, pendiente=False, document=None):
        self.document = document
        self.pregunta = pregunta
        self.user = user
        self.disponible = disponible
        self.pendiente = pendiente
        self.fecha = fecha

    @staticmethod
    def from_dict(source, document):
        return Pregunta(
            pregunta=source['pregunta'],
            user=source['user'],
            fecha=source['fecha'],
            disponible=source['disponible'],
            pendiente=source['pendiente'],
            document=document)

    def to_dict(self):
        return {
            "pregunta": self.pregunta,
            "user": self.user,
            "fecha": self.fecha,
            "disponible": self.disponible,
            "pendiente": self.pendiente}

    def __repr__(self):
        return 'Pregunta(document="{}", pregunta="{}", user="{}", fecha="{}", disponible="{}", pendiente="{}")'\
                .format(self.document, self.pregunta, self.user, self.fecha, self.disponible, self.pendiente)
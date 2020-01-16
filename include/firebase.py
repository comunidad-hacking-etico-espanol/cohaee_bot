class Firebase:
    collection = None
    model = None

    def __init__(self):
        import firebase_admin
        import logging
        from firebase_admin import credentials
        from firebase_admin import firestore

        cred = credentials.Certificate('firebase.json')
        firebase_admin.initialize_app(cred)
        self.__db = firestore.client()
        self.__logger = logging.getLogger()

    def __get_collection(self):
        try:
            collection = self.__db.collection(self.collection)
        except Exception as error:
            self.__log(error, "__get_collection")
        return collection

    def __log(self, log):
        self.__logger.info(log)

    def __error(self, error, method):
        self.__log("")
        self.__log("FIREBASE ERROR")

        self.__log("Collection: {}".format(self.collection))
        self.__log("Model: {}".format(self.model))
        self.__log("Function: {}".format(method))
        self.__log("Exception: {}".format(type(error)))
        self.__log("Args: {}".format(error.args))
        self.__log("Error: {}".format(error))
        self.__log("")

    def where(self, field_path, op_string, value):
        data = []
        try:
            data = [self.model.from_dict(doc.to_dict(), doc.id) for doc in self.__get_collection().where(field_path, op_string, value).stream()]
        except Exception as error:
            self.__error(error, 'where')
        return data

    def read_from_collection(self, collection):
        data = []
        try:
            data = [self.model.from_dict(doc.to_dict(), doc.id) for doc in collection.stream()]
        except Exception as error:
            self.__error(error, 'read_from_collection')
        return data

    def create(self, obj):
        self.update(obj)

    def read(self, document=None, query=None):
        data = []
        try:
            if document is not None:
                data = self.model.from_dict(self.__get_collection().document(document).get().to_dict(), document)
            else:
                data = [self.model.from_dict(doc.to_dict(), doc.id) for doc in self.__get_collection().stream()]
        except Exception as error:
            self.__error(error, 'read')
        return data

    def update(self, obj):
        try:
            if obj.document is None:
                obj.document = self.__get_collection().document().id
            self.__get_collection().document(obj.document).set(obj.to_dict())
        except Exception as error:
            self.__error(error, 'update')
        finally:
            return obj.document

    def delete(self, obj):
        document = None
        try:
            document = self.__get_collection().document(obj.document)
        except Exception as error:
            self.__error(error, 'delete')
        finally:
            if document is not None:
                document.delete()

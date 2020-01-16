class Chats:
    from models.chat import Chat
    __collection = "chats"
    __model = Chat

    def __init__(self, firebase):
        self.__firebase = firebase

    def __get_db(self):
        self.__firebase.collection = self.__collection
        self.__firebase.model = self.__model
        return self.__firebase

    def existe_id(self, chat_id):
        if self.get_id(chat_id) is not None:
            return True
        return False

    def get_id(self, chat_id):
        lst_chats = self.__get_db().where('id', '==', chat_id)
        if len(lst_chats) == 1:
            return lst_chats[0]
        return None

    def actualizar(self, chat):
        return self.__get_db().update(chat)

    def agregar(self, chat):
        if self.existe_id(chat.id) is True:
            return chat.id
        self.__get_db().update(chat)

from include.firebase import Database


class Chats(Database):
    def __init__(self, firestore):
        from models.chat import Chat
        super().__init__(firestore=firestore, collection='chats', model=Chat)

    def existe_id(self, chat_id):
        if self.get_id(chat_id) is not None:
            return True
        return False

    def get_id(self, chat_id):
        lst_chats = self._db().where('id', '==', chat_id)
        if len(lst_chats) == 1:
            return lst_chats[0]
        return None

    def actualizar(self, chat):
        return self._db().update(chat)

    def agregar(self, chat):
        if self.existe_id(chat.id) is True:
            return chat.id
        self._db().update(chat)

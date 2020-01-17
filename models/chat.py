class Chat(object):
    username = None
    title = None
    oficial=False

    def __init__(self, id, type, title=None, oficial=None, username=None, document=None):
        self.document = document
        self.id = id
        self.type = type
        self.username = username
        self.title = title
        self.oficial = oficial

    @staticmethod
    def from_dict(source, document):
        chat = Chat(
            id=source['id'],
            type=source['type'],
            title=source['title'],
            document=document)

        if source['username'] is not None:
            chat.username = source['username']
        if source['title'] is not None:
            chat.title = source['title']

        return chat

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "title": self.title,
            "username": self.username,
            "oficial": self.oficial}

    def __repr__(self):
        return 'Chat(document="{}", id="{}", type="{}", title="{}", username="{}", oficial="{}")'\
                .format(self.document, self.id, self.type, self.title, self.username, self.oficial)

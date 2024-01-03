class Corousel:
    def __init__(self, id, title, content, image, link):
        self.id = id
        self.title = title
        self.content = content
        self.image = image
        self.link = link

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'image': self.image,
            'link': self.link
        }

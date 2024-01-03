class Blog:
    def __init__(self, id, topic, title, shortdesc, image, imagetitle, imagedesc, socialmedias, introduction, content, conclution):
        self.id = id
        self.topic = topic
        self.title = title
        self.shortdesc = shortdesc
        self.image = image
        self.imagetitle = imagetitle
        self.imagedesc = imagedesc
        self.socialmedias = socialmedias
        self.introduction = introduction
        self.content = content
        self.conclution = conclution

    def to_dict(self):
        return {
            'id': self.id,
            'topic': self.topic,
            'title': self.title,
            'shortdesc': self.shortdesc,
            'image': self.image,
            'imagetitle': self.imagetitle,
            'imagedesc': self.imagedesc,
            'socialmedias': self.socialmedias,
            'introduction': self.introduction,
            'content': self.content,
            'conclution': self.conclution
        }

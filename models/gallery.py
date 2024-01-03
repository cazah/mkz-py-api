class Gallery:
    def __init__(self, id, image):
        self.id = id
        self.image = image

    def to_dict(self):
        return {'id' : self.id,
                'image': self.image}
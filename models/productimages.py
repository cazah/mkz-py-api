class ProductImage:
    def __init__(self, id, title, image, category):
        self.id = id
        self.title = title
        self.image = image
        self.category = category

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'image': self.image,
            'category': self.category
        }

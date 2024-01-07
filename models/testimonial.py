class Testinonial:
    def __init__(self, id,message,type,name):
        self.id = id
        self.name = name
        self.message = message
        self.type = type

    def to_dict(self):
        return {'id': self.id,
                'name': self.name,
                'message': self.message,
                'type': self.type
                }
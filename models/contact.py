class Contact:
    def __init__(self, id,name,subname,email,logo,phones,socialmedias,address,location):
        self.id = id
        self.name = name
        self.subname = subname
        self.email = email
        self.logo = logo
        self.phones = phones
        self.socialmedias = socialmedias
        self.address = address
        self.location = location

    def to_dict(self):
        return {'id': self.id,
                'name': self.name,
                'subname': self.subname,
                'email': self.email,
                'logo': self.logo,
                'phones': self.phones,
                'socialmedias': self.socialmedias,
                'address': self.address,
                'location': self.location
                }
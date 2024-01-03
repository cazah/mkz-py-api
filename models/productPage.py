class ProductPage:
    def __init__(self, id, details, content, quote_content, extra_content):
        self.id = id
        self.details = details
        self.content = content
        self.quote_content = quote_content
        self.extra_content = extra_content

    def to_dict(self):
        return {
            'id': self.id,
            'details': self.details,
            'content': self.content,
            'quote_content': self.quote_content,
            'extra_content': self.extra_content
        }

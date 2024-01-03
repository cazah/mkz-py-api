class ServicePage:
    def __init__(self, id, topic, title, introduction, content, makizh_amc_service_json, makizh_amc_service_note, amc_service_json, amc_service_note, package_table):
        self.id = id
        self.topic = topic
        self.title = title
        self.introduction = introduction
        self.content = content
        self.makizh_amc_service_json = makizh_amc_service_json
        self.makizh_amc_service_note = makizh_amc_service_note
        self.amc_service_json = amc_service_json
        self.amc_service_note = amc_service_note
        self.package_table = package_table

    def to_dict(self):
        return {
            'id': self.id,
            'topic': self.topic,
            'title': self.title,
            'introduction': self.introduction,
            'content': self.content,
            'makizh_amc_service_json': self.makizh_amc_service_json,
            'makizh_amc_service_note': self.makizh_amc_service_note,
            'amc_service_json': self.amc_service_json,
            'amc_service_note': self.amc_service_note,
            'package_table': self.package_table
        }

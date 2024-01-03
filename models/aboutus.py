class Aboutus:
    def __init__(self, id, companyname, info, visioncontent, empowercontent, costcontent, missioncontent, valuescontent, principlecontent, principlekey, integrity):
        self.id = id
        self.companyname = companyname
        self.info = info
        self.visioncontent = visioncontent
        self.empowercontent = empowercontent
        self.costcontent = costcontent
        self.missioncontent = missioncontent
        self.valuescontent = valuescontent
        self.principlecontent = principlecontent
        self.principlekey = principlekey
        self.integrity = integrity

    def to_dict(self):
        return {
            'id': self.id,
            'companyname': self.companyname,
            'info': self.info,
            'visioncontent': self.visioncontent,
            'empowercontent': self.empowercontent,
            'costcontent': self.costcontent,
            'missioncontent': self.missioncontent,
            'valuescontent': self.valuescontent,
            'principlecontent': self.principlecontent,
            'principlekey': self.principlekey,
            'integrity': self.integrity
        }
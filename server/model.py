from settings import db

class Url(db.Model):
    __tablename__ = 'urls'

    url = db.Column(db.String(255), primary_key=True)
    converted_url = db.Column(db.String(255), nullable=False)

    def __init__(self, url, converted_url):
        self.url = url
        self.converted_url = converted_url

    def __repr__(self):
        return {"url": self.url, "converted_url": self.converted_url}
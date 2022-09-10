from settings import db

class Url(db.Model):
    __tablename__ = 'urls'

    url = db.Column(db.String(255), primary_key=True)
    shortened_key = db.Column(db.String(255), nullable=False)

    def __init__(self, url, shortened_key):
        self.url = url
        self.shortened_key = shortened_key

    def __repr__(self):
        return {"url": self.url, "shortened_key": self.shortened_key}
from app.db import db
from datetime import datetime

class Image(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    name =db.Column(db.Integer, nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)
    rendered_data =db.Column(db.Text, nullable=False)
    text=db.Column(db.Text)
    pic_date =db.Column(db.DateTime,nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'Pic Name {self.name} Date:{self.data} created on {self.pic_date}'

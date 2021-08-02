from app.db import db
from datetime import datetime

class ImageModel(db.Model):
    '''recebe o dado,name,rendered_data,desc (opc)
    '''
    id =db.Column(db.Integer, primary_key=True)
    filename =db.Column(db.Text, nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)
    rendered_data =db.Column(db.Text, nullable=False)
    descricao=db.Column(db.Text,default='< without description provided  >')
    created_at =db.Column(db.DateTime,nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'Pic Name {self.name} Date:{self.data} created on {self.pic_date}'

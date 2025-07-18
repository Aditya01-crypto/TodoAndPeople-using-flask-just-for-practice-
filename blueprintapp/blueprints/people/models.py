from blueprintapp.app import db

class Person(db.Model):
    __table__name="person"

    pid=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    age=db.Column(db.Integer)
    job=db.Column(db.String)

    def __repr__(self):
        return f"<Person {self.name}, age: {self.age}>"


    def get_id(self):
        return self.pid
from blueprintapp.app import db

class Todo(db.Model):
    __table__name="todos"

    tid=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String,nullable=False)
    description=db.Column(db.String)
    done=db.Column(db.Boolean,nullable=False)

    def __repr__(self):
        return f"To-do : {self.title}, Done: {self.done} "


    def get_id(self):
        return self.tid
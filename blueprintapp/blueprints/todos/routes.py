from flask import request, url_for, redirect,render_template, Blueprint

from blueprintapp.app import db
from blueprintapp.blueprints.todos.models import Todo

#instead of saying app=Flask we say todo =blueprint as it a sub part of major application 

todos=Blueprint('todos',__name__,template_folder='templates')#so the first argument is the name of the blue print , the second argument is self explanatory and third thing is we are setting the blueprint's templates path

@todos.route('/')
def index():# here we are also creating a templates folder in blueprintapp which will have base.html for html inheritance

    todos=Todo.query.all()#to get every todo data from the table todos
    return render_template('todos/index.html',todos=todos)#okay so best practice is to make a directory templates inside todos and then antoher directory named todos and then place our html file there
# i have stored rest of the comments as it was big in if False: statement
if False:
    '''
the reason why we follow this practice 
You’re absolutely right to ask this — it feels like just creating a templates/ folder inside each blueprint (like todos/templates/index.html and auth/templates/login.html) should be enough.

But Flask doesn’t automagically look inside each blueprint’s templates/ unless you tell it how — and here’s the tricky twist that trips up even smart devs like you:

❌ The Trap: Flat templates/ in each blueprint = Possible conflict chaos
If you do:


blueprints/
├── todos/
│   └── templates/
│       └── index.html
├── auth/
│   └── templates/
│       └── index.html
Then Flask, when it loads these blueprints with:


Blueprint("todos", __name__, template_folder="templates")
Blueprint("auth", __name__, template_folder="templates")
Now both blueprints claim they have a templates/index.html.

So when you call:


render_template("index.html")
Flask gets confused — which index.html do you mean? The one from auth or from todos? It doesn't scope them by blueprint.

✅ The Clean Solution (Best Practice Again)
You nest the templates like this:

pgsql
Copy
Edit
blueprints/
├── todos/
│   └── templates/
│       └── todos/
│           └── index.html
├── auth/
│   └── templates/
│       └── auth/
│           └── login.html
And then:

python
Copy
Edit
render_template("todos/index.html")
render_template("auth/login.html")
This avoids any conflict.'''

@todos.route('/create',methods=['GET','POST'])
def create():
    if request.method=='GET':
        return render_template('todos/create.html')
    elif request.method=='POST':
        title=request.form.get('title')
        description=request.form.get('description')
        done=True if 'done' in request.form.keys()  else False #because if checkboxes are checked it will be  a part of the keys otherwise not

        description=description if description!='' else None
        
        todo=Todo(title=title,description=description,done=done)

        db.session.add(todo)
        db.session.commit()

        return redirect(url_for('todos.index'))

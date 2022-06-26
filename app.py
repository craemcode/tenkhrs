from flask import Flask, render_template
from models import db, Plug, Product

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SECRET_KEY'] = 'JABAWABA2'
db.init_app(app)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db)


@app.route('/')
def index():
    
    
    
    
    return render_template('domanip.html')















if __name__ == '__main__':
    app.run(debug=True)
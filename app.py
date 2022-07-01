from flask import Flask, render_template
from models import db, Plug, Product
from forms import PlugForm, ProductForm
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SECRET_KEY'] = 'JABAWABA2'
db.init_app(app)
migrate = Migrate(app,db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db)


@app.route('/')
def index():
    plug_form = PlugForm()

    
    
    
    return render_template('domanip.html', plug_form=plug_form)

@app.route('/add_prod', methods=['GET','POST'])
def add_product():
    prod_form = ProductForm()


    return render_template('addprod.html', prod_form=prod_form)













if __name__ == '__main__':
    app.run(debug=True)
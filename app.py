# importation des bibliothèques Flask et permettant de sécuriser les mots de passe

from flask import Flask , render_template , request , session , flash , url_for , redirect
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.security import generate_password_hash , check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin



app = Flask(__name__)

# Implementation d une securite
app.wsgi_app = ProxyFix(app.wsgi_app)

# Code secret
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# chargement de la base de données
db_name = 'data2.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


# definition des classes des tables contenues dans la base de donnees
class users(UserMixin,db.Model):
    username = db.Column(db.String(200),primary_key=True,unique=True)
    password = db.Column(db.String(2000))


#
@app.route('/register', methods=('POST','GET'))
def register():
    '''
    fonction permettant de recuperer les donnees remplies par l'utilisateur sur la
    page html pour creer un nouveau compte. Un message d erreur sera renvoyé si le
    nom de l utilisateur ou le mot de passe n'est pas renseigné ou si le nom d utilisateur
    a deja été utilisé. Autrement les donnes seront envoyées dans une base de donnee et le
    mot de passe sera crypté

    '''

    if request.method == 'POST':

        username_input = request.form['username']
        password_input = request.form['password']
        error = None

        if not (db.session.query(users).filter_by(username=username_input).all()):
            db.session.add(users(username=username_input, password=generate_password_hash(password_input)))
            db.session.commit()
            return redirect(url_for("login"))
        else:
            error = "username already exists"
        flash(error)
        return render_template('register.html')
    return render_template('register.html')



@app.route('/login',methods=['POST','GET'])
def login():
    '''
    cette fonction permet a l utilisateur de se connecter.
    Le bouton reset lui permettra de supprimer toutes les donnees deja entrées
    Le bouton new account redigera l utilisateur vers la page pour se connecter
    Le bouton connect permettra a l utilsateur de se connecter, si l'utilisateur
    ou le mot de passe n est pas renseigné ou si l utilisateur n existe pas ou
    que le mot de passe associé n'est pas correct un message d erreur s affichera
    autrement l utilisateur sera redirige vers la page de bienvenue
    '''

    if request.method == 'POST':

        if request.form.get('RESET')=='RESET':
            return redirect(url_for("login"))

        elif request.form.get('NEW ACCOUNT')=='NEW ACCOUNT':
            return redirect(url_for("register"))

        elif request.form.get('CONNECT')=='CONNECT' :
            username_input= request.form['username']
            password_input = request.form['password']
            error = None
            if not username_input:
                error = 'Username is required.'
            if not password_input:
                error = 'Password is required.'
            if error is None:
                user = db.session.query(users).filter_by(username=username_input).first()
                if not user :
                    error = 'Username does not exist'
                elif check_password_hash(user.password , password_input) :
                    return redirect(url_for("bienvenue"))
                else:
                    error = "wrong password"
        flash(error)
    return render_template("login.html")


@app.route('/bienvenue', methods=('GET', 'POST'))
def bienvenue():
    '''
    cette fonction renvoit la page affichée lorsque l utilisateur a
    reussi a se connecter
    '''
    return render_template("bienvenue.html")

app.run(debug=True)

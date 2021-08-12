from flask import Flask, render_template, redirect, request, session, flash
from flask_mail import Mail, Message 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'Bluetrip' # Chave de criptografia para guardar sessão de login

# mail_settings = {
#     "MAIL_SERVER": 'smtp.gmail.com',
#     "MAIL_PORT": 465,
#     "MAIL_USE_TLS": False,
#     "MAIL_USE_SSL": True,
#     "MAIL_USERNAME": 'bluetrip.contato@gmail.com',
#     "MAIL_PASSWORD": 'Bluetrip123'
# }

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://otvtzlxv:fBUj8Z_IpFLUv9geGbDS5u3r_kAFQ8nd@kesavan.db.elephantsql.com/otvtzlxv'

db = SQLAlchemy(app)

class Viagem(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    destino = db.Column(db.String(150), nullable=False)
    preco = db.Column(db.Integer(), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    link = db.Column(db.String(300), nullable=False)
    tipo_viagem = db.Column(db.String(10000), nullable=False)
   
    def __init__(self, destino, preco, descricao, link, tipo_viagem):
        self.destino = destino
        self.preco = preco
        self.descricao = descricao
        self.link = link
        self.tipo_viagem = tipo_viagem


# ----------- ROTAS -------------

@app.route('/')
def index():
   session['usuario_logado'] = None
   viagens = Viagem.query.all()  # Busca todas as viagens no banco e coloca na variável Viagem, que se transforma em uma lista.
   return render_template('index.html', viagens=viagens) # Renderiza a página index.html mandando a lista de projetos

@app.route('/pacotes')
def pacotes():
   viagens = Viagem.query.all()
   return render_template('pacotes.html', viagens=viagens, viagem='')

@app.route('/missao')
def missao():
    return render_template('missao.html')

@app.route('/admin')
def adm():
   if 'usuario_logado' not in session or session['usuario_logado'] == None:
      flash('Faça o login antes de entrar nessa rota!')
      return redirect('/login')
   viagens = Viagem.query.all() # Busca todos os projetos no banco e coloca na veriável projetos, que se transforma em uma lista.
   return render_template('admin.html', viagens=viagens, viagem='')
   
@app.route('/listagem')
def listagem():
   if 'usuario_logado' not in session or session['usuario_logado'] == None:
      flash('Faça o login antes de entrar nessa rota!')
      return redirect('/login')
   viagens = Viagem.query.all()
   return render_template('listagem.html', viagens=viagens, viagem='')


@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/login')
def login():
   session['usuario_logado'] = None
   return render_template('login.html')


#/auth



@app.route('/auth', methods=['GET', 'POST'])
def auth():
   if request.form['senha'] == 'Bluetrip':
      session['usuario_logado'] = 'admin'
      flash('Login feito com sucesso!')
      return redirect('/admin') 
   else:
      flash('Erro no login, tente novamente!')
      return redirect('/login')

@app.route('/logout')
def logout():
   session['usuario_logado'] = None
   return redirect('/login')



# ROTAS DE CRUD

# CREATE
@app.route('/new', methods=['GET', 'POST'])
def new():
   if request.method == 'POST':     
      viagem = Viagem(
         request.form['destino'],
         request.form['preco'],
         request.form['descricao'],
         request.form['link'],
         request.form['tipo_viagem']
      )
      db.session.add(viagem) # Adiciona o objeto projeto no banco de dados.
      db.session.commit() # Confirma a operação
      flash('Viagem adicionada ao catálogo com sucesso!') # Mensagem de sucesso.
      return redirect('/admin') # Redireciona para a rota admin

# Rota edit que recebe um paremetro
@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
   viagem = Viagem.query.get(id) # Busca um projeto no banco através do id
   viagens = Viagem.query.all()
   if request.method == "POST": # Se a requisição for um POST, faça:
      # Alteração de todos os campos de projetoEdit selecionado no get id
      viagem.destino = request.form['destino']
      viagem.preco = request.form['preco']
      viagem.descricao = request.form['descricao']
      viagem.link = request.form['link']
      viagem.tipo_viagem = request.form['tipo_viagem']
      db.session.commit() # Confirma a operação
      return redirect('/listagem')
       #Redireciona para a rota adm
   # Renderiza a página adm.html passando o projetoEdit (projeto a ser editado)
   return render_template('editar.html', viagem=viagem , viagens=viagens )


# Rota delete
@app.route('/delete/<id>') 
def delete(id):
   viagemdel = Viagem.query.get(id) # Busca um projeto no banco através do id
   db.session.delete(viagemdel) # Apaga o projeto no banco de dados
   db.session.commit() # Confirma a operação
   flash('Viagem deletada do catálogo com sucesso!')
   return redirect('/listagem') #Redireciona para a rota adm
if __name__ == '__main__':
   db.create_all() # Cria o banco assim que a aplicação é ligada.
   app.run(debug=True)
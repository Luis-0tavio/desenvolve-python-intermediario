from flask import render_template, request, redirect, url_for
from app import app, alquimias
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/')
@login_required
def index():
    user = None
    posts = []
    if current_user.is_authenticated:
        user = current_user
        posts = alquimias.get_timeline()
    return render_template('index.html', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    erro = None
    if request.method == 'POST':
        username = request.form.get('username', '').lower()
        password = request.form.get('password', '')
        
        try:
            if not username or not password:
                erro = 'Usuário e senha são obrigatórios'
            else:
                user = alquimias.validate_user_password(username, password)
                if user:
                    login_user(user, remember=user.remember)
                    return redirect(url_for('index'))
                else:
                    erro = 'Usuário ou senha inválidos'
        except Exception as e:
            erro = f'Erro ao fazer login: {str(e)}'
    
    return render_template('login.html', erro=erro)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    erro = None
    if request.method == 'POST':
        username = request.form.get('username', '').lower()
        password = request.form.get('password', '')
        foto = request.form.get('foto', '')
        bio = request.form.get('bio', '')
        remember = True if request.form.get('remember') == 'on' else False
        
        try:
            if not username or not password:
                erro = 'Usuário e senha são obrigatórios'
            elif len(username) < 3:
                erro = 'Usuário deve ter pelo menos 3 caracteres'
            elif len(password) < 3:
                erro = 'Senha deve ter pelo menos 3 caracteres'
            elif alquimias.user_exists(username):
                erro = 'Usuário já existe'
            else:
                user = alquimias.create_user(username, password, remember, foto=foto, bio=bio)
                login_user(user, remember=remember)
                return redirect(url_for('index'))
        except ValueError as ve:
            erro = str(ve)
        except Exception as e:
            erro = f'Erro ao criar usuário: {str(e)}'
    
    return render_template('cadastro.html', erro=erro)

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    erro = None
    if request.method == 'POST':
        body = request.form.get('body', '').strip()
        
        try:
            if not body:
                erro = 'Post não pode ser vazio'
            else:
                alquimias.create_post(body, current_user)
                return redirect(url_for('index'))
        except Exception as e:
            erro = f'Erro ao criar post: {str(e)}'
    
    return render_template('post.html', erro=erro)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login_route'))
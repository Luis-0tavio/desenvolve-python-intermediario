from datetime import datetime
from sqlalchemy import select, desc
from app import db
from app.models.models import User, Post

def validate_user_password(username, password):
    '''Retorna o usuário se a senha está correta, None caso contrário'''
    try:
        if not username or not password:
            return None
        user = db.session.scalars(select(User).where(User.username == username.lower())).first()
        if user and user.password == password:
            return user
        return None
    except Exception as e:
        print(f"Erro ao validar usuário: {e}")
        return None

def user_exists(username):
    '''Retorna o usuário se existe no banco'''
    try:
        if not username:
            return None
        user = db.session.scalars(select(User).where(User.username == username.lower())).first()
        return user
    except Exception as e:
        print(f"Erro ao verificar usuário: {e}")
        return None

def create_user(username, password, remember=False, foto='', bio=''):
    '''Cria um novo usuário e retorna o objeto User'''
    try:
        if not username or not password:
            raise ValueError("Usuário e senha não podem ser vazios")
        
        # Validar se usuário já existe
        if user_exists(username):
            raise ValueError("Usuário já existe")
        
        new_user = User(
            username=username.lower().strip(),
            password=password.strip(),
            remember=remember,
            last_login=datetime.now(),
            foto=foto.strip() if foto else '',
            bio=bio.strip() if bio else ''
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao criar usuário: {e}")
        raise

def create_post(body, user):
    '''Cria um novo post e retorna o objeto Post'''
    try:
        if not body or not body.strip():
            raise ValueError("Post não pode ser vazio")
        
        new_post = Post(
            body=body.strip(),
            author=user,
            timestamp=datetime.now()
        )
        db.session.add(new_post)
        db.session.commit()
        return new_post
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao criar post: {e}")
        raise

def get_timeline():
    '''Retorna os 5 posts mais recentes ordenados por timestamp'''
    try:
        posts = db.session.scalars(
            select(Post).order_by(desc(Post.timestamp)).limit(5)
        ).all()
        return posts
    except Exception as e:
        print(f"Erro ao obter timeline: {e}")
        return []
from app import app, db
from app.models import Post

with app.app_context():
    # Crea una nueva publicación de prueba
    post = Post(title='Prueba', content='Contenido de prueba')
    db.session.add(post)
    db.session.commit()

    # Consulta todas las publicaciones
    posts = Post.query.all()
    print(posts)

# BLUEPRINT figurinhas — pluga as rotas /figurinhas/ no Flask
from controllers.figurinhas_controller import figurinhas_bp
app.register_blueprint(figurinhas_bp)

# layout.html: url_for('figurinhas.index')

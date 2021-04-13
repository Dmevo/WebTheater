from flask import render_template, url_for
from application import app
from application.model.dao.categoriaDAO import CategoriaDAO
from application.model.entity.categoria import Categoria
from application.model.dao.videoDAO import VideoDAO
from application.model.entity.video import Video


@app.route("/")
def home():
    categoria_dao = CategoriaDAO()
    categoria_lista = categoria_dao.mostrar_categorias()
    return render_template("index.html", lista_categoria = categoria_lista)

@app.route("/video/<id>")
def videos(id):
    video_dao = VideoDAO()
    video_lista = video_dao.mostrar_videos()
    for video in video_lista:
        if str(video.get_id()) == id:
            return render_template("video.html", video = video)
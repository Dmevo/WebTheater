class Categoria:
    
    def __init__(self, id = None, nome = None, url_foto = None, descricao_categoria = None, lista_video = None):
        self.id = id
        self.nome = nome
        self.quantidade_videos = 0
        self.url_foto = url_foto
        self.lista_video = lista_video

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_quantidade_videos(self, quantidade_videos):
        self.quantidade_videos = quantidade_videos

    def get_quantidade_videos(self):
        return self.quantidade_videos

    def set_url_foto(self, url_foto):
        self.url_foto = url_foto

    def get_url_foto(self):
        return self.url_foto

    def set_descricao_categoria(self, descricao_categoria):
        self.descricao_categoria = descricao_categoria

    def get_descricao_categoria(self):
        return self.descricao_categoria

    def add_lista_video(self, video):
        self.lista_video.append(video)

    def get_lista_video(self):
        return self.lista_video

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id



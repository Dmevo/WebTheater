class Video:
    
    def __init__(self, id = None, titulo = None, curtidas = None, descricao = None, url_video = None, url_img = None, data_publicacao = None, qtd_visualizacao = None, categoria = None):
        self.titulo = titulo
        self.curtidas = curtidas
        self.descricao = descricao
        self.url_video = url_video
        self.data_publicacao = data_publicacao
        self.qtd_visualizacao = qtd_visualizacao
        self.categoria = categoria
        self.url_img = url_img
        self.id = id

    def set_titulo(self, titulo):
        self.titulo = titulo
    
    def get_titulo(self):
        return self.titulo

    def get_curtidas(self):
        return self.curtidas

    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_descricao(self):
        return self.descricao

    def set_url_video(self, url_video):
        self.url_video = url_video

    def get_url_video(self):
        return self.url_video

    def set_data_publicacao(self, data_publicacao):
        self.data_publicacao = data_publicacao

    def get_data_publicacao(self):
        return self.data_publicacao

    def set_qtd_visualizacao(self, qtd_visualizacao):
        self.qtd_visualizacao = qtd_visualizacao

    def get_qtd_visualizacao(self):
        return self.qtd_visualizacao

    def set_categoria(self, categoria):
        self.categoria = categoria

    def get_categoria(self):
        return self.categoria

    def set_url_img(self, url_img):
        self.url_img = url_img

    def get_url_img(self):
        return self.url_img

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

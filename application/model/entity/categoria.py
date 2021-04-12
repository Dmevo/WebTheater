class Categoria:
    
    def __init__(self, nome = None, url_foto = None, descricao_categoria = None):
        self.nome = nome
        self.quantidade_videos = 0
        self.url_foto = url_foto
        self.id = id

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

"""

categoria1 = Categoria()

categoria1.set_nome("Danilo")
categoria1.set_id("156.782.000")
categoria1.set_quantidade_videos(5)
categoria1.set_url_foto("fotinha.png")

print("Nome da categoria é {}".format(categoria1.get_nome()))
print("Possui {} videos".format(categoria1.get_quantidade_videos()))
print("O ID é {}".format(categoria1.get_id()))
print("O URL da foto é {}".format(categoria1.get_url_foto()))

"""


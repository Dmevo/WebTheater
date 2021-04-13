from application import categoria_lista
from application.model.entity.categoria import Categoria


class CategoriaDAO:

    def __init__(self):
        self.categoria_lista = categoria_lista

    def mostrar_categorias(self):
        return self.categoria_lista
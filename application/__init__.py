from flask import Flask
import os
from application.model.entity.video import Video
from application.model.entity.categoria import Categoria

app=Flask(__name__, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/templates"))

video1 = Video(1 ,"One Piece Ep 965", 653, "Roger vs Whitebeard", "https://www.youtube.com/embed/UOZpCJhxv-w", "rogervswhitebeard.jpg", "22/06/2020", 28098, "One Piece")
video2 = Video(2 ,"One Piece Ep 726", 389, "Gear 4: Boundman", "https://www.youtube.com/embed/5pWw5M97Cks", "boundman.jpg", "29/06/2020", 23984, "One Piece")
video3 = Video(3 ,"One Piece Ep 870", 453, "Gear 4: Snakeman", "https://www.youtube.com/embed/APIU8HJOK3Q", "snakeman.png", "06/06/2020", 31763, "One Piece")
video4 = Video(4 ,"Gatinho toca piano", 82316, "Gatinho toca piano", "https://www.youtube.com/embed/bpYQRPZyHwM", "catpiano.jpg", "12/07/2001", 124736, "Memes")
video5 = Video(5 ,"Crash Woah", 57123, "Crash Woah", "https://www.youtube.com/embed/u29WUpWLZJk", "woah.png", "23/09/2011", 86213, "Memes")
video6 = Video(6 ,"Nyan Cat", 1769154, "Nyan Cat", "https://www.youtube.com/embed/QH2-TGUlwu4", "nyancat.jpg", "05/11/2007", 2127632, "Memes")


video_lista = [video1, video2, video3, video4, video5, video6]

categoria_lista=[]

categoria1 = Categoria(1 ,"One piece", "url_foto", "Videos sobre one piece", [video1, video2, video3])
categoria2 = Categoria(2 ,"Memes", "url_foto", "Videos engraçados", [video4, video5, video6])

categoria_lista=[categoria1, categoria2]

from application.controller import home_controller
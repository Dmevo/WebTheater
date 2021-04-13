from application import video_lista
from application.model.entity.video import Video

class VideoDAO():
    
    def __init__(self):
        self.video_lista = video_lista

    def mostrar_videos(self):
        return self.video_lista
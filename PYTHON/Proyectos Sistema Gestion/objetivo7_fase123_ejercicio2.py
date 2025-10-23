# Nombre: LiLi Fernández Pedrosa 
# Grupo: 2ºDAM 

# Crear dos clases padres (Video y Audio) y una subclase Media que herede de ambas.
# Todas las respuestas son originales y comentadas para facilitar su comprensión.
# Clase Video
# Representa un contenido de video con título, duración y categoría.
class Video:
    # Constructor para inicializar los atributos de Video.
    def __init__(self, titulo_video, categoria, duracion):
        self.titulo_video = titulo_video
        self.categoria = categoria
        self.duracion = duracion

    # Método mirar_video: muestra que el video ha comenzado y su información.
    def mirarVideo(self):
        print("Iniciando el video...")
        print(f"El video que estás viendo se titula '{self.titulo_video}' de la categoría '{self.categoria}' con una duración de {self.duracion} minutos.")

    # Método detener_video: muestra que el video ha sido detenido.
    def detenerVideo(self):
        print("Deteniendo el video.")


# Clase Audio
# Representa un contenido de audio con título y artista.
class Audio:
    # Constructor para inicializar los atributos de Audio.
    def __init__(self, titulo_audio, artista):
        self.titulo_audio = titulo_audio
        self.artista = artista

    # Método escuchar_audio: muestra que el audio ha comenzado y su información.
    def escucharAudio(self):
        print("Iniciando el audio...")
        print(f"El audio que estás escuchando es '{self.titulo_audio}' producido por el artista '{self.artista}'")

    # Método detener_audio: muestra que el audio ha sido detenido.
    def detenerAudio(self):
        print("Deteniendo la reproducción del audio.")


# Clase Media
# Hereda de Video y Audio, representa un contenido multimedia completo.
class Media(Video, Audio):
    # Constructor que inicializa todos los atributos de Media.
    def __init__(self, titulo, categoria, duracion, artista):
        Video.__init__(self, titulo, categoria, duracion)
        Audio.__init__(self, titulo, artista)


# Ejemplos de pruebas / casos de uso
medio1 = Media("Titulo 1", "infantil", 180, "Artista 1")
medio1.escucharAudio()
medio1.mirarVideo()
medio1.detenerAudio()
medio1.detenerVideo()
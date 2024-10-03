import os
import sys
from pytube import Playlist
import yt_dlp

def download_video(url, output_path, convert_to_mp3=False):
    try:
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Ruta de salida
            'format': 'bestvideo+bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Usar ffmpeg para extraer audio
                'preferredcodec': 'mp3',  # Convertir a mp3
                'preferredquality': '192',  # Calidad de audio
            }] if convert_to_mp3 else [],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"Video descargado correctamente en {output_path}")

    except Exception as e:
        print(f"Error al descargar el video: {e}")

# Función para descargar playlist de YouTube
def download_playlist(url, output_path):
    try:
        playlist = Playlist(url)
        print(f"Descargando lista de reproducción: {playlist.title}")
        for video in playlist.videos:
            print(f"Descargando video: {video.title}")
            download_video(video.watch_url, output_path)  # Usar la función de descarga
        print(f"Lista de reproducción descargada correctamente en {output_path}")
    except Exception as e:
        print(f"Error al descargar la lista de reproducción: {e}")

# Menú principal
def main_menu():
    print("Bienvenido al descargador de YouTube")
    print("1. Descargar un video de YouTube")
    print("2. Descargar una lista de reproducción de YouTube")
    print("3. Descargar un video y convertirlo a MP3")
    print("4. Salir")
    choice = input("Selecciona una opción: ")

    output_path = input("Ingresa la ruta de salida (deja vacío para usar la ruta actual): ")
    if not output_path:
        output_path = os.getcwd()  # Usar directorio actual si no se proporciona uno

    if choice == '1':
        video_url = input("Ingresa la URL del video: ")
        download_video(video_url, output_path)

    elif choice == '2':
        playlist_url = input("Ingresa la URL de la lista de reproducción: ")
        download_playlist(playlist_url, output_path)

    elif choice == '3':
        video_url = input("Ingresa la URL del video: ")
        download_video(video_url, output_path, convert_to_mp3=True)  # Conversión a MP3

    elif choice == '4':
        print("Saliendo...")
        sys.exit()

    else:
        print("Opción no válida, inténtalo de nuevo.")
        main_menu()

if __name__ == '__main__':
    while True:
        main_menu()

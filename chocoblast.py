import ctypes
import os
import requests

SPI_SETDESKWALLPAPER = 0x0014

def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        # Créer le répertoire si nécessaire
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        return True
    else:
        return False

def change_wallpaper(file_path):
    file_path = os.path.abspath(file_path)
    file_path = file_path.encode('utf-16le') + b'\x00\x00'
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_path, 3)

if __name__ == "__main__":
    image_url = 'https://cdn.discordapp.com/attachments/1164132960925143060/1197669336593207407/Sans_titre-13.png?ex=65bc1b7d&is=65a9a67d&hm=60e0e0b6bb4d862cf98d913ab8d9908c781cb8c1306c535e009b4a0a8da57cfe&'
    local_path = 'C:\\Users\\maila\\Documents\\Projet2024\\hack\\image.png'

    if download_image(image_url, local_path):
        change_wallpaper(local_path)
        print("Fond d'écran changé avec succès!")
    else:
        print("Échec du téléchargement de l'image.")

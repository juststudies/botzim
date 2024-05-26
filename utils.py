from pathlib import Path

def get_music_folder():
    desktop_path = Path.home() / 'Desktop'
    music_folder = desktop_path / 'musicas'

    if music_folder.exists() and music_folder.is_dir():
        return music_folder
    else:
        raise FileNotFoundError(f'A pasta "musicas" não foi encontrada em {desktop_path}')

try:
    music_folder = get_music_folder()
    print(f'Pasta de músicas encontrada: {music_folder}')
except FileNotFoundError as e:
    print(e)
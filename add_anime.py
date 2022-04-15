import os
import search
import mapper
import json
import sys
from colorama import Fore, Back, Style, init

def get_download_folder():
    with open(os.path.join(sys.path[0], 'config.json')) as f:
        config = json.load(f)
    return config['download_folder']

def get_anime_folder():
    with open(os.path.join(sys.path[0], 'config.json')) as f:
        config = json.load(f)
    return config['anime_folder']

def get_folders_in_downloads():
    folders = []
    download_folder = get_download_folder()
    for file in sorted(os.listdir(download_folder)):
        if file.startswith('.'):
            continue
        d = os.path.join(download_folder, file)
        if os.path.isdir(d):
            folders.append(d)
    if len(folders) == 0:
        print(f'\n{Fore.GREEN}{download_folder}{Fore.RED} does not have any folders!{Style.RESET_ALL}')
        quit()
    return folders

def folder_selection(folders):
    print()
    for folder in folders:
        print(f'[{Fore.GREEN}{str(folders.index(folder) + 1)}{Style.RESET_ALL}] {folder.split("/")[-1]}')
    selection = folders[int(input('\nSelect a folder: ')) - 1]
    return selection

def get_episodes(folder):
    episodes = []
    for file in sorted(os.listdir(folder)):
        if file.startswith('.'):
            continue
        episodes.append(file)
    return episodes

def rename(episodes, folder):
    print(f'\nFirst file name: {Fore.GREEN}{episodes[0]}{Style.RESET_ALL}')
    print(f'Number of files: {Fore.GREEN}{str(len(episodes))}{Style.RESET_ALL}\n')
    start_input = input(f'Enter starting episode number {Fore.CYAN}(blank for 1){Style.RESET_ALL}: ')
    start = 1
    if start_input != "":
        start_input = int(start_input)
    last_episode = start + len(episodes)
    cur_episode = start
    os.chdir(folder)
    for episode in episodes:
        cur_episode_str = str(cur_episode)
        while len(cur_episode_str) != len(str(last_episode)):
            cur_episode_str = '0' + cur_episode_str
        old_ext = os.path.splitext(episode)[1]
        os.rename(episode, f'Episode {cur_episode_str + old_ext}')
        cur_episode += 1

def move(episodes, folder):
    anime_folder = get_anime_folder()
    anime_name = input(f'Enter anime name {Fore.CYAN}(blank to reuse folder name){Style.RESET_ALL}: ')
    if anime_name == '':
        anime_name = folder.split('/')[-1]
    season_number = input(f'Enter season number {Fore.CYAN}(blank for no season){Style.RESET_ALL}: ')
    dest_folder = ''
    if season_number == '':
        dest_folder = f'{anime_folder}/{anime_name}'
    else:
        dest_folder = f'{anime_folder}/{anime_name}/Season {int(season_number)}'
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    for file in os.listdir(folder):   
        os.rename(f'{folder}/{file}', f'{dest_folder}/{file}')
    os.rmdir(folder)

if __name__ == "__main__":
    init() # For colorama
    downloads_folders = get_folders_in_downloads()
    selected_folder = folder_selection(downloads_folders)
    episodes = get_episodes(selected_folder)
    rename(episodes, selected_folder)
    move(episodes, selected_folder)
    anilist_id = search.get_anilist_id()
    mapper.map_folder(selected_folder, anilist_id)

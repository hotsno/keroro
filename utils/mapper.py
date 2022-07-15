from colorama import Fore, Style
import json
import os
import sys

from . import anilist_requests
from . import search
from . import config

g = Fore.GREEN
c = Fore.CYAN
re = Style.RESET_ALL

def map():
    remove_invalid_paths()
    leaf_folders = get_leaf_folders()
    unmapped_folders = get_unmapped_folders(leaf_folders)
    while len(unmapped_folders) != 0:
        unmapped_folders = map_folder_from_unmapped(unmapped_folders)

def remove_invalid_paths():
    folder_map = get_map()
    temp = {}
    for folder in folder_map:
        if os.path.isdir(folder):
            temp[folder] = folder_map[folder]
    folder_map = temp
    save_map(folder_map)

def get_leaf_folders():
    folders = []
    stack = [config.get_config()["anime_folder"]]
    while len(stack) != 0:
        cur = stack.pop()
        is_end = True
        for file in sorted(os.listdir(cur)):
            d = os.path.join(cur, file)
            if file.startswith('.') or not os.path.isdir(d):
                continue
            stack.append(d)
            is_end = False
        if is_end:
            folders.append(cur)
    return folders

def get_unmapped_folders(folders):
    folder_map = get_map()
    unmapped_folders = []
    for folder in folders:
        if folder not in folder_map:
            unmapped_folders.append(folder)
    return unmapped_folders

def map_folder_from_unmapped(unmapped_folders):
    print(f"{g}Unmapped folders:{re}")
    i = 1
    for folder in unmapped_folders:
        anime_folder_len = len(config.get_config()["anime_folder"])
        print(f'[{g}{i}{re}] {c}{folder[anime_folder_len + 1:]}{re}')
        i += 1
    user_input = input("\nSelect a folder to map (or 's' to skip): ")
    if user_input in ["s"]:
        return []
    folder_number = int(user_input) - 1
    folder = unmapped_folders[folder_number]
    anilist_id = search.get_anilist_id()
    map_folder(folder, anilist_id)
    del unmapped_folders[folder_number]
    if len(unmapped_folders) == 0:
        print(f'\n{g}All your folders are mapped!{re}')
    return unmapped_folders

def map_folder(folder, anilist_id):
    if anilist_id == None:
        return
    title = anilist_requests.get_title(anilist_id)
    folder_map = get_map()
    folder_map[folder] = {
        "anilist_id": anilist_id,
        "title": title
    }
    save_map(folder_map)
    print(f'\n{g}Mapped to AniList ID{re} {anilist_id}')

def get_map():
    try:
        with open(os.path.join(sys.path[0], 'map.json')) as f:
            folder_map = json.load(f)
    except:
        folder_map = {}
    return folder_map

def save_map(folder_map):
    with open(os.path.join(sys.path[0], 'map.json'), 'w') as f:
        f.seek(0)
        json.dump(folder_map, f, indent = 4)
        f.truncate()

if __name__ == "__main__":
    map()
    quit()
from colorama import Fore, Style
import json
import os
import sys

from . import anilist_requests
from . import search
from . import config

def save_map(folder_map):
    with open(os.path.join(sys.path[0], 'map.json'), 'w') as f:
        f.seek(0)
        json.dump(folder_map, f, indent = 4)
        f.truncate()

def remove_invalid_paths():
    folder_map = get_folder_map()

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
    folder_map = get_folder_map()
    unmapped_folders = []
    for folder in folders:
        if folder not in folder_map:
            unmapped_folders.append(folder)
    return unmapped_folders

def map_folder_from_unmapped(unmapped_folders, skippable):
    i = 1
    for folder in unmapped_folders:
        anime_folder_len = len(config.get_config()["anime_folder"])
        print(f'[{Fore.GREEN}{i}{Style.RESET_ALL}] {Fore.CYAN}{folder[anime_folder_len + 1:]}{Style.RESET_ALL}')
        i += 1
    if skippable:
        prompt = "\nSelect a folder to map (type 's' to skip): "
    else:
        prompt = "\nSelect a folder to map (type 'q' to quit): "
    user_input = input(prompt)
    if user_input in ["q", "s"]:
        return []
    folder_number = int(user_input) - 1
    folder = unmapped_folders[folder_number]
    anilist_id = search.get_anilist_id()
    map_folder(folder, anilist_id)
    del unmapped_folders[folder_number]
    if len(unmapped_folders) == 0:
        print('\nAll your folders are mapped!')
    return unmapped_folders

def map_folder(folder, anilist_id):
    if anilist_id == None:
        return
    title = anilist_requests.get_title(anilist_id)
    folder_map = get_folder_map()
    folder_map[folder] = {
        "anilist_id": anilist_id,
        "title": title
    }
    save_map(folder_map)
    print(f'\nMapped to AniList ID {anilist_id}')

def get_folder_map():
    try:
        with open(os.path.join(sys.path[0], 'map.json')) as f:
            folder_map = json.load(f)
    except:
        folder_map = {}
    return folder_map

def map(skippable):
    remove_invalid_paths()
    leaf_folders = get_leaf_folders()
    unmapped_folders = get_unmapped_folders(leaf_folders)
    while len(unmapped_folders) != 0:
        unmapped_folders = map_folder_from_unmapped(unmapped_folders, skippable)

if __name__ == "__main__":
    map(False)
    quit()
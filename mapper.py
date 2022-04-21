import os
import json
import sys
from colorama import Fore, Style
import anilist_requests
import search

with open(os.path.join(sys.path[0], 'config.json')) as f:
    config = json.load(f)

def save_map(folder_map):
    with open(os.path.join(sys.path[0], 'map.json'), 'r+') as f:
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
    stack = [config["anime_folder"]]
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

def map_folder_from_unmapped(unmapped_folders):
    folder_map = get_folder_map()
    print('\nSelect an unmapped folder:')
    i = 1
    for folder in unmapped_folders:
        print(f'[{Fore.GREEN}{i}{Style.RESET_ALL}] {Fore.CYAN}{folder[29:]}{Style.RESET_ALL}')
        i += 1
    folder_number = int(input('\n')) - 1
    folder = unmapped_folders[folder_number]
    anilist_id = search.get_anilist_id()
    map_folder(folder, anilist_id)
    del unmapped_folders[folder_number]
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
    with open(os.path.join(sys.path[0], 'map.json')) as f:
        folder_map = json.load(f)
    return folder_map

if __name__ == "__main__":
    remove_invalid_paths()
    leaf_folders = get_leaf_folders()
    unmapped_folders = get_unmapped_folders(leaf_folders)
    while len(unmapped_folders) != 0:
        unmapped_folders = map_folder_from_unmapped(unmapped_folders)
    print('\nAll your folders are mapped!')
    quit()


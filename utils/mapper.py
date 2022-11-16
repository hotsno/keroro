import json, os, sys
import utils.anilist_requests, utils.search, utils.config
from colorama import Fore, Style

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
    stack = [utils.config.get_config()["anime_folder"]]
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

    print(colored_text([[Fore.GREEN, '\nUnmapped folders:']]))
    for i, folder in enumerate(unmapped_folders):
        anime_folder_len = len(utils.config.get_config()["anime_folder"])
        relative_folder_path = folder[anime_folder_len + 1:]
        print(colored_text([
            [None, '['],
            [Fore.GREEN,  str(i + 1)],
            [None, '] '],
            [Fore.CYAN,  relative_folder_path]
        ]))
    
    user_input = input(colored_text([
        [None, '\nSelect a folder to map (or '],
        [Fore.GREEN, "'s' "],
        [None, "to skip): "]
    ]))
    if user_input == 's':
        return []
    
    try:
        folder_index = int(user_input) - 1
        if not 0 <= folder_index < len(unmapped_folders):
            raise Exception
    except:
        print(colored_text([[Fore.RED, '\nInvalid folder number!']]))
        map_folder_from_unmapped(unmapped_folders)

    anilist_id = utils.search.get_anilist_id()
    if not anilist_id:
        return []

    map_folder(unmapped_folders[folder_index], anilist_id)
    del unmapped_folders[folder_index]

    if len(unmapped_folders) == 0:
        print(colored_text([
            [Fore.GREEN, '\nAll your folders are mapped!']
        ]))
    
    return unmapped_folders

def map_folder(folder, anilist_id):
    title = utils.anilist_requests.get_title(anilist_id)
    folder_map = get_map()
    folder_map[folder] = {
        "anilist_id": anilist_id,
        "title": title
    }
    save_map(folder_map)
    print(colored_text([
        [Fore.GREEN, 'Mapped to AniList ID '],
        [Fore.BLUE, anilist_id]
    ]))

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

def colored_text(text_arr):
    s = ""
    for style, text in text_arr:
        if not style:
            style = Style.RESET_ALL
        s += str(style) + str(text)
    return s + Style.RESET_ALL
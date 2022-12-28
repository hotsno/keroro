import os
from colorama import Style, Fore

GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW

def colored_text(text_arr):
    s = ''
    for style, text in text_arr:
        if not style:
            style = Style.RESET_ALL
        s += str(style) + str(text)
    return s + Style.RESET_ALL

def get_episode_number(file_path, folder_map):
    folder_path, file_name = os.path.split(file_path)
    if folder_path not in folder_map:
        quit()
    offset = 0
    if 'offset' in folder_map[folder_path]:
        offset = folder_map[folder_path]['offset']
    sorted_file_names = [file for file in sorted(os.listdir(folder_path)) if not file.startswith('.')]
    return sorted_file_names.index(file_name) + 1 + offset

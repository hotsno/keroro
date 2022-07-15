import pathlib
from colorama import Fore, Style
import json
import sys
import os
import subprocess

def is_set_up():
    if os.path.exists(os.path.join(sys.path[0], 'config.json')):
        return True
    return False

def set_up():
    if is_set_up():
        return
    update_lua_script()
    anime_folder = input(f'Anime folder path: ')
    anilist_user = input(f'AniList username: ')
    mpv_path = get_mpv_path()

    config = {
        "anime_folder": anime_folder,
        "anilist_user": anilist_user,
        "mpv_path": mpv_path,
        "token": ""
    }

    with open(os.path.join(sys.path[0], 'config.json'), 'w') as f:
        f.seek(0)
        json.dump(config, f, indent=4)
        f.truncate()

    print(f"\nPlease manually enter your {Fore.GREEN}'token'{Style.RESET_ALL} into {Fore.GREEN}'config.json'{Style.RESET_ALL}!\nTo get your token, visit {Fore.GREEN}https://anilist.co/api/v2/oauth/authorize?client_id=7723&response_type=token{Style.RESET_ALL}")

def get_mpv_path():
    is_windows = os.name == "nt"
    try:
        if is_windows:
            mpv_path = subprocess.check_output(['where', 'mpv']).decode("utf-8").splitlines()[0]
        else:
            mpv_path = subprocess.check_output(['which', 'mpv']).decode("utf-8").splitlines()[0]
        print(f"\nUsing mpv path: {mpv_path}")
    except:
        print("\nCould not find mpv in your PATH")
        if is_windows:
            example = "ex. C:\\Program Files\\mpv\\mpv.exe"
        else:
            example = "ex. /usr/local/bin/mpv"
        mpv_path = input(f"\nPath to mpv ({example}): ")
    return mpv_path

def get_config():
    with open(os.path.join(sys.path[0], 'config.json')) as f:
        config = json.load(f)
        return config

def update_lua_script():
    update_path = os.path.join(sys.path[0], "update.py")
    python_path = sys.executable
    to_prepend = f'local python_path = "{python_path}"\nlocal update_path = "{update_path}"\n'
    with open(os.path.join(sys.path[0], "mpv", "scripts", "anilist.lua"), 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(to_prepend + '\n' + content)
from colorama import Fore, Style
import json
import sys
import os
import subprocess

g = Fore.GREEN
r = Fore.RED
re = Style.RESET_ALL

def set_up():
    if os.path.exists(os.path.join(sys.path[0], 'config.json')):
        return

    update_lua_script()

    print(f"\n{g}Running setup!{re}\n")
    anime_folder = input('Anime folder path: ')
    anilist_user = input('AniList username: ')
    mpv_path = get_mpv_path()
    config = {
        "anime_folder": anime_folder,
        "anilist_user": anilist_user,
        "mpv_path": mpv_path,
        "token": ""
    }
    save_config(config)

    print(f"\nPlease manually enter your {g}'token'{re} into {g}'config.json'{re}!\nTo get your token, visit {g}https://anilist.co/api/v2/oauth/authorize?client_id=7723&response_type=token{re}")
    input("\nPress enter when done.")

    print(f"\nPlease copy {g}'anilist.lua'{re} into your mpv script folder.")
    input("\nPress enter when done.")
    print()

def get_mpv_path():
    is_windows = os.name == "nt"
    try:
        if is_windows:
            mpv_path = subprocess.check_output(['where', 'mpv']).decode("utf-8").splitlines()[0]
        else:
            mpv_path = subprocess.check_output(['which', 'mpv']).decode("utf-8").splitlines()[0]
        print(f"\n{g}Auto-detected mpv path:{re} {mpv_path}")
    except:
        print(f"\n{r}Could not find mpv in your PATH{re}")
        if is_windows:
            example = "ex. C:\\Program Files\\mpv\\mpv.exe"
        else:
            example = "ex. /usr/local/bin/mpv"
        mpv_path = input(f"\nPath to mpv ({example}): ")
    return mpv_path

def update_lua_script():
    update_path = os.path.join(sys.path[0], "update.py")
    python_path = sys.executable
    to_prepend = f'local python_path = "{python_path}"\nlocal update_path = "{update_path}"\n'
    with open(os.path.join(sys.path[0], "mpv", "scripts", "anilist.lua"), 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(to_prepend + '\n' + content)

def get_config():
    with open(os.path.join(sys.path[0], 'config.json')) as f:
        config = json.load(f)
        return config

def save_config(config):
    with open(os.path.join(sys.path[0], 'config.json'), 'w') as f:
        f.seek(0)
        json.dump(config, f, indent=4)
        f.truncate()

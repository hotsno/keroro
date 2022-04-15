import json
import sys
import os
from colorama import Fore, Back, Style, init

download_folder = input(f'{Fore.GREEN}Download folder{Style.RESET_ALL} path: ')
anime_folder = input(f'{Fore.GREEN}Anime folder{Style.RESET_ALL} path: ')
anilist_user = input (f'AniList {Fore.GREEN}username{Style.RESET_ALL}: ')

config = {
    "download_folder": download_folder,
    "anime_folder": anime_folder,
    "anilist_user": anilist_user,
    "token": ""
}

with open(os.path.join(sys.path[0], 'config.json'), 'r+') as f:
    f.seek(0)
    json.dump(config, f, indent = 4)
    f.truncate()

print(f"\nPlease manually enter your {Fore.GREEN}'token'{Style.RESET_ALL} into {Fore.GREEN}'config.json'{Style.RESET_ALL}!\nTo get your token, visit {Fore.GREEN}https://anilist.co/api/v2/oauth/authorize?client_id=7723&response_type=token{Style.RESET_ALL}")

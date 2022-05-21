import sys
import json
import os
from colorama import Fore, Style
import anilist_requests

with open(os.path.join(sys.path[0], 'map.json')) as f:
    folder_map = json.load(f)

def get_available_list(watchlist):
    user_list = []
    for folder in folder_map:
        if not os.path.isdir(folder):
            continue
        if folder_map[folder]["anilist_id"] in watchlist:
            watchlist[folder_map[folder]["anilist_id"]]["folder"] = folder
            user_list.append(watchlist[folder_map[folder]["anilist_id"]])
    return user_list

def get_episode_path(selected_anime_folder, selected_anime_episode):
    episodes = []
    for file in sorted(os.listdir(selected_anime_folder)):
        if file.startswith('.'):
            continue
        episodes.append(file)
    if len(episodes) == 0:
        print(f"\n{Fore.RED}'{selected_anime_folder}/Episode {selected_anime_episode}.mkv' does not exist!{Style.RESET_ALL}")
        quit()
    digits = len(episodes[-1]) - 13 # 'Episode .mkv' = 13 digits
    while len(selected_anime_episode) <= digits:
        selected_anime_episode = "0" + selected_anime_episode
    return f"{selected_anime_folder}/Episode {selected_anime_episode}.mkv"

def print_user_list(user_list):
    i = 1
    for anime in user_list:
        print(f'[{Fore.GREEN}{i}{Style.RESET_ALL}] {Fore.CYAN}{anime["title"]}{Style.RESET_ALL} - {Fore.YELLOW}Episode {int(anime["progress"]) + 1}{Style.RESET_ALL}')
        i += 1
    print()

def play_episode(episode_path):
    if not os.path.exists(episode_path):
        print(f"{Fore.RED}\n'{episode_path}' does not exist!")
        exit()
    os.system(f"mpv '{episode_path}' >/dev/null 2>&1 & disown")

if __name__ == "__main__":
    print()
    watching_list = anilist_requests.get_watching_list()
    available_list = get_available_list(watching_list)
    print_user_list(available_list)
    selected_anime = available_list[int(input(f"\nSelect an anime:{Fore.GREEN} ")) - 1]
    selected_anime_folder = selected_anime["folder"]
    selected_anime_episode = str(selected_anime["progress"] + 1)
    episode_path = get_episode_path(selected_anime_folder, selected_anime_episode)
    play_episode(episode_path)

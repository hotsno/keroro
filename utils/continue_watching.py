import subprocess
from colorama import Fore, Style
import os

from . import anilist_requests
from . import mapper
from . import offset

g = Fore.GREEN
re = Style.RESET_ALL

def continue_watching():
    print()
    watching_list = anilist_requests.get_watching_list()
    available_list = get_available_list(watching_list)
    if len(available_list) == 0:
        print("\nYou have nothing to watch! (or AniList status isn't \"WATCHING\")")
        quit()

    i = 1
    for anime in available_list:
        print(f'[{Fore.GREEN}{i}{Style.RESET_ALL}] {Fore.CYAN}{anime["title"]}{Style.RESET_ALL} - {Fore.YELLOW}Episode {int(anime["progress"]) + 1}{Style.RESET_ALL}')
        i += 1
    user_input = input("\nSelect an anime ('m' for more options): ")
    if user_input == "m":
        more_options()
    selected_anime = available_list[int(user_input) - 1]
    selected_anime_folder = selected_anime["folder"]
    selected_anime_episode = selected_anime["progress"] + 1
    episode_path = get_episode_path(selected_anime_folder, selected_anime_episode)
    play_episode(episode_path)

def get_available_list(watchlist):
    user_list = []
    folder_map = mapper.get_map()
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
    folder_map = mapper.get_map()
    offset = 0
    if "offset" in folder_map[selected_anime_folder]:
        offset = folder_map[selected_anime_folder]["offset"]
    index_to_play = selected_anime_episode - 1 - offset
    if index_to_play >= len(episodes):
        print(f"\n{Fore.RED}Episode not found! Check the folder below and add an episode offset if needed:\n{selected_anime_folder}")
        quit()
    return f"{selected_anime_folder}/{episodes[index_to_play]}"

def play_episode(episode_path):
    if not os.path.exists(episode_path):
        print(f"{Fore.RED}\n'{episode_path}' does not exist!")
        exit()
    subprocess.Popen(["mpv", episode_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    quit()

def more_options():
    while True:
        print(f"\n{g}Type 'm' to map folders to AniList IDs.")
        print(f"Type 'o' to add an offset.")
        print(f"Type 'w' to watch.")
        print(f"Type 'q' to quit.{re}")
        user_input = input("\nInput: ")
        if user_input == "m":
            mapper.map()
        elif user_input == "o":
            offset.create_offset()
        elif user_input == "w":
            continue_watching()
        elif user_input == "q":
            quit()
        else:
            print("Choose a valid option!")

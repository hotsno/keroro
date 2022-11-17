import subprocess, os
import utils.anilist_requests, utils.mapper, utils.offset, utils.config
from utils.common import colored_text, GREEN, CYAN, YELLOW, RED

def continue_watching():

    watching_list = utils.anilist_requests.get_watching_list()
    available_list = get_available_list(watching_list)
    if not available_list:
        print('\nYou have nothing to watch! (or AniList status isn\'t "WATCHING")')
        quit()
    
    print()
    for i, anime in enumerate(available_list):
        print(colored_text([
            [None, '['],
            [GREEN, str(i + 1)],
            [None, '] '],
            [CYAN, anime['title']],
            [None, ' - '],
            [YELLOW, f'Episode {int(anime["progress"]) + 1}']
        ]))
    user_input = input("\nSelect an anime ('m' for more options): ")
    if user_input == 'm':
        more_options()
    
    selected_anime = available_list[int(user_input) - 1]
    selected_anime_folder = selected_anime['folder']
    selected_anime_episode = selected_anime['progress'] + 1
    episode_path = get_episode_path(selected_anime_folder, selected_anime_episode)
    if not episode_path:
        print(colored_text([[RED, f'Episode not found! Check the folder below and add an episode offset if needed:\n{selected_anime_folder}']]))
        quit()
    play_episode(episode_path)

def get_available_list(watchlist):
    user_list = []
    folder_map = utils.mapper.get_map()
    for folder in folder_map:
        if not os.path.isdir(folder):
            continue
        if folder_map[folder]['anilist_id'] in watchlist:
            episode_progess = watchlist[folder_map[folder]['anilist_id']]['progress']
            if not get_episode_path(folder, episode_progess + 1):
                continue
            watchlist[folder_map[folder]['anilist_id']]['folder'] = folder
            user_list.append(watchlist[folder_map[folder]['anilist_id']])
    return user_list

def get_episode_path(selected_anime_folder, selected_anime_episode):
    episodes = []
    for file in sorted(os.listdir(selected_anime_folder)):
        if file.startswith('.'):
            continue
        episodes.append(file)
    folder_map = utils.mapper.get_map()
    offset = 0
    if 'offset' in folder_map[selected_anime_folder]:
        offset = folder_map[selected_anime_folder]['offset']
    index_to_play = selected_anime_episode - 1 - offset
    try:
        return f'{selected_anime_folder}/{episodes[index_to_play]}'
    except:
        return None

def play_episode(episode_path):
    if not os.path.exists(episode_path):
        print(colored_text([[RED, f"\n'{episode_path}' does not exist!"]]))
        exit()
    mpv_path = utils.config.get_config()['mpv_path']
    subprocess.Popen([mpv_path, episode_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    quit()

def more_options():
    while True:
        print(colored_text([
            [GREEN, '\nm'],
            [None, ' - map folders to AniList IDs\n'],
            [GREEN, 'o'],
            [None, ' - add offset\n'],
            [GREEN, 'w'],
            [None, ' - watch\n'],
            [GREEN, 'q'],
            [None, ' - quit'],
        ]))
        user_input = input('\nInput: ')
        if user_input == 'm':
            utils.mapper.map()
        elif user_input == 'o':
            utils.offset.create_offset()
        elif user_input == 'w':
            continue_watching()
        elif user_input == 'q':
            quit()
        else:
            print('\nInvalid option!')
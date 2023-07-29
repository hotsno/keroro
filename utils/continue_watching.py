import subprocess, os
import utils.anilist_requests, utils.mapper, utils.offset, utils.config
from utils.common import colored_text, GREEN, CYAN, YELLOW, RED

def sync_with_anilist():
    watchlist = utils.anilist_requests.get_watching_list()
    folder_map = utils.mapper.get_map()
    for _, o in folder_map.items():
        anilist_id = o['anilist_id']
        if anilist_id in watchlist:
            o['status'] = 'WATCHING'
            anilist_progress = watchlist[anilist_id]['progress']
            if 'progress' in o and o['progress'] > anilist_progress:
                # TODO: Add colors to this (way too lazy to do this rn)
                print(f'\nMismatched progress for {watchlist[anilist_id]["title"]}!\n')
                keep = input(f'AniList progress: {anilist_progress}\nLocal progress: {o["progress"]}\n\nKeep local? [y/n] ') == 'y'
                if not keep:
                    o['progress'] = watchlist[anilist_id]['progress']
                else:
                    utils.anilist_requests.update_progress(anilist_id, o['progress'])
            else:
                o['progress'] = watchlist[anilist_id]['progress']
        else:
            o['status'] = 'UNKNOWN'
    utils.mapper.save_map(folder_map)

def check_local_progress(available_list):
    folder_map = utils.mapper.get_map()
    print(folder_map)
    for _, v in folder_map.items():

        print(available_list)
        if 'local_progress' in v and v['local_progress'] > available_list[v['title']]['progress']:
            print('ye')

def continue_watching():
    try:
        sync_with_anilist()
    except:
        print('\nCan\'t connect to AniList!')

    folder_map = utils.mapper.get_map()
    # We do a little trolling
    available_list = [{**v, 'folder': k} for k, v in folder_map.items() if 'status' in v and v['status'] == 'WATCHING' and get_episode_path(k, v['progress'] + 1)]
    if not available_list:
        print('\nNo valid items found!')
        more_options()
    
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
    user_input = input("\nSelect a show ('m' for more options): ")
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

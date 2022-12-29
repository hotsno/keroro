import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Add parent directory to sys path so we can import utils
import utils.anilist_requests, utils.config, utils.mapper, utils.common

def update_progress_local(watched_episode, folder_path, folder_map):
    folder_map[folder_path]['progress'] = watched_episode
    utils.mapper.save_map(folder_map)

def update_progress(watched_episode, folder_path):
    media_id = folder_map[folder_path]["anilist_id"]
    progress = utils.anilist_requests.get_progress(media_id)
    if watched_episode <= progress:
        quit()
    utils.anilist_requests.update_progress(media_id, watched_episode)

if __name__ == '__main__':
    file_path = sys.argv[1]
    folder_map = utils.mapper.get_map()
    watched_episode = utils.common.get_episode_number(file_path, folder_map)
    folder_path = os.path.split(file_path)[0]
    try:
        update_progress(watched_episode, folder_path)
        print('Updated AniList!')
    except:
        update_progress_local(watched_episode, folder_path, folder_map)
        print('Updated progress locally!')

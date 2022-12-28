import os, sys
import utils.anilist_requests, utils.config, utils.mapper, utils.common

def get_progress(mediaId):
    return utils.anilist_requests.get_progress(mediaId)

def update_progress(file_path):
    folder_map = utils.mapper.get_map()
    watched_episode = utils.common.get_episode_number(file_path, folder_map)
    folder_path = os.path.split(file_path)[0]
    mediaId = folder_map[folder_path]["anilist_id"]
    progress = get_progress(mediaId)
    if watched_episode <= progress:
        quit()
    utils.anilist_requests.update_progress(mediaId, watched_episode)

if __name__ == '__main__':
    update_progress(sys.argv[1])

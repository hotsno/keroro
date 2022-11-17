import os, sys
import utils.anilist_requests, utils.config, utils.mapper

def get_progress(mediaId):
    return utils.anilist_requests.get_progress(mediaId)

def update_progress(mediaId, progress, offset):
    episodes = []
    for file in sorted(os.listdir(folder_path)):
        if file.startswith('.'):
            continue
        episodes.append(file)
    watched_episode = episodes.index(file_name) + 1 + offset
    if watched_episode <= progress:
        quit()
    utils.anilist_requests.update_progress(mediaId, watched_episode)


file_path = sys.argv[1]
folder_path, file_name = os.path.split(file_path)
folder_map = utils.mapper.get_map()
if folder_path not in folder_map:
    quit()

mediaId = folder_map[folder_path]["anilist_id"]
progress = get_progress(mediaId)
offset = 0
if 'offset' in folder_map[folder_path]:
    offset = folder_map[folder_path]['offset']
update_progress(mediaId, progress, offset)
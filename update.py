import os
import sys

import utils.anilist_requests
import utils.config
import utils.mapper

file_path = sys.argv[1]
(folder_path, file_name) = os.path.split(file_path)
folder_map = utils.mapper.get_map()
offset = 0
print(folder_map)
print(folder_path)
print(file_name)
if "offset" in folder_map[folder_path]:
    offset = folder_map[folder_path]["offset"]

def get_progress(mediaId):
    return utils.anilist_requests.get_progress(mediaId)

def update_progress(mediaId, progress):
    episodes = []
    for file in sorted(os.listdir(folder_path)):
        if file.startswith('.'):
            continue
        episodes.append(file)
    watched_episode = episodes.index(file_name) + 1 + offset
    if watched_episode <= progress:
        quit()
    utils.anilist_requests.update_progress(mediaId, watched_episode)

for folder in folder_map:
    if folder_path == folder:
        mediaId = folder_map[folder]["anilist_id"]
        progress = get_progress(mediaId)
        update_progress(mediaId, progress)
        break

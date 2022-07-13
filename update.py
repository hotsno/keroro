import anilist_requests
import json
import os
import sys

file_path = sys.argv[1]
file_name = file_path.split('/')[-1]
folder_path = file_path[:file_path.rfind('/')]

with open(os.path.join(sys.path[0], 'map.json')) as f:
    folder_map = json.load(f)

def get_progress(mediaId):
    return anilist_requests.get_progress(mediaId)

def update_progress(mediaId, progress):
    watched_episode = int(file_name.split('.')[0].split(' ')[1])
    if watched_episode <= progress:
        quit()
    anilist_requests.update_progress(mediaId, watched_episode)

for folder in folder_map:
    if folder_path == folder:
        mediaId = folder_map[folder]["anilist_id"]
        progress = get_progress(mediaId)
        update_progress(mediaId, progress)
        break

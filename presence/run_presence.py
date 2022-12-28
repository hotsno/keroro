from pypresence import Presence
import time, os, json, sys

def get_map():
    try:
        with open(os.path.join(sys.path[0], 'presence.json')) as f:
            folder_map = json.load(f)
    except:
        folder_map = {}
    return folder_map

client_id = '1043754107464327268'
RPC = Presence(client_id)
RPC.connect()

while True:
    time.sleep(5)
    m = get_map()
    if not m:
        continue
    title = m['title']
    episode = 'Episode ' + m['episode']
    large_image = m['poster']
    large_text = str(int(float(m['percent']))) + '% complete' # Converts from '1.395293' to '1'
    small_image = 'anilist'
    small_text = m['username'] + ' on AniList'
    buttons = [
        {
            'label': 'Try Keroro',
            'url': 'https://github.com/hotsno/keroro'
        },
        {
            'label': 'AniList entry',
            'url': m['link']
        }
    ]
    RPC.update(details=title, state=episode, large_image=large_image, large_text=large_text, small_image=small_image, small_text=small_text, buttons=buttons)

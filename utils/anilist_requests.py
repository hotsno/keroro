import requests

from . import config

def anilist_call(query, variables):
    url = 'https://graphql.anilist.co'
    response = requests.post(
        url,
        json = {'query': query, 'variables': variables}
    )
    return response.json()

def anilist_call_mutate(query, variables):
    config_dict = config.get_config()
    url = 'https://graphql.anilist.co'
    response = requests.post(
        url,
        headers = {'Authorization': 'Bearer ' + config_dict["token"], 'Content-Type': 'application/json', 'Accept': 'application/json'},
        json = {'query': query, 'variables': variables}
    )
    return response.json()

def get_watching_list():
    config_dict = config.get_config()
    anilist_user = config_dict["anilist_user"]
    variables = {
        "userName": anilist_user
    }
    query = '''
    query ($userName: String) {
      Page(page: 1, perPage: 20) {
        mediaList(userName: $userName, status_in: [CURRENT, REPEATING], type: ANIME) {
          progress
          media {
            id
            title {
              userPreferred
            }
          }
        }
      }
    }
    '''
    result = anilist_call(query, variables)
    cleaned_up = {}
    watchlist = result["data"]["Page"]["mediaList"]
    for item in watchlist:
        cleaned_up[item["media"]["id"]] = {
            "title": item["media"]["title"]["userPreferred"],
            "progress": item["progress"],
            "id": item["media"]["id"]
        }
    return cleaned_up

def get_search_results(searchTerm, page):
    variables = {
        "searchTerm": searchTerm,
        "page": page
    }
    query = '''
    query ($searchTerm: String, $page: Int) {
      Page(page: $page, perPage: 5) {
        media(search: $searchTerm, type: ANIME) {
          title {
            romaji
          }
          id
        }
      }
    }
    '''
    result = anilist_call(query, variables)
    cleaned_up = []
    watchlist = result["data"]["Page"]["media"]
    for item in watchlist:
        cleaned_up.append([item["title"]["romaji"], item["id"]])
    return cleaned_up

def update_progress(mediaId, progress):
    variables = {
        "mediaId": mediaId,
        "progress": progress
    }
    query = '''
    mutation ($mediaId: Int, $progress: Int) {
      SaveMediaListEntry (mediaId: $mediaId, progress: $progress) {
          progress
      }
    }
    '''
    anilist_call_mutate(query, variables)

def get_progress(mediaId):
    config_dict = config.get_config()   
    variables = {
        "userName": config_dict["anilist_user"],
        "mediaId": mediaId
    }
    query = '''
    query ($userName: String, $mediaId: Int) {
      MediaList(userName: $userName, mediaId: $mediaId) {
          progress
      }
    }
    '''
    result = anilist_call(query, variables)
    if result["data"]["MediaList"] == None:
        raise ValueError(f'AniList ID {mediaId} is not on your AniList.')
    return result["data"]["MediaList"]["progress"]

def get_title(anilist_id):
    variables = {
        "id": anilist_id
    }
    query = '''
    query ($id: Int) {
      Media(id: $id) {
        title {
          romaji
        }
      }
    }
    '''
    result = anilist_call(query, variables)
    return result["data"]["Media"]["title"]["romaji"]
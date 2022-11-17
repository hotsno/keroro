import utils.anilist_requests
from utils.common import colored_text, GREEN, RED, CYAN

def get_anilist_id():
    search_term = input(colored_text(
        [
            [None, "\nEnter a "],
            [GREEN, "search term "],
            [None, "or "],
            [GREEN, "'m' "],
            [None, "to manually enter ID: "]
        ]
    ))

    if not search_term:
        print(colored_text([[RED, "\nAborted mapping!"]]))
        return(None)

    elif search_term == 'm':
        id = input("Enter ID: ")
        try:
            return int(id)
        except:
            print(colored_text([[RED, '\nNot a valid number!']]))
            get_anilist_id()
        
    page = 1
    while True:
        search_results = search(search_term, page)
        print()
        for i, result in enumerate(search_results):
            print(colored_text([
                [None, '['],
                [GREEN, str(i + 1)],
                [None, '] '],
                [CYAN, str(result[0])]
            ]))
        choice = input("\nEnter a number, 'n' for next, or 'p' for previous: ")
        if choice == 'n':
            page += 1
        elif choice == 'p':
            page = page - 1 if page > 1 else 1
        else:
            return search_results[int(choice) - 1][1]
            
def search(searchTerm, page):
    return utils.anilist_requests.get_search_results(searchTerm, page)
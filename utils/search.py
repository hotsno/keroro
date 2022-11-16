from colorama import Fore, Style
import utils.anilist_requests

def get_anilist_id():
    search_term = input(colored_text(
        [
            [Style.RESET_ALL, "\nEnter a "],
            [Fore.GREEN, "search term "],
            [Style.RESET_ALL, "or "],
            [Fore.GREEN, "'m' "],
            [Style.RESET_ALL, "to manually enter ID: "]
        ]
    ))

    if not search_term:
        print(colored_text([[Fore.RED, "\nAborted mapping!"]]))
        return(None)

    elif search_term == 'm':
        id = input("Enter ID: ")
        try:
            return int(id)
        except:
            print(colored_text([[Fore.RED, '\nNot a valid number!']]))
            get_anilist_id()
        
    page = 1
    while True:
        search_results = search(search_term, page)
        print()
        x = 1
        for result in search_results:
            print(f"[{Fore.GREEN}{x}{Style.RESET_ALL}] {Fore.CYAN}{result[0]}{Style.RESET_ALL}")
            x += 1
        choice = input('\nEnter a number, \'n\' for next, or \'p\' for previous: ')
        if choice == 'n':
            page += 1
        elif choice == 'p':
            page = page - 1 if page > 0 else 0
        else:
            return search_results[int(choice) - 1][1]
            
def search(searchTerm, page):
    return utils.anilist_requests.get_search_results(searchTerm, page)

def colored_text(text_arr):
    s = ""
    for style, text in text_arr:
        s += style + text
    return s + Style.RESET_ALL
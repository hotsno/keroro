from colorama import Fore, Style
import anilist_requests

def search(searchTerm, page):
    return anilist_requests.get_search_results(searchTerm, page)

def get_anilist_id():
    search_term = input(f"\nEnter a {Fore.GREEN}search term {Style.RESET_ALL}or{Fore.GREEN} 'm'{Style.RESET_ALL} to manually enter ID {Fore.CYAN}(blank to skip mapping){Style.RESET_ALL}: ")
    if search_term == '':
        print(f'{Fore.RED}Mapping skipped!{Style.RESET_ALL}')
        return(None)
    elif search_term == 'm':
        return int(input("Enter ID: "))

    page = 1
    while True:
        search_results = search(search_term, page)
        print()
        x = 1
        for result in search_results:
            print(f"[{x}] {result[0]}")
            x += 1
        choice = input('\nEnter a number, or \'n\' for the next set of results: ')
        if choice == 'n':
            page += 1
        else:
            return search_results[int(choice) - 1][1]

from colorama import Style, Fore

GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW

def colored_text(text_arr):
    s = ''
    for style, text in text_arr:
        if not style:
            style = Style.RESET_ALL
        s += str(style) + str(text)
    return s + Style.RESET_ALL
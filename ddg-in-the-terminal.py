def typewriter(text, delay=0.02, randomize=False):
    for char in text:
        print(char, end="", flush=True)
        if randomize: time.sleep(0.1)
        else:
            time.sleep(delay)
    print() # move to next line after finishing


from ddgs import DDGS
import colorama
import time
from colorama import Style, Fore
colorama.init()

print(Fore.LIGHTYELLOW_EX + """⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⣶⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⢀⣴⣿⣿⣭⡤⠄⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀
⠀⢀⣿⣿⣿⣿⣿⡶⠋⠀⠀⠀⠈⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀
⠀⣾⣿⣿⣿⣿⡏⠀⠄⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⢰⣿⣿⣿⣿⣿⡇⠀⢠⣄⠀⠀⠀⠀⢰⡦⢹⣿⣿⣿⣿⣿⣿⣿⣿⡆
⢸⣿⣿⣿⣿⣿⡇⠀⠈⠉⠀⠀⠀⠀⠀⠀⠘⠋⠉⠉⣉⣽⣿⣿⣿⡇
⠸⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⠇
⠀⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⢠⣤⣀⡉⠉⢉⣀⣤⣼⣿⣿⣿⡿⠀
⠀⠘⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠘⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⡿⠁⠀
⠀⠀⠈⢿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠙⠉⠀⠘⣿⣿⣿⣿⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣇⠀⠀⠀⠀⠀⠰⣤⣴⣿⣿⡿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠛⠀⠀⠀⠀⠀⠀⠘⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀""" + Style.RESET_ALL)

print()
query = input("YOUR SEARCH QUERY > ")
with DDGS() as ddgs:
    results = ddgs.text(query, max_results=5)
    for i,result in enumerate(results, 1):
        typewriter(f"\n [{i}] {result['title']}")
        print(f"    {result['href']}")
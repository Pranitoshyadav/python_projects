import re, random
from colorama import Fore, init

init(autoreset=True)

destination = {
               "beachs" : ["bali", "maldives", "phuket"],
               "mountain" : ["alps", "rocky mountain", "Himalaya", " mt.everest"],
               "cities" : ["tokoy", "Paris", "kathmandu", "new york"]
               }
jokes = ["Why don't programmers like nature? Too many bugs!",

"Why did the computer go to the doctor? Because it had a virus!",

"Why do travelers always feel warm? Because of all their hot spots!"]

def normalise_input(text):
    re.sub(r"\s +" "".strip().lower())
import re,random
from  colorama import Fore,init

init(autoreset=True)

destinations = {
    "beach":["Bali","Maldives","Hawaii"],
    "mountains":["Swiss Alps","Rocky Mountains","Himalayas"],
    "city":["New York","Paris","Tokyo"]
}
jokes = {
    "Why dont programmers like nature? It has too many bugs.": "😂",
    "Why do Java developers wear glasses? Because they dont see sharp.": "🤣",
    "How many programmers does it take to change a light bulb? None, thats a hardware problem.": "😆"
}

def normalize_input(user_input):
    return re.sub(r'[^\w\s]','',user_input.lower())

def reccomend():
    print(Fore.CYAN+"Travebot: Where would you like to go? Beach, Mountains, or City?")
    preference=input(Fore.GREEN+"You:")
    preference=normalize_input(preference)

    if preference in destinations:
        suggestion=random.choice(destinations[preference])
        print(Fore.CYAN+f"Travebot: I recommend visiting {suggestion}!")
        print(Fore.LIGHTBLUE_EX+"Do you like it (yes/no)?")
        answer=input(Fore.GREEN+"You:").lower()

        if answer=="yes":
            print(Fore.CYAN+"Travebot: Great choice! I hope you have an amazing trip!")
        elif answer=="no":
            print(Fore.CYAN+"Travebot: No worries! Let me suggest another destination.")
            reccomend()
        else:
            print(Fore.RED+"Travebot: I didnt understand that. Please answer with yes or no.")
            reccomend()
    else:
        print(Fore.RED+"Travebot: Sorry, I dont have suggestions for that preference. Please choose Beach, Mountains, or City.")

    show_help()

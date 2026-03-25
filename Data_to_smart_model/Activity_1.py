import colorama
from colorama import Fore,Style
from textblob import textblob

colorama.init()
print(f"{Fore.CYAN} Welcome to sentiment spy! {Style.RESET_ALL}")
user_name = input(f"{Fore.MAGENNTA}Please enter your name:"{Style.RESET_ALL})
if not user_name:
    user_name="Mystery Agent"

conversation_history = []
print(f"\n{Fore.CYAN}Hello,Agent{user_name}!")
print(f"Type of sentence and i will analyze your sentence with textblob and show you the sentiment")
print(f"Type{Fore.Yellow}'reset{Fore.cyan}, {Fore.YELLOW}ry'{Fore.CYAN}")
    f"or {Fore.YELLOW} 'exit' {Fore..CYAN} to quit. {Style.RESET_ALL}\n")

While True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{fore.RED}Please enter some text or valid command.{Style.RESET_ALL}")
        continue
    polarity=TextBlob(user
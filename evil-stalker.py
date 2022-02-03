#libs
from colorama import *
import os
from googlesearch import *

logo = print(Fore.LIGHTBLUE_EX + """
   .    _  .     _____________     evil-stalker
   |\_|/__/|    /             \    ------------
  / / \/ \  \  /     evil      \   support:
 /__|O||O|__ \ \    stalker    /   linkedin
|/_ \_/\_/ _\ | \  ___________/    twitch.tv
| | (____) | ||  |/                instagram
\/\___/\__/  // _/                 facebook
(_/         ||                     twitter
 |          ||\                    steam
  \        //_/                    etc
   \______//                       ------------
  __|| __||                        maded by more#6123
 (____(____)   """.center(os.get_terminal_size().columns))
print("")
print("")
print(Fore.WHITE + """options: nickname / fullname / back""")
print("")

def Search():
    option = input("> ")
    os.system("clear")
    print("")
    if option == "back":
        os.system("clear")
        print(logo)
        print(credit)
        print("")
        print("")
        print(Fore.WHITE + """options: nickname / fullname / back""")
        print("")
        Search()
    if option == "fullname":
        person = input("Full Name: ")
        resultados = int(input("results per site: "))
        print("")
        query = '"'+person+'"' + " site:facebook.com"
        for uno in search(query, tld="co.in", num=resultados, stop=resultados, pause=2, safe='on'):
            print(Fore.BLUE + uno)
        print("")
        query = '"'+person+'"' + " site:instagram.com"
        for dos in search(query, tld="co.in", num=resultados, stop=resultados, pause=3, safe='on'):
            print(Fore.MAGENTA  + dos)
        print("")
        query = '"'+person+'"' + " site:twitter.com"
        for tres in search(query, tld="co.in", num=resultados, stop=resultados, pause=4, safe='on'):
            print(Fore.CYAN + tres)
        print("")
        query = '"'+person+'"' + " site:linkedin.com"
        for cuatro in search(query, tld="co.in", num=resultados, stop=resultados, pause=5, safe='on'):
            print(Fore.LIGHTBLUE_EX + cuatro)
        print("")
        query = '"'+person+'"' + " site:tiktok.com"
        for cinco in search(query, tld="co.in", num=resultados, stop=resultados, pause=6, safe='on'):
            print(Fore.CYAN + cinco)
        print("")
        query = '"'+person+'"' + " site:youtube.com"
        for siete in search(query, tld="co.in", num=resultados, stop=resultados, pause=6, safe='on'):
            print(Fore.RED + siete)
        print("")
        query = '"'+person+'"' + " site:reddit.com"
        for seis in search(query, tld="co.in", num=resultados, stop=resultados, pause=6, safe='on'):
            print(Fore.YELLOW+ seis)
        print("")
        query = '"'+person+'"' + " site:twitch.tv"
        for ocho in search(query, tld="co.in", num=resultados, stop=resultados, pause=4, safe='on'):
            print(Fore.MAGENTA + ocho)
        print("")
        query = '"'+person+'"' + " site:spotify.com"
        for nicknueve in search(query, tld="co.in", num=resultados, stop=resultados, pause=9, safe='on'):
            print(Fore.GREEN + nueve)
        print("")
        print(Style.RESET_ALL)
        Search()

    if option == "nickname":
        nickname = input("nickname: ")
        resultados2 = int(input("results per site: "))
        print("")
        query = '"'+nickname+'"' + " site:steamcommunity.com"
        for nickuno in search(query, tld="co.in", num=resultados2, stop=resultados2, pause=2, safe='on'):
            print(Fore.BLUE + nickuno)
        print("")
        query = '"'+nickname+'"' + " site:xboxgamertag.com"
        for nickdos in search(query, tld="co.in", num=resultados2, stop=resultados2, pause=3, safe='on'):
            print(Fore.GREEN + nickdos)
        print("")
        query = '"'+nickname+'"' + " site:twitch.tv"
        for nicktres in search(query, tld="co.in", num=resultados2, stop=resultados2, pause=4, safe='on'):
            print(Fore.MAGENTA + nicktres)
        print("")
        query = '"'+nickname+'"' + " site:instagram.com"
        for nickcuatro in search(query, tld="co.in", num=resultados2, stop=resultados2, pause=5, safe='on'):
            print(Fore.MAGENTA  + nickcuatro)
        print("")
        query = '"'+nickname+'"' + " site:booyah.live"
        for nickcinco in search(query, tld="co.in", num=resultados2, stop=resultados2, pause=6, safe='on'):
            print(Fore.YELLOW  + nickcinco)
        print("")
        query = '"'+nickname+'"' + " site:wattpad.com"
        for nickseis in search(query, tld="co.in", num=resultados2, stop=resultados2, pause=7, safe='on'):
            print(Fore.YELLOW + nickseis)
        print("")
        query = '"'+nickname+'"' + " site:soundcloud.com"
        for nickocho in search(query, tld="co.in", num=resultados2, stop=resultados2, pause=8, safe='on'):
            print(Fore.YELLOW + nickocho)
        print("")
        query = '"'+nickname+'"' + " site:spotify.com"
        for nicknueve in search(query, tld="co.in", num=resultados2, stop=resultados2, pause=9, safe='on'):
            print(Fore.GREEN + nicknueve)
        print("")
        query = '"'+nickname+'"' + " site:facebook.com"
        for nickdiez in search(query, tld="co.in", num=resultados2, stop=resultados2, pause=10, safe='on'):
            print(Fore.BLUE  + nickdiez)
        print("")
        query = '"'+nickname+'"' + " site:youtube.com"
        for nickdiez in search(query, tld="co.in", num=resultados2, stop=resultados2, pause=10, safe='on'):
            print(Fore.RED + nickdiez)
        print("")
        print(Style.RESET_ALL)
        Search()



Search()

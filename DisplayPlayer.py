import ProcessName
import requests, webbrowser, re
import bs4

completion_range = 3

def SearchPlayer(Name):
    res = requests.get("http://pesdb.net/pes2019/?name=" + Name + "&sort=overall_at_max_level")
    soup = bs4.BeautifulSoup(res.text, "lxml")
    url = soup.find_all("a", href=re.compile("\.\/\?id"))
    #print(url)
    return url

def Display(target, object):
    player_data=[]
    for i in object:
        player_data.append((i.string.upper(),i.get("href").split(".")[1]))
    #print(len(player_data))
    i = 0
    while i < len(player_data) and i < 3:
        #print(player_data)
        webbrowser.open("http://pesdb.net/pes2019" + player_data[i][1])
        i += 1
    #if target in player_data[0][:]:
    #    print("clear")
    #    print(player_data[:][0].index(target))


def main():
    english_name = ProcessName.main()
    cnt = 0
    #player_list=[]
    while cnt < completion_range:
        #print(english_name)
        player_list = SearchPlayer(english_name)
        if not player_list:
            cnt += 1
            english_name = english_name[:-1]
        else:
            break
    if cnt == completion_range:
        print("Can not find")
        return -1
    else:
        #print(player_list)
        Display(english_name, player_list)



# main関数呼び出し
if __name__ == "__main__":
    main()

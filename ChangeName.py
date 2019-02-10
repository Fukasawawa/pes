import requests, re
import bs4

def getName():
    while True:
        print("please input name")
        original_name = input()
        if(not original_name):
            print("empty name")
        else:
            break
    return original_name

def searchName(Name):
    res = requests.get("https://google.com/search?q=" + Name + "+wiki")
    soup = bs4.BeautifulSoup(res.text, "lxml")
    url = soup.select(".r a")
    return url

def pickupName(url):
    res = requests.get("https://google.com" + url.get("href"))
    soup = bs4.BeautifulSoup(res.text, "lxml")
    name_list = soup.find_all("td", text=re.compile("[A-z]{2}"))
    #name_list.extend(soup.find_all("p", text=re.compile("[A-z]{2}")))
    name_list.sort(key=len, reverse=True)
    #print(name_list)
    #print(soup.find_all("p").find_all("b"))
    return name_list[0].string.split("\n")[1]

def main():
    original_name = getName()
    wiki = searchName(original_name)
    #print("https://google.com" + wiki[0].get("href"))
    #print(pickupName(wiki[0]))
    return pickupName(wiki[0])

# main関数呼び出し
if __name__ == "__main__":
    main()

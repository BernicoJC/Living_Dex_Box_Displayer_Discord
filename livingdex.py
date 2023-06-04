from bs4 import BeautifulSoup
from requests_html import HTMLSession
import bot

def pokedex(link, boxnumber):
    session = HTMLSession()
    response = session.get(link)
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')

    links = []
    long = ""
    for link in soup.findAll('tr'):
        for i in link.findAll("a", attrs={'href': lambda x: x.startswith("/pokemon") or x.startswith("/pokedex")}):
            if i.text:
                links.append(i.text)
            if len(i.text) > len(long):
                long = i.text

    fulldex = []
    line = []
    box = []
    for mons in links:
        if len(line) + 1 != 7:
            line.append(mons)
        else:
            box.append(line)
            line = [mons]
        
        if len(box) == 5:
            fulldex.append(box)
            box = []
        
    box.append(line)
    fulldex.append(box)

    full = ""
    format = "```\n"
    for line in fulldex[boxnumber]: # sample, prints the first box
        for mons in line:
            full = full + mons + ","
            format = format + "{:<15}"
        format = format + "\n"
    format = format + "\n```"
    return f"```Box {boxnumber + 1} / {len(fulldex)}```" + format.format(*full.split(",")) 

def box_length(link):
    session = HTMLSession()
    response = session.get(link)
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')

    links = []
    long = ""
    for link in soup.findAll('tr'):
        for i in link.findAll("a"):
            if i.text:
                links.append(i.text)
            if len(i.text) > len(long):
                long = i.text

    fulldex = []
    line = []
    box = []
    for mons in links:
        if len(line) + 1 != 7:
            line.append(mons)
        else:
            box.append(line)
            line = [mons]
        
        if len(box) == 5:
            fulldex.append(box)
            box = []
        
    box.append(line)
    fulldex.append(box)

    return len(fulldex) - 1

# test = "https://www.serebii.net/scarletviolet/paldeapokedex.shtml"
# print(pokedex(test, 0))
# print(box_length(test))

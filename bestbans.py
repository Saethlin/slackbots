import re
import operator
import requests


REGION = "NA"
GOLD_URL = "http://bestbans.com/bestBans/gold"
PLAT_URL = "http://bestbans.com/bestBans/platinum"

cookie = dict(bestBansRegion=REGION)
table_regex = re.compile('<table.*?>(.+?)</table>', re.DOTALL)
td_regex = re.compile('<td>(.+?)</td>', re.DOTALL)
text_regex = re.compile('(?<=>)[^<>]*\S[^<>]*(?=<)')


def find_best_bans():
    influence_dict = dict()

    the_page = requests.get(GOLD_URL, cookies=cookie).text

    table = table_regex.findall(the_page)[0]
    entries = td_regex.findall(table)

    names = entries[::6]
    names = [text_regex.findall(n)[0].strip() for n in names]

    influence = entries[1::6]
    influence = [float(i) for i in influence]

    for (x,y) in zip(names, influence):
        influence_dict[x] = y

    the_page = requests.get(PLAT_URL, cookies=cookie).text

    table = table_regex.findall(the_page)[0]
    entries = td_regex.findall(table)

    names = entries[::6]
    names = [text_regex.findall(n)[0].strip() for n in names]

    influence = entries[1::6]
    influence = [float(i) for i in influence]

    for (x,y) in zip(names, influence):
        influence_dict[x] = (influence_dict[x] + y)/2

    sorted_dict = sorted(influence_dict.items(), key=operator.itemgetter(1))

    suggestions = sorted_dict[::-1][:10]

    max_name_length = len("Champion")
    for (champ, influence) in suggestions:
        max_name_length = max(len(champ), max_name_length)

    output = "```\nChampion"
    output += " "*(max_name_length - len(output))
    output += "    Influence\n"

    for (champ, influence) in suggestions:
        name = champ
        name += " "*(max_name_length - len(name))
        output += name + "    " + str(round(influence,0)) + "\n"
    output += "```"

    return output

if __name__ == "__main__":
    print(find_best_bans())

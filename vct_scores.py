import re
import time
import requests
from bs4 import BeautifulSoup


def vlr_upcoming():
    URL = "https://www.vlr.gg/matches"
    html = requests.get(URL)
    soup = BeautifulSoup(html.content, "lxml")
    status = html.status_code

    base = soup.find(id="wrapper")

    vlr_module = base.find_all(
        "a",
        {"class": "wf-module-item"},
    )

    result = []
    for module in vlr_module:
        # link to match info
        url_path = module["href"]

        # Match completed time
        eta_container = module.find("div", {"class": "match-item-eta"})
        eta = "TBD"
        eta_time = eta_container.find("div", {"class": "ml-eta"})
        if eta_time is not None:
            eta = (
                      eta_time
                          .get_text()
                          .strip()
                  ) + " from now"

        if eta == "TBD":
            result.append(
                {
                    "time_until_match": eta,
                    "match_page": url_path,
                }
        )
    segments = {"status": status, "segments": result}
    data = {"data": segments}

    return data

# Finds team names
def find_teams(url):
    html = requests.get(f"https://www.vlr.gg{url}")
    soup = BeautifulSoup(html.content, "lxml")
    status = html.status_code
    base = soup.find(id="wrapper")

    vlr_module = base.find(
        "div",
        {"class": "vlr-rounds-row-col"},
    )

    teams = [re.sub("[^A-z0-9]", "", team.text) for team in vlr_module if re.sub("[^A-z0-9]", "", team.text) != '']
    return teams

# Finds game scores
def find_game_score(url):
    html = requests.get(f"https://www.vlr.gg{url}")
    soup = BeautifulSoup(html.content, "lxml")
    status = html.status_code
    base = soup.find(id="wrapper")

    vlr_module = base.find_all(
        "div",
        {"class": "score"},
    )

    game_score = vlr_module[-2:]
    return game_score

# Finds series score
def find_series_score(url):
    html = requests.get(f"https://www.vlr.gg{url}")
    soup = BeautifulSoup(html.content, "lxml")
    status = html.status_code
    base = soup.find(id="wrapper")

    vlr_module = base.find(
        "div",
        {"class": "match-header-vs-score"},
    )

    series_score = re.sub("[^0-9:]", "", vlr_module.text.replace("Bo3", ""))
    return series_score

# Formats the data
def format(url):
    final = ""
    teams = find_teams(url)
    game_score = find_game_score(url)
    series_score = find_series_score(url)

    if "0" not in game_score[0].text and "0" not in game_score[2].text:
        final = (f"\n{teams[0]} - {game_score[0].text.strip()} ({series_score[0]})\n"
                  f"{teams[1]} - {game_score[0].text.strip()} ({series_score[2]})\n")
        return final
    else:
        return ""

if __name__ == '__main__':
    while True:
        data = vlr_upcoming()
        scores = ""

        for x in data['data']['segments']:
            scores += format(x['match_page'])

        f = open("scores.txt", "w")
        f.write(scores)
        f.close()

        time.sleep(60)

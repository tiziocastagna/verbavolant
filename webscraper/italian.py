import requests
from bs4 import BeautifulSoup


def find_italian_verb(name):
    url = "https://www.italian-verbs.com/verbi-italiani/coniugazione.php?verbo=" + name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    if len(soup.find_all('strong')) != 0:
        return None

    divs = soup.find_all('div', class_="section group")

    Verb = {"INDICATIVO": {}, "CONGIUNTIVO": {}}
    Verb["INDICATIVO"] = {}

    columns = divs[0].find_all('div', class_='col span_1_of_2')

    simple_tenses = columns[0]
    complex_tenses = columns[1]

    trs = simple_tenses.find_all('tr')

    tense = []
    tense_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#009900':
            if len(tense) > 0:
                Verb["INDICATIVO"].update({tense_name: tense})
                tense = []
            tense_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds:
                verbo += td.text.strip()
            tense.append(verbo)
    Verb["INDICATIVO"].update({tense_name: tense})


    trs = complex_tenses.find_all('tr')

    tense = []
    tense_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#009900':
            if len(tense) > 0:
                Verb["INDICATIVO"].update({tense_name: tense})
                tense = []
            tense_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds:
                verbo += td.text.strip()
            tense.append(verbo)
    Verb["INDICATIVO"].update({tense_name: tense})

    columns = divs[1].find_all('div', class_='col span_1_of_2')

    simple_tenses = columns[0]
    complex_tenses = columns[1]

    trs = simple_tenses.find_all('tr')

    tense = []
    tense_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#009900':
            if len(tense) > 0:
                Verb["CONGIUNTIVO"].update({tense_name: tense})
                tense = []
            tense_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds:
                verbo += td.text.strip()
            tense.append(verbo)
    Verb["CONGIUNTIVO"].update({tense_name: tense})


    trs = complex_tenses.find_all('tr')

    tense = []
    tense_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#009900':
            if len(tense) > 0:
                Verb["CONGIUNTIVO"].update({tense_name: tense})
                tense = []
            tense_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds:
                verbo += td.text.strip()
            tense.append(verbo)
    Verb["CONGIUNTIVO"].update({tense_name: tense})
    return Verb
import requests, json
from bs4 import BeautifulSoup

def get_divs_with_class(url, class_name):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        divs = soup.find_all('div', class_=class_name)
        return divs
    else:
        print(f"Failed to fetch the URL. Status code: {response.status_code}")
        return None


def find_verb(name):
    url = "https://www.dizionario-latino.com/dizionario-latino-flessione.php?lemma=" + name +"100"
    class_name = "section group"
    divs = get_divs_with_class(url, class_name)


    Verb = {"indicativo": {}, "congiuntivo": {}}
    Verb["indicativo"] = {}

    columns = divs[0].find_all('div', class_='col span_1_of_2')

    simple_tences = columns[0]
    complex_tences = columns[1]

    trs = simple_tences.find_all('tr')

    tence = []
    tence_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#008000':
            if len(tence) > 0:
                Verb["indicativo"].update({tence_name: tence})
                tence = []
            tence_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds[1:]:
                verbo += td.text.strip()
            tence.append({"grammatica": tds[0].text.strip(), "verbo": verbo})
    Verb["indicativo"].update({tence_name: tence})


    trs = complex_tences.find_all('tr')

    tence = []
    tence_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#008000':
            if len(tence) > 0:
                Verb["indicativo"].update({tence_name: tence})
                tence = []
            tence_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds[1:]:
                verbo += td.text.strip()
            tence.append({"grammatica": tds[0].text.strip(), "verbo": verbo})
    Verb["indicativo"].update({tence_name: tence})

    columns = divs[1].find_all('div', class_='col span_1_of_2')

    simple_tences = columns[0]
    complex_tences = columns[1]

    trs = simple_tences.find_all('tr')

    tence = []
    tence_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#008000':
            if len(tence) > 0:
                Verb["congiuntivo"].update({tence_name: tence})
                tence = []
            tence_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds[1:]:
                verbo += td.text.strip()
            tence.append({"grammatica": tds[0].text.strip(), "verbo": verbo})
    Verb["congiuntivo"].update({tence_name: tence})


    trs = complex_tences.find_all('tr')

    tence = []
    tence_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#008000':
            if len(tence) > 0:
                Verb["congiuntivo"].update({tence_name: tence})
                tence = []
            tence_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds[1:]:
                verbo += td.text.strip()
            tence.append({"grammatica": tds[0].text.strip(), "verbo": verbo})
    Verb["congiuntivo"].update({tence_name: tence})
    return Verb

def save_verb(verb_name):
    verb = find_verb(verb_name)
    with open('./db/' + verb_name + '.json', 'w', encoding='utf-8') as json_file:
        json.dump(verb, json_file, ensure_ascii=False, indent=4)

verbs_to_save = ["EO", "CAPIO", "AMO", "FERO", "FIO"]

for verb_name in verbs_to_save:
    save_verb(verb_name)
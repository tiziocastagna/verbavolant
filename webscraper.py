import requests, json
from bs4 import BeautifulSoup

def find_italian_verb(name):
    url = "https://www.italian-verbs.com/verbi-italiani/coniugazione.php?verbo=" + name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    divs = soup.find_all('div', class_="section group")

    Verb = {"INDICATIVO": {}, "CONGIUNTIVO": {}}
    Verb["INDICATIVO"] = {}

    columns = divs[0].find_all('div', class_='col span_1_of_2')

    simple_tences = columns[0]
    complex_tences = columns[1]

    trs = simple_tences.find_all('tr')

    tence = []
    tence_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#009900':
            if len(tence) > 0:
                Verb["INDICATIVO"].update({tence_name: tence})
                tence = []
            tence_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds:
                verbo += td.text.strip()
            tence.append(verbo)
    Verb["INDICATIVO"].update({tence_name: tence})


    trs = complex_tences.find_all('tr')

    tence = []
    tence_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#009900':
            if len(tence) > 0:
                Verb["INDICATIVO"].update({tence_name: tence})
                tence = []
            tence_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds:
                verbo += td.text.strip()
            tence.append(verbo)
    Verb["INDICATIVO"].update({tence_name: tence})

    columns = divs[1].find_all('div', class_='col span_1_of_2')

    simple_tences = columns[0]
    complex_tences = columns[1]

    trs = simple_tences.find_all('tr')

    tence = []
    tence_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#009900':
            if len(tence) > 0:
                Verb["CONGIUNTIVO"].update({tence_name: tence})
                tence = []
            tence_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds:
                verbo += td.text.strip()
            tence.append(verbo)
    Verb["CONGIUNTIVO"].update({tence_name: tence})


    trs = complex_tences.find_all('tr')

    tence = []
    tence_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#009900':
            if len(tence) > 0:
                Verb["CONGIUNTIVO"].update({tence_name: tence})
                tence = []
            tence_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds:
                verbo += td.text.strip()
            tence.append(verbo)
    Verb["CONGIUNTIVO"].update({tence_name: tence})
    return Verb

person_map = {
    "I sing.": 0,
    "II sing.": 1,
    "III sing.": 2,
    "I plur.": 3,
    "II plur.": 4,
    "III plur.": 5
}

def get_base_latin_verb_translations(verb_name):
    url = "https://www.dizionario-latino.com/dizionario-latino-italiano.php?lemma=" + verb_name +"100"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    translations_spans = soup.find_all('span', class_="italiano")
    translations = []
    for translation_sapan in translations_spans:
        for translation in translation_sapan.text.strip().split(", "):
            translations.append(translation)
    return translations

latin_to_italian_tences_map = {
    "INDICATIVO": {
        "PRESENTE": "PRESENTE",
        "IMPERFETTO": "IMPERFETTO",
        "FUTURO SEMPLICE": "FUTURO SEMPLICE",
        "PERFETTO": ["PASSATO REMOTO", "PASSATO PROSSIMO", "TRAPASSATO REMOTO"],
        "PIUCHEPERFETTO": "TRAPASSATO PROSSIMO",
        "FUTURO ANTERIORE": "FUTURO ANTERIORE"
    },
    "CONGIUNTIVO": {
        "PRESENTE": "PRESENTE",
        "IMPERFETTO": "IMPERFETTO",
        "PERFETTO": "PASSATO",
        "PIUCHEPERFETTO": "TRAPASSATO"
    }
}

def get_uninterrupted_strings(strings):
    valid_strings = []
    for translation in strings:
        if [translation] == translation.split(" "):
            valid_strings.append(translation)
    return valid_strings

def get_verb_translations(italian_verbs, mood, latin_tence, person):
    translations = []
    for italian_verb in italian_verbs:
        tences = latin_to_italian_tences_map[mood][latin_tence]
        if str(tences) == tences:
            translation = italian_verb[mood][tences][person_map[person]]
            if translation != "-":
                translations.append(translation)
            if translation[:7] == "lui/lei":
                translations.append("lui" + translation[7:])
                translations.append("lei" + translation[7:])
        else:
            for tence in tences:
                translation = translations.append(italian_verb[mood][tence][person_map[person]])
                if translation != "-":
                    translations.append(translation)
                if translation[:7] == "lui/lei":
                    translations.append("lui" + translation[7:])
                    translations.append("lei" + translation[7:])
    return translations

def find_latin_verb(verb_name):
    url = "https://www.dizionario-latino.com/dizionario-latino-flessione.php?lemma=" + verb_name +"100"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    divs = soup.find_all('div', class_="section group")


    translations = get_base_latin_verb_translations(verb_name)

    valid_translations = get_uninterrupted_strings(translations)

    Verb = {"translation": translations, "valid_translations": valid_translations, "INDICATIVO": {}, "CONGIUNTIVO": {}}
    
    italian_verbs = []
    for valid_translation in valid_translations:
        italian_verbs.append(find_italian_verb(valid_translation))

    columns = divs[0].find_all('div', class_='col span_1_of_2')

    simple_tences = columns[0]
    complex_tences = columns[1]

    trs = simple_tences.find_all('tr')

    tence = []
    tence_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#008000':
            if len(tence) > 0:
                Verb["INDICATIVO"].update({tence_name: tence})
                tence = []
            tence_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds[1:]:
                verbo += td.text.strip()
            grammatica = tds[0].text.strip()
            tence.append({"grammatica": grammatica, "verbo": verbo, "traduzioni": get_verb_translations(italian_verbs, "INDICATIVO", tence_name, grammatica)})
    Verb["INDICATIVO"].update({tence_name: tence})


    trs = complex_tences.find_all('tr')

    tence = []
    tence_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#008000':
            if len(tence) > 0:
                Verb["INDICATIVO"].update({tence_name: tence})
                tence = []
            tence_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds[1:]:
                verbo += td.text.strip()
            grammatica = tds[0].text.strip()
            tence.append({"grammatica": grammatica, "verbo": verbo, "traduzioni": get_verb_translations(italian_verbs, "INDICATIVO", tence_name, grammatica)})
    Verb["INDICATIVO"].update({tence_name: tence})

    columns = divs[1].find_all('div', class_='col span_1_of_2')

    simple_tences = columns[0]
    complex_tences = columns[1]

    trs = simple_tences.find_all('tr')

    tence = []
    tence_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#008000':
            if len(tence) > 0:
                Verb["CONGIUNTIVO"].update({tence_name: tence})
                tence = []
            tence_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds[1:]:
                verbo += td.text.strip()
            grammatica = tds[0].text.strip()
            tence.append({"grammatica": grammatica, "verbo": verbo, "traduzioni": get_verb_translations(italian_verbs, "CONGIUNTIVO", tence_name, grammatica)})
    Verb["CONGIUNTIVO"].update({tence_name: tence})


    trs = complex_tences.find_all('tr')

    tence = []
    tence_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#008000':
            if len(tence) > 0:
                Verb["CONGIUNTIVO"].update({tence_name: tence})
                tence = []
            tence_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds[1:]:
                verbo += td.text.strip()
            grammatica = tds[0].text.strip()
            tence.append({"grammatica": grammatica, "verbo": verbo, "traduzioni": get_verb_translations(italian_verbs, "CONGIUNTIVO", tence_name, grammatica)})
    Verb["CONGIUNTIVO"].update({tence_name: tence})
    return Verb

def save_verb(verb_name):
    verb = find_latin_verb(verb_name)
    with open('./db/' + verb_name + '.json', 'w', encoding='utf-8') as json_file:
        json.dump(verb, json_file, ensure_ascii=False, indent=4)

verbs_to_save = ["VIDEO"]

for verb_name in verbs_to_save:
    save_verb(verb_name)
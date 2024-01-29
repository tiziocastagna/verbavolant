import requests, json
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
            desinenza = translation[-3:]
            if desinenza == "are" or desinenza == "ere" or desinenza == "ire":
                translations.append(translation)
    return translations

latin_to_italian_tenses_map = {
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

def join_strings(strings):
    result = ""
    for string in strings:
        result += string
    return result

def separate_parts(verb):
    if ", " in verb:
        words = []
        options = []
        last_index = 0
        for i in range(1, len(verb)):
            if verb[i] == ",":
                options.append(verb[last_index:i])
                last_index = i + 1
            elif verb[i] == " " and verb[i - 1] != ",":
                words.append(verb[last_index:i])
                last_index = i
        options.append(verb[last_index:])

        base_verb = join_strings(words)

        results = []
        for option in options:
            results.append(base_verb + option)
        return results
    else:
        return [verb]

def add_spelling_options(verb):
    results = []
    verb_parts = separate_parts(verb)
    for verb_part in verb_parts:
        if verb_part[:7] == "lui/lei":
            if verb_part[-3:] == "o/a":
                results.append("lui" + verb_part[7:-3] + "o")
                results.append("lei" + verb_part[7:-3] + "a")
                results.append("egli" + verb_part[7:-3] + "o")
            else:
                results.append("lui" + verb_part[7:])
                results.append("lei" + verb_part[7:])
                results.append("egli" + verb_part[7:])
        elif verb_part[:11] == "che lui/lei":
            if verb_part[-3:] == "o/a":
                results.append("che lui" + verb_part[11:-3] + "o")
                results.append("che lei" + verb_part[11:-3] + "a")
                results.append("che egli" + verb_part[11:-3] + "o")
            else:
                results.append("che lui" + verb_part[11:])
                results.append("che lei" + verb_part[11:])
                results.append("che egli" + verb_part[11:])
        elif verb_part[:4] == "loro":
            if verb_part[-3:] == "i/e":
                results.append(verb_part[:-3] + "i")
                results.append(verb_part[:-3] + "e")
                results.append("essi" + verb_part[4:-3] + "i")
            else:
                results.append(verb_part)
                results.append("essi" + verb_part[4:])
        elif verb_part[:8] == "che loro":
            if verb_part[-3:] == "i/e":
                results.append(verb_part[:-3] + "i")
                results.append(verb_part[:-3] + "e")
                results.append("che essi" + verb_part[8:-3] + "i")
            else:
                results.append(verb_part)
                results.append("che essi" + verb_part[8:])
        elif verb_part[-3:] == "o/a":
            results.append(verb_part[:-3] + "o")
            results.append(verb_part[:-3] + "a")
        elif verb_part[-3:] == "i/e":
            results.append(verb_part[:-3] + "i")
            results.append(verb_part[:-3] + "e")
        else:
            results.append(verb_part)
    return results

def get_verb_translations(italian_verbs, mood, latin_tense, person):
    translations = []
    for italian_verb in italian_verbs:
        tenses = latin_to_italian_tenses_map[mood][latin_tense]
        if str(tenses) == tenses:
            translation = italian_verb[mood][tenses][person_map[person]]
            if (translation != "—" and translation != None):
                translations += add_spelling_options(translation)
        else:
            for tense in tenses:
                translation = italian_verb[mood][tense][person_map[person]]
                if (translation != "—" and translation != None):
                    translations += add_spelling_options(translation)
    return translations

def find_latin_verb(verb_name):
    url = "https://www.dizionario-latino.com/dizionario-latino-flessione.php?lemma=" + verb_name +"100"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    if len(soup.find_all('b')) == 20:
        return None

    divs = soup.find_all('div', class_="section group")


    translations = get_base_latin_verb_translations(verb_name)

    valid_translations = get_uninterrupted_strings(translations)

    Verb = {"translation": translations, "valid_translations": valid_translations, "INDICATIVO": {}, "CONGIUNTIVO": {}}
    
    italian_verbs = []
    for valid_translation in valid_translations:
        italian_verb = find_italian_verb(valid_translation)
        if italian_verb != None:
            italian_verbs.append(italian_verb)

    columns = divs[0].find_all('div', class_='col span_1_of_2')

    simple_tenses = columns[0]
    complex_tenses = columns[1]

    trs = simple_tenses.find_all('tr')

    tense = []
    tense_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#008000':
            if len(tense) > 0:
                Verb["INDICATIVO"].update({tense_name: tense})
                tense = []
            tense_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds[1:]:
                verbo += td.text.strip()
            persona = tds[0].text.strip()
            tense.append({"persona": persona, "verbo": verbo, "traduzioni": get_verb_translations(italian_verbs, "INDICATIVO", tense_name, persona)})
    Verb["INDICATIVO"].update({tense_name: tense})


    trs = complex_tenses.find_all('tr')

    tense = []
    tense_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#008000':
            if len(tense) > 0:
                Verb["INDICATIVO"].update({tense_name: tense})
                tense = []
            tense_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds[1:]:
                verbo += td.text.strip()
            persona = tds[0].text.strip()
            tense.append({"persona": persona, "verbo": verbo, "traduzioni": get_verb_translations(italian_verbs, "INDICATIVO", tense_name, persona)})
    Verb["INDICATIVO"].update({tense_name: tense})

    columns = divs[1].find_all('div', class_='col span_1_of_2')

    simple_tenses = columns[0]
    complex_tenses = columns[1]

    trs = simple_tenses.find_all('tr')

    tense = []
    tense_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#008000':
            if len(tense) > 0:
                Verb["CONGIUNTIVO"].update({tense_name: tense})
                tense = []
            tense_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds[1:]:
                verbo += td.text.strip()
            persona = tds[0].text.strip()
            tense.append({"persona": persona, "verbo": verbo, "traduzioni": get_verb_translations(italian_verbs, "CONGIUNTIVO", tense_name, persona)})
    Verb["CONGIUNTIVO"].update({tense_name: tense})


    trs = complex_tenses.find_all('tr')

    tense = []
    tense_name = ""
    for tr in trs:
        if tr.get('bgcolor') == '#008000':
            if len(tense) > 0:
                Verb["CONGIUNTIVO"].update({tense_name: tense})
                tense = []
            tense_name = tr.text.strip()
        else:
            tds = tr.find_all('td')
            verbo = ""
            for td in tds[1:]:
                verbo += td.text.strip()
            persona = tds[0].text.strip()
            tense.append({"persona": persona, "verbo": verbo, "traduzioni": get_verb_translations(italian_verbs, "CONGIUNTIVO", tense_name, persona)})
    Verb["CONGIUNTIVO"].update({tense_name: tense})
    return Verb

def save_verb(verb_name):
    verb = find_latin_verb(verb_name)
    if verb == None:
        print(verb_name + " not found")
        return
    with open('./db/' + verb_name.upper() + '.json', 'w', encoding='utf-8') as json_file:
        json.dump(verb, json_file, ensure_ascii=False, indent=4)

with open('./db/verbs.json', 'r') as file:
    verbs_to_save = json.load(file)
    for i in range(len(verbs_to_save)):
        verb_name = verbs_to_save[i]
        save_verb(verb_name)
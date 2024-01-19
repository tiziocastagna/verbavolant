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
            desinenza = translation[-3:]
            if desinenza == "are" or desinenza == "ere" or desinenza == "ire":
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
                if verb_part[-1] == "a":
                    results.append("egli" + verb_part[7:-1] + "o")
                else:
                    results.append("egli" + verb_part[7:])
        elif verb_part[:11] == "che lui/lei":
            if verb_part[-3:] == "o/a":
                results.append("che lui" + verb_part[11:-3] + "o")
                results.append("che lei" + verb_part[11:-3] + "a")
                results.append("che egli" + verb_part[11:-3] + "o")
            else:
                results.append("che lui" + verb_part[11:])
                results.append("che lei" + verb_part[11:])
                if verb_part[-1] == "a":
                    results.append("che egli" + verb_part[11:-1] + "o")
                else:
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

def get_verb_translations(italian_verbs, mood, latin_tence, person):
    translations = []
    for italian_verb in italian_verbs:
        tences = latin_to_italian_tences_map[mood][latin_tence]
        if str(tences) == tences:
            translation = italian_verb[mood][tences][person_map[person]]
            if (translation != "—" and translation != None):
                translations += add_spelling_options(translation)
        else:
            for tence in tences:
                translation = italian_verb[mood][tence][person_map[person]]
                if (translation != "—" and translation != None):
                    translations += add_spelling_options(translation)
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
        italian_verb = find_italian_verb(valid_translation)
        if italian_verb != None:
            italian_verbs.append(italian_verb)

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
            persona = tds[0].text.strip()
            tence.append({"persona": persona, "verbo": verbo, "traduzioni": get_verb_translations(italian_verbs, "INDICATIVO", tence_name, persona)})
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
            persona = tds[0].text.strip()
            tence.append({"persona": persona, "verbo": verbo, "traduzioni": get_verb_translations(italian_verbs, "INDICATIVO", tence_name, persona)})
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
            persona = tds[0].text.strip()
            tence.append({"persona": persona, "verbo": verbo, "traduzioni": get_verb_translations(italian_verbs, "CONGIUNTIVO", tence_name, persona)})
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
            persona = tds[0].text.strip()
            tence.append({"persona": persona, "verbo": verbo, "traduzioni": get_verb_translations(italian_verbs, "CONGIUNTIVO", tence_name, persona)})
    Verb["CONGIUNTIVO"].update({tence_name: tence})
    return Verb

def save_verb(verb_name):
    verb = find_latin_verb(verb_name)
    with open('./db/' + verb_name + '.json', 'w', encoding='utf-8') as json_file:
        json.dump(verb, json_file, ensure_ascii=False, indent=4)

verbs_to_save = ["AMO", "MITTO", "VIDEO", "AUDIO", "CAPIO", "SUM", "POSSUM", "ADSUM", "EO", "VOLO", "MALO", "NOLO", "FERO", "FIO"]

for verb_name in verbs_to_save:
    save_verb(verb_name)
    print(verb_name + " finished")
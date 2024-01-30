import requests, json
from bs4 import BeautifulSoup

def get_page_results(urls):
    verbs_found = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        letters = soup.find_all('div', class_="mw-category-group")
        for letter in letters:
            for li in letter.find_all('li'):
                verbs_found.append(li.text.strip())
    return verbs_found
    

def upadte_verb_list():
    coniugazioni_found = []
    coniugazioni = [
        [
            "https://it.wiktionary.org/wiki/Categoria:Verbi_di_prima_coniugazione_in_latino",
            "https://it.wiktionary.org/w/index.php?title=Categoria:Verbi_di_prima_coniugazione_in_latino&pagefrom=evito#mw-pages",
        ],
        ["https://it.wiktionary.org/wiki/Categoria:Verbi_di_seconda_coniugazione_in_latino"],
        ["https://it.wiktionary.org/wiki/Categoria:Verbi_di_terza_coniugazione_in_latino"],
        ["https://it.wiktionary.org/wiki/Categoria:Verbi_di_quarta_coniugazione_in_latino"]
    ]
    for con in coniugazioni:
        coniugazioni_found.append(get_page_results(con))
    with open('../db/verbs.json', 'w', encoding='utf-8') as json_file:
        json.dump(coniugazioni_found, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    upadte_verb_list()
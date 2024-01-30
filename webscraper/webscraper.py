import json
from latin import find_latin_verb

def save_verb(verb_name, coniugazione):
    verb = find_latin_verb(verb_name, coniugazione)
    if verb == None:
        print(verb_name + " not found")
        return
    with open('../db/' + verb_name.upper() + '.json', 'w', encoding='utf-8') as json_file:
        json.dump(verb, json_file, ensure_ascii=False, indent=4)

def save_listed_verbs():
    with open('../db/verbs.json', 'r') as file:
        content = json.load(file)
        operation_size = 0
        for i in range(len(content)):
            operation_size += len(content[i])
        operation_state = 0
        for i in range(len(content)):
            coniugazione = str(i + 1)
            for j in range(len(content[i])):
                verb_name = content[i][j]
                save_verb(verb_name, coniugazione)
                operation_state += 1;
                print(verb_name + " finished " + "[" + str(operation_state) + "/" + str(operation_size) + "]")

def main():
    save_listed_verbs()

if __name__ == "__main__":
    main()
var database_info = [];
var Verbs = [];
var verb_identifiers = [];

async function get_database_info() {
    await fetch(`/api/getFile/verbs`).then(response => response.json()).then(data => {
        database_info = data;
    });
}

function update_loaded_verbs_list() {
    const right_div = document.getElementById("right_div");
    const shown_list = document.getElementById("loaded_verbs_list")
    while (shown_list.firstChild) {
        shown_list.removeChild(shown_list.firstChild);
    }

    for(const verb_identifier of verb_identifiers) {
        const li = document.createElement("li");
        li.innerText = verb_identifier;
        shown_list.appendChild(li);
    }
}

async function random_load() {
    const random_coniugazione = database_info[Math.floor(Math.random() * database_info.length)];
    const verb_identifier = random_coniugazione[Math.floor(Math.random() * random_coniugazione.length)];
    verb_identifiers.push(verb_identifier.toUpperCase());
    Verbs.push(await get_verb_from_db(verb_identifier.toUpperCase()));
    document.getElementById("loaded_verbs_container").classList.remove("hide");
    update_loaded_verbs_list();
}

async function get_verb_from_db(verb_name) {
    const response = await fetch(`/api/getFile/${verb_name}`);
    return response.json();
}

function get_random_question_from_verb(verb, filter) {
    const filteredQuestions = [];
    for(const mood of Object.keys(verb)) {
        if(Object.keys(filter).includes(mood)) {
            for(const tense of Object.keys(verb[mood])) {
                if(filter[mood].includes(tense)) {
                    filteredQuestions.push(...verb[mood][tense]);
                }
            }
        }
    }
    const random_index =  Math.floor(Math.random() * filteredQuestions.length);
    const question = filteredQuestions[random_index]["verbo"];
    const answers = [];
    for(const filtered_question of filteredQuestions) {
        if(filtered_question["verbo"] == question) {
            answers.push(...filtered_question["traduzioni"]);
        }
    }
    return new Question(question, answers);
}
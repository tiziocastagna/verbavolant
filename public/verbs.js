async function get_verb_from_db(verb_name) {
    const fileTitle = verb_name;
    const response = await fetch(`/api/getFile/${fileTitle}`);
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
            console.log(filtered_question)
        }
    }
    console.log(answers)
    return new Question(question, answers);
}
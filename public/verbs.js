async function get_verb_from_db(verb_name) {
    const fileTitle = verb_name;

    try {
        const response = await fetch(`/api/getFile/${fileTitle}`);

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        return response.json();
    } catch (error) {
        console.error('Fetch error:', error);
        throw error;
    }
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
    const answers = filteredQuestions[random_index]["traduzioni"];
    return new Question(question, answers);
}
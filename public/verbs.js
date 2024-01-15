class Verb {
    constructor(table, translated_table) {
        this.table = table;
        this.translated_table = translated_table;
    }
    get_random_question(moodList, tenseList) {
        const filteredQuestions = [];
        for(const mood in this.table) {
            if(moodList.includes(mood)) {
                for(const tense in this.table[mood]) {
                    if(tenseList.includes(tense)) {
                        filteredQuestions.push(...this.table[mood][tense]);
                    }
                }
            }
        }
        const random_index =  Math.floor(Math.random() * filteredQuestions.length);
        const question = filteredQuestions[random_index];
        const answer = this.translated_table[filteredQuestions[random_index]];
        return new Question(question, answer);
    }
}

const Eo = new Verb(
    {
        indicative: {
            present: [
                "eo",
                "is",
                "it",
                "imus",
                "itis",
                "eunt"
            ],
            imperfect: [
                "ibam",
                "ibas",
                "ibat",
                "ibamus",
                "ibatis",
                "ibant"
            ]
        }
    }, {
        "eo": "io vado",
        "is": "tu vai",
        "it": "egli va",
        "imus": "noi andiamo",
        "itis": "voi andate",
        "eunt": "essi vanno",

        "ibam": "io andavo",
        "ibas": "tu andavi",
        "ibat": "egli andava",
        "ibamus": "noi andavamo",
        "ibatis": "voi andavate",
        "ibant": "essi andavano"
    }
);
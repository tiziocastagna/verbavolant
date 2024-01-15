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

const Eo = new Verb({
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
            ],
            future: [
                "ibo",
                "ibis",
                "ibit",
                "ibimus",
                "ibitis",
                "ibunt"
            ],
            perfect: [
                "ii", "ivi",
                "iisti", "ivisti",
                "iit", "ivit",
                "iimus", "ivimus",
                "istis", "ivitis",
                "ierunt", "iverunt"
            ],
            pluperfect: [
                "ieram", "iveram",
                "ieras", "iveras",
                "ierat", "iverat",
                "ieramus", "iveramus",
                "ieratis", "iveratis",
                "ierant", "iverant"
            ],
            future_perfect: [
                "iero", "ivero",
                "ieris", "iveris",
                "ierit", "iverit",
                "ierimus", "iverimus",
                "ieritis", "iveritis",
                "ierint", "iverint"
            ]
        },
        subjunctive: {
            present: [
                "eam",
                "eas",
                "eat",
                "eamus",
                "eatis",
                "eant"
            ],
            imperfect: [
                "irem",
                "ires",
                "iret",
                "iremus",
                "iretis",
                "irent"
            ],
            perfect: [
                "ierim", "iverim",
                "ieris", "iveris",
                "ierit", "iverit",
                "ierimus", "iverimus",
                "ieritis", "iveritis",
                "ierint", "iverint"
            ],
            plusperfec: [
                "iissem", "ivissem",
                "iisses", "ivisses",
                "iisset", "ivisset",
                "iissemus", "ivissemus",
                "iisetis", "ivissetis",
                "iissent", "ivissent"
            ]
        },
        imperative: {
            present: [
                "i", "ei",
                "ite"
            ],
            future: [
                "ito",
                "ito",
                "iote",
                "eunto"
            ]
        },
        infinite: {
            present: [
                "ire", "irier"
            ],
            perfect: [
                "iisse", "ivisse"
            ],
            future: [
                "iturum -am, -um esse",
                "ituros -as -a esse"
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
        "ibant": "essi andavano",

        "ibo": "io andrò",
        "ibis": "tu andrai",
        "ibit": "egli andrà",
        "ibimus": "noi andremo",
        "ibitis": "voi andrete",
        "ibunt": "essi andranno",

        "ii": "io andai",
        "ivi": "io andai",
        "iisti": "tu andasti",
        "ivisti": "tu andasti",
        "iit": "egli andò",
        "ivit": "egli andò",
        "iimus": "noi andammo",
        "ivimus": "noi andammo",
        "istis": "voi andaste",
        "ivitis": "voi andaste",
        "ierunt": "essi andarono",
        "iverunt": "essi andarono",

        "ieram": "io ero andato",
        "iveram": "io ero andato",
        "ieras": "tu eri andato",
        "iveras": "tu eri andato",
        "ierat": "egli era andato",
        "iverat": "egli era andato",
        "ieramus": "noi eravamo andati",
        "iveramus": "noi eravamo andati",
        "ieratis": "voi eravate andati",
        "iveratis": "voi eravate andati",
        "ierant": "essi erano andati",
        "iverant": "essi erano andati",

        "iero": "io sarò andato",
        "ivero": "io sarò andato",
        "ieris": "tu sarai andato",
        "iveris": "tu sarai andato",
        "ierit": "egli sarà anato",
        "iverit": "egli sarà anato",
        "ierimus": "noi saremo andati",
        "iverimus":  "noi saremo andati",
        "ieritis": "voi sarete andati",
        "iveritis": "voi sarete andati",
        "ierint": "essi saranno andati",
        "iverint": "essi saranno andati",

        "eam": "che io vada",
        "eas": "che tu vada",
        "eat": "che egli vada",
        "eamus": "che noi andiamo",
        "eatis": "che voi andiate",
        "eant": "che essi vadano",

        "irem": "che io andassi",
        "ires": "che tu andassi",
        "iret": "che egli andasse",
        "iremus": "che noi andassimo",
        "iretis": "che voi andaste",
        "irent": "che essi andassero",

        "ierim": "che io sia andato",
        "iverim": "che io sia andato",
        "ieris": "che tu sia andato",
        "iveris": "che tu sia andato",
        "ierit": "che egli sia andato",
        "iverit": "che egli sia andato",
        "ierimus": "che noi siamo andati",
        "iverimus": "che noi siamo andati",
        "ieritis": "che voi siate andati",
        "iveritis": "che voi siate andati",
        "ierint": "che essi siano andati",
        "iverint": "che essi siano andati",

        "iissem": "che io fossi andato",
        "ivissem": "che io fossi andato",
        "iisses": "che tu fossi andato",
        "ivisses": "che tu fossi andato",
        "iisset": " che egli fosse andato",
        "ivisset": " che egli fosse andato",
        "iissemus": "che noi fossimo andati",
        "ivissemus": "che noi fossimo andati",
        "iisetis": " che voi foste andati",
        "ivissetis": " che voi foste andati",
        "iissent": "che essi fossero andati",
        "ivissent": "che essi fossero andati",
        
        "i": "vai tu",
        "ei": "vai tu",
        "ite": "andate voi",

        "ito": "andrai tu",
        "ito": "andrà egli",
        "iote": "andrete voi",
        "eunto": "andranno essi",

        "ire": "andare",
        "irier": "andare",

        "iisse": "essere andato",
        "ivisse": "essere andato",

        "iturum -am, -um esse": "essere sul punto di andare",
        "ituros -as -a esse": "essere sul punto di andare"
    }
);
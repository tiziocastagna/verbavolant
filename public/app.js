class Question {
    constructor(question, expected_answers) {
        this.question = question;
        this.expected_answers = expected_answers;
    }
    validate(answer) {
        if(this.expected_answers.includes(answer)) {
            return true;
        }
        return false;
    }
}

function get_random_question(Verbs, filter) {
    return get_random_question_from_verb(Verbs[Math.floor(Math.random() * Verbs.length)], filter);
}

function update_score(score, best_score, score_element, score_value, best_score_value, best=false, fail=false) {
    if(best) {
        localStorage.setItem("best_score", best_score);
        score_element.classList.add("best");
    }
    if(fail) {
        if(score_element.classList.contains("best")) {score_element.classList.remove("best");}
    }
    score_value.textContent = score;
    best_score_value.textContent = best_score;
}

window.onload = async function() {
    const AMO = await get_verb_from_db("AMO");
    const VIDEO = await get_verb_from_db("VIDEO");
    const SUM = await get_verb_from_db("SUM");
    const EO = await get_verb_from_db("EO");
    const ADSUM = await get_verb_from_db("ADSUM");
    const Verbs = [AMO ,VIDEO, SUM, EO, ADSUM];

    const questionFilter = {"INDICATIVO": ["PRESENTE", "IMPERFETO", "FUTURO_SEMPLICE", "PERFETTO", "PIUCCHEPERFETTO", "FUTURO_ANTERIORE"], "CONGIUNTIVO": ["PRESENTE", "IMPERFETO", "PERFETTO", "PIUCCHEPERFETTO"]};

    let best_score = parseInt(localStorage.getItem("best_score")) || 0;

    const input = document.getElementById("input");
    const question_element = document.getElementById("question");
    const score_element = document.getElementById("score");
    const score_value = document.getElementById("score_value");
    const best_score_value = document.getElementById("best_score_value");

    let score = 0;
    update_score(score, best_score, score_element, score_value, best_score_value);
    let question = get_random_question(Verbs, questionFilter);
    question_element.innerText = question.question;
    input.onkeydown = event => {
        if (event.key === 'Enter') {
            if(question.validate(input.value.trim())) {
                question_element.style.color = "lightgreen";
                score++;
                if(score > best_score) {
                    best_score = score;
                    update_score(score, best_score, score_element, score_value, best_score_value, true);
                } else {
                    update_score(score, best_score, score_element, score_value, best_score_value);
                }
            } else {
                question_element.style.color = "red";
                score = 0;
                update_score(score, best_score, score_element, score_value, best_score_value, false, true);
            }
            input.disabled = true;
            setTimeout(() => {
                input.disabled = false;
                question_element.style.color = "white";
                
                question = get_random_question(Verbs, questionFilter);
                question_element.innerText = question.question;
                input.value = "";
                input.focus();
            }, 1000);
        }
    }
}
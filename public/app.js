class Question {
    constructor(question, expected_answer) {
        this.question = question;
        this.expected_answer = expected_answer;
    }
    validate(answer) {
        if(answer == this.expected_answer) {
            return true;
        }
        return false;
    }
}

const moods = ["indicative", "subjective", "imperative", "infinite"];
const tenses = ["present", "imperfect", "perfect", "plusperfect", "future", "future_perfect"];

const Verbs = [Eo];

function get_random_question() {
    return Verbs[Math.floor(Math.random() * Verbs.length)].get_random_question(moods, tenses);
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

window.onload = function() {
    let best_score = parseInt(localStorage.getItem("best_score")) || 0;

    const input = document.getElementById("input");
    const question_element = document.getElementById("question");
    const score_element = document.getElementById("score");
    const score_value = document.getElementById("score_value");
    const best_score_value = document.getElementById("best_score_value");

    let score = 0;
    update_score(score, best_score, score_element, score_value, best_score_value);
    let question = get_random_question();
    question_element.innerText = question.question;
    input.onkeydown = event => {
        if (event.key === 'Enter') {
            if(question.validate(input.value.trim())) {
                question_element.style.color = "lightgreen";
                score++;
                if(score > best_score) {
                    best_score = score;
                    update_score(score, best_score, score_element, score_value, best_score_value, best=true);
                } else {
                    update_score(score, best_score, score_element, score_value, best_score_value);
                }
            } else {
                question_element.style.color = "red";
                score = 0;
                update_score(score, best_score, score_element, score_value, best_score_value, fail=true)
            }
            input.disabled = true;
            setTimeout(() => {
                input.disabled = false;
                question_element.style.color = "white";
                
                question = get_random_question();
                question_element.innerText = question.question;
                input.value = "";
                input.focus();
            }, 1000);
        }
    }
}
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

const test_questions = [new Question("ciao", "ciao"), new Question("Hello", "World")];

function get_random_question() {
    return test_questions[Math.floor(Math.random() * test_questions.length)];
}

function update_text_element(element, text) {
    element.textContent = text;
}

window.onload = function() {
    const input = document.getElementById("input");
    const question_element = document.getElementById("question");
    const score_value = document.getElementById("score_value");

    let score = 0;
    let question = get_random_question();
    question_element.innerText = question.question;
    input.onkeydown = event => {
        if (event.key === 'Enter') {
            console.log(question);
            if(question.validate(input.value.trim())) {
                score++;
                question_element.style.color = "green";
                update_text_element(score_value, score);
            } else {
                question_element.style.color = "red";
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


let player = "x";
let score_rabbit = 0;
let score_carrot = 0;
let score_draw = 0;

function clicked(id) {
    let element = document.getElementById(id);
    if (element.dataset.value) return;

    element.dataset.value = player;

    if (player === "x") {
        element.getElementsByClassName("rabbit-img")[0].classList.add("visible");
    } else {
        element.getElementsByClassName("carrot-img")[0].classList.add("visible");
    }

    player = player === "x" ? "o" : "x";
    checkWinner();
}

function checkWinner() {
    let b1 = document.getElementById("1").dataset.value || "";
    let b2 = document.getElementById("2").dataset.value || "";
    let b3 = document.getElementById("3").dataset.value || "";
    let b4 = document.getElementById("4").dataset.value || "";
    let b5 = document.getElementById("5").dataset.value || "";
    let b6 = document.getElementById("6").dataset.value || "";
    let b7 = document.getElementById("7").dataset.value || "";
    let b8 = document.getElementById("8").dataset.value || "";
    let b9 = document.getElementById("9").dataset.value || "";

    const lines = [
        [b1, b2, b3], [b4, b5, b6], [b7, b8, b9],
        [b1, b4, b7], [b2, b5, b8], [b3, b6, b9],
        [b1, b5, b9], [b3, b5, b7]
    ];

    for (const [a, b, c] of lines) {
        if (a && a === b && b === c) {
            if (a === "x") {
                score_rabbit++;
                document.getElementById("score_rabbit").textContent = score_rabbit;
                alert("Переміг кролик!");
            }
            else {
                score_carrot++;
                document.getElementById("score_carrot").textContent = score_carrot;
                alert("Перемогла морква!");
            }
            return;
        }
        
    }

    if (b1 && b2 && b3 && b4 && b5 && b6 && b7 && b8 && b9) {
        score_draw++;
        document.getElementById("score_draw").textContent = score_draw;
        alert("Нічия!");
    }
}

function reset() {
    for (let i = 1; i <= 9; i++) {
        document.getElementById(i).dataset.value = "";
        document.getElementById(i).getElementsByClassName("rabbit-img")[0].classList.remove("visible");
        document.getElementById(i).getElementsByClassName("carrot-img")[0].classList.remove("visible")
    }

    player = "x";
}



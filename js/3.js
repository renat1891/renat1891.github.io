
let player = "x";
let score_p1 = 0;
let score_p2 = 0;
let score_draw = 0;

const images = {
    rabbit: "images/rabbit.png",
    carrot: "images/carrot.png",
    dog:    "images/dog.png",
    meat:   "images/meat.png"
};

const labels = {
    rabbit: "Кролик",
    carrot: "Морква",
    dog:    "Собака",
    meat:   "М'ясо"
};

function getChoice(playerNum) {
    return document.getElementById("select-" + playerNum).value;
}

function changeAvatar(playerNum) {
    const val1 = getChoice(1);
    const val2 = getChoice(2);

    if (val1 === val2) {
        const allValues = ["rabbit", "carrot", "dog", "meat"];
        if (playerNum === 1) {
            for (let i = 0; i < allValues.length; i++) {
                if (allValues[i] !== val1) {
                    document.getElementById("select-2").value = allValues[i];
                    break;
                }
            }
        } else {
            for (let i = 0; i < allValues.length; i++) {
                if (allValues[i] !== val2) {
                    document.getElementById("select-1").value = allValues[i];
                    break;
                }
            }
        }
    }

    updateAvatars();
}

function updateAvatars() {
    const c1 = getChoice(1);
    const c2 = getChoice(2);
    document.getElementById("avatar-1").src = images[c1];
    document.getElementById("avatar-2").src = images[c2];
    document.getElementById("turn-p1-name").textContent = labels[c1];
    document.getElementById("turn-p2-name").textContent = labels[c2];
}

function clicked(id) {
    let element = document.getElementById(id);
    if (element.dataset.value) return;

    element.dataset.value = player;

    let choice;
    if (player === "x") {
        choice = getChoice(1);
    } else {
        choice = getChoice(2);
    }

    const img = element.getElementsByClassName("cell-img")[0];
    img.src = images[choice];
    img.classList.add("visible");

    if (player === "x") {
        player = "o";
    } else {
        player = "x";
    }

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
                score_p1++;
                document.getElementById("score_p1").textContent = score_p1;
                alert("Переміг Player 1 (" + labels[getChoice(1)] + ")");
            } else {
                score_p2++;
                document.getElementById("score_p2").textContent = score_p2;
                alert("Переміг Player 2 (" + labels[getChoice(2)] + ")");
            }
            return;
        }
    }

    if (b1 && b2 && b3 && b4 && b5 && b6 && b7 && b8 && b9) {
        score_draw++;
        document.getElementById("score_draw").textContent = score_draw;
        alert("Нічия");
    }
}

function reset() {
    for (let i = 1; i <= 9; i++) {
        document.getElementById(i).dataset.value = "";
        const img = document.getElementById(i).getElementsByClassName("cell-img")[0];
        img.classList.remove("visible");
        img.src = "";
    }
    player = "x";
}

updateAvatars();
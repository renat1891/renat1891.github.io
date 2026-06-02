// function TrueorFalse(num){
//     if (num % 2 == 0){
//         return true;
//     }
//     else{
//         return false;
//     }
// }


// console.log(TrueorFalse())






// let secret = Math.floor(Math.random()* 10) + 1;
// function check(){
//     let user = Number(document.getElementById('guess').value);
//     let result = document.getElementById("result");


//     if (user == secret){
//         result.textContent = "You Won"

//     } else if(user > secret){
//         result.textContent = "less"

//     }
//     else{
//         result.textContent = "more"
//     }

// }


function showInfo() {
    let name = document.getElementById("name").value;
    let price = Number(document.getElementById("price").value);
    let quantity = Number(document.getElementById("quantity").value);

    let total = price * quantity;

    let message = "Товар: " + name + "<br>";
    message += "Ціна за 1 шт: " + price + " грн<br>";
    message += "Кількість: " + quantity + "<br>";
    message += "Загальна сума: " + total + " грн<br>";

    if (total > 20000) {
        message += "Це дорога покупка";
    } else {
        message += "Це звичайна покупка";
    }

    document.getElementById("result").innerHTML = message;
}
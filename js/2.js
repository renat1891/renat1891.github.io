let products = [];

function addProduct() {
    let title = document.getElementById("title").value;
    let price = document.getElementById("price").value;

    if (title === "" || price === "") {
        document.getElementById("result").innerHTML = "Заповни всі поля";
        return;
    }

    let product = {
        title: title,
        price: Number(price)
    };

    products.push(product);

    document.getElementById("result").innerHTML = "Товар додано";

    document.getElementById("title").value = "";
    document.getElementById("price").value = "";
}

function showProducts() {
    let text = "";

    for (let i = 0; i < products.length; i++) {
        text += products[i].title + " - " + products[i].price + " грн<br>";
    }

    document.getElementById("result").innerHTML = text;
}

function calculateTotal() {
    let total = 0;

    for (let i = 0; i < products.length; i++) {
        total += products[i].price;
    }

    document.getElementById("result").innerHTML =
        "Загальна сума: " + total + " грн";
}
calculate = function (operation, num1, num2){
    num1 = parseInt(num1)
    num2 = parseInt(num2)
    let result = 0
    switch (operation){
        case "add":
            result = num1 + num2
            break
        case "sub":
            result = num1 - num2
            break
        case "multi":
            result = num1 * num2
            break
        case "div":
            result = num1 / num2
            break
    }
    resultField.textContent = result.toString()

}

// Start -napille kuuntelija joka kutsuu calculate -funktiota oikealla laskutoimituksella.
const calcButton = document.getElementById("start");
const calcOption = document.getElementById("operation");
const num1 = document.getElementById("num1");
const num2 = document.getElementById("num2");
calcButton.addEventListener("click",function() {calculate(calcOption.value, num1.value, num2.value)})

const resultField = document.getElementById("result");
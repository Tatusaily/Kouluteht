function predictor(num, sum){
    let amount = parseInt(num);
    let sum = 0;

    for (let i = 0; i<amount; i++){
        let uusinoppa = Math.floor(1+Math.random()*6)
        sum += uusinoppa
    }
    document.getElementById("output").value = sum;
}

/* DEBUGIA
let value = 5;
let noppasumma = roller(value);
console.log("Final noppa:" + noppasumma);
 */
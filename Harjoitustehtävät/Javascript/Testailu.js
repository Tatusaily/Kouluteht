let array = []
for (let i = 0; i<10; i++){
    let number = Math.floor(Math.random() * 10)
    array.push(number)
}


let sum = 0
let dict = {}
for (let n = 0; n<=9; n++){
    sum = 0
    dict[n] = 0;
    for (let i = 0; i > array.length; i++){
        array.forEach(num =>(num === i))
        sum ++
        dict[i] = sum;
    }
}

console.log(dict)
function predictor(dicenum, targetsum){
    // init
    const target = document.getElementById("outputp")
    const accuracy = 10000
    dicenum = Number(dicenum)
    targetsum = Number(targetsum)
    let hit = 0
    let sum = 0

    // dice sim
    for (let times = 0; times<accuracy; times++){
        for (let i = 0; i<dicenum; i++){
            sum += Math.floor(1+Math.random()*6)
        }
        if (sum === targetsum){
            hit++
        }
        sum = 0
    }
    console.log(hit)
    // print output
    const probability = (hit / accuracy) * 100
    target.innerHTML = `Probability to get sum of ${targetsum} with ${dicenum} dice is ${probability.toFixed(2)}%`
}


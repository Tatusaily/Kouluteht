function rollUntil6(){
    let is6 = false
    while(!is6){
        // Roll the dice
        let newroll = Math.floor(1+ Math.random() * 6)
        console.log(newroll)
        if (newroll === 6){is6 = true}

        // Insert diceroll into list
        let newline = document.createElement("li")
        newline.innerText = newroll.toString()
        document.querySelector("#target").appendChild(newline)
    }
    console.log("Dice rolled.")
}

rollUntil6()
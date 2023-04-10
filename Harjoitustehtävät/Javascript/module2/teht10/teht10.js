// initialize
let candidates = []
function initializeVote(){
    const numOfCands = +prompt("Please input the number of CANDIDATES.")
    for (let i = 1; i <= numOfCands; i++){
        // take the names of candidates
        let newname = prompt(`Please input the name of candidate number ${i}`)
        candidates.push({"name": newname, "votes": 0})

        // let's write the candidate's name to a list so voters can see them easily
        let newline = document.createElement("li")
        newline.innerText = newname
        document.querySelector("#candidates").appendChild(newline)
    }
}

// election
function election(candidates){
    const numOfVoters = +prompt("Please input the number of VOTERS.")
    for (let i = 1; i <= numOfVoters; i++){
        let selection = prompt(`Voter number ${i}, please input your candidate's name:`)
        candidates.forEach(cand => {
            if(cand.name.toLowerCase() === selection.toLowerCase()){
                cand.votes++}
        })
    }
    // sort the candidates and print to console
    candidates.sort((a, b) => b.votes - a.votes)
    console.log(`The winner is ${candidates[0].name} with ${candidates[0].votes} votes!`)
    console.log("results:")
    candidates.forEach((cand)=>{
        console.log(`${cand.name}: ${cand.votes} votes`)
    })
}
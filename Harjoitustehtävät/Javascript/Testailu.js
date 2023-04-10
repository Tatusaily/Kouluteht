// initialize
let candidates = [
    {
        name: "tati",
        votes: 0,
    },
    {
        name: "miri",
        votes: 0,
    },
    ]
console.log(candidates)
candidates.forEach(cand => {if (cand.name === "tati"){cand.votes++}})
console.log(candidates)
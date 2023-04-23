async function getNorris (){
    const formQuery = `${document.getElementById("query").value}`
    const apiurl = `https://api.chucknorris.io/jokes/search?query=${formQuery}`
    const targetDiv = document.getElementById("results")


    const response = await fetch(apiurl)
    const jsonresponse = await response.json()
    const jokes = jsonresponse.result
    console.log(jokes)
    await jokes.forEach(joke=>{
        console.log(joke)
        const joketext = joke.value
        const article = document.createElement("article")
        const jokeP = document.createElement("p")
        jokeP.innerHTML = joketext
        article.appendChild(jokeP)
        targetDiv.appendChild(article)
    })

}
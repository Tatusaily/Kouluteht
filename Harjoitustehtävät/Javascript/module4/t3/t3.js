async function TVHakija(){
    const apiUrl = "https://api.tvmaze.com/search/shows?q="
    const formQuery = `${document.getElementById("query").value}`
 try {
        const result = await fetch(apiUrl + formQuery)
        console.log(`Lähetettiin ${apiUrl + formQuery}`)
        const jsonResult = await result.json()
        console.log("1")
        console.log(jsonResult)
        await displayResults(jsonResult)
   } catch(error) {
        console.log("2")
        console.log(error.message)
    }


}

async function displayResults(input){
    console.log("3")
    console.log(input)
    try {
        document.getElementById("results").innerHTML = ""
        input.forEach(result => {
            // Haetaan tiedot muuttujiin
            const showName = result.show.name
            const showURL = result.show.url
            const showImg = result.show.image?.medium
            const showSum = result.show.summary

            // Laitetaan tiedot HTML -elementteihin ja liitetään ne artikkeliin
            const showArticle = document.createElement("article")
            const artName = document.createElement("h2")
            artName.innerHTML = showName
            showArticle.appendChild(artName)
            const artURL = document.createElement("a")
            artURL.href = showURL
            artURL.innerHTML = "info"
            artURL.target = "_blank"
            showArticle.appendChild(artURL)
            const artIMG = document.createElement("img")
            artIMG.src = showImg
            artIMG.alt = showName
            showArticle.style.backgroundImage = `url("${showImg}")`
            showArticle.appendChild(artIMG)
            const artSum = document.createElement("div")
            artSum.innerHTML = showSum
            showArticle.appendChild(artSum)

            // Laitetaan artikkeli nettisivulle
            document.getElementById("results").appendChild(showArticle)
        })
    }catch (error){
        console.log(error.message)
    }
}
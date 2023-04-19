async function TVHakija(){
    const apiUrl = "https://api.tvmaze.com/search/shows?q="
    const formQuery = `${document.getElementById("query").value}`
    try {
        const result = await fetch(apiUrl + formQuery)
        console.log(`Lähetettiin ${apiUrl + formQuery}`)
        const jsonResult = await result.json()
        console.log("1")
        console.log(jsonResult)
    } catch(error) {
        console.log("2")
        console.log(error.message)
    }
}
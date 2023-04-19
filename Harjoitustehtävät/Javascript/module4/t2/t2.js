function TVHakija(){
    const apiUrl = "https://api.tvmaze.com/search/shows?q="
    const formQuery = `${document.getElementById("query").value}`
    const result = fetch(apiUrl + formQuery)
    console.log(result)
}
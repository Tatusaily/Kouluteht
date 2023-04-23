async function getNorris (){
    try {
        const response = await fetch("https://api.chucknorris.io/jokes/random")
        const jsonresponse = await response.json()
        const joke = jsonresponse.value
        console.log(joke)

    } catch (error){console.log(error.message)}
}
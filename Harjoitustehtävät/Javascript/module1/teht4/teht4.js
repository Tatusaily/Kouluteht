function sortinghat(id) {
    const nimi = prompt("Hey. I am an electronic sorting hat. Tell me your name and I shall assign you into one of the four houses.")
    const kohde = document.querySelector(`#${id}`)
    const randi = Math.floor(1 + Math.random() * 4)
    switch (randi) {
        case 1:
            kohde.innerHTML = `${nimi}, you are Gryffindor`
            break
        case 2:
            kohde.innerHTML = `${nimi}, you are Slytherin`
            break
        case 3:
            kohde.innerHTML = `${nimi}, you are Hufflepuff`
            break
        case 4:
            kohde.innerHTML = `${nimi}, you are Ravenclaw`
            break
    }
}
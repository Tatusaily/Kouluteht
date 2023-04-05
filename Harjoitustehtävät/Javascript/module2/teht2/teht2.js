const participants = +prompt("Anna osallistujien lukumäärä:")
let partNames = []

// Otetaan nimet ja laitetaan ne listaan
for (let i = 0; i<participants; i++){
  let nimi = prompt(`Anna ${i+1}. osallistujan nimi:`)
  partNames.push(nimi)
}
partNames.sort()

// Nimet on listassa, laitetaan ne HTML listaan
for (let i = 0; i < partNames.length; i++){
    let nimi = document.createElement("li")                 // Tekee <li> elementin
    nimi.innerText = partNames[i]                                   // Laittaa <li> elementtiin nimen
    document.querySelector("#target").appendChild(nimi)     // Laittaa <li>:n #target listaan.
}

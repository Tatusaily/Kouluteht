const numLista = []
for (let i = 1; i <= 5; i++){
  let luku = +prompt(`Anna ${i}. luku.`)
  numLista.push(luku)
}
console.log("Kokonainen lista:", numLista)

for (let i = numLista.length-1; i>=0; i--){
  console.log(numLista[i])
}

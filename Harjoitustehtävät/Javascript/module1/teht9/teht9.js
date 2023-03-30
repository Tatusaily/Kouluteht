function alkuluku(num, id) {
    num = Number(num)
    id = document.getElementById(id)
    let on_alku = true
    // Jos num = 1 tai 2, tehdään erikoispäätös
    if (num === 1) {
        on_alku = false
    } else if (num === 2) {
        on_alku = true
    } else {
        // Varsinainen alkuluku-loop. Mennään num kerrallaan, kahden luvun välein alkaen kolmesta.
        // 1 ja 2 käsiteltiin äsken. Alkuluku ei voi olla parillinen joten tarkistetaan vain parittomat.
        let i = 3
        while (i < (num - 1)) {
            if (num % i === 0) {
                on_alku = false
                break
            }
            i += 2
        }
    }
    if (on_alku === true){
        id.innerHTML = `${num} is prime!`
        id.style.color = "green"
    } else if (on_alku === false) {
        id.innerHTML = `${num} is not prime!`
        id.style.color = "red"
    }
}
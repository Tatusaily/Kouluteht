function summa(eka, toka){
    return eka + toka;
}
function tulo(eka, toka){
    return eka * toka;
}
function keskiarvo(eka, toka){
    return eka+toka/2;
}
function laske(eka, toka){
    console.log(eka, toka)
    console.log(summa(eka, toka))
    console.log(tulo(eka, toka))
    console.log(keskiarvo(eka, toka))
    // Jos näitä ei parsee niin sit ne on stringejä.
    // Miksi? Ne osoitetaan HTML:ssä numeroiksi. Melkoinen työmaa.
    eka = parseInt(eka)
    toka = parseInt(toka)
    document.getElementById("summa").value = summa(eka, toka)
    document.getElementById("tulo").value = tulo(eka, toka)
    document.getElementById("keskiarvo").value = keskiarvo(eka, toka)
}
function summa(eka, toka, kolmas){
    return eka + toka + kolmas;
}
function tulo(eka, toka, kolmas){
    return eka * toka * kolmas;
}
function keskiarvo(eka, toka, kolmas){
    return (eka+toka+kolmas)/3;
}
function laske(eka, toka, kolmas){
    // Jos näitä ei parsee niin sit ne on stringejä.
    // Miksi? Ne osoitetaan HTML:ssä numeroiksi. Melkoinen työmaa.
    eka = Number(eka)
    toka = Number(toka)
    kolmas = Number(kolmas)
    document.getElementById("summa").value = summa(eka, toka, kolmas)
    document.getElementById("tulo").value = tulo(eka, toka, kolmas)
    document.getElementById("keskiarvo").value = keskiarvo(eka, toka, kolmas)
}
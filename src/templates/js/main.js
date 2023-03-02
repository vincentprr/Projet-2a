const POPUP = document.getElementById('popup');
const POPTEXT = document.getElementById('poptext');

function displayHeader() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

function showpopup(texte) {
    if (POPUP!=null && POPTEXT!=null){
        POPUP.style.display = 'block';
        POPTEXT.innerHTML = texte;
    }
   }
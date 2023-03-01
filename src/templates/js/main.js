function displayHeader() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

function showpopup() {
    window.open("http://urldelapageacharger.htm", "nomdelafenetrepopup", "height=XXX, width=XXX, menubar='yes|no', toolbar='yes|no', location='yes|no', status='yes|no', scrollbars='yes|no'");
   }
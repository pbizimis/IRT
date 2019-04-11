function openNav() {
    document.getElementById("sidenav").style.width = "100%";
}

function closeNav() {
    document.getElementById("sidenav").style.width = "0";
}


function toggleNavbar() {
    var element = document.getElementById("test");
    if(element.classList.contains("is-active")) {
        element.classList.remove("is-active");
        document.getElementById("sidenav").style.width = "0";
    } else {
        element.classList.add("is-active");
        document.getElementById("sidenav").style.width = "100%";
    }
}
    
function openNav() {
    document.getElementById("sidenav").style.right = "0";
    document.getElementById("body").style.overflow = "hidden";
}

function closeNav() {
    document.getElementById("sidenav").style.right = "100%";
    document.getElementById("body").style.overflow = "visible";
}


/*
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
*/
function openNav() {
    document.getElementById("sidenav").style.right = "0";
    document.getElementById("body").style.overflow = "hidden";
}

function closeNav() {
    document.getElementById("sidenav").style.right = "100%";
    document.getElementById("body").style.overflow = "visible";
}

function togglePanel() {
    var panel = document.getElementsByClassName("panel-konzept")[0];
    var plus = document.getElementsByClassName("plus")[0];
    if (panel.style.maxHeight){
        panel.style.maxHeight = null;
        plus.style.transform = "rotate(0deg)";
    } else {
        panel.style.maxHeight = panel.scrollHeight + "px";
        plus.style.transform = "rotate(45deg)";
    }
}

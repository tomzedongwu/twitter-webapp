window.onscroll = function() {
    var tools = document.querySelector(".filters");
    var sticky = tools.offsetTop;

    if (window.pageYOffset >= sticky) {
        tools.classList.add("sticky")
    } else {
        tools.classList.remove("sticky");
    }
}

window.onload = function() {
    let oBtn = document.querySelector(".search");
    let oHusky = document.querySelector(".instruct");
    oBtn.onclick = function() {
        oHusky.remove();
    }
}


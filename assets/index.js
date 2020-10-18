window.onscroll = function() {
    var tools = document.querySelector(".filters");
    var sticky = tools.offsetTop;

    if (window.pageYOffset >= sticky) {
        tools.classList.add("sticky")
    } else {
        tools.classList.remove("sticky");
    }
}



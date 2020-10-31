var navIcon = {
    "active": '<path fill-rule="evenodd" d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>',
    "inactive": '<path fill-rule="evenodd" d="M2.5 11.5A.5.5 0 0 1 3 11h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4A.5.5 0 0 1 3 7h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4A.5.5 0 0 1 3 3h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"/>'
}

function navShow() {
    var $navCollapse = document.getElementById("navbarNavAltMarkup");
    if (! $navCollapse.classList.contains("show")) {
        setTimeout(() => {
            document.getElementById("navbar").classList.remove("hide");
            document.getElementById("navbar").classList.add("show");
        }, 10);

        setTimeout(() => {
            document.getElementById("collapse-icon").innerHTML = navIcon["active"];
        }, 290);
    } else {
        setTimeout(() => {
            document.getElementById("navbar").classList.remove("show");
            document.getElementById("navbar").classList.add("hide");
            document.getElementById("collapse-icon").innerHTML = navIcon["inactive"];
        }, 300);
    }
}

document.getElementById("collapse-button").addEventListener("click", navShow);

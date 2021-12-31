employer_det_div = dom.getElementById("employer_info_div")
profile_logo_card = dom.getElementById("profile_logo_card")


function check_size_employer_profile() {
    if (window.outerWidth < 790) {
        employer_det_div.className = "col-12"
        profile_logo_card.className = "col-12 d-none d-md-block"

    }
    console.log(window.outerWidth)
    if (window.outerWidth > 790) {
        employer_det_div.className = "col-6"
        profile_logo_card.className = "col-5 d-none d-md-block"

    }

}

window.onresize = check_size_employer_profile
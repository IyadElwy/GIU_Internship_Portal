employer_det_div = dom.getElementById("employer_info_div")
profile_logo_card = dom.getElementById("profile_logo_card")


function check_size_employer_profile() {
    if (window.outerWidth < 1153) {
        employer_det_div.className = "col-6"
        profile_logo_card.className = "col-6 d-none d-md-block"

    }
    if (window.outerWidth > 1153) {
        employer_det_div.className = "col-7"
        profile_logo_card.className = "col-5 d-none d-md-block"

    }

}

window.onresize = check_size_employer_profile
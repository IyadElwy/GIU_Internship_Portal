var dom = document

student_det_div = dom.getElementById("student_info_div")
profile_logo_card_student = dom.getElementById("profile_logo_card_student")

function check_size_student_profile() {


    if (window.outerWidth < 1153) {
        student_det_div.className = "col-12"
        profile_logo_card.className = "col-12 d-none d-md-block"

    }
    if (window.outerWidth > 1153) {
        student_det_div.className = "col-6"
        profile_logo_card.className = "col-5 d-none d-md-block"

    }

}

window.onresize = check_size_student_profile
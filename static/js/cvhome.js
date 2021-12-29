let dom = document

let navShow = dom.getElementById('showNav')
let navEdit = dom.getElementById('editNav')
let navDelete = dom.getElementById('deleteNav')
let resumeHomeBody = dom.getElementById('resume_home_body')

navShow.addEventListener('click', function () {
    navEdit.className = "nav-link"
    navShow.className = "nav-link active"
    navDelete.className = "nav-link"
    navEdit.ariaCurrent = false
    navShow.ariaCurrent = true
    navDelete.ariaCurrent = false
    resumeHomeBody.innerHTML = "<br>\n" +
        "                <br>\n" +
        "                <br><h5 class=\"card-title\">See your current resume</h5>\n" +
        "                <p class=\"card-text\">Ps. You can download your resume as a PDF!</p>\n" +
        "                <a href=\"#\" class=\"btn btn-primary\">Show resume</a>\n<br>\n" +
        "                <br>\n" +
        "                <br><br>\n" +
        "                <br>\n" +
        "                <br><br>\n" +
        "                <br>\n" +
        "                <br><br>"

})

navEdit.addEventListener('click', function () {
    navEdit.className = "nav-link active"
    navShow.className = "nav-link"
    navDelete.className = "nav-link"
    navEdit.ariaCurrent = true
    navShow.ariaCurrent = false
    navDelete.ariaCurrent = false
    resumeHomeBody.innerHTML = "<br>\n" +
        "                <br>\n" +
        "                <br><h5 class=\"card-title\">Edit your resume</h5>\n" +
        "                <p class=\"card-text\">Always keep your resume up to date!</p>\n" +
        "                <a href=\"{% url 'editresume' %}\" class=\"btn btn-primary\">Edit resume</a>\n<br>\n" +
        "                <br>\n" +
        "                <br><br>\n" +
        "                <br>\n" +
        "                <br><br>\n" +
        "                <br>\n" +
        "                <br><br>"
})

navDelete.addEventListener('click', function () {
    navEdit.className = "nav-link"
    navShow.className = "nav-link"
    navDelete.className = "nav-link active"
    navEdit.ariaCurrent = false
    navShow.ariaCurrent = false
    navDelete.ariaCurrent = true
    resumeHomeBody.innerHTML = "<br>\n" +
        "                <br>\n" +
        "                <br><h5 class=\"card-title\">Delete your resume</h5>\n" +
        "                <p class=\"card-text\">Want a do-over? Delete your resume and start over.</p>\n" +
        "                <a href=\"{% url 'deleteresume' %}\" class=\"btn btn-primary\">Delete resume</a>\n<br>\n" +
        "                <br>\n" +
        "                <br><br>\n" +
        "                <br>\n" +
        "                <br><br>\n" +
        "                <br>\n" +
        "                <br><br>"
})
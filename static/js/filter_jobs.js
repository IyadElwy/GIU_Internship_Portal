dom = document

var addFacultyButton = dom.getElementById("filter_btn_add_fac")
var facfilterdiv = dom.getElementById("faculty_input")

addFacultyButton.addEventListener('click', function () {
    facfilterdiv.innerHTML +=
        "                                <label for=\"inputState\">Faculty</label>\n" +
        "                                <select id=\"inputState\" class=\"form-control \">\n" +
        "                                    <option selected>Choose...</option>\n" +
        "                                    <option>CS</option>\n" +
        "                                    <option>Business</option>\n" +
        "                                    <option>Engineering</option>\n" +
        "                                    <option>Design</option>\n" +
        "                                    <option>Architecture</option>\n" +
        "                                    <option>Pharmaceutical</option>\n" +
        "                                </select>\n" +
        "                                <br>"
})

allFacFilterBoxes = dom.getElementsByClassName("fac_input_class")

searchBox = dom.getElementById("searchbutton")
searchBox.addEventListener('click', function () {
    var facultiesToFilter = ""
    for (let i = 0; i < allFacFilterBoxes.length; i++) {
        var choosebox = allFacFilterBoxes[i].getElementsByClassName("choosebox")
        facultiesToFilter += choosebox[0].value
    }
    var reqSemBox = dom.getElementsByClassName("required_semester_class_box")
    requiredSemesters = reqSemBox[0].value


    var allJobBoxes = dom.getElementsByClassName("job_box")
    for (let i = 0; i < allJobBoxes.length; i++) {
        var job = allJobBoxes[i]
        var jobSem = job.getElementsByClassName("required_semester")[0].textContent
        var required_faculties = job.getElementsByClassName("faculty")[0].textContent


        if (jobSem > requiredSemesters || (!required_faculties.includes(facultiesToFilter) && !facultiesToFilter.includes("Choose..."))) {
            job.style.display = "none"

        } else {
            job.style.display = "block"
        }
    }

})
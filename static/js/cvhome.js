let dom = document

let navShow = dom.getElementById('showNav')
let navEdit = dom.getElementById('editNav')
let navDelete = dom.getElementById('deleteNav')
let resumeDivShow = dom.getElementById('showDiv')
let resumeDivEdit = dom.getElementById('editDiv')
let resumeDivDelete = dom.getElementById('deleteDiv')

navShow.addEventListener('click', function () {
    navEdit.className = "nav-link"
    navShow.className = "nav-link active"
    navDelete.className = "nav-link"
    navEdit.ariaCurrent = false
    navShow.ariaCurrent = true
    navDelete.ariaCurrent = false
    resumeDivEdit.style.display = "None"
    resumeDivShow.style.display = ""
    resumeDivDelete.style.display = "None"
})

navEdit.addEventListener('click', function () {
    navEdit.className = "nav-link active"
    navShow.className = "nav-link"
    navDelete.className = "nav-link"
    navEdit.ariaCurrent = true
    navShow.ariaCurrent = false
    navDelete.ariaCurrent = false
    resumeDivShow.style.display = "None"
    resumeDivEdit.style.display = ""
    resumeDivDelete.style.display = "None"


})

navDelete.addEventListener('click', function () {
    navEdit.className = "nav-link"
    navShow.className = "nav-link"
    navDelete.className = "nav-link active"
    navEdit.ariaCurrent = false
    navShow.ariaCurrent = false
    navDelete.ariaCurrent = true
    resumeDivEdit.style.display = "None"
    resumeDivShow.style.display = "None"
    resumeDivDelete.style.display = ""


})
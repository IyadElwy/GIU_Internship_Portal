const dom = document;

let sideBarBox = dom.getElementsByClassName('side_item')


for (let i = 0; i < sideBarBox.length; i++) {

    sideBarBox[i].addEventListener('click', function () {

        let firstLastName = sideBarBox[i].getElementsByTagName('strong')
        let jobPk = sideBarBox[i].getElementsByTagName('p')
        let content = dom.getElementsByClassName(firstLastName[0].textContent + '-' + jobPk[0].textContent)

        let contentTemp = dom.getElementsByClassName('page-content-wrapper')

        for (let j = 0; j < contentTemp.length; j++) {
            if (contentTemp[j].className !== content[0].className) {
                contentTemp[j].style.display = 'none'
            }
        }
        content[0].style.display = 'block'


    })
}

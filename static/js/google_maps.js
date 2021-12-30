// Initialize and add the map
let dom = document

company_address = dom.getElementById("company_address").textContent
api_key = dom.getElementById("api_key").textContent
api_key_positions = dom.getElementById("api_key_positions").textContent


let linkLonLat = "http://api.positionstack.com/v1/forward?access_key=" + api_key_positions.toString().slice(0, -1) + "&query=" + company_address


function initMap() {
    // The location of Uluru
    fetch(linkLonLat).then(function (response) {
        return response.json();
    }).then(function (data) {
        var lat = parseFloat(data['data'][0]['latitude'])
        var lon = parseFloat(data['data'][0]['longitude'])

        const company_location = {
            lat: lat, lng: lon
        };
        // The map, centered at Uluru
        const map = new google.maps.Map(document.getElementById("map"), {
            zoom: 4,
            center: company_location,
        });
        // The marker, positioned at Uluru
        const marker = new google.maps.Marker({
            position: company_location,
            map: map,
        });


    }).catch(function (err) {
        console.warn("Something went wrong", err)

    });

}

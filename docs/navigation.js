document.addEventListener("DOMContentLoaded", function() {
    // Initialiser la carte par défaut sur 'map1' pour le Bénin et afficher 'map3'
    document.getElementById('map1').style.display = 'block'; // Afficher la première carte
    document.getElementById('map3').style.display = 'block'; // Afficher la troisième carte

    // Charger la carte Bénin dans map1
    const iframe = document.getElementById('map-frame');
    iframe.src = 'isibf_benin.html'; // Carte par défaut pour le Bénin

    // Afficher le menu déroulant pour 'Normalisation par pays'
    document.getElementById('countryDropdown').style.display = 'block';
});

// Function to toggle visibility of the maps
function toggleMap(showMapId, group) {
    // Hide maps that are not part of the specified group
    const maps = document.getElementsByClassName('map');
    for (let i = 0; i < maps.length; i++) {
        if (!maps[i].classList.contains(group)) {
            maps[i].style.display = 'none'; // Hide maps not in the current group
        }
    }

    // Show the specified map
    document.getElementById(showMapId).style.display = 'block';

    // Display the dropdown only for 'Normalisation par pays' (map1)
    if (showMapId === 'map1') {
        document.getElementById('countryDropdown').style.display = 'block';
    } else {
        document.getElementById('countryDropdown').style.display = 'none';
    }
}

// Function to update the map based on the selected country
function showCountryMap() {
    const countrySelect = document.getElementById('country-select').value;
    const iframe = document.getElementById('map-frame');

    // Change the iframe source based on the selected country
    iframe.src = `isibf_${countrySelect}.html`;
}

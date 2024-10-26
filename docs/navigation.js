document.addEventListener("DOMContentLoaded", function() {
    // Initialiser la carte par défaut sur 'map1' pour le Bénin et afficher 'chart3'
    document.getElementById('map1').style.display = 'block'; // Afficher la première carte
    document.getElementById('chart3').style.display = 'block'; // Afficher le diagramme par défaut

    // Charger la carte du Bénin dans map1 par défaut
    const iframe = document.getElementById('map-frame');
    iframe.src = 'isibf_benin.html'; // Carte par défaut pour le Bénin

    // Afficher le menu déroulant pour 'Normalisation par pays'
    document.getElementById('countryDropdown').style.display = 'block';
});

// Function to toggle visibility of the maps and charts
function toggleMap(showMapId) {
    const mapsAndCharts = document.querySelectorAll('.map, .chart');
    mapsAndCharts.forEach(element => {
        element.style.display = 'none'; // Hide all maps and charts
    });
    
    // Show the selected map or chart
    document.getElementById(showMapId).style.display = 'block';

    // Afficher le menu déroulant seulement pour 'Normalisation par pays' (map1)
    if (showMapId === 'map1') {
        document.getElementById('countryDropdown').style.display = 'block';
    } else if (showMapId === 'chart3') {
        document.getElementById('countryDropdown2').style.display = 'block';
    } else {
        document.getElementById('countryDropdown').style.display = 'none';
        document.getElementById('countryDropdown2').style.display = 'none';
    }
}

// Function to update the map based on the selected country in the first dropdown
function showCountryMap() {
    const countrySelect = document.getElementById('country-select').value;
    const iframe = document.getElementById('map-frame');

    // Change the iframe source based on the selected country
    iframe.src = `isibf_${countrySelect}.html`;
}

// Function to display the selected country's chart in chart3
function showCountryChart() {
    const countrySelect2 = document.getElementById('country-select2').value;
    const iframe2 = document.getElementById('chart-frame2');

    // Change the iframe source based on the selected country
    iframe2.src = `indicateur_demographique_${countrySelect2}.html`;
}

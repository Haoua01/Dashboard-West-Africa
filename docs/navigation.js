document.addEventListener("DOMContentLoaded", function() {
    // Initial hide of country map and dropdown until 'Normalisation par pays' is clicked
    document.getElementById('countryDropdown').style.display = 'none';
    document.getElementById('map1').style.display = 'none';
});

function toggleMap(showMapId, group) {
    // Hide all maps not in the current group
    Array.from(document.getElementsByClassName('map')).forEach(map => {
        map.style.display = map.classList.contains(group) ? 'none' : map.style.display;
    });

    // Show the specified map
    document.getElementById(showMapId).style.display = 'block';

    // Display the dropdown only for 'Normalisation par pays' (map1)
    document.getElementById('countryDropdown').style.display = (showMapId === 'map1') ? 'block' : 'none';
}

function showCountryMap() {
    const countrySelect = document.getElementById('country-select').value;
    const iframe = document.getElementById('map-frame');

    // Update iframe source based on selected country
    iframe.src = `isibf_${countrySelect}.html`;
}

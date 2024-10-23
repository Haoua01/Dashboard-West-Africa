document.addEventListener("DOMContentLoaded", function() {
    // Create the 'Back to Dashboard' button
    const backButton = document.createElement("a");
    backButton.href = "index.html"; // Link back to the dashboard (main page)
    backButton.textContent = "Retour";
    backButton.classList.add("map-link"); // Add the existing class for styling

    // Find the container where you want to insert the button
    const container = document.querySelector(".container");

    if (container) {
        // Insert the button at the end of the container
        container.appendChild(backButton);
    }

    // Initial hide of country map and dropdown until 'Normalisation par pays' is clicked
    document.getElementById('countryDropdown').style.display = 'none';
    document.getElementById('map1').style.display = 'none';
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
    if (countrySelect === 'benin') {
        iframe.src = 'isibf_benin.html';
    } else if (countrySelect === 'togo') {
        iframe.src = 'isibf_togo.html';
    } else if (countrySelect === 'coteivoire') {
        iframe.src = 'isibf_civ.html';
    } else if (countrySelect === 'combined') {
        iframe.src = 'isibf_benin_togo_civ_norm.html';
    }
}

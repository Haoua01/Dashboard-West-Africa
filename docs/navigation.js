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

    // Show map1 and map3 by default
    document.getElementById('map1').style.display = 'block'; // Show map1
    document.getElementById('map3').style.display = 'block'; // Show map3

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
}



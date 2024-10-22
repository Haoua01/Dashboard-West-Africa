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

    // Add event listeners for the first set of toggle buttons (maps 1 and 2)
    const toggleButtons1 = document.querySelectorAll('.toggle-buttons:first-of-type button');
    toggleButtons1.forEach((button) => {
        button.addEventListener('click', function() {
            toggleMap(this.textContent.includes('Normalisation par pays') ? 'map1' : 'map2');
        });
    });

    // Add event listeners for the second set of toggle buttons (maps 3 and 4)
    const toggleButtons2 = document.querySelectorAll('.toggle-buttons:last-of-type button');
    toggleButtons2.forEach((button) => {
        button.addEventListener('click', function() {
            toggleMap(this.textContent.includes('Résultats globaux') ? 'map3' : 'map4');
        });
    });
});

// Function to toggle visibility of the maps
function toggleMap(mapId) {
    // Hide all maps
    var maps = document.getElementsByClassName('map');
    for (var i = 0; i < maps.length; i++) {
        maps[i].style.display = 'none';
    }
    
    // Show the selected map
    document.getElementById(mapId).style.display = 'block';
}

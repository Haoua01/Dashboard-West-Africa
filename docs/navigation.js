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

    // Add event listeners for the first set of toggle buttons
    const toggleButtons1 = document.querySelectorAll('.toggle-buttons button');
    toggleButtons1.forEach((button) => {
        button.addEventListener('click', function() {
            const mapId = this.textContent.includes('Normalisation par pays') ? 'map1' : 'map2';
            toggleMap(mapId);
        });
    });

    // Add event listeners for the second set of toggle buttons
    const toggleButtons2 = document.querySelectorAll('.toggle-buttons + .toggle-buttons button');
    toggleButtons2.forEach((button) => {
        button.addEventListener('click', function() {
            const mapId = this.textContent.includes('Résultats globaux') ? 'map3' : 'map4';
            toggleMap(mapId);
        });
    });

    // Initialize map1 and map3 as visible
    toggleMap('map1'); // Show the first map of the first indicator
    toggleMap('map3'); // Show the first map of the second indicator
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
    
    // Display map3 if map1 is visible
    if (mapId === 'map1') {
        document.getElementById('map3').style.display = 'block';
    }
}

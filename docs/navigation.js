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
    const toggleButtons1 = document.querySelectorAll('.toggle-buttons:first-of-type button');
    toggleButtons1.forEach((button) => {
        button.addEventListener('click', function() {
            const mapId = this.textContent.includes('Normalisation par pays') ? 'map1' : 'map2';
            toggleMap(mapId);
        });
    });
    toggleMap('map1', true); // Show map1 and keep it visible

    // Add event listeners for the second set of toggle buttons
    const toggleButtons2 = document.querySelectorAll('.toggle-buttons:last-of-type button');
    toggleButtons2.forEach((button) => {
        button.addEventListener('click', function() {
            const mapId = this.textContent.includes('Résultats globaux') ? 'map3' : 'map4';
            toggleMap(mapId);
        });
    });

    toggleMap('map3', true); // Show map3 and keep it visible
});

// Function to toggle visibility of the maps
function toggleMap(mapId, show = false) {
    // Hide all maps
    var maps = document.getElementsByClassName('map');
    for (var i = 0; i < maps.length; i++) {
        maps[i].style.display = 'none';
    }
    
    // Show the selected map if show is true
    if (show) {
        document.getElementById(mapId).style.display = 'block';
    } else {
        // If not showing, show the selected map normally
        document.getElementById(mapId).style.display = 'block';
    }
}

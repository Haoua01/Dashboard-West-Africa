document.addEventListener("DOMContentLoaded", function() {
    // Create the 'Back to Dashboard' button
    const backButton = document.createElement("a");
    backButton.href = "index.html"; // Link back to the dashboard (main page)
    backButton.textContent = "Retour au Dashboard";
    backButton.classList.add("map-link"); // Add the existing class for styling

    // Find the container where you want to insert the button (you can adjust the selector if needed)
    const container = document.querySelector(".container");

    if (container) {
        // Insert the button at the end of the container
        container.appendChild(backButton);
    }
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

// Initialize the first map as visible
window.onload = function() {
    toggleMap('map1'); // Show the first map by default
}
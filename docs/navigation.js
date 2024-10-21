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

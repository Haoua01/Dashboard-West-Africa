document.addEventListener("DOMContentLoaded", function() {
    const toggle = document.getElementById("map-toggle");
    const maps = document.querySelectorAll(".maps a");

    toggle.addEventListener("change", function() {
        if (toggle.checked) {
            maps.forEach(map => {
                map.style.display = "inline-block"; // Show both maps
            });
        } else {
            maps.forEach((map, index) => {
                map.style.display = index === 0 ? "inline-block" : "none"; // Show only the first map
            });
        }
    });

    // Initial state: Show only the first map
    maps.forEach((map, index) => {
        map.style.display = index === 0 ? "inline-block" : "none";
    });
});

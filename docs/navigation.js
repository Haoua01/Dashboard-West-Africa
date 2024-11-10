document.addEventListener("DOMContentLoaded", function() {
    // Show map1 and the corresponding dropdown by default
    document.getElementById('map1').style.display = 'block';
    document.getElementById('countryDropdown11').style.display = 'block';
    
    // Show chart3 and the corresponding dropdown by default
    document.getElementById('chart3').style.display = 'block';
    document.getElementById('countryDropdown21').style.display = 'block';

    // Hide all elements of group2 except chart3 by default
    const group2Elements = document.querySelectorAll('.group2');
    group2Elements.forEach(element => {
        if (element.id !== 'chart3') {
            element.style.display = 'none';
        }
    });

    // Set the default button active for 'map1'
    setActiveButton('map1');
    setActiveButton('chart3');

    // Set the map to 'Bénin' by default for map1
    const iframe = document.getElementById('map-frame');
    iframe.src = 'results/ISIBF_benin.html';

    // Set the chart for 'Bénin' by default for chart3
    const iframe2 = document.getElementById('chart-frame2');
    iframe2.src = 'results/demographic_indicator_benin.html';

    // Show the slider for 'CIV' if it's selected
    const civSelect = document.getElementById('country-select11');
    showCountryMap1(civSelect.value); // Call to initialize map view based on default country
});

// Function to show or hide slider and update map based on the country selection
function showCountryMap1(countrySelect) {
    const iframe = document.getElementById('map-frame');
    const sliderContainer = document.getElementById('slider-civ-container');
    
    if (countrySelect === 'civ') {
        // Show the slider when 'CIV' is selected
        sliderContainer.style.display = 'block';
        
        // Set the map based on the slider value
        toggleMapView(); // This function will check the slider's value
    } else {
        // Hide the slider for other countries
        sliderContainer.style.display = 'none';
        
        // Load the default map for the selected country
        iframe.src = `results/ISIBF_${countrySelect}.html`;
    }
}

// Function to update the map based on country selection in the second dropdown (map2)
function showCountryMap2() {
    const countrySelect = document.getElementById('country-select12').value;
    const iframe = document.getElementById('map2-frame');
    iframe.src = `results/ISIBF2_${countrySelect}.html`;
}

// Function to update the chart based on the country selection in chart3
function showCountryChart() {
    const countrySelect = document.getElementById('country-select21').value;
    const iframe2 = document.getElementById('chart-frame2');
    iframe2.src = `results/demographic_indicator_${countrySelect}.html`;
}

// Function to toggle between "Par districts" and "Par départements" based on slider value
function toggleMapView() {
    const sliderValue = document.getElementById('slider-civ').value;
    const iframe = document.getElementById('map-frame');

    // Update the label based on the slider value
    updateSliderLabel(sliderValue);

    // Toggle the map based on the slider value
    if (sliderValue === '0') {
        iframe.src = 'results/ISIBF_civ_districts.html'; // Map by districts
    } else if (sliderValue === '1') {
        iframe.src = 'results/ISIBF_civ_departments.html'; // Map by departments
    }
}

// Function to update the label based on the slider value
function updateSliderLabel(sliderValue) {
    const sliderLabel = document.getElementById('slider-label');
    if (sliderValue === '0') {
        sliderLabel.textContent = 'Districts'; // Show "Par districts"
    } else if (sliderValue === '1') {
        sliderLabel.textContent = 'Départements'; // Show "Par départements"
    }
}

// Function to activate the correct button (for map or chart)
function setActiveButton(activeId) {
    const buttons = document.querySelectorAll('.toggle-buttons button');
    buttons.forEach(button => button.classList.remove('active'));

    const activeButton = Array.from(buttons).find(button => button.onclick.toString().includes(activeId));
    if (activeButton) {
        activeButton.classList.add('active');
    }
}

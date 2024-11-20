document.addEventListener("DOMContentLoaded", function() {
    // Afficher uniquement 'map1' de group1 au démarrage
    document.getElementById('map1').style.display = 'block'; // Afficher la première carte par défaut
    document.getElementById('countryDropdown11').style.display = 'block'; // Afficher le menu déroulant associé

    // Afficher uniquement 'chart3' de group2 au démarrage
    document.getElementById('chart3').style.display = 'block'; // Afficher le premier histogramme par défaut
    document.getElementById('countryDropdown21').style.display = 'block'; // Afficher le menu déroulant associé

    // Masquer tous les éléments de group2 au démarrage
    const group2Elements = document.querySelectorAll('.group2');
    group2Elements.forEach(element => {
        if (element.id !== 'chart3') {
            element.style.display = 'none';
        }
    });

    // Charger la carte du Bénin dans map1 par défaut
    const iframe = document.getElementById('map-frame');
    iframe.src = 'results/ISIBF_régions_benin.html'; // Carte par défaut pour le Bénin

    // Charger l'histogramme du Bénin dans chart3 par défaut
    const iframe2 = document.getElementById('chart-frame2');
    iframe2.src = 'results/demographic_indicator_régions_benin.html'; // Histogramme par défaut pour le Bénin


});



function toggleGroup2(showMapId) {
    const charts = document.querySelectorAll('.group2');
    charts.forEach(element => {
        if (element.id !== showMapId) {
            element.style.display = 'none';
        }
    });
    
    // Afficher la carte ou l'histogramme sélectionné
    document.getElementById(showMapId).style.display = 'block';


    // Contrôle de la visibilité des dropdowns
    if (showMapId === 'chart3') {
        document.getElementById('countryDropdown21').style.display = 'block'; // Afficher dropdown pour chart3
    } else {
        document.getElementById('countryDropdown21').style.display = 'none'; // Masquer dropdown pour chart3
    }

}



// Fonction pour mettre à jour la carte en fonction du pays sélectionné dans le premier menu déroulant
function showCountryMap1() {
    const countrySelect = document.getElementById('country-select11').value;
    const iframe = document.getElementById('map-frame');
    const toggleSwitch = document.getElementById('toggle-switch');
 
    if (countrySelect === 'civ') {
        updateSliderValue();
        toggleSwitch.style.display = 'block';
    } else if (countrySelect === 'mali') {
        updateSliderValue();
        toggleSwitch.style.display = 'block';
    } else if (countrySelect === 'burkina') {
        updateSliderValue();
        toggleSwitch.style.display = 'block';
    } else if (countrySelect === 'combined') {
        updateSliderValue();
        toggleSwitch.style.display = 'block';
    } else {
        // For other countries, load the default map
        iframe.src = `results/ISIBF_régions_${countrySelect}.html`;
        toggleSwitch.style.display = 'none';
    }
}




// Fonction pour afficher le graphique de barres correspondant au pays sélectionné dans chart3
function showCountryChart() {
    const countrySelect2 = document.getElementById('country-select21').value;
    const iframe2 = document.getElementById('chart-frame2');
    if (countrySelect2 === 'civ') {
        iframe2.src = `results/demographic_indicator_districts_${countrySelect2}.html`;
    } else {
        iframe2.src = `results/demographic_indicator_régions_${countrySelect2}.html`;
    }
}


// Function to update the map based on toggle switch (checkbox) state
function updateSliderValue() {
    const countrySelect = document.getElementById('country-select11').value;
    const iframe = document.getElementById('map-frame');
    const checkbox = document.getElementById('checkbox');
    const districtLabel = document.getElementById('region-label');
    const departmentLabel = document.getElementById('department-label');

    // Check if checkbox is checked (1 = "Par départements", 0 = "Par districts")
    if (countrySelect === 'civ') {
        if (checkbox.checked) {
            iframe.src = 'results/ISIBF_départements_civ.html'; // Map by departments
            departmentLabel.style.fontWeight = 'bold'; // Highlight "Départements"
            districtLabel.style.fontWeight = 'normal'; // Remove highlight from "Districts"
        }
        else {
            iframe.src = 'results/ISIBF_districts_civ.html'; // Map by departments
            districtLabel.style.fontWeight = 'bold'; // Highlight "Districts"
            departmentLabel.style.fontWeight = 'normal'; // Remove highlight from "Départements"
        }
    } else if (countrySelect === 'mali') {
        if (checkbox.checked) {
            iframe.src = 'results/ISIBF_cercles_mali.html'; // Map by departments
            departmentLabel.style.fontWeight = 'bold'; // Highlight "Départements"
            districtLabel.style.fontWeight = 'normal'; // Remove highlight from "Districts"
        }
        else {
            iframe.src = 'results/ISIBF_régions_mali.html'; // Map by departments
            districtLabel.style.fontWeight = 'bold'; // Highlight "Districts"
            departmentLabel.style.fontWeight = 'normal'; // Remove highlight from "Départements"
        } 
    } else if (countrySelect === 'burkina') {
        if (checkbox.checked) {
            iframe.src = 'results/ISIBF_départements_burkina.html'; // Map by departments
            departmentLabel.style.fontWeight = 'bold'; // Highlight "Départements"
            districtLabel.style.fontWeight = 'normal'; // Remove highlight from "Districts"
        }
        else {
            iframe.src = 'results/ISIBF_régions_burkina.html'; // Map by departments
            districtLabel.style.fontWeight = 'bold'; // Highlight "Districts"
            departmentLabel.style.fontWeight = 'normal'; // Remove highlight from "Départements"
        } 
    } else if (countrySelect === 'combined') {
        if (checkbox.checked) {
            iframe.src = 'results/ISIBF_régions_combined.html'; // Map by departments
            departmentLabel.style.fontWeight = 'bold'; // Highlight "Départements"
            districtLabel.style.fontWeight = 'normal'; // Remove highlight from "Districts"
        }
        else {
            iframe.src = 'results/ISIBF_pays_combined.html'; // Map by departments
            districtLabel.style.fontWeight = 'bold'; // Highlight "Districts"
            departmentLabel.style.fontWeight = 'normal'; // Remove highlight from "Départements"
        }
    } 

    // Dynamically change the labels based on country
    if (countrySelect === 'civ') {
        districtLabel.textContent = 'Districts'; // Change label for Côte d'Ivoire to "Districts"
        departmentLabel.textContent = 'Départements'; // Keep department label as "Départements"
    } else if (countrySelect === 'mali') {
        districtLabel.textContent = 'Régions'; // Update region label for Mali to "Cercles"
        departmentLabel.textContent = 'Cercles'; // Update department label for Mali to "Régions"
    } else if (countrySelect === 'combined') {
        districtLabel.textContent = 'Pays'; // Update region label for Mali
        departmentLabel.textContent = 'Régions'; // Update department label for Mali
    }    
}



let background_box = document.querySelector(".background_box");
    let toggle_box = document.querySelector(".toggle_box");
    let circle = document.querySelector(".circle");
    let checkbox = document.getElementById("checkbox");

    toggle_box.onclick = function(){
        if(checkbox.checked){
            circle.style.transform = "translateX(100px)";
        }else{
            circle.style.transform = "translateX(0px)";
        }
    }

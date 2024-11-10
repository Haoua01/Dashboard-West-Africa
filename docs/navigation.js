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

    // Activer le bouton par défaut pour 'map1'
    setActiveButton('map1');
    setActiveButton('chart3');

    // Charger la carte du Bénin dans map1 par défaut
    const iframe = document.getElementById('map-frame');
    iframe.src = 'results/ISIBF_benin.html'; // Carte par défaut pour le Bénin

    // Charger l'histogramme du Bénin dans chart3 par défaut
    const iframe2 = document.getElementById('chart-frame2');
    iframe2.src = 'results/demographic_indicator_benin.html'; // Histogramme par défaut pour le Bénin


});

// Fonction pour basculer l'affichage des cartes et des histogrammes
function toggleGroup1(showMapId) {
    // Masquer tous les éléments de group1
    const maps = document.querySelectorAll('.group1');
    maps.forEach(element => {
        element.style.display = 'none';
    });

    // Afficher la carte sélectionnée
    document.getElementById(showMapId).style.display = 'block';

    // Activer le bouton correspondant
    setActiveButton(showMapId);

    // Contrôle de la visibilité des dropdowns
    if (showMapId === 'map1') {
        document.getElementById('countryDropdown11').style.display = 'block'; // Afficher dropdown pour map1
        document.getElementById('countryDropdown12').style.display = 'none';  // Masquer dropdown pour map2
    } else if (showMapId === 'map2') {
        document.getElementById('countryDropdown11').style.display = 'none';  // Masquer dropdown pour map1
        document.getElementById('countryDropdown12').style.display = 'block'; // Afficher dropdown pour map2
        
        // Charger la carte par défaut dans map2
        const iframe = document.getElementById('map2-frame');
        iframe.src = 'results/ISIBF2_benin.html'; 
    }
}

function toggleGroup2(showMapId) {
    const charts = document.querySelectorAll('.group2');
    charts.forEach(element => {
        if (element.id !== showMapId) {
            element.style.display = 'none';
        }
    });
    
    // Afficher la carte ou l'histogramme sélectionné
    document.getElementById(showMapId).style.display = 'block';

    // Activer le bouton correspondant
    setActiveButton(showMapId);

    // Contrôle de la visibilité des dropdowns
    if (showMapId === 'chart3') {
        document.getElementById('countryDropdown21').style.display = 'block'; // Afficher dropdown pour chart3
    } else {
        document.getElementById('countryDropdown21').style.display = 'none'; // Masquer dropdown pour chart3
    }

    // Assurez-vous que map4 n'est affiché que lorsqu'il est explicitement sélectionné
    if (showMapId === 'map4') {
        document.getElementById('map4').style.display = 'block';
    }
}

// Fonction pour activer le style du bouton actif
function setActiveButton(activeId) {
    // Supprimer la classe active de tous les boutons
    const buttons = document.querySelectorAll('.toggle-buttons button');
    buttons.forEach(button => button.classList.remove('active'));

    // Ajouter la classe active au bouton correspondant à l'élément affiché
    const activeButton = Array.from(buttons).find(button => button.onclick.toString().includes(activeId));
    if (activeButton) {
        activeButton.classList.add('active');
    }
}

// Fonction pour mettre à jour la carte en fonction du pays sélectionné dans le premier menu déroulant
function showCountryMap1() {
    const countrySelect = document.getElementById('country-select11').value;
    const iframe = document.getElementById('map-frame');
    const toggleSwitch = document.getElementById('toggle-switch-civ');
 
    if (countrySelect === 'civ') {
        updateSliderValue();
        toggleSwitch.style.display = 'block';
    } else {
        // For other countries, load the default map
        iframe.src = `results/ISIBF_${countrySelect}.html`;
        toggleSwitch.style.display = 'none';
    }
}



// Fonction pour afficher le graphique de barres correspondant au pays sélectionné dans chart3
function showCountryChart() {
    const countrySelect2 = document.getElementById('country-select21').value;
    const iframe2 = document.getElementById('chart-frame2');
    iframe2.src = `results/demographic_indicator_${countrySelect2}.html`;
}


// Function to update the map based on toggle switch (checkbox) state
function updateSliderValue() {
    const iframe = document.getElementById('map-frame');
    const checkbox = document.getElementById('checkbox');
    const districtLabel = document.getElementById('district-label');
    const departmentLabel = document.getElementById('department-label');

    // Check if checkbox is checked (1 = "Par départements", 0 = "Par districts")
    if (checkbox.checked) {
        iframe.src = 'results/ISIBF_civ_departments.html'; // Map by departments
        departmentLabel.style.fontWeight = 'bold'; // Highlight "Départements"
        districtLabel.style.fontWeight = 'normal'; // Remove highlight from "Districts"
    } else {
        iframe.src = 'results/ISIBF_civ_districts.html'; // Map by districts
        districtLabel.style.fontWeight = 'bold'; // Highlight "Districts"
        departmentLabel.style.fontWeight = 'normal'; // Remove highlight from "Départements"
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

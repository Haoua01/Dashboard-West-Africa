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
function showCountryMap11() {
    const countrySelect = document.getElementById('country-select11').value;
    const iframe = document.getElementById('map-frame');

    if (countrySelect === 'civ') {
        // Carte spécifique pour la Côte d'Ivoire
        iframe.src = 'results/ISIBF_civ_districts.html';
    } else {
        iframe.src = `results/ISIBF_${countrySelect}.html`;
    }
}

// Fonction pour mettre à jour la carte en fonction du pays sélectionné dans le premier menu déroulant
function showCountryMap12() {
    const countrySelect = document.getElementById('country-select12').value;
    const iframe = document.getElementById('map-frame');

    if (countrySelect === 'civ') {
        // Carte spécifique pour la Côte d'Ivoire
        iframe.src = 'results/ISIBF_civ_departments.html';
    } else {
        iframe.src = `results/ISIBF_${countrySelect}.html`;
    }
}

// Fonction pour mettre à jour la carte en fonction du pays sélectionné dans le deuxième menu déroulant
function showCountryMap2() {
    const countrySelect = document.getElementById('country-select12').value;
    const iframe = document.getElementById('map2-frame');
    iframe.src = `results/ISIBF2_${countrySelect}.html`;
}

// Fonction pour afficher le graphique de barres correspondant au pays sélectionné dans chart3
function showCountryChart() {
    const countrySelect2 = document.getElementById('country-select21').value;
    const iframe2 = document.getElementById('chart-frame2');
    iframe2.src = `results/demographic_indicator_${countrySelect2}.html`;
}

// Function to toggle between "Régions" and "Départements" for Côte d'Ivoire
function toggleMapView() {
    const selectedCountry = document.getElementById('country-select11').value;
    const iframe = document.getElementById('map-frame');

    if (selectedCountry === 'civ') {
        var map1 = document.getElementById('map1');
        var regionsLabel = document.getElementById('left-label');
        var departementsLabel = document.getElementById('right-label');

        // Switch between regions and departments maps for Côte d'Ivoire
        if (document.getElementById('toggle-civ').checked) {
            map1.style.display = 'none';  // Hide regions map
            iframe.src = 'results/ISIBF_civ_departments.html'; // Show departments map
            regionsLabel.style.fontWeight = 'normal';
            departementsLabel.style.fontWeight = 'bold';
        } else {
            map1.style.display = 'block'; // Show regions map
            iframe.src = 'results/ISIBF_civ.html'; // Show regions map
            regionsLabel.style.fontWeight = 'bold';
            departementsLabel.style.fontWeight = 'normal';
        }
    }
}
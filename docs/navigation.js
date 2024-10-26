document.addEventListener("DOMContentLoaded", function() {
    // Afficher uniquement 'map1' de group1 au démarrage
    document.getElementById('map1').style.display = 'block'; // Afficher la première carte par défaut
    document.getElementById('countryDropdown').style.display = 'block'; // Afficher le menu déroulant associé

    // Masquer tous les éléments de group2 au démarrage
    const group2Elements = document.querySelectorAll('.group2');
    group2Elements.forEach(element => {
        element.style.display = 'none';
    });

    // Activer le bouton par défaut pour 'map1'
    setActiveButton('map1');

    // Charger la carte du Bénin dans map1 par défaut
    const iframe = document.getElementById('map-frame');
    iframe.src = 'isibf_benin.html'; // Carte par défaut pour le Bénin

    // Définir Bénin comme pays par défaut pour la deuxième cellule et afficher son histogramme
    document.getElementById('country-select2').value = 'benin';
    showCountryChart(); // Charger l'histogramme pour le Bénin par défaut
});

// Fonction pour basculer l'affichage des cartes et des histogrammes
function toggleMap(showMapId) {
    // Masquer tous les éléments de group1 et group2
    const mapsAndCharts = document.querySelectorAll('.map, .chart');
    mapsAndCharts.forEach(element => {
        element.style.display = 'none';
    });
    
    // Afficher la carte ou l'histogramme sélectionné
    document.getElementById(showMapId).style.display = 'block';

    // Activer le bouton correspondant
    setActiveButton(showMapId);

    // Contrôle de la visibilité des dropdowns
    if (showMapId === 'map1') {
        document.getElementById('countryDropdown').style.display = 'block';
        document.getElementById('countryDropdown2').style.display = 'none';
    } else if (showMapId === 'chart3') {
        document.getElementById('countryDropdown2').style.display = 'block';
        document.getElementById('countryDropdown').style.display = 'none';
    } else {
        document.getElementById('countryDropdown').style.display = 'none';
        document.getElementById('countryDropdown2').style.display = 'none';
    }

    // Assurez-vous que map4 n'est affiché que lorsqu'il est explicitement sélectionné
    if (showMapId === 'map4') {
        document.getElementById('map4').style.display = 'block';
    }
}

// Fonction pour activer le style du bouton actif
function setActiveButton(activeId) {
    const buttons = document.querySelectorAll('.toggle-buttons button');
    buttons.forEach(button => button.classList.remove('active'));

    const activeButton = document.querySelector(`.toggle-buttons button[onclick="toggleMap('${activeId}')"]`);
    if (activeButton) {
        activeButton.classList.add('active');
    }
}

// Fonction pour mettre à jour la carte en fonction du pays sélectionné dans le premier menu déroulant
function showCountryMap() {
    const countrySelect = document.getElementById('country-select').value;
    const iframe = document.getElementById('map-frame');
    iframe.src = `isibf_${countrySelect}.html`;
}

// Fonction pour afficher le graphique de barres correspondant au pays sélectionné dans chart3
function showCountryChart() {
    const countrySelect2 = document.getElementById('country-select2').value;
    const iframe2 = document.getElementById('chart-frame2');
    iframe2.src = `indicateur_demographique_${countrySelect2}.html`;
}

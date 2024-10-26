document.addEventListener("DOMContentLoaded", function() {
    // Afficher uniquement 'map1' de group1 au démarrage
    document.getElementById('map1').style.display = 'block';
    document.getElementById('countryDropdown').style.display = 'block';

    // Masquer tous les éléments de group2 au démarrage
    const group2Elements = document.querySelectorAll('.group2');
    group2Elements.forEach(element => {
        element.style.display = 'none';
    });

    // Activer le bouton par défaut pour 'map1'
    setActiveButton('map1');

    // Charger la carte du Bénin dans map1 par défaut
    const iframe = document.getElementById('map-frame');
    iframe.src = 'isibf_benin.html';
});

// Fonction pour basculer l'affichage des cartes dans le groupe 1
function toggleGroup1(showMapId) {
    // Masquer uniquement les éléments du groupe 1
    const group1Elements = document.querySelectorAll('.group1');
    group1Elements.forEach(element => {
        element.style.display = 'none';
    });

    // Afficher l'élément sélectionné dans le groupe 1
    document.getElementById(showMapId).style.display = 'block';
    setActiveButton(showMapId);

    // Contrôle de la visibilité du dropdown pour le groupe 1
    if (showMapId === 'map1') {
        document.getElementById('countryDropdown').style.display = 'block';
    } else {
        document.getElementById('countryDropdown').style.display = 'none';
    }
}

// Fonction pour basculer l'affichage des graphiques dans le groupe 2
function toggleGroup2(showMapId) {
    // Masquer uniquement les éléments du groupe 2
    const group2Elements = document.querySelectorAll('.group2');
    group2Elements.forEach(element => {
        element.style.display = 'none';
    });

    // Afficher l'élément sélectionné dans le groupe 2
    document.getElementById(showMapId).style.display = 'block';
    setActiveButton(showMapId);

    // Contrôle de la visibilité du dropdown pour le groupe 2
    if (showMapId === 'chart3') {
        document.getElementById('countryDropdown2').style.display = 'block';
    } else {
        document.getElementById('countryDropdown2').style.display = 'none';
    }
}

// Fonction pour activer le style du bouton actif
function setActiveButton(activeId) {
    const buttons = document.querySelectorAll('.toggle-buttons button');
    buttons.forEach(button => button.classList.remove('active'));

    const activeButton = document.querySelector(`.toggle-buttons button[onclick*="${activeId}"]`);
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

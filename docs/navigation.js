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

    const spinner = document.getElementById("loading-spinner-map");  // Spinner for the map
    spinner.style.display = "block";  // Show the spinner when the map starts loading
    // Charger la carte combiné dans map1 par défaut
    const iframe = document.getElementById('map-frame');

    const checkbox = document.getElementById('checkbox');
    const districtLabel = document.getElementById('region-label');
    const departmentLabel = document.getElementById('department-label');
    const toggleSwitch = document.getElementById('toggle-switch');

    iframe.src = 'results/ISIBF_pays_combined_leaflet.html'; // Carte par défaut
    districtLabel.textContent = 'Pays'; 
    departmentLabel.textContent = 'Régions'; 
    districtLabel.style.fontWeight = 'bold'; // Highlight "Districts"
    departmentLabel.style.fontWeight = 'normal'; // Remove highlight from "Départements"
    toggleSwitch.style.display = 'block'; // Masquer le bouton bascule par défaut
    iframe.onload = function() {
        spinner.style.display = "none";
    };

    // Charger l'histogramme su bénin dans chart3 par défaut
    const iframe2 = document.getElementById('chart-frame2');
    iframe2.src = 'results/demographic_indicator_région_benin_leaflet.html'; // Histogramme par défaut pour la Côte d'Ivoire


});

function toggleGroup1(showMapId) {
    const maps = document.querySelectorAll('.group1');
    maps.forEach(element => {
        if (element.id !== showMapId) {
            element.style.display = 'none';
        }
    });
    
    // Afficher la carte ou l'histogramme sélectionné
    document.getElementById(showMapId).style.display = 'block';

    // Contrôle de la visibilité des dropdowns
    if (showMapId === 'map1') {
        document.getElementById('countryDropdown11').style.display = 'block'; // Afficher dropdown pour map1
    } else {
        document.getElementById('countryDropdown11').style.display = 'none'; // Masquer dropdown pour map1
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


    // Contrôle de la visibilité des dropdowns
    if (showMapId === 'chart3') {
        document.getElementById('countryDropdown21').style.display = 'block'; // Afficher dropdown pour chart3
    } else {
        document.getElementById('countryDropdown21').style.display = 'none'; // Masquer dropdown pour chart3
    }

}
// Configuration mapping for each country
const countryMapConfig = {
    'benin': {
        maps: {
            byDepartment: 'results/ISIBF_commune_benin_leaflet.html',
            byDistrict: 'results/ISIBF_département_benin_leaflet.html'
        },
        labels: {
            department: 'Communes',
            district: 'Départements'
        }
    },
    'togo': {   
        maps: {
            byDepartment: 'results/ISIBF_préfecture_togo_leaflet.html',
            byDistrict: 'results/ISIBF_région_togo_leaflet.html'
        },
        labels: {
            department: 'Préfectures',
            district: 'Régions'
        }
    },
    'civ': {
        maps: {
            byDepartment: 'results/ISIBF_département_civ_leaflet.html',
            byDistrict: 'results/ISIBF_district_civ_leaflet.html'
        },
        labels: {
            department: 'Départements',
            district: 'Districts'
        }
    },
    'mali': {
        maps: {
            byDepartment: 'results/ISIBF_cercle_mali_leaflet.html',
            byDistrict: 'results/ISIBF_région_mali_leaflet.html'
        },
        labels: {
            department: 'Cercles',
            district: 'Régions'
        }
    },
    'burkina': {
        maps: {
            byDepartment: 'results/ISIBF_province_burkina_leaflet.html',
            byDistrict: 'results/ISIBF_région_burkina_leaflet.html'
        },
        labels: {
            department: 'Provinces',
            district: 'Régions'
        }
    },
    'guinee': {
        maps: {
            byDepartment: 'results/ISIBF_secteur_guinee_leaflet.html',
            byDistrict: 'results/ISIBF_région_guinee_leaflet.html'
        },
        labels: {
            department: 'Secteurs',
            district: 'Régions'
        }
    },
    'niger': {
        maps: {
            byDepartment: 'results/ISIBF_département_niger_leaflet.html',
            byDistrict: 'results/ISIBF_région_niger_leaflet.html'
        },
        labels: {
            department: 'Départements',
            district: 'Régions'
        }
    },
    'combined': {
        maps: {
            byDepartment: 'results/ISIBF_région_combined_leaflet.html',
            byDistrict: 'results/ISIBF_pays_combined_leaflet.html'
        },
        labels: {
            department: 'Régions',
            district: 'Pays'
        }
    }
};

// Function to update the map based on the selected country and checkbox
function updateSliderValue() {
    const countrySelect = document.getElementById('country-select11').value;
    const iframe = document.getElementById('map-frame');
    const checkbox = document.getElementById('checkbox');
    const districtLabel = document.getElementById('region-label');
    const departmentLabel = document.getElementById('department-label');
    const spinner = document.getElementById("loading-spinner-map");
    spinner.style.display = "block";  // Show the spinner when the map starts loading

    const config = countryMapConfig[countrySelect];

    if (config) {
        const mapSrc = checkbox.checked ? config.maps.byDepartment : config.maps.byDistrict;
        iframe.src = mapSrc;

        departmentLabel.style.fontWeight = checkbox.checked ? 'bold' : 'normal';
        districtLabel.style.fontWeight = checkbox.checked ? 'normal' : 'bold';

        departmentLabel.textContent = config.labels.department;
        districtLabel.textContent = config.labels.district;
    }

    // Simulate map loading process 
    iframe.onload = function() {
        spinner.style.display = "none";
    };
}

// Function to update the map based on the selected country from the first dropdown
function showCountryMap1() {
    const countrySelect = document.getElementById('country-select11').value;
    const iframe = document.getElementById('map-frame');
    const toggleSwitch = document.getElementById('toggle-switch');
    const spinner = document.getElementById("loading-spinner-map");

    spinner.style.display = "block";  // Show the spinner when the map starts loading

    const countriesWithToggle = ['benin', 'togo', 'civ', 'mali', 'burkina', 'guinee', 'niger', 'combined'];

    if (countriesWithToggle.includes(countrySelect)) {
        updateSliderValue();
        toggleSwitch.style.display = 'block';
    } else {
        iframe.src = `results/ISIBF_région_${countrySelect}_leaflet.html`;
        toggleSwitch.style.display = 'none';
    }

    // Simulate map loading process 
    iframe.onload = function() {
        spinner.style.display = "none";
    };
}

// Function to show the chart based on the selected country from chart3
function showCountryChart() {
    const countrySelect2 = document.getElementById('country-select21').value;
    const iframe2 = document.getElementById('chart-frame2');
    iframe2.src = `results/demographic_indicator_${countrySelect2 === 'civ' ? 'districts' : 'régions'}_${countrySelect2}.html`;
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

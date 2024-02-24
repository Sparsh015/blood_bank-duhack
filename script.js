import { Loader } from '@googlemaps/js-api-loader';
function initBloodBankMap() {

const apiOptions = {
     apiKey: "AIzaSyCGweoKd029a1h5ZVTQlppDH4L3EdhyngI"
}

const loader = new Loader(apiOptions);

loader.load().then(() => {
    console.log('Maps JS API Loaded');
});

    // Check if the Google Maps API key is provided
    if (!apiKey) {
        console.error('Google Maps API key is missing. Please provide a valid API key.');
        return;
    }

    // Load the Google Maps API with the provided API key
    var script = document.createElement('script');
    script.src = 'https://maps.googleapis.com/maps/api/js?key=' + apiKey + '&libraries=places&callback=initializeMap';
    document.body.appendChild(script);
}

// Callback function to initialize the map after the Google Maps API is loaded
function initializeMap() {
    // Set the map options
    var mapOptions = {
        center: { lat: -34.397, lng: 150.644 }, // Set the initial map center coordinates
        zoom: 8 // Set the initial zoom level
    };

    // Create a new Google Map instance
    var map = new google.maps.Map(document.getElementById('bloodBankMap'), mapOptions);
}

// Function to handle button click to find blood donation centers
function findBloodDonationCenters() {
    // Implement code to find and display blood donation centers on the map
}

// Remove the unnecessary functions and event listeners from the original script.js

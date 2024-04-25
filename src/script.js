console.log("JavaScript file connected and executing!");

function fetchWeatherData() {
    fetch(`http://127.0.0.1:5000/`)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        updateWeatherInfo(data);
    })
    .catch(error => {
        console.error('Error fetching weather data:', error);
    });
}

function updateWeatherInfo(weatherData) {
    // Skip setting the location value since it's not provided by the server
    document.getElementById('location-value').textContent = 'Auckland';
    document.getElementById('temperature-value').textContent = `${weatherData.temperature} °C`;
    document.getElementById('description-value').textContent = weatherData.description;
    document.getElementById('humidity-value').textContent = `${weatherData.humidity}%`;
    document.getElementById('wind-speed-value').textContent = `${weatherData.wind_speed} m/s`;

    // need to update the weather icon based on the weather description
    const weatherIcon = document.getElementById('weather-icon');
    const weatherDescription = weatherData.description.toLowerCase();

    if (weatherDescription.includes('rain')) {
        weatherIcon.className = 'fas fa-cloud-rain';
    } else if (weatherDescription.includes('cloud')) {
        weatherIcon.className = 'fas fa-cloud';
    } else if (weatherDescription.includes('sun')) {
        weatherIcon.className = 'fas fa-sun';
    } else if (weatherDescription.includes('wind')) {
        weatherIcon.className = 'fas fa-wind';
    } else {
        // Default icon
        weatherIcon.className = 'fas fa-question';
    }
}

fetchWeatherData();

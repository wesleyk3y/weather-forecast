function fetchWeatherData(location) {
    fetch(`/weather/${location}`)
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
    document.getElementById('location-value').textContent = weatherData.name;
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

fetchWeatherData('Auckland');
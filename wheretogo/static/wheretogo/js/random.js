
document.addEventListener("DOMContentLoaded", function() {
    const placesData = JSON.parse(document.getElementById('places-data').textContent);

    const btn = document.getElementById('btn-random');

    btn.addEventListener('click', function() {
        let totalWeight = 0;
        for (let i = 0; i < placesData.length; i++) {
            let weight = placesData[i].rating ? placesData[i].rating : 1;
            totalWeight += weight;

        }
        let randomNum = Math.random() * totalWeight;
        let currentSum = 0;
        let selectedPlace = null;

        for (let i = 0; i < placesData.length; i++) {
            let weight = placesData[i].rating ? placesData[i].rating : 1;
            currentSum += weight;
            if (randomNum <= currentSum) {
                selectedPlace = placesData[i];
                break;}}

        const resultDiv = document.getElementById('random-result')
        const ratingStars = selectedPlace.rating ? '⭐'.repeat(selectedPlace.rating) : 'N/A';

        resultDiv.innerHTML = `
            <div class="card border-info bg-dark text-light shadow-lg w-100" style="max-width: 400px;">
                <div class="card-body">
                    <a href="/place/${selectedPlace.id}/" class="text-info text-decoration-none">
                        <h4 class="card-title text-info mb-2">${selectedPlace.name}</h4>
                    </a>
                    <p class="card-text text-secondary mb-3">${selectedPlace.description || ''}</p>
                    <div class="small">
                        <div class="mb-1"><strong>Type:</strong> ${selectedPlace.type || 'N/A'}</div>
                        <div class="mb-1"><strong>Location:</strong> ${selectedPlace.location || 'Secret place👀'}</div>
                        <div><strong>Rating:</strong> <span class="text-warning">${ratingStars}</span></div>
                    </div>
                </div>
            </div>
        `;
    });
});
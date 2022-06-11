document.addEventListener('DOMContentLoaded', function (){
    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
        .then(response => response.json())
        .then(data => {
            const temperatura_maxima = data.data[0].tMax;
            const temperatura_minima = data.data[0].tMin;

            document.getElementById('temperatura_maxima').innerHTML = temperatura_maxima + 'ºC';
            document.getElementById('temperatura_minima').innerHTML = temperatura_minima + 'ºC';
        });
});
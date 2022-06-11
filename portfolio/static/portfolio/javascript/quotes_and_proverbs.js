const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '956545b6d1mshc60baf74e2245b9p199adajsn2c719607c9bb',
		'X-RapidAPI-Host': 'random-words5.p.rapidapi.com'
	}
};

fetch('https://random-words5.p.rapidapi.com/getMultipleRandom?count=5', options)
	.then(response => response.json())
	.then(data => {
        document.getElementById('palavra').innerHTML = data[0];
    })
	.catch(err => console.error(err));
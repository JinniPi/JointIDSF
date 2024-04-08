
const form = document.getElementById('news-form');


form.addEventListener('submit', async (event) => {

  event.preventDefault();


  const input = document.getElementById('news-text').value;

  try {
    const response = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({text: input}),
    });


    if (response.ok) {
      const result = await response.json();

      const prediction = result.prediction;
      const resultDiv = document.getElementById('prediction-result');
      console.log(prediction);
      console.log(result);

//     <label for="output">The result is: </label><textarea id="prediction-result" cols="40" rows="10"></textarea> <br><br>;
//      resultDiv.innerText = prediction === 0 ? 'The news is Real' : 'The news is Fake';
       resultDiv.innerText = prediction;


    } else {
      console.error('Request failed:', response.status);
    }
  } catch (error) {
    console.error('Request failed:', error);
  }
});

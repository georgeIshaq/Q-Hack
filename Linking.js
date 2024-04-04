// Capture the form submission event

function submitForm() {
  // Prevent the default form submission

  // Extract the user input
  var userInput = document.getElementById('field-2').value;
  console.log('User input:', userInput);

  // Send the user input to the backend
  fetch('http://localhost:5000/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({"user_input": userInput})
  })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch((error) => {
    console.error('Error:', error);
  });
}
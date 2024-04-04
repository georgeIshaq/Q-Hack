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
  .then(data => {
    var resDiv = document.createElement('div');
    resDiv.innerHTML = `<div class="uui-testimonial14_client">
                        <div class="uui-testimonial14_client-image-wrapper"><img src="images/Chara_1.webp" loading="lazy" alt="" sizes="48px" srcset="images/Chara_1Chara.webp 500w, images/Chara_1.webp 798w" class="uui-testimonial14_customer-image"></div>
                        <div class="uui-testimonial14_client-info">
                        <div class="uui-testimonial14_client-heading">Mathy Co</div>
                        <div class="uui-text-size-small-2">${data.response}</div>
                        </div>
                    </div>`;
    var block = document.getElementsByClassName('chatblock')
    block[0].appendChild(resDiv);
    if (data.image != null) {
        var image = document.createElement('img');
        image.src = `http://localhost:5000/image/${data.image}`;
        block[0].appendChild(image)
    }
})
  .catch((error) => {
    console.error('Error:', error);
  });

    // Create a new div element
    var newDiv = document.createElement('div');
    newDiv.setAttribute('id', 'Please God work')
    console.log('Data:', userInput)
    newDiv.innerHTML = `
                        <div class="uui-testimonial14_client">
                        <div class="uui-testimonial14_client-image-wrapper"><img src="images/Chara2_1.webp" loading="lazy" alt="" sizes="48px" srcset="images/Chara2_1Chara2.webp 500w, images/Chara2_1Chara2.webp 800w, images/Chara2_1.webp 859w" class="uui-testimonial14_customer-image"></div>
                        <div class="uui-testimonial14_client-info">
                            <div class="uui-testimonial14_client-heading">George</div>
                            <div class="uui-text-size-small-2">${userInput}</div>
                        </div>
                        </div>`;
    

    // Set the text received as the content of the new div
    // Append the new div to the document body
    var block = document.getElementsByClassName('chatblock')
    block[0].appendChild(newDiv);
}

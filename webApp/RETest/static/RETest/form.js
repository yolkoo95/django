document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#re_form').onsubmit = () => {
        // initialize a new request
        const request = new XMLHttpRequest();
        const re_input = document.querySelector('#re_input').value;
        const re_samples = document.querySelector('#re_samples').value;
        
        request.open('POST', '/RETest/api/checker');

        request.onload = () => {
            const data = JSON.parse(request.responseText);
            alert('received');
            if (!date) {
                document.querySelector('#re_results').innerHTML = data;
            } 
            else {
                alert("JsonError: fail to explain json file");
            }
        }

        // pack data

        const data = new FormData();
        data.append('re_input', re_input);
        data.append('re_samples', re_samples);

        request.send(data);

        return false;
    }
})

// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
    'use strict'
  
    window.addEventListener('load', function () {
      // Fetch all the forms we want to apply custom Bootstrap validation styles to
      var forms = document.getElementsByClassName('needs-validation')
  
      // Loop over them and prevent submission
      Array.prototype.filter.call(forms, function (form) {
        form.addEventListener('submit', function (event) {
          if (form.checkValidity() === false) {
            event.preventDefault()
            event.stopPropagation()
          }
          form.classList.add('was-validated')
        }, false)
      })
    }, false)
  }())
  
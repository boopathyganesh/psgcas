    // Show input error messages
    function showError(input, message) {
        const formControl = input.parentElement;
        formControl.className = 'form-group error';
        const small = formControl.querySelector('small');
        small.innerText = message;
    }
    function showErrorRadio(radioGroup) {
      //console.log(radioGroup);
      const formGroup = radioGroup[0].parentNode.parentNode.parentNode;
      formGroup.classList.add('error');
      const small = formGroup.querySelector('.radio-error');
      small.innerText = 'Select any one of the options';
    }
    
    // Show success color
    function showSuccess(input) {
        const formControl = input.parentElement;
        formControl.className = 'form-group success';
    }

    // Check if email is valid
    function checkEmail(inputs) {
      const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      let allValid = true;
      inputs.forEach(input => {
        if (re.test(input.value.trim())) {
          showSuccess(input);
        } else {
          showError(input, 'Email is invalid');
          allValid = false;
        }
      });
      return allValid;
    }
    

    // Check required fields
    function checkRequired(inputArr) {
        let sts = true
        inputArr.forEach(function(input) {
            if (input.value.trim() === '') {
                showError(input, `${getFieldName(input)} is required`);
                sts = false;
            } else {
                showSuccess(input);
            }
        });
        return sts;
    }

    function validateRadio(radioGroups) {
      //const radioGroups = document.querySelectorAll('.radiogrp');
      let sts = true;
      radioGroups.forEach(group => {
        const radios = group.querySelectorAll('input[type="radio"]');
        let isChecked = false;
        radios.forEach(radio => {
          if (radio.checked) {
            isChecked = true;
          }
        });
        const errorElement = group.querySelector('.radio-error');
        errorElement.textContent = "";
        if (!isChecked) {
          sts = false;
          errorElement.parentElement.classList.add('error');
          errorElement.textContent = 'Please select an option.';
        }
      });
      return sts;
    }
    
    // Get field name
    function getFieldName(input) {
        return input.id.charAt(0).toUpperCase() + input.id.slice(1);
    }

    // proceedButton.addEventListener('click', function(event) {
    //     event.preventDefault(); // Prevent the default button click behavior

    //     checkRequired([rollno, email, fname, con]);
    //     checkEmail(email);
    //     validateRadio(current_pursuing);

    //     // Perform additional form validation or submission logic
    // });

    function showAlert(target) {
      var alertMessage = document.createElement("div");
      alertMessage.classList.add("alert", "alert-danger", "alert-dismissible", "fade", "show");
      alertMessage.textContent = "This field can select values automatically. Please enter Reg.No & DOB again";
    
      // Create the close button
      var closeButton = document.createElement("button");
      closeButton.setAttribute("type", "button");
      closeButton.classList.add("close");
      closeButton.setAttribute("data-dismiss", "alert");
      closeButton.setAttribute("aria-label", "Close");
      closeButton.innerHTML = '<span aria-hidden="true">&times;</span>';
    
      // Append the close button to the alert message
      alertMessage.appendChild(closeButton);
      //console.log(target.nextElementSibling);
      var targetSibling =target.nextElementSibling;
      // Clear any existing content in the target element
      targetSibling.innerHTML = "";
    
      // Append the alert message to the target element
      targetSibling.appendChild(alertMessage);
    }
    
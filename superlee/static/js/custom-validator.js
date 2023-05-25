    // Show input error messages
    function showError(input, message) {
        const formControl = input.parentElement;
        formControl.className = 'form-group error';
        const small = formControl.querySelector('small');
        small.innerText = message;
    }
    function showErrorRadio(radioGroup) {
      console.log(radioGroup);
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
    //datepicker
    function validateDate(input) {
      var sts = false;
      var old = new Date('1975-01-01');
      input.addEventListener("blur", function() {    
        // Get the date of birth value and convert it to a Date object
        var dob = new Date(this.value);
        var val = this.value
        console.log("$", this.value);
        // Check if the date of birth is in the future
        var ageDiffMs = Date.now() - dob.getTime();
        var ageDate = new Date(ageDiffMs);
        var age = Math.abs(ageDate.getUTCFullYear() - 1970);
    
        if (dob.getTime() > Date.now()) {
          // If it is, clear the age field and return
          document.getElementById("age").value = "";
          sts = false;
          Swal.fire({
            icon: 'error',
            title: 'Error in Date of Birth',
            text: "I Think you are not born Yet!",
            showConfirmButton: false,
            timer: 3500
          })
        }
    
        if (dob.getTime() < old.getTime()) {
          // If it is, clear the age field and return
          sts = false;
          document.getElementById("age").value = "";
          Swal.fire({
            icon: 'error',
            title: 'Error in Date of Birth',
            text: "I Think you are aged for this registration",
            showConfirmButton: false,
            timer: 3500
          })
        }
    
        // Calculate the age based on the current date and the date of birth
        var ageDiffMs = Date.now() - dob.getTime();
        var ageDate = new Date(ageDiffMs);
        var age = Math.abs(ageDate.getUTCFullYear() - 1970);
        // Set the value of the age field
        document.getElementById("age").value = age;
    
        // Check if the date of birth field is empty
        if (input.value === "") {
          // If the date of birth field is empty, set sts to false
          sts = false;
          Swal.fire({
            icon: 'error',
            title: 'Error in Date of Birth',
            text: "Please enter your date of birth",
            showConfirmButton: false,
            timer: 3500
          })
        }
      });
    
      return val;
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
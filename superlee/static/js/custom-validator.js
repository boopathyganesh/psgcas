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
    // function checkEmail(inputs) {
    //   const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    //   let allValid = true;
    //   inputs.forEach(input => {
    //     if (re.test(input.value.trim())) {
    //       showSuccess(input);
    //     } else {
    //       showError(input, 'Email is invalid');
    //       allValid = false;
    //     }
    //   });
    //   return allValid;
    // }
    function checkEmail(inputs) {
      const validDomains = ['gmail.com', 'psgcas.ac.in', 'outlook.com'];
      const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,})$/;
      let allValid = true;
      
      inputs.forEach(input => {
        const email = input.value.trim();
        const domain = email.substring(email.lastIndexOf('@') + 1);
        
        if (re.test(email) && validDomains.includes(domain)) {
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


    // function handleFileUpload(event, index,errorFields) {
    //   const file = event.target.files[0];
    //   var isValid = true;
    //   // Validate file extension
    //   const allowedExtensions = ['.pdf'];
    //   const fileExtension = getFileExtension(file.name);
    //   console.log(fileExtension);
    //   if (!allowedExtensions.includes(fileExtension)) {
    //     errorFields[index].textContent = 'Invalid file extension. Allowed extension is .pdf';
    //     isValid = false;
    //     return;
    //   }
    
    //   // Validate file size
    //   const maxSizeInBytes = 10 * 1024 * 1024; // 10MB
    //   if (file.size > maxSizeInBytes) {
    //     errorFields[index].textContent = 'File size exceeds the limit. Maximum allowed size is 10MB.';
    //     isValid = false;
    //     return;
    //   }
    
    //   // Proceed with file upload
    //   // ...
    // return isValid;
    // }
    
    // function getFileExtension(filename) {
    //   return '.' + filename.split('.').pop();
    // }

    function fileValidation(fileInputs){
      fileInputs.forEach(function(fileInput) {

        const fileError = fileInput.parentElement.querySelector('.file-error');
        const fileGrp = fileInput.parentElement;
        fileInput.addEventListener('change', function() {
          console.log(fileGrp)
          const file = fileInput.files[0];
          if (file) {
            const fileType = file.type;
            if (fileType !== 'application/pdf') {
              fileGrp.classList.add('error')
              fileError.textContent = 'Please select a PDF file.';
              console.log(fileInput.value);
              fileInput.value = ''; // Clear the file input

            } else {
              fileError.textContent = ''; // Clear the error message
            }
          } else {
            fileGrp.classList.add('error')
            fileError.textContent = 'Please select a file.';
          }
        });
      });
    }

    function isFileEmpty(fileInputs) {
      //var fileInputs = document.getElementsByClassName('fileInput');
      var isValid = true;
      for (var i = 0; i < fileInputs.length; i++) {
        var fileInput = fileInputs[i];
        var file = fileInput.value;
        console.log(fileInput.value);
        const fileError = fileInput.parentElement.querySelector('.file-error');
        const fileGrp = fileInput.parentElement;
        if (!fileInput || !file) {
          //alert('Please select a file to upload.');
          fileGrp.classList.add('error')
          fileError.textContent = 'Please select the file!';
          isValid =  false;
        }
        
        if (file.size === 0) {
          //alert('Selected file is empty.');
          fileGrp.classList.add('error')
          fileError.textContent = 'File is invalid! Choose another file';
          isValid = false;
        }
      }
      
      return isValid;
    }

    function validateContactFields(contactFields) {
      let isValid = true;
    
      for (let i = 0; i < contactFields.length; i++) {
        const contactField = contactFields[i];
        const contact = contactField.value.trim();
        const regex = /^\d{10}$/; // Matches exactly 10 digits
        console.log(contact);
        if (regex.test(contact)) {
          showSuccess(contactField);
        } else {
          isValid = false;
          showError(contactField, "Contact number is invalid");
        }
      }
    
      return isValid;
    }
    
    function formatter(input) {
      input.addEventListener('input', (event) => {
        let { value } = event.target;
        value = value.replace(/[\s.-]/g, ''); // Remove spaces, dots, and hyphens
        value = value.slice(0, 12); // Restrict the total number of characters to 12
        value = value.replace(/\./g, '#'); // Replace dots with the desired symbol
        event.target.value = value;
        console.log("$", value);
      });
    }
    
    function modifyPasswordField(passwordField) {
      const modifiedPassword = passwordField.value.split('.').join('#'); // Replace '.' with the desired symbol
      passwordField.value = modifiedPassword;
    
      passwordField.addEventListener('input', () => {
        modifyPasswordField(passwordField);
      });
    }
    
    
    function isNumber(input) {
      var value = input.value;
      var num = /^\d+$/.test(value);
      
      if (num) {
        showSuccess(input);
      } else {
        showError(input, 'Invalid Aadhar Number');
      }
      
      return isValid;
    }
    



    
    
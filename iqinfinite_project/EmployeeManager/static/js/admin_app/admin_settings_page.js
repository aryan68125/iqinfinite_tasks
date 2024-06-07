$('body').ready(function(){
    console.log("admin settings page js ready!!")
    fetchProfilePicture()
})

// GET CSRF TOKEN FROM THE BROWSER'S COOCKIE STARTS
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
// GET CSRF TOKEN FROM THE BROWSER'S COOCKIE ENDS

// ADMIN CHANGE PROFILE PICTURE STARTS

// upload image (starts)
$(document).ready(function() {
    // Trigger the file input when the select button is clicked
    $('#select_profile_picture_button').on('click', function() {
        $('#profile_picture_input').click();
    });

    // Handle the file upload when the upload button is clicked
    $('#upload_profile_pic_admin').on('click', function() {
        var fileInput = $('#profile_picture_input')[0];
        if (fileInput.files.length > 0) {
            var formData = new FormData();
            formData.append('profile_picture', fileInput.files[0]);

            fetch(UploadAdminProfilePictureView_url, {
                method: 'PATCH',
                headers: {
                    'X-CSRFToken': getCookie("csrftoken")
                },
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.status == 200) {
                    fetchProfilePicture()
                    Swal.fire({
                        position: "top-end",
                        icon: "success",
                        title: data.msg,
                        showConfirmButton: false,
                        timer: 1500
                    });
                } else {
                    var error_msg = data.error;
                    Swal.fire({
                        position: "top-end",
                        icon: "error",
                        title: error_msg,
                        showConfirmButton: false,
                        timer: 1500
                    });
                }
            })
            .catch(error => {
                console.error('Error:', error);
                Swal.fire({
                    position: "top-end",
                    icon: "error",
                    title: 'An error occurred while uploading the profile picture.',
                    showConfirmButton: false,
                    timer: 1500
                });
            });
        } else {
            Swal.fire({
                position: "top-end",
                icon: "warning",
                title: 'Please select a file to upload.',
                showConfirmButton: false,
                timer: 1500
            });
        }
    });
});
// upload image (ends)

// get image (starts)
function fetchProfilePicture() {
    console.log("fetchProfilePicture function called")
    fetch(GetAdminProfilePictureView_url)  // Replace with your actual back-end URL
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.status === 200) {
            const imageUrl = data.data.profile_picture;
            document.getElementById('admin_profile_pic').src = imageUrl;
        } else {
            console.error('Failed to load image:', data);
        }
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}
// get image (ends)

// ADMIN CHANGE PROFILE PICTURE ENDS

// ADMIN INFO RELATED UI LOGIC STARTS
$(document).on('click','#save_admin_updated_info_button',function(){
      console.log("save_admin_updated_info_button clicked!") 
      get_admin_info_from_form() 
})
function get_admin_info_from_form(){
    console.log("get_admin_info_from_form function called")
    var first_name = $('#first_name_admin_settings_form').val()
    var last_name  = $('#last_name_admin_settings_form').val()
    var email      = $('#email_admin_settings_form').val()
    var data={
        first_name : first_name,
        last_name : last_name,
        email : email
    }
    console.log(data)
    fetch(
        ChangeAdminInfoView_url,{
            method:'PATCH',
            headers:{
                Accept:'application/json',
                'Content-Type':'application/json',
                'X-CSRFToken':getCookie("csrftoken")
            },
            body:JSON.stringify(data)
        }
    ).then(response=>response.json())
    .then(data=>{
        if(data.status == 200){
            reset_admin_info_form()
            msg = data.msg
            Swal.fire({
                position: "top-end",
                icon: "success",
                title: msg,
                showConfirmButton: false,
                timer: 1500
            });
        }
        else{
            error_msg = data.error
            Swal.fire({
                position: "top-end",
                icon: "error",
                title: error_msg,
                showConfirmButton: false,
                timer: 1500
            });
        }
    })
}
function reset_admin_info_form(){
    $('#first_name_admin_settings_form').val("")
    $('#last_name_admin_settings_form').val("")
    $('#email_admin_settings_form').val("")
}
$(document).ready(function(){
    get_admin_username()
})
function get_admin_username(){
    console.log("get_admin_username function called")
    fetch(
        GetAdminUsernameView_url,{
            method:'GET',
            headers:{
                Accept:'application/json',
                'Content-Type':'application/json',
                'X-CSRFToken':getCookie("csrftoken")
            }
        }
    ).then(response=>response.json())
    .then(data=>{
        if(data.status==200){
            console.log("get_admin_username : ",data)
            $('#username_admin_settings_form').val(data.username)
            $('#admin_user_id').text(data.user_id)
        }
        else{
            error_msg = data.error
            Swal.fire({
                position: "top-end",
                icon: "error",
                title: error_msg,
                showConfirmButton: false,
                timer: 1500
            });
        }
    })
}
// ADMIN INFO RELATED UI LOGIC ENDS

//ADMIN PASSWORD CHANGE RELATED UI LOGIC STARTS
$(document).on('click','#save_admin_updated_password_button',function(){
      console.log("save_admin_updated_password_button clicked!")  
      get_passwords_from_the_form()
})
function get_passwords_from_the_form(){
    console.log("get_passwords_from_the_form function called")
    var password = $('#password_admin_settings_form').val()
    var password2 = $('#password2_admin_settings_form').val()
    var user_id = $('#admin_user_id').text()
    var data = {
        user_id:user_id,
        password:password,
        password2:password2
    }
    console.log(data)
    fetch(
        ChangeAdminPasswordView_url,{
            method:'PATCH',
            headers:{
                Accept:'application/json',
                'Content-Type':'application/json',
                'X-CSRFToken':getCookie("csrftoken")
            },
            body:JSON.stringify(data)
        }
    ).then(response=>response.json())
    .then(data=>{
        if(data.status==200){
            reset_password_form()
            msg = data.msg
            Swal.fire({
                position: "top-end",
                icon: "success",
                title: msg,
                showConfirmButton: false,
                timer: 1500
            });
        }
        else{
            msg = data.error
            Swal.fire({
                position: "top-end",
                icon: "error",
                title: msg,
                showConfirmButton: false,
                timer: 1500
            });
        }
    })
}
function reset_password_form(){
    console.log("reset_password_form called")
    $('#password_admin_settings_form').val("")
    $('#password2_admin_settings_form').val("")
}
//ADMIN PASSWORD CHANGE RELATED UI LOGIC ENDS
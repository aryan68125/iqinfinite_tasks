$('body').ready(function(){
    console.log("This is manage_user_page js ")
    $('#Add_Users_UI').empty()
    $('#Verify_otp_ui').empty()
    $('#update_user_ui').empty()
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

// >>>>>>>>>>Add users STARTS<<<<<<<<<<<<<<
$('body').on('click','#add_users',function(){
    if ($('#Verify_otp_ui').is(':empty')) {
        console.log('Verify_otp_ui is empty.');
        $('#update_user_ui').empty()
        show_add_users_related_content()
    } else {
        console.log('Verify_otp_ui is not empty.');
        error_msg = "First verify otp before trying to add another user"
        Swal.fire({
            position: "top-end",
            icon: "error",
            title: error_msg,
            showConfirmButton: false,
            timer: 1500
          });
    }
    
    get_user_role_from_db()
})
function show_add_users_related_content(){
    console.log("Add users related content")
    // TODO generate the entire html form to add users here 
    $('#Add_Users_UI').empty()
    $('#Add_Users_UI').append(
        `
        <div class="card my-1">
            <div class="card-body">
                <div class="title_bar_options_card_body_inner_div">
                    <div><h5>Add Users</h5></div>
                </div>
                <div class="row">
                    <div class="col-sm-12 col-md-4 col-lg-3">
                        <div class="mb-3">
                            <label for="user_name" class="form-label">User Name</label>
                            <input type="text" class="form-control" id="user_name" aria-describedby="username">
                        </div>
                    </div>
                    <div class="col-sm-12 col-md-4 col-lg-3">
                        <div class="mb-3">
                            <label for="email" class="form-label">Email address</label>
                            <input type="email" class="form-control" id="email" aria-describedby="emailHelp">
                            <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                        </div>
                    </div>
                    <div class="col-sm-12 col-md-4 col-lg-3">
                        <div class="mb-3">
                            <label for="password1" class="form-label">Password</label>
                            <input type="password" class="form-control" id="password1">
                        </div>
                    </div>
                    <div class="col-sm-12 col-md-4 col-lg-3">
                        <div class="mb-3">
                            <label for="password2" class="form-label">Re-type Password</label>
                            <input type="password" class="form-control" id="password2">
                        </div>        
                    </div>
                    <div class="col-sm-12 col-md-4 col-lg-3">
                        <div class="mb-3">
                            <select class="form-group mx-2" style="width:97%" id="role">
                                <!--Render the options using javascript -->
                            </select>
                        </div>
                    </div>
                    <div class="col-sm-12 col-md-4 col-lg-3">
                        <button type="button" class="btn btn-dark" id="sign_up">Add User</button>
                    </div>
                </div>
            </div>
        </div>
        `
    )
}

//GET DATA OF THE USER FROM THE FORM AND SEND IT TO THE BACKEND STARTS
$('body').on('click','#sign_up' ,function(){
    collect_form_data()
})
function collect_form_data(){
    var username = $('#user_name').val()
    var email = $('#email').val()
    var role = $('#role').val()
    var password = $('#password1').val()
    var password2 = $('#password2').val()
    var data = {
        username:username,
        email:email,
        role:role,
        password:password,
        password2:password2
    }
    console.log(data)
    fetch(
        register_user_url,{
            method:'POST',
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
            reset_form()
            Swal.fire({
                position: "top-end",
                icon: "success",
                title: data.msg,
                showConfirmButton: false,
                timer: 1500,
              });
            //   window.location.href=verify_otp_page_url //change here 
            //display verify otp ui when the status returns 200
            display_verify_otp_ui()
            $('#Add_Users_UI').empty()
        }
        else{
            console.log(data)
            console.log(data.error)
            var error_msg = data.error
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
//GET DATA OF THE USER FROM THE FORM AND SEND IT TO THE BACKEND ENDS

//DISPLAY VERIFY OTP UI AND VERIFY OTP LOGIC STARTS
function display_verify_otp_ui(){
    $('#Verify_otp_ui').empty()
    $('#Verify_otp_ui').append(`
        <div class="card w-50">
            <div class="card-body">
                <div><h3 class="verify_otp">Verify OTP</h3></div>
                <div class="mb-3">
                    <label for="otp" class="form-label">Enter OTP</label>
                    <input type="text" class="form-control" id="otp" aria-describedby="otp">
                </div>
                <div class="w-100 display_flex_style_button">
                    <div class="mx-1">
                        <button type="submit" class="btn btn-dark" id="verify_button">Verify</button>
                    </div>
                    <div class="mx-1">
                        <button type="submit" class="btn btn-dark" id="resend_otp">Re-send OTP</button>
                    </div>
                </div>
            </div>
        </div>
    `)
}

//GET FORM DATA STARTS
$('body').on('click','#verify_button', function(){
    get_form_data()
})
function get_form_data(){
    var otp = $('#otp').val()
    var data = {
        'otp':otp,
    }
    //FETCH API STARTS
    fetch(
        VerifyOTPResendOTP_url,{
            method:'POST',
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
            Swal.fire({
                position: "top-end",
                icon: "success",
                title: data.msg,
                showConfirmButton: false,
                timer: 1500,
              });
            //reset form 
            //redirect user to login page
            // window.location.href=login_page_url
            //hide the verify otp ui when status 200
            $('#Verify_otp_ui').empty()
            show_add_users_related_content()
            get_user_role_from_db()
        }
        else{
            //show validation errors handled in backend here
            //show other types of  exceptions here
            var error_msg = data.error
            Swal.fire({
                position: "top-end",
                icon: "error",
                title: error_msg,
                showConfirmButton: false,
                timer: 1500
              });
        }
    })
    //FETCH API ENDS
}
//GET FORM DATA ENDS

//RESEND OTP STARTS
$('body').on('click','#resend_otp',function(){
    resend_otp()
})
function resend_otp(){
    //reset form
    reset_form()
    //resend otp via fetch
    fetch(
        VerifyOTPResendOTP_url,{
            method:'GET',
            headers:{
                Accept:'application/json',
                'Content-Type':'application/json',
                'X-CSRFToken':getCookie("csrftoken")
            }
        }
    ).then(response=>response.json())
    .then(data=>{
        if (data.status==200){
            $('#Verify_otp_ui').empty()
            Swal.fire({
                position: "top-end",
                icon: "success",
                title: data.msg,
                showConfirmButton: false,
                timer: 1500,
              });
        }
        else{
            var error_msg = data.error
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
function reset_form(){
    $('#otp').val("")
}
//RESEND OTP ENDS
//DISPLAY VERIFY OTP UI AND VERIFY OTP LOGIC ENDS

//GET DATA ABOUT USER ROLES FROM THE BACKEND AND SHOW IT IN THE DROP-DOWN STARTS
function get_user_role_from_db(){
    fetch(read_user_role_url,{
        method : 'GET',
        headers : {
            Accept:'application/json',
            'Content-Type':'application/json',
            'X-CSRFToken':getCookie("csrftoken")
        },
    }).then(response=>response.json())
    .then(data=>{
        if (data.status==200){
            console.log(data)
            console.log(data.data)
            $('#role').append(`
            <option value="default">--SELECT ROLE--</option>
            `)
            for(i=0;i<data.data.length;i++){
                // console.log(data.data[i])
                // console.log(data.data[i].id)
                // console.log(data.data[i].role_name)
                dropdown_options(data.data[i].id,data.data[i].role_name)
            }
        }
        else{
            var error_msg = data.error
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

// create the options in the dropdown dynamically STARTS
function dropdown_options(id,role_name){
    $('#role').append(`
    <option value="${id}">${role_name}</option>
    `)
}
// create the options in the dropdown dynamically ENDS

//GET DATA ABOUT USER ROLES FROM THE BACKEND AND SHOW IT IN THE DROP-DOWN ENDS

// RESET FORM STARTS
function reset_form(){
    $('#user_name').val("")
    $('#email').val("")
    $('#role').val("default")
    $('#password1').val("")
    $('#password2').val("")
}
// RESET FORM ENDS

// >>>>>>>Add users ENDS<<<<<<<<<<<<






// Update users STARTS
$('body').on('click','#update_users',function(){
    if ($('#Verify_otp_ui').is(':empty')) {
        console.log('Verify_otp_ui is empty.');
        $('#Add_Users_UI').empty()
        show_update_users_related_content()
        get_all_users_from_db()
    } else {
        console.log('Verify_otp_ui is not empty.');
        error_msg = "First verify otp before trying to update user"
        Swal.fire({
            position: "top-end",
            icon: "error",
            title: error_msg,
            showConfirmButton: false,
            timer: 1500
          });
    }
})
function get_all_users_from_db(){
    fetch(
        GetAllUsers_url,{
            method:'GET',
            headers:{
                Accept:'application/json',
                'Content-Type':'accplication/json',
                'X-CSRFToken':getCookie("csrftoken")
            }
        }
    ).then(response=>response.json())
    .then(data=>{
        if(data.status==200){
            console.log(data.data)
            console.log(data.data[0].user_profile.role_name)
            $('#usersTable').DataTable({
                data: data.data,
                columns: [
                    { title: 'User ID', data: 'id' },
                    { title: 'User Name', data: 'username' },
                    { title: 'Email', data: 'email' },
                    { title: 'Role Name', data: 'user_profile.role_name' },
                    { title: 'Created By', data: 'user_profile.created_by' },
                    { title: 'Updated By', data: 'user_profile.updated_by' },
                    { title: 'Is Deleted', data: 'user_profile.is_deleted' },
                    { title: 'Is Blocked', data: 'user_profile.is_blocked' },
                    { title: 'Created At', data: 'user_profile.created_at' },
                    { title: 'Updated At', data: 'user_profile.updated_at' }
                ]
            });
        }
        else{
            error_msg = "data.error"
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
function show_update_users_related_content(){
    console.log("Update users related content")

    $('#update_user_ui').empty()
    $('#update_user_ui').append(
        `
            <div class="card">
                <div class="card-body">
                  <div>
                     <table id="usersTable"></table>
                  </div>
                </div>
            </div>
        `
    )
}
// Update users ENDS
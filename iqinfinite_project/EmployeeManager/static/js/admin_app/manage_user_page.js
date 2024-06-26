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
        console.log('Verify_otp_ui is empty');
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
            $('#Add_Users_UI').empty()
            display_verify_otp_ui()
            Swal.fire({
                position: "top-end",
                icon: "success",
                title: data.msg,
                showConfirmButton: false,
                timer: 1500,
              });
            //   window.location.href=verify_otp_page_url //change here 
            //display verify otp ui when the status returns 200
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
                <div>
                    <button type="button" class="btn btn-dark" id="verify_button_1">Verify</button>
                    <button type="button" class="btn btn-dark" id="resend_otp_1">resend otp</button>
                    <div class="mt-5">
                        <button type="button" class="btn btn-light" id="resend_otp"></button>
                    </div>
                </div>
            </div>
        </div>
    `)
}
// 
$('body').on('click','#verify_button_1',function(){
    console.log("verify_button_1 clicked")
    get_form_data();
})
$('body').on('click','#resend_otp_1',function(){
    console.log("resend_otp_1 clicked")
    resend_otp()
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
            // $('#Verify_otp_ui').empty()
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






// >>>>>>>>>>>>>>>>Update users STARTS<<<<<<<<<<<<<<<<<<<<<<
function generate_update_user_UI()
{
    $('#Add_Users_UI').empty()
    show_update_users_related_content()
    get_all_users_from_db()
    //populate the role_selector drop down menu
    get_all_user_roles_update_user_form() 
}
$('body').on('click','#update_users',function(){
    if ($('#Verify_otp_ui').is(':empty')) {
        console.log('Verify_otp_ui is empty.');
        generate_update_user_UI()
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
            console.log("GET ALL users")
            destroyDataTable()
            $('#usersTable').DataTable({
                data: data.data,
                columns: [
                    { title: 'User ID', data: 'id' },
                    { title: 'User Name', data: 'username' },
                    { title: 'Email', data: 'email' },
                    { title: 'Role Name', data: 'user_profile.role_name' },
                    { title: 'Created By', data: 'user_profile.created_by.username' },
                    { title: 'Updated By', data: 'user_profile.updated_by.username' },
                    {
                        title: 'Is Deleted',
                        data: 'user_profile.is_deleted',
                        render: function(data, type, row) {
                            if (data == true) {
                                return '<button class="btn btn-light border border-dark userDeleteButton"><i class="text-primary fa-solid fa-trash-can-arrow-up"></i></button>';
                            } else {
                                return '<button class="btn btn-light border border-dark userDeleteButton"><i class="text-danger fa-solid fa-trash"></i></button>';
                            }
                        }
                    },
                    { 
                        title: 'Is Active', 
                        data: 'user_profile.is_active',
                        render: function(data, type, row) {
                            if (data == true) {
                                return '<button class="btn btn-light border border-dark userActiveButton"><i class="text-success fa-solid fa-check"></i></button>';
                            } else {
                                return '<button class="btn btn-light border border-dark userActiveButton"><i class="text-danger fa-solid fa-xmark"></i></button>';
                            }
                        }
                    },
                    { title: 'Created At', data: 'user_profile.created_at' },
                    { title: 'Updated At', data: 'user_profile.updated_at' }
                ],
                responsive: true // Enable responsiveness
            });

            // CLICK EVENT LISTENER ON BUTTONS IN DATA_TABALE STARTS TESTING >>
            // userActiveButton()
            // userDeleteButton()
            // data_table_row_click_event_handler()
            // data_table_row_long_click_event_handler()
            data_table_row_double_click_event_handler()
            // CLICK EVENT LISTENER ON BUTTONS IN DATA_TABALE ENDS TESTING >>
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

// CLICK EVENT LISTENER ON BUTTONS IN DATA_TABALE STARTS 
//event listner function for is_active
function userActiveButton(){
    // Add event listener for is_active button clicks STARTS
    $('#usersTable').on('click', '.userActiveButton', function() {
        var table = $('#usersTable').DataTable();
        var data = table.row($(this).closest('tr')).data();
        var userId = data.id;
        console.log('is_active column User ID:', userId);
        var data = {
            user_pk:userId
        }
        fetch(
            SetUserIsActive_url,{
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
                $('#Add_Users_UI').empty()
                $('#update_user_ui').empty()
                show_update_users_related_content()
                if ($.fn.DataTable.isDataTable('#usersTable')) {
                    $('#usersTable').DataTable().clear().destroy();
                }
                // get_all_users_from_db()'
                // refreshDataTable() //EXPERIMENTAL
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
    });
    // Add event listener for is_active button clicks ENDS
}

//event listner function for is_deleted
function userDeleteButton(){
    // Add event listener for is_deleted button clicks STARTS
    $('#usersTable').on('click', '.userDeleteButton', function() {
        var table = $('#usersTable').DataTable();
        var data = table.row($(this).closest('tr')).data();
        var userId = data.id;
        console.log('is_deleted column User ID:', userId);
        var data = {
            user_pk:userId
        }
        fetch(
            SetUserIsDeleted_url,{
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
                $('#Add_Users_UI').empty()
                $('#update_user_ui').empty()
                show_update_users_related_content()
                if ($.fn.DataTable.isDataTable('#usersTable')) {
                    $('#usersTable').DataTable().clear().destroy();
                }
                // get_all_users_from_db()
                // refreshDataTable() //EXPERIMENTAL
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
    });
    // Add event listener for is_deleted button clicks ENDS
}

//ADD a LONG CLICK event on each row of the DataTable STARTS (ARCHIVE DO NOT DELETE)
// function handleRowLongClick(row) {
//     var table = $('#usersTable').DataTable();
//     var data = table.row(row).data();
//     var userId = data.id;
//     console.log('Long click User ID:', userId);
//     // Perform desired action on long click
//     fetch(
//         `/admin_app/api/GetOneUser/${userId}/`,
//         {
//             method:'GET',
//             headers:{
//                 Accept:'application/json',
//                 'Content-Type':'application/json',
//                 'X-CSRFToken':getCookie("csrftoken")
//             },
//         }
//     ).then(response=>response.json())
//     .then(data=>{
//         if(data.status==200){
//             // if status==200
//             $('#user_data_table_card').hide()
//             $('#user_update_form_card').show()
//             check_user_update_form_card_hidden()
//             console.log(data)
//             var user_id = data.data.id
//             var username = data.data.username
//             var first_name = data.data.first_name
//             var last_name = data.data.last_name
//             var email = data.data.email
//             var user_role_id = data.data.user_profile.role
//             // console.log(user_id)

//             // populate the form in user_update_form_card 
//             //show user id and username in here using text span_user_id_user_name
//             set_user_data_into_the_update_user_form(user_id, username, first_name, last_name, email,user_role_id) // This function populate the form 
//             //populate the role_selector drop down menu
//             get_all_user_roles_update_user_form()
//         }
//         else{
//             error_msg = data.error
//             Swal.fire({
//                 position: "top-end",
//                 icon: "error",
//                 title: error_msg,
//                 showConfirmButton: false,
//                 timer: 1500
//             });
//         }
//     })
// }

// var timer;
// var longClickDuration = 1500; // 1.5 second
// function data_table_row_long_click_event_handler(){
//     $('#usersTable tbody').on('mousedown', 'tr', function() {
//         var that = this;
//         timer = setTimeout(function() {
//             handleRowLongClick(that);
//         }, longClickDuration);
//     });
// }
//ADD a LONG CLICK event on each row of the DataTable ENDS (ARCHIVE DO NOT DELETE)

// Add click event listener to rows STARTS   (ARCHIVE NOTE DO NOT DELETE)
// function data_table_row_click_event_handler(){
    
//     $('#usersTable tbody').on('click', 'tr', function() {
//         var table = $('#usersTable').DataTable();
//         $('#usersTable tbody tr').css('background-color', '');

//         // Add the background color to the clicked row
//         $(this).css('background-color', 'lightgrey');

//         var data = table.row(this).data();
//         var userId = data.id;

//         //get on user from DB via api call
//         console.log('Row click User ID :', data)

//         fetch(
//             `/admin_app/api/GetOneUser/${userId}/`,
//             {
//                 method:'GET',
//                 headers:{
//                     Accept:'application/json',
//                     'Content-Type':'application/json',
//                     'X-CSRFToken':getCookie("csrftoken")
//                 },
//             }
//         ).then(response=>response.json())
//         .then(data=>{
//             if(data.status==200){
//                 // if status==200
//                 $('#user_data_table_card').hide()
//                 $('#user_update_form_card').show()
//                 check_user_update_form_card_hidden()
//                 console.log(data)
//                 var user_id = data.data.id
//                 var username = data.data.username
//                 var first_name = data.data.first_name
//                 var last_name = data.data.last_name
//                 var email = data.data.email
//                 var user_role_id = data.data.user_profile.role
//                 // console.log(user_id)

//                 // populate the form in user_update_form_card 
//                 //show user id and username in here using text span_user_id_user_name
//                 set_user_data_into_the_update_user_form(user_id, username, first_name, last_name, email,user_role_id) // This function populate the form 
//                 //populate the role_selector drop down menu
//                 get_all_user_roles_update_user_form()
//             }
//             else{
//                 error_msg = data.error
//                 Swal.fire({
//                     position: "top-end",
//                     icon: "error",
//                     title: error_msg,
//                     showConfirmButton: false,
//                     timer: 1500
//                 });
//             }
//         })
        
//     });
    
// }
// Add click event listener to rows ENDS   (ARCHIVE NOTE DO NOT DELETE)

// Add DOUBLE click event listener to rows STARTS   
function data_table_row_double_click_event_handler(){
    
    $('#usersTable tbody').on('dblclick', 'tr', function() {
        var table = $('#usersTable').DataTable();
        $('#usersTable tbody tr').css('background-color', '');

        // Add the background color to the clicked row
        $(this).css('background-color', 'lightgrey');

        var data = table.row(this).data();
        var userId = data.id;

        //get on user from DB via api call
        console.log('Row click User ID :', data)

        fetch(
            `/admin_app/api/GetOneUser/${userId}/`,
            {
                method:'GET',
                headers:{
                    Accept:'application/json',
                    'Content-Type':'application/json',
                    'X-CSRFToken':getCookie("csrftoken")
                },
            }
        ).then(response=>response.json())
        .then(data=>{
            if(data.status==200){
                // if status==200
                $('#user_data_table_card').hide()
                $('#user_update_form_card').show()
                check_user_update_form_card_hidden()
                console.log(data)
                var user_id = data.data.id
                var username = data.data.username
                var first_name = data.data.first_name
                var last_name = data.data.last_name
                var email = data.data.email
                var user_role_id = data.data.user_profile.role
                var user_is_active = data.data.user_profile.is_active
                var user_is_deleted = data.data.user_profile.is_deleted
                // console.log(user_role_id)

                // populate the form in user_update_form_card 
                //populate the role_selector drop down menu
                // get_all_user_roles_update_user_form() //---> FIX THIS BAWASEER HERE
                //show user id and username in here using text span_user_id_user_name
                set_user_data_into_the_update_user_form(user_id, username, first_name, last_name, email, user_role_id, user_is_active, user_is_deleted) // This function populate the form 
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
        
    });
    
}
// Add DOUBLE click event listener to rows ENDS 

// CLICK EVENT LISTENER ON BUTTONS IN DATA_TABALE ENDS 

function show_update_users_related_content(){
    console.log("Update users related content")

    $('#update_user_ui').empty()
    $('#update_user_ui').append(
        `
            <div class="card" id="user_data_table_card">
                <div class="card-body">
                  <div>
                    <h5>User Data:</h5>
                  </div>
                  <div>
                     <table id="usersTable"></table>
                  </div>
                </div>
            </div>

            <div class="card user_update_form_card" id="user_update_form_card">
                <div class="card-body">
                    <div class="my-3" style="display:flex">
                        <button class="btn btn-dark mx-2" id="user_update_form_back_button"><i class="fa-solid fa-arrow-left"></i></button>
                        <h5 class="mx-2">Update User: <span id="span_user_id_user_name"></span></h5>
                    </div>
                    <div class="my-3">
                        <div class="row">
                            <div class="col-sm-12 col-md-4 col-lg-3">
                                <div class="mb-3">
                                    <label for="username" class="form-label">Username:</label>
                                    <input type="text" class="form-control" id="username" aria-describedby="emailHelp">
                                </div>
                            </div>
                            <div class="col-sm-12 col-md-4 col-lg-3">
                                <div class="mb-3">
                                    <label for="first_name" class="form-label">First Name:</label>
                                    <input type="text" class="form-control" id="first_name" aria-describedby="emailHelp">
                                </div>
                            </div>
                            <div class="col-sm-12 col-md-4 col-lg-3">
                                <div class="mb-3">
                                    <label for="last_name" class="form-label">Last Name:</label>
                                    <input type="text" class="form-control" id="last_name" aria-describedby="emailHelp">
                                </div>
                            </div>
                            <div class="col-sm-12 col-md-4 col-lg-3">
                                <div class="mb-3">
                                    <label for="email" class="form-label">Email</label>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp">
                                </div>
                            </div>
                            <div class="col-sm-12 col-md-4 col-lg-3">
                                <div class="mb-3 mt-1">
                                    <select class="form-group mx-2 mt-4" style="width:97%; height:40px;" id="role_user_update_form_dropdown">
                                        <!--Render the options using javascript -->
                                    </select>
                                </div>
                            </div>
                            <div class="col-sm-12 col-md-4 col-lg-3">
                                <div class="mb-3 mt-4" style="display:flex">
                                    <div class="mx-1 mt-3">
                                        <label for="delete_user" class="form-label">Delete User</label>
                                        <input type="checkbox" id="delete_user" class="mx-3"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-12 col-md-4 col-lg-3">
                                <div class="mb-5" style="display:flex;">
                                    <!--save user data button-->
                                    <button class="btn btn-dark mx-2 mt-2" id="update_user_data_button">Save changes</button>
                                </div>
                            </div>
                        </div>
                    </div>

                    
                    <div id="change_user_password_section">
                        <div class="card">
                            <div class="card-body">
                                <div class="mb-3">
                                    <h5>Change Password</h5>
                                </div>
                                <div style="display:flex">
                                    <div class="mb-3 mx-2">
                                        <label for="password" class="form-label">Password</label>
                                        <input type="password" class="form-control" id="password">
                                    </div>
                                    <div class="mb-3 mx-2">
                                        <label for="password2" class="form-label">Confirm Password</label>
                                        <input type="password" class="form-control" id="password2">
                                    </div>
                                    <div class="mb-3 mx-2 mt-4">
                                        <button class="btn btn-dark mt-2" id="change_password">Save Changes</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `
    )
    $('#user_update_form_card').hide()
    update_form_button_click_event_listener()
    check_user_update_form_card_hidden()
}

// UPDATE FORM CLICK EVENT LISTENER STARTS
function update_form_button_click_event_listener()
{
        //LOGIC FOR THE BACK BUTTON #user_update_form_back_button STARTS
        $('body').on('click','#user_update_form_back_button',function(){
            //this function resets form and hide the form and shows the data_table 
            reset_form_and_go_back_function()
        })
        //LOGIC FOR THE BACK BUTTON #user_update_form_back_button ENDS
        //LOGIC to add click event listener for save changes with the id = update_user_data_button button STARTS
        $('body').on('click','#update_user_data_button',function(){
            console.log("#update_user_data_button saved changes clicked")
            get_user_data_from_update_user_form()
            reset_form_and_go_back_function()
        })
        //LOGIC to add click event listener for save changes with the id = update_user_data_button button ENDS

        $('body').on('click','#change_password',function(){
            console.log("#change_password button clicked")
            //CHANGE PASSWORD
            change_password_get_form_data()
            change_password_reset_form()
        })

}
// UPDATE FORM CLICK EVENT LISTENER ENDS

//Check if the Update user form exists on the screen or not {user_update_form_card} STARTS
function check_user_update_form_card_hidden(){
    if ($('#user_update_form_card').is(':hidden')) {
        // The element with ID 'user_update_form_card' is hidden
        console.log('The user_update_form_card is hidden');
    } else {
        // The element with ID 'user_update_form_card' is visible
        console.log('The user_update_form_card is visible');
        
        //apply backend logic for the user update form here if the form exist

    }
}

//GET THE VALUES FROM THE UPDATE USER DATA FORM STARTS 
function extractNumberFromString(str) {
    // Use regular expression to match the number in the string
    var match = str.match(/\(UID: (\d+) \/ Username:/);
    if (match && match[1]) {
        return parseInt(match[1], 10);
    }
    return null; // Return null if no match is found
}
function get_user_data_from_update_user_form(){
    //collect all data from the form
    var inputString = $('#span_user_id_user_name').text()
    var user_id = extractNumberFromString(inputString);
    var username = $('#username').val()
    var first_name = $('#first_name').val()
    var last_name = $('#last_name').val()
    var email = $('#email').val()
    var role_id = $('#role_user_update_form_dropdown').val()
    if ($('#delete_user').is(":checked"))
        {
          var is_deleted = true
        }
    else{
        var is_deleted = false
    }

    var data = {
        user_id:user_id,
        username:username,
        first_name:first_name,
        last_name:last_name,
        email:email,
        role_id:role_id,
        is_deleted:is_deleted
    }
    console.log("get_user_data_from_the_form :",data)
    if (inputString){
        fetch(
            UpdateUser_url,{
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
                console.log(data)
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
}
// Function to refresh the DataTable
function refreshDataTable() {
    // Destroy the existing DataTable instance
    if ($.fn.DataTable.isDataTable('#usersTable')) {
        $('#usersTable').DataTable().clear().destroy();
    }

    // Fetch and reinitialize the DataTable
    get_all_users_from_db();
}
//Function destroy table
function destroyDataTable() {
    // Destroy the existing DataTable instance
    if ($.fn.DataTable.isDataTable('#usersTable')) {
        $('#usersTable').DataTable().clear().destroy();
    }
}
function reset_form_and_go_back_function(){
    $('#user_update_form_card').hide()
    $('#user_data_table_card').show()
    $('#span_user_id_user_name').text("")
    $('#username').val("")
    $('#first_name').val("")
    $('#last_name').val("")
    $('#email').val("")
    $("#delete_user").prop("checked", false);
    $('#role_user_update_form_dropdown').val("default")
    refreshDataTable() // EXPERIMENTAL
}
//GET THE VALUES FROM THE UPDATE USER DATA FORM ENDS 

//CALL THIS FUNCTION WHEN TABLE ROW IS CLICKED : SET THE VALUES IN THE UPDATE USER FORM STARTS
function set_user_data_into_the_update_user_form(user_id, username_, first_name_, last_name_, email_, user_role_id_, user_is_active, user_is_deleted){
    var set_title = `(UID: ${user_id} / Username: ${username_})`
    $('#span_user_id_user_name').text(set_title)
    $('#username').val(username_)
    $('#first_name').val(first_name_)
    $('#last_name').val(last_name_)
    $('#email').val(email_)
    if (user_is_deleted == true){
        console.log("user_is_deleted :: ",user_is_deleted)
        $("#delete_user").prop("checked", true);
    }
    if(user_is_deleted == false){
        console.log("user_is_deleted :: ",user_is_deleted)
        $("#delete_user").prop("checked", false);
    }

    console.log("set_user_data_into_the_update_user_form role id : ",  user_role_id_) //DEBUGGING

    $('#role_user_update_form_dropdown').val(user_role_id_); 
}
//CALL THIS FUNCTION WHEN TABLE ROW IS CLICKED : SET THE VALUES IN THE UPDATE USER FORM ENDS
//call the api that fetches all the user roles
function get_all_user_roles_update_user_form(){
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
            console.log("get_all_user_roles_update_user_form : ",data)
            // console.log(data.data)
            $('#role_user_update_form_dropdown').empty()
            $('#role_user_update_form_dropdown').append(`
            <option value="default">--SELECT ROLE--</option>
            `)
            for(i=0;i<data.data.length;i++){
                console.log("render the options in the role select dropdown count : ",i )
                render_options_for_role_user_update_form_dropdown(data.data[i].id,data.data[i].role_name)
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
function render_options_for_role_user_update_form_dropdown(role_id,role_name){
    console.log("render_options_for_role_user_update_form_dropdown id :: value :-", role_id,role_name)
    $('#role_user_update_form_dropdown').append(`
        <option value="${role_id}">${role_name}</option>
    `)
}
//Check if the Update user form exists on the screen or not {user_update_form_card} ENDS

//CHNAGE PASSWORD FUNCTIONS STARTS
function change_password_get_form_data(){
    var inputString = $('#span_user_id_user_name').text()
    var user_id = extractNumberFromString(inputString);
    var  password  = $('#password').val()
    var  password2 = $('#password2').val()
    var data = {
        user_id:user_id,
        password:password,
        password2:password2
    }
    fetch(
        ChangeUserPassword_url,{
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
            var msg = data.msg
            change_password_reset_form()
            Swal.fire({
                position: "top-end",
                icon: "success",
                title: msg,
                showConfirmButton: false,
                timer: 1500
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
function change_password_reset_form(){
    $('#password').val("")
    $('#password2').val("")
}
//CHNAGE PASSWORD FUNCTIONS ENDS
// >>>>>>>>>>>>>>>>>>>>>>Update users ENDS<<<<<<<<<<<<<<<<<<<<<<<<<












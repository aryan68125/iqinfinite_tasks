$('body').ready(function(){
    console.log('Register user page javascript is here')
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
              window.location.href=verify_otp_page_url
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

//GET DATA ABOUT USER ROLES FROM THE BACKEND AND SHOW IT IN THE DROP-DOWN STARTS
$('body').ready(function(){
    get_user_role_from_db()
})
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
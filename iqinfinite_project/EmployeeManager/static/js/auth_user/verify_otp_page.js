$('body').ready(function(){
    console.log("This is verify otp js")
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
            window.location.href=login_page_url
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
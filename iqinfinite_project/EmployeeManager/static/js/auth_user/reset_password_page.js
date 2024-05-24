$('body').ready(function(){
    console.log("Reset password page JS ready!!")
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

function get_form_data(){
    var password = $('#password').val()
    var password2 = $('#password2').val()
    var data = {
        password:password,
        password2:password2
    }
    fetch(
        url,{
            method:'POST',
            headers:{
                Accept:'application/json',
                'Content-Type':'application/json',
                'X-CRFToken':getCookie("csrftoken")
            },
            body:JSON.stringify(data)
        }
    ).then(response=>response.json())
    .then(data=>{
        if (data.status==200){
            var msg = data.msg
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
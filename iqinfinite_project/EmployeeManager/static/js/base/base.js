$('body').ready(function(){
    console.log("Base js is active")
    $('#user_id').hide()
    display_user_data()
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

$('body').on('click','#signout',function(){
    logout()
})
function logout(){
    fetch(logout_url,{
        method:'GET',
        headers:{
            Accept:'application/json',
            'Content-Type':'application/json',
            'X-CERFToken':getCookie("cerftoken"),
        }
    }).then(response=>response.json())
    .then(data=>{
        if(data.status==200){
            //logout user
            console.log(data)
            window.location.href=login_page_url
        }
        else{
            //something went wrong
        }
    })
}
function display_user_data(){
    user_data = $('#user_id').text()
    console.log(user_data)
    data = {
        user_id:user_data,
    }
    fetch(
        HomeLoginTester_url,{
            method:'GET',
            headers:{
                Accept:'application/json',
                'Content-Type':'application/json',
                'X-CEFToken':getCookie("csrftoken")
            }
        }
    ).then(response=>response.json())
    .then(data=>{
        if (data.status==200){
            console.log(data.user_data)
            console.log(data.user_data.username)
            console.log(data.user_data.email)
            console.log(data.user_data.user_role)
            set_user_name(data.user_data.username, data.user_data.user_role)
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
function set_user_name(username, user_role){

    $('#logged_in_user_name').append(`
    <p class="mt-1 mx-1">${username}</p>
    <p class="mt-1 mx-1">(${user_role})</p>
    `)
}
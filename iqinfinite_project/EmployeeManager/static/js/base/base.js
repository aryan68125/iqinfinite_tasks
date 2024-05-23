$('body').ready(function(){
    console.log("Base js is active")
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
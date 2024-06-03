$('body').ready(function(){
    console.log("admin_assign_user page js ready")
    // $('#Assign_Hr_to_Manager_UI_container').empty()
    $('#Assign_Employee_to_Hr_UI_container').empty()
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

/* Assign_Hr_to_Manager_UI_container RELATED UI LOGIC STARTS */
$('body').on('click','#Assign_Hr_to_Manager_ui_show_button',function(){
    console.log("Assign_Hr_to_Manager_ui_show_button clicked")
    console.log("Assign_Hr_to_Manager_UI_container UI destroyed")
    $('#Assign_Hr_to_Manager_UI_container').empty()
    console.log("Assign_Employee_to_Hr_UI_container UI destroyed")
    $('#Assign_Employee_to_Hr_UI_container').empty()
    Assign_Hr_to_Manager_UI_container_function()
})
function Assign_Hr_to_Manager_UI_container_function(){
    console.log("Assign_Hr_to_Manager_UI_container_function called")
    console.log("Assign_Hr_to_Manager_UI_container rendered")
    $('#Assign_Hr_to_Manager_UI_container').append(
        `
        <div class="card" id="manager_data_table_card">
            <div class="card-body">
                <div>
                  <h5>Manager Data:</h5>
                </div>
                <div>
                   <table id="ManagerTable"></table>
                </div>
            </div>
        </div>
        `
    )
}
function get_all_managers(){
    console.log("get_all_managers function called")
    console.log("fectch api call to get all managers")
    fetch(
        url,{
            method:'GET',
            headers:{
                Accept:'application/json',
                'Content-Type':'application/json',
                'X-CSRFToken':getCookie("csrftoken")
            }
        }
    ).then(response = response.json())
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
/* Assign_Hr_to_Manager_UI_container RELATED UI LOGIC ENDS */

/* Assign_Employee_to_Hr_UI_container RELATED UI LOGIC STARTS */
$('body').on('click','#Assign_Employee_to_Hr_ui_show_button',function(){
    console.log("Assign_Employee_to_Hr_ui_show_button clicked")
    console.log("Assign_Hr_to_Manager_UI_container UI destroyed")
    $('#Assign_Hr_to_Manager_UI_container').empty()
    console.log("Assign_Employee_to_Hr_UI_container UI destroyed")
    $('#Assign_Employee_to_Hr_UI_container').empty()
    Assign_Employee_to_Hr_UI_container_function()
})
function Assign_Employee_to_Hr_UI_container_function(){
    console.log("Assign_Employee_to_Hr_UI_container_function called")
    console.log("Assign_Employee_to_Hr_UI_container rendered")
    $('#Assign_Employee_to_Hr_UI_container').append(
        `
        <div class="card">
            <div class="card-body">
                UI related to assign employee to hr
            </div>
        </div>
        `
    )
}
/* Assign_Employee_to_Hr_UI_container RELATED UI LOGIC ENDS */
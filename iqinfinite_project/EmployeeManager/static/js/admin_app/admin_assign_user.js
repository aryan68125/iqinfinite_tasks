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
    get_all_managers()
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
    console.log("fetch api call to get all managers")
    fetch(
        GetAllManagersListView_url,{
            method:'GET',
            headers:{
                Accept:'application/json',
                'Content-Type':'application/json',
                'X-CSRFToken':getCookie("csrftoken")
            }
        }
    ).then(response => response.json())
    .then(data=>{
        console.log("get_all_managers function api call result : ",data)
        ManagerTable_destroy_data_table()
        console.log("Create ManagerTable DataTable")
        $('#ManagerTable').DataTable({
            data:data,
            columns:[
                {title:'User ID', data:'id'},
                { title: 'User Name', data: 'username' },
                { title: 'Email', data: 'email' },
                { title: 'Role Name', data: 'user_profile.role_name' },
                { title: 'Created By', data: 'user_profile.created_by.username' },
                { title: 'Updated By', data: 'user_profile.updated_by.username' },
                { title: 'Created At', data: 'user_profile.created_at' },
                { title: 'Updated At', data: 'user_profile.updated_at' }
            ],
            responsive: true // Enable responsiveness
        })

        ManagerTable_data_table_row_double_click_event_handler()
    })
}
function ManagerTable_destroy_data_table(){
    console.log("destroy ManagerTable DataTable")
    if ($.fn.DataTable.isDataTable('#ManagerTable')) {
        $('#ManagerTable').DataTable().clear().destroy();
    }
}
function ManagerTable_data_table_row_double_click_event_handler(){
    console.log("ManagerTable_data_table_row_double_click_event_handler function called")
    console.log("Attched the click event handler to ManagerTable")

    $('#ManagerTable tbody').on('dblclick', 'tr', function() {
        var table = $('#ManagerTable').DataTable();
        $('#ManagerTable tbody tr').css('background-color', '');

        // Add the background color to the clicked row
        $(this).css('background-color', 'lightgrey');

        var data = table.row(this).data();
        var userId = data.id;
        var username = data.username
        var role = data.user_profile.role_name

        //get on user from DB via api call
        console.log('ManagerTable Row click User ID :', data)

        //render a form
        render_form_to_assign_hr(userId, username, role)
    });
}
function render_form_to_assign_hr(userId, username, role){
    console.log("render_form_to_assign_hr function called");
    console.log("Assign_Hr_to_Manager_UI_container UI destroyed that contained ManagerTable")
    $('#Assign_Hr_to_Manager_UI_container').empty()
    ManagerTable_destroy_data_table()
    get_all_hr()
    $('#Assign_Hr_to_Manager_UI_container').append(
        `
        <div class="card" id="manager_data_table_card">
            <div class="card-body">
                <div style="display:flex">
                    <button class="btn btn-dark mx-2" id="assign_hr_to_manager_form_back_button"><i class="fa-solid fa-arrow-left"></i></button>
                    <h5>Assign Hr to: <span id="selected_manager_data">(userId : ${userId} | username : ${username} | role : ${role})</span></h5>
                </div>
                <div>
                    <table id="HrTable"></table>
                </div>
                <div>
                    <button class="btn btn-dark" id="assign_user">Assign</button>
                </div>
            </div>
        </div>
        `
    )
    assign_hr_to_manager_form_back_button_function()
    assign_user_button_click_event_handler()
}
function assign_hr_to_manager_form_back_button_function(){
    console.log("assign_hr_to_manager_form_back_button_function called")
    console.log("Attched the click event handler to assign_hr_to_manager_form_back_button")
    $('body').on('click','#assign_hr_to_manager_form_back_button',function(){
        console.log("Assign_Hr_to_Manager_UI_container UI destroy that contained HrTable")
        $('#Assign_Hr_to_Manager_UI_container').empty()
        HrTable_destroy_data_table()
        Assign_Hr_to_Manager_UI_container_function()
    })
}
function HrTable_destroy_data_table(){
    console.log("destroy HrTable DataTable")
    if ($.fn.DataTable.isDataTable('#HrTable')) {
        $('#HrTable').DataTable().clear().destroy();
    }
}
function assign_user_button_click_event_handler(){
    console.log("assign_user_button_click_event_handler called")
    $('body').on('click','#assign_user',function(){
        console.log("#assign_user button clicked")
        get_selected_hrs_from_table()
    })
}
function get_all_hr(){
    console.log("get_all_hr function called")
    console.log("fetch api call to get all hrs")
    fetch(
        GetAllHrListView_url,{
            method:'GET',
            headers:{
                Accept: 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie("csrftoken")
            }
        }
    ).then(response=>response.json())
    .then(data=>{
        console.log("get_all_hr function api call result : ",data)
        HrTable_destroy_data_table()
        console.log("Create HrTable DataTable")
        $('#HrTable').DataTable({
            data:data,
            columns:[
                {title:'User ID', data:'id'},
                { title: 'User Name', data: 'username' },
                { title: 'Email', data: 'email' },
                { title: 'Role Name', data: 'user_profile.role_name' },
                { title: 'Created By', data: 'user_profile.created_by.username' },
                { title: 'Updated By', data: 'user_profile.updated_by.username' },
                { title: 'Created At', data: 'user_profile.created_at' },
                { title: 'Updated At', data: 'user_profile.updated_at' },
                { title: 'Working under', data: 'user_profile.superior.username' }
            ],
            responsive: true // Enable responsiveness
        })
        HrTable_row_click_event_handler()
    })
}
// Add click event listener to rows STARTS   (ARCHIVE NOTE DO NOT DELETE)
var selected_hrs = []
function HrTable_row_click_event_handler(){
    console.log("HrTable_row_click_event_handler function called")
    console.log("selected_hrs array initialized")
    $('#HrTable tbody').on('click', 'tr', function() {
        var table = $('#HrTable').DataTable();
        $('#HrTable tbody tr').css('background-color', '');

        // Add the background color to the clicked row
        // $(this).css('background-color', 'lightgrey');

        var data = table.row(this).data();

        //get on user from DB via api call
        //check if username is in database
        console.log('HrTable_row_click_event_handler Row click User ID :', data)
        var index = selected_hrs.findIndex(function(hr) {
            return hr.username === data.username;
        });

        if (index === -1) {
            selected_hrs.push(data);
            console.log("selected_hrs array :: added user to the array");
            console.log("selected_hrs array elements : ", selected_hrs);
        } else {
            selected_hrs.splice(index, 1);
            console.log("selected_hrs array :: removed user from the array");
            console.log("selected_hrs array elements : ", selected_hrs);
        }

        // Add background color to rows of DataTable based on selected_hrs
        $('#HrTable tbody tr').each(function() {
            var rowData = table.row(this).data();
            var username = rowData.username;
            if (selected_hrs.some(function(hr) { return hr.username === username; })) {
                $(this).css('background-color', '#a2a8d3');
            }
        });
    });
}
function extractUserId() {
    console.log("extractUserId function called")
    // Get the text from the span element
    var managerDataText = $('#selected_manager_data').text();

    // Use a regular expression to extract the userId
    var userIdMatch = managerDataText.match(/userId\s*:\s*([^\s|]+)/);

    // If the userId is found, return it, otherwise return null or an appropriate message
    if (userIdMatch && userIdMatch.length > 1) {
        return userIdMatch[1];
    } else {
        return null; // or you can return a message like "UserId not found"
    }
}
function get_selected_hrs_from_table(){
    console.log("get_selected_hrs_from_table function called")
    if(selected_hrs.length>0){
        var user_id = extractUserId()
        var data = {
            user_id:user_id,
            selected_hrs:selected_hrs
        }
        console.log("get_selected_hrs_from_table : making the fetch api-call to send the data to the backend")
        fetch(
            AssignHrToManagerView_url,{
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
                error_msg = data.msg
                Swal.fire({
                    position: "top-end",
                    icon: "success",
                    title: error_msg,
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
}
// Add click event listener to rows ENDS   (ARCHIVE NOTE DO NOT DELETE)
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
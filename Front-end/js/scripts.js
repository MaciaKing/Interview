// https://startbootstrap.com/previews/bare


/**
 * This function is called when the page is loaded.
 * It sends a request to the server to get all the heroes.
 * */
window.addEventListener('DOMContentLoaded', event => {
    getAllHeros();
});


/**
 * This function is called when the data is received from the server
 * It creates a table with the data received from the server
 * The table is created using the DataTables library.
 * 
 * @param {*} data  data received from the server in the form of a JSON string
 */
function showAllHeros(data) {
    const json = JSON.parse(data);
    const contentDiv = document.getElementById('content');
    const table = document.createElement('table');
    contentDiv.appendChild(table);
    $(table).DataTable({
        data: json,
        columns: [
            { data: 'id', title:"ID" },
            { data: 'name', title: "Name" },
            //{ data: 'description', },
            { data: 'n_comics', title: "Appearance in comics" },
            { data: 'n_series', title: "Appearance in series" },
            {
                data: 'thumbnail', render: function (data, type, row) {
                    return '<img src="' + data + '" width="100" height="100" />';
                }, title: "Image"
            }
        ]
    });
}

/**
 * This function is called when the page is loaded.
 * It sends a request to the server to get all the heroes.
 * The server responds with a JSON string containing all the heroes.
 * The function showAllHeros() is called to create a table with the data received from the server.
 * 
 * @param {*} data  data received from the server in the form of a JSON string.
 * */
function getAllHeros() {
    jQuery.ajax({
        type: 'POST',
        url: '../Backend/php/reciver.php',
        data: {
            dat: "getHeroes"
        },
        success: function (data) {
            showAllHeros(data);
        },
        error: function (xhr, status, error) {
            var err = eval("(" + xhr.responseText + ")");
            alert(err.Message);
        }
    });
}
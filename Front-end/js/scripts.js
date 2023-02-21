// https://startbootstrap.com/previews/bare

/*!
* Start Bootstrap - Bare v5.0.7 (https://startbootstrap.com/template/bare)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-bare/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


window.addEventListener('DOMContentLoaded', event => {
    getAllHeros();
});

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
function onSearchSuccess( response ) {
    for( var i = 0; i < response.CatalogEntryView.length; i++ ) {
        var item = response.CatalogEntryView[i];
        var proText = "";
        var conText = "";
         // get the #1 pro
        $.ajax({
            url : "products/" + item.partNumber + "/gettoppros=1",
            success : function (data) {
                if( data == "" )
                {
                    return;
                }
                data = JSON.parse(data);
                proText = data[0].message;
            },
            async : false
        });
        // get the #1 con
        $.ajax({
            url : "products/" + item.partNumber + "/gettopcons=1",
            success : function (data) {
                if( data == "" )
                {
                    return;
                }
                data = JSON.parse(data);
                conText = data[0].message;
            },
            async : false
        });

        if (proText === "") {
            proText = "Be the first to add a pro!";
        }
        if (conText === "") { 
            conText = "Be the first to add a con!";
        }
        $("#search-results-table > tbody:last").append("<tr><td><img width='100' height='100' src='" + item.fullImage + "' />" + "</td><td class='vert-align'><a href='/products/" + item.partNumber + "'>" + item.title + '</a><br /><span class="glyphicon glyphicon-ok"></span> : ' + proText + '<br /><span class="glyphicon glyphicon-remove"></span> : ' + conText + "</td></tr>");
    }
    
    $("#search-results-table").fadeIn();
}

function onSearchError( response ) {
    $("#search-results-table").fadeIn();
}

function executeSearch() {
    $("#search-results-table > tbody").empty();
    
    $("#search-results-table").fadeOut();
    
    $.ajax({
        url : "https://api.target.com/v2/products/search?searchTerm=" +
        $("#search-query").val() +
        "&key=J5PsS2XGuqCnkdQq0Let6RSfvU7oyPwF",
        success : onSearchSuccess,
        error : onSearchError,
        async : true
    });
}

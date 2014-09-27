function onSearchSuccess( response ) {
    for( var i = 0; i < response.CatalogEntryView.length; i++ ) {
        var item = response.CatalogEntryView[i];
        var proText = "";
        var conText = "";
        $.ajax({    // get the #1 pro
            url : "products/" + item.partNumber + "/gettoppros=1",
            success : function (data) {
                proText = data.message
            },
            error : function () {},
            async : true
        });
        $.ajax({    // get the #1 con
            url : "products/" + item.partNumber + "/gettopcons=1",
            success : function (data) {
                conText = data.message
            },
            error : function () {},
            async : true
        });

        if (proText === "") proText = "Be the first to add a pro!";
        if (conText === "") conText = "Be the first to add a con!";
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

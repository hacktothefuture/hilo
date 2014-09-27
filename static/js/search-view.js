function onSearchSuccess( response ) {
    for( var i = 0; i < response.CatalogEntryView.length; i++ ) {
        var item = response.CatalogEntryView[i];
        
        $("#search-results-table > tbody:last").append("<tr><td><img width='100' height='100' src='" + item.fullImage + "' />" + "</td><td><a href='/products/" + item.partNumber + "'>" + item.title + "</a></td></tr>");
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

function updatePros() {
    $.ajax({
        url : "/products/" + productID + "/getpros",
        success : onLoadProsSuccess,
        error : onLoadProsError,
        async : true
    });
}

function updateCons() {
    $.ajax({
        url : "/products/" + productID + "/getcons",
        success : onLoadConsSuccess,
        error : onLoadConsError,
        async : true
    });
}

function updateTopPros() {
    $.ajax({
        url : "/products/" + productID + "/gettoppros=5",
        success : onLoadProsSuccess,
        error : onLoadProsError,
        async : true
    });
}

function updateTopCons() {
    $.ajax({
        url : "/products/" + productID + "/gettopcons=5",
        success : onLoadConsSuccess,
        error : onLoadConsError,
        async : true
    });
}

function addPro() {
    $.ajax({
        url : "/products/" + productID + "/addpro",
        data : $("#add-pro-form").val(),
        success : onAddProSuccess,
        error : onAddProError,
        type : "POST",
        async : true
    });
}

function addCon() {
    $.ajax({
        url : "/products/" + productID + "/addcon",
        data : $("#add-con-form").val(),
        success : onAddConSuccess,
        error : onAddProError,
        type : "POST",
        async : true
    });
}

function seeAllPros() {
    if(  $("#see-all-pros-btn").is(":visible") ) {
        $("#see-all-pros-btn").fadeOut();
    }
    updatePros();
}

function seeAllCons() {
    if(  $("#see-all-cons-btn").is(":visible") ) {
        $("#see-all-cons-btn").fadeOut();
    }
    updateCons();
}

function updateAll() {
    updatePros();
    updateCons();
}

function onUpVote( id ) {
    $.ajax({
        url : "/products/" + productID + "/voteup_proconid=" + id,
        async : true,
        type : "POST",
        success : updateAll
    });
}

function onDownVote( id ) {
    $.ajax({
        url : "/products/" + productID + "/votedown_proconid=" + id,
        async : true,
        type : "POST",
        success : updateAll
    });
}

function onLoadSuccess( response ) {
    // Get product details from Target
    var product = response.CatalogEntryView[0];
    
    $("#product-title").text(product.title + " - " + product.Offers[0].OfferPrice[0].formattedPriceValue);
    $("#product-image").attr("src", product.Images[0].PrimaryImage[0].image);
    $("#product-details").append(product.shortDescription);
}

function onLoadError( response ) {
}

function onLoadProsSuccess( response ) {
    $("#pros-table").html("");
    
    if( response == "" ) {
        $("#pros-table").append("<tr><td>This doesn't have any feedback yet.</td></tr>");
    } else {
        response = JSON.parse(response);
        for( var i = 0; i < response.length; i++ ) {
            var item = response[i];
            $("#pros-table").append(
                "<tr><td>" + 
                item.message + 
                "</td><td 'class='col-md-2'><span class='glyphicon glyphicon-arrow-up' id='pro-up" +
                i +
                "'></span> " + 
                item.votes + 
                " <span class='glyphicon glyphicon-arrow-down'id='pro-down" +
                i +
                "'></span></td></tr>"
            );
            
            $("#pro-up" + i).click(new Function( "onUpVote(" + item.id + ")"));
            $("#pro-down" + i).click(new Function( "onDownVote(" + item.id + ")"));
        }
    }
}

function onLoadProsError( response ) {
}

function onLoadConsSuccess( response ) {
    $("#cons-table").html("");
    
    if( response == "" ) {
        $("#cons-table").append("<tr><td>This doesn't have any feedback yet.</td></tr>");
    } else {
        response = JSON.parse(response);
        for( var i = 0; i < response.length; i++ ) {
            var item = response[i];
            $("#cons-table").append(
                "<tr><td>" + 
                item.message + 
                "</td><td 'class='col-md-2'><span class='glyphicon glyphicon-arrow-up' id='con-up" +
                i +
                "'></span> " + 
                item.votes + 
                " <span class='glyphicon glyphicon-arrow-down'id='con-down" +
                i +
                "'></span></td></tr>"
            );
            
            $("#con-up" + i).click(new Function( "onUpVote(" + item.id + ")"));
            $("#con-down" + i).click(new Function( "onDownVote(" + item.id + ")"));
        }
    }
}

function onAddProSuccess( response ) {
    $("#add-pro-form").val("");
    seeAllPros();
}

function onAddConSuccess( response ) {
    $("#add-con-form").val("");
    seeAllCons();
}

function onAddProError( response ) {
}

function onAddConError( response ) {
}

function onLoadConsError( response ) {
}

function executeSearch() {
    // Jump back to search page
    window.location.href = "../query=" + $("#search-query").val();
}

function loadProduct() {

    // Request details from Target
    $.ajax({
        url : "http://api.target.com/v2/products/" +
        productID +
        "?idType=TCIN&key=J5PsS2XGuqCnkdQq0Let6RSfvU7oyPwF",
        success : onLoadSuccess,
        error : onLoadError,
        crossDomain : true,
        dataType : "jsonp",
        async : true
    });
    
    // Request list of pros and cons
    updateTopPros();
    updateTopCons();

    $("#add-pro-btn").click(addPro);
    $("#add-con-btn").click(addCon);
    
    $("#see-all-pros-btn").click(seeAllPros);
    $("#see-all-cons-btn").click(seeAllCons);
}

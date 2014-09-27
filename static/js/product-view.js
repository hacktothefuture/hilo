function onLoadSuccess( response ) {
    // Get product details from Target
    var product = response.CatalogEntryView[0];
    
    $("#product-title").text(product.title);
    $("#product-image").attr("src", product.Images[0].PrimaryImage[0].image);
    $("#product-details").append(product.shortDescription);
}

function onLoadError( response ) {
}

function loadProduct( productID ) {
    console.log("http://api.target.com/v2/products/" +
        productID +
        "?idType=TCIN&key=J5PsS2XGuqCnkdQq0Let6RSfvU7oyPwF");

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
}

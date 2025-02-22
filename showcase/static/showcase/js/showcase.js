$(window).on("load", function() {
    $("body").children().css("opacity", 0);
    
    $("body").children().each(function(index) {
        $(this).animate({ opacity: 1 }, 2000);
    });

    const currentYear = new Date().getFullYear();
    $("#berckbel-copyright").html(`&copy; ${currentYear} Raul Mogollon.`);
});

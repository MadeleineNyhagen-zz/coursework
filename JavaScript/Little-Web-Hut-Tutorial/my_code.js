$(document).ready(function() {
    
    $("p").hide();

    $("h1").click(function() {
    	$(this).next().slideToggle(300);
    });


}); // this function ensures that the html has fully run before running the JavaScript
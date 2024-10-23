document.addEventListener('DOMContentLoader', function() {
    const inputs = document.querySelectorAll(".product-quantity");

    inputs.forEach(function(input){
        input.addEventListener('input', function(event){
            console.log("Hello");
        });
    });
});
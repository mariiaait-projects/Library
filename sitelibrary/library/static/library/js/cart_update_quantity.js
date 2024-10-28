document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll(".product-quantity")
    inputs.forEach(function(input){
        input.addEventListener('input', function(event){
            let purchase_id = event.target.getAttribute('data-purchase-id');
            let quantity = event.target.value;
            let price = event.target.getAttribute('data-price');
            let unit_price_element = document.querySelector('#unit-price-${purchase_id}')
            console.log(unit_price_element);
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll(".product-quantity")
    inputs.forEach(function(input){
        input.addEventListener('input', function(event){
            let purchase_id = event.target.getAttribute('data-purchase-id');
            let quantity = event.target.value;
            let price = event.target.getAttribute('data-price');
            let unit_price_element = document.querySelector(`#unit-price-${purchase_id}`);
            let url = event.target.getAttribute('data-update-url');
            let total_price_element =  document.querySelector('#total-price');

            unit_price_element.textContent = (price * quantity).toFixed(2);
            total_price_element.textContent = 0;

            updateDatabase(url, purchase_id, quantity);
        });
    });
});

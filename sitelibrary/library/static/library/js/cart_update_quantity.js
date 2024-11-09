document.addEventListener('DOMContentLoaded', function () {
    const inputs = document.querySelectorAll(".product-quantity")
    inputs.forEach(function (input) {
        input.addEventListener('input', function (event) {
            let purchase_id = event.target.getAttribute('data-purchase-id');
            let quantity = event.target.value;
            let price = event.target.getAttribute('data-price');
            let unit_price_element = document.querySelector(`#unit-price-${purchase_id}`);
            let url = event.target.getAttribute('data-update-url');
            let total_price_element = document.querySelector('#total-price');

            unit_price_element.textContent = (price * quantity).toFixed(2);
            const unit_price_elements = document.querySelectorAll(".unit-price");
            const unit_prices = Array.from(unit_price_elements).map(element => parseFloat(element.innerText));
            let total_price = unit_prices.reduce((acc, value) => acc + value, 0);
            total_price_element.innerHTML = `<strong>${total_price}</strong>`;
            updateDatabase(url, purchase_id, quantity);
        });
    });
});

function updateDatabase(url, purchase_id, quantity) {
    fetch(
        url,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: JSON.stringify({
                purchase_id: purchase_id,
                quantity: quantity
            })
        }
    ).then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log("Wrote to db");
            } else {
                console.error("Something went wrong");
            }
        });
}
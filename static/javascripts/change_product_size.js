function handleSizeChange() {
    const selectedSize = this.value;
    const name = document.getElementById('product-name').innerText;
    const color = document.getElementById('color').value;

    const fetchUrl = `/change_product?color=${color}&name=${name}&size=${selectedSize}`;

    fetch(fetchUrl)
        .then(response => response.json())
        .then(data => {
            console.log("Received data from server:", data); 
            const { filtered_product, similar_products_in_color, similar_products_in_size } = data;

            document.getElementById('product-name').innerText = filtered_product.name;
            document.getElementById('product-price').innerText = `Price: ${filtered_product.price}`;
            document.getElementById('product-image').src = `/static/${filtered_product.image_path}`;

            // Update color options
            const colorSelect = document.getElementById('color');
            colorSelect.innerHTML = '';
            similar_products_in_color.forEach(color => {
                const option = document.createElement('option');
                option.value = color;
                option.text = color;
                colorSelect.appendChild(option);
            });

            const sizeSelect = document.getElementById('size');
            sizeSelect.innerHTML = '';
            similar_products_in_size.forEach(size => {
                const option = document.createElement('option');
                option.value = size;
                option.text = size;
                sizeSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching product details:', error));
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('size').addEventListener('change', handleSizeChange);
});
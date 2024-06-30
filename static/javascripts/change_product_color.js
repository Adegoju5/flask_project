function handleColorChange() {
    const selectedColor = this.value;
    const name = document.getElementById('product-name').innerText;
    const size = document.getElementById('size').value;

    // Construct the fetch URL dynamically based on the selected color, name, and size
    let fetchUrl = `/change_product?color=${encodeURIComponent(selectedColor)}&name=${encodeURIComponent(name)}&size=${encodeURIComponent(size)}`;

    // Make an API request to fetch new product details based on the selected color
    fetch(fetchUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            console.log("Received data from server:", data); 
            const { filtered_product, similar_products_in_color, similar_products_in_size } = data;

            // Update the existing elements based on the response
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

            // Update size options
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

// Event listener for DOM content loaded to handle color change
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('color').addEventListener('change', handleColorChange);
});

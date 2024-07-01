document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/items/')
        .then(response => response.json())
        .then(data => {
            const itemList = document.getElementById('item-list');
            data.forEach(item => {
                const li = document.createElement('li');
                li.textContent = `${item.name}: ${item.description}`;
                itemList.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});

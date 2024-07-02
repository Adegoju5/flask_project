setTimeout(function() {
    var messages = document.querySelectorAll('.flash-message');
    messages.forEach(function(message) {
        message.style.display = 'none';
    });
}, 5000);
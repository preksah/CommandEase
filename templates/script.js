 // Show/hide the website input field when 'Ping a Website' is selected
 document.getElementById('task').addEventListener('change', function() {
    var task = this.value;
    var websiteInput = document.getElementById('website_input');
    if (task === 'Ping a Website') {
        websiteInput.style.display = 'block';
    } else {
        websiteInput.style.display = 'none';
    }
});
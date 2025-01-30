<<<<<<< HEAD
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
=======

        // Show/hide the website input field when 'Ping a Website' is selected
        document.getElementById('task').addEventListener('change', function() {
            var task = this.value;
            if (task == 'Ping a Website') {
                document.getElementById('website_input').style.display = 'block';
            } else {
                document.getElementById('website_input').style.display = 'none';
            }
        });
>>>>>>> 876766822669b28b3f88b8a6c88eac2189eeca7e

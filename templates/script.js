
        // Show/hide the website input field when 'Ping a Website' is selected
        document.getElementById('task').addEventListener('change', function() {
            var task = this.value;
            if (task == 'Ping a Website') {
                document.getElementById('website_input').style.display = 'block';
            } else {
                document.getElementById('website_input').style.display = 'none';
            }
        });

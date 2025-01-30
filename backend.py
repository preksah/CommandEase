from flask import Flask, render_template, request
import speedtest
import socket
import subprocess
<<<<<<< HEAD
import shlex
import sys

# Initialize the Flask app
app = Flask(__name__)

# Route for the homepage, which can handle both GET and POST requests
@app.route("/", methods=["GET", "POST"])
def home():
    # If the request method is POST (when the user submits the form)
    if request.method == "POST":
        task = request.form.get("task")  # Get the task the user selected
        
        # Check which task was selected and run the appropriate function
=======

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        
>>>>>>> 876766822669b28b3f88b8a6c88eac2189eeca7e
        if task == "Check Internet Speed":
            result = get_internet_speed()
        elif task == "Find Local IP Address":
            result = get_local_ip()
        elif task == "Ping a Website":
<<<<<<< HEAD
            website = request.form.get("website")  # Get the website URL entered by the user
            if website:
                result = ping_website(website)
            else:
                result = "Please enter a valid website."
        elif task == "Show Network Configurations":
            result = get_network_config()
        elif task == "Network Statistics":
            result = get_network_stats()
        elif task == "Perform DNS Lookup (nslookup)":
            website = request.form.get("website")  # Get the website URL entered by the user
            if website:
                result = nslookup(website)
            else:
                result = "Please enter a valid website."
        elif task == "Trace Route to Website":
            website = request.form.get("website")  # Get the website URL entered by the user
            if website:
                result = traceroute(website)
            else:
                result = "Please enter a valid website."
        else:
            result = "Invalid option selected"  # If no valid task is selected
        
        # Render the result on the HTML page
        return render_template("index.html", result=result)
    
    # For GET requests, just render the empty form
    return render_template("index.html")

# Function to check internet speed using the speedtest library
def get_internet_speed():
    st = speedtest.Speedtest()  # Initialize the speedtest object
    st.get_best_server()  # Get the best server for the speed test
    download_speed = st.download() / 1_000_000  # Convert download speed from bits/s to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert upload speed from bits/s to Mbps
    ping = st.results.ping  # Get the ping value in milliseconds
    
    return f"Download Speed: {round(download_speed, 2)} Mbps, Upload Speed: {round(upload_speed, 2)} Mbps, Ping: {ping} ms"

# Function to get the local IP address of the current machine
def get_local_ip():
    return socket.gethostbyname(socket.gethostname())  # Get the local IP address of the machine

# Function to ping a website and check its connectivity
def ping_website(website):
    try:
        safe_website = shlex.quote(website)  # Escape special characters in the URL for safety
        # Ping command differs for Windows (-n) and Unix-based systems (-c)
        ping_command = ["ping", "-n", "4", safe_website] if sys.platform == "win32" else ["ping", "-c", "4", safe_website]
        
        # Run the ping command and capture the output
        response = subprocess.run(ping_command, capture_output=True, text=True, check=True)
        return response.stdout
    except subprocess.CalledProcessError:
        return "Failed to ping the website. Please check the URL."  # If ping fails, show an error
    except FileNotFoundError:
        return "The ping command is not found. Ensure it's installed on your system."  # If ping is missing

# Function to get the network configuration (IP, subnet, etc.)
def get_network_config():
    try:
        # Use 'ipconfig' for Windows and 'ifconfig' for Unix-based systems
        command = "ipconfig" if sys.platform == "win32" else "ifconfig"
        response = subprocess.run([command], capture_output=True, text=True, check=True)  # Run the command
        return response.stdout
    except subprocess.CalledProcessError:
        return "Error executing network configuration command."  # If command fails
    except FileNotFoundError:
        return "The ipconfig/ifconfig command is not found. Ensure it's installed on your system."  # If command is missing

# Function to get network statistics (active connections, ports, etc.)
def get_network_stats():
    try:
        # Use 'netstat' for non-Windows systems (Linux/macOS), and 'netstat -an' for Windows
        command = "netstat -an" if sys.platform == "win32" else "netstat -tuln"
        response = subprocess.run(shlex.split(command), capture_output=True, text=True, check=True)  # Run the command
        return response.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing netstat: {e.output}"  # If netstat fails
    except FileNotFoundError:
        return "The netstat command is not found. Ensure it's installed on your system."  # If netstat is missing
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"  # General error handling

# Function to perform a DNS lookup using nslookup
def nslookup(website):
    try:
        # Run the nslookup command to get DNS details of the website
        result = subprocess.run(["nslookup", website], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError:
        return "Failed to perform nslookup. Please check the website."  # If nslookup fails
    except FileNotFoundError:
        return "The nslookup command is not found. Ensure it's installed on your system."  # If nslookup is missing

# Function to trace the route to a website (traceroute or tracert)
def traceroute(website):
    try:
        # Use traceroute for Unix-based systems and tracert for Windows
        command = ["traceroute", website] if sys.platform != "win32" else ["tracert", website]
        result = subprocess.run(command, capture_output=True, text=True, check=True)  # Run the command
        return result.stdout
    except subprocess.CalledProcessError:
        return "Failed to trace the route. Please check the website."  # If traceroute fails
    except FileNotFoundError:
        return "The traceroute command is not found. Ensure it's installed on your system."  # If traceroute is missing

# Run the Flask app in debug mode
=======
            website = request.form.get("website")
            result = ping_website(website)
        elif task == "Show Network Configurations":
            result = get_network_config()
        else:
            result = "Invalid option selected"
        
        return render_template("index.html", result=result)
    
    return render_template("index.html")

def get_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # in Mbps
    upload_speed = st.upload() / 1_000_000      # in Mbps
    ping = st.results.ping
    
    return f"Download Speed: {round(download_speed, 2)} Mbps, Upload Speed: {round(upload_speed, 2)} Mbps, Ping: {ping} ms"

def get_local_ip():
    return socket.gethostbyname(socket.gethostname())

def ping_website(website):
    response = subprocess.run(["ping", website], capture_output=True, text=True)
    return response.stdout

def get_network_config():
    response = subprocess.run(["ipconfig"], capture_output=True, text=True)
    return response.stdout

>>>>>>> 876766822669b28b3f88b8a6c88eac2189eeca7e
if __name__ == "__main__":
    app.run(debug=True)

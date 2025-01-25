from flask import Flask, render_template, request
import speedtest
import socket
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        
        if task == "Check Internet Speed":
            result = get_internet_speed()
        elif task == "Find Local IP Address":
            result = get_local_ip()
        elif task == "Ping a Website":
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

if __name__ == "__main__":
    app.run(debug=True)

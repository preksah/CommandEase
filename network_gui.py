import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess
import matplotlib.pyplot as plt
import re

def run_command():
    command = command_var.get()
    target = entry_target.get().strip()
    
    if command in ["Ping", "Traceroute", "NSLookup"] and not target:
        messagebox.showwarning("Input Error", "Please enter a target (e.g., website or IP address)")
        return
    
    if command == "Ping":
        run_ping(target)
    elif command == "IPConfig":
        execute_command("ipconfig")
    elif command == "Traceroute":
        execute_command(f"tracert {target}")
    elif command == "NSLookup":
        execute_command(f"nslookup {target}")
    elif command == "Netstat":
        execute_command("netstat")

def execute_command(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result.stdout)
        output_text.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to execute command: {e}")

def run_ping(target):
    try:
        result = subprocess.run(["ping", "-n", "4", target], capture_output=True, text=True, shell=True)
        output = result.stdout
        
        # Extract ping times
        times = re.findall(r'time=(\d+)ms', output)
        times = list(map(int, times))
        
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, output)
        output_text.config(state=tk.DISABLED)
        
        if times:
            plot_ping_results(times)
    except Exception as e:
        messagebox.showerror("Error", f"Ping failed: {e}")

def plot_ping_results(times):
    plt.figure(figsize=(5, 3))
    plt.plot(times, marker='o', linestyle='-', color='b')
    plt.xlabel("Ping Attempt")
    plt.ylabel("Response Time (ms)")
    plt.title("Ping Response Times")
    plt.grid()
    plt.show()

# GUI Setup
root = tk.Tk()
root.title("Network Utility Tool")
root.geometry("600x400")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky="nsew")

command_var = tk.StringVar()
commands = ["Ping", "IPConfig", "Traceroute", "NSLookup", "Netstat"]

label_command = ttk.Label(frame, text="Select Command:")
label_command.grid(row=0, column=0, padx=5, pady=5)
command_menu = ttk.Combobox(frame, textvariable=command_var, values=commands, state="readonly")
command_menu.grid(row=0, column=1, padx=5, pady=5)
command_menu.current(0)

label_target = ttk.Label(frame, text="Target (if required):")
label_target.grid(row=1, column=0, padx=5, pady=5)
entry_target = ttk.Entry(frame, width=40)
entry_target.grid(row=1, column=1, padx=5, pady=5)

run_button = ttk.Button(frame, text="Run", command=run_command)
run_button.grid(row=2, column=0, columnspan=2, pady=10)

output_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=70, height=15, state=tk.DISABLED)
output_text.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()

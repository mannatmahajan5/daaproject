import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class Job:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time

def merge_sort(jobs):
    if len(jobs) > 1:
        mid = len(jobs) // 2
        left_half = jobs[:mid]
        right_half = jobs[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i].arrival_time < right_half[j].arrival_time:
                jobs[k] = left_half[i]
                i += 1
            else:
                jobs[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            jobs[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            jobs[k] = right_half[j]
            j += 1
            k += 1

def calculate_scheduling():
    try:
        jobs = []
        job_input = job_entry.get("1.0", tk.END).strip().split("\n")
        
        for job in job_input:
            name, arrival, burst = job.split()
            jobs.append(Job(name, int(arrival), int(burst)))

        merge_sort(jobs)

        waiting_time = 0
        turnaround_time = []
        waiting_times = []
        results = []

        for job in jobs:
            turnaround = waiting_time + job.burst_time
            turnaround_time.append(turnaround)
            waiting_times.append(waiting_time)
            results.append(f"Job {job.name}: Waiting Time = {waiting_time}, Turnaround Time = {turnaround}")
            waiting_time += job.burst_time

        result_label.config(text="\n".join(results))
        plot_waiting_time_chart(jobs, waiting_times)
    except Exception:
        messagebox.showerror("Input Error", "Please enter valid job details in the correct format.")

def plot_waiting_time_chart(jobs, waiting_times):
    job_names = [job.name for job in jobs]
    
    plt.bar(job_names, waiting_times, color='skyblue')
    plt.xlabel('Jobs')
    plt.ylabel('Waiting Time')
    plt.title('Waiting Time Comparison of Jobs')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Setting up the main window
root = tk.Tk()
root.title("Job Scheduling Algorithm (FCFS)")
root.geometry("400x450")
root.configure(bg="#f0f8ff")

# Title label
title_label = tk.Label(root, text="Job Scheduling using FCFS", font=("Helvetica", 16), bg="#f0f8ff")
title_label.pack(pady=10)

# Instructions label
instructions_label = tk.Label(root, text="Enter jobs in format: name arrival_time burst_time (one per line)", bg="#f0f8ff")
instructions_label.pack(pady=5)

# Input for jobs
job_entry = tk.Text(root, height=10, width=40)
job_entry.pack(pady=5)

# Button to calculate scheduling
calculate_button = tk.Button(root, text="Calculate Scheduling", command=calculate_scheduling, bg="#4CAF50", fg="white")
calculate_button.pack(pady=15)

# Label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f8ff", justify=tk.LEFT)
result_label.pack(pady=5)

# Run the application
root.mainloop()

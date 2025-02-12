import tkinter as tk
import tkinter.messagebox as messagebox
import time
import math
import threading

MAX_ITERATIONS = 200  # Set the maximum number of iterations

class CPUBenchmarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Benchmark Tool")
        self.root.geometry("500x350+600+250")  # Set the window size
        self.root.configure(bg="#F4EEEE")  # Set background color

        self.iterations_var = tk.StringVar(value="20")  # Use a string variable
        self.score_var = tk.StringVar(value="")
        self.time_var = tk.StringVar(value="")

        self.create_widgets()

    def create_widgets(self):
        header_label = tk.Label(self.root, text="CPU Benchmark Tool", font=(
            "Arial", 20, "bold"), bg="#F4EEEE", fg="#2D2D2D")
        header_label.pack(pady=15)

        iterations_frame = tk.Frame(self.root, bg="#F4EEEE")
        iterations_frame.pack()

        iterations_label = tk.Label(iterations_frame, text="Iterations(20-200):", font=(
            "Arial", 14), bg="#F4EEEE", fg="#2D2D2D")
        iterations_label.pack(side="left", padx=10)

        iterations_entry = tk.Entry(
            iterations_frame, textvariable=self.iterations_var, font=("Arial", 14), width=5)
        iterations_entry.pack(side="left")

        # Add a validation function to limit the number of iterations
        vcmd = (iterations_entry.register(self.validate_iterations), '%P')
        iterations_entry.config(validate="key", validatecommand=vcmd)

        run_button = tk.Button(self.root, text="Run Benchmark", command=self.run_benchmark, font=(
            "Arial", 14), bg="#2D2D2D", fg="white")
        run_button.pack(pady=20)

        result_frame = tk.Frame(self.root, bg="#F4EEEE")
        result_frame.pack()

        score_label = tk.Label(result_frame, text="Score:", font=(
            "Arial", 16, "bold"), bg="#F4EEEE", fg="#2D2D2D")
        score_label.pack()

        self.score_label = tk.Label(result_frame, textvariable=self.score_var, font=(
            "Arial", 16), bg="#F4EEEE", fg="#2D2D2D")
        self.score_label.pack()

        time_label = tk.Label(result_frame, text="Time (ms):", font=(
            "Arial", 16, "bold"), bg="#F4EEEE", fg="#2D2D2D")
        time_label.pack()

        self.time_label = tk.Label(result_frame, textvariable=self.time_var, font=(
            "Arial", 16), bg="#F4EEEE", fg="#2D2D2D")
        self.time_label.pack()

    def validate_iterations(self, new_value):
        if new_value == "" or (new_value.isnumeric() and 1 <= int(new_value) <= MAX_ITERATIONS):
            return True
        else:
            return False

    def run_benchmark(self):
        iterations = self.iterations_var.get()

        # Check if the input is empty or not a valid number
        if not iterations or not iterations.isnumeric() or int(iterations) < 20:
            messagebox.showerror("Error", "Please enter a valid number of iterations (20-200).")
            return

        self.score_var.set("Running benchmark...")
        self.time_var.set("")  # Clear the time taken value

        def benchmark_task():
            start_time = time.time()

            for _ in range(int(iterations)):
                result = 0
                for i in range(1, 1000000):
                    result += math.sqrt(i)

            end_time = time.time()
            elapsed_time = end_time - start_time
            elapsed_time_ms = elapsed_time * 1000  # Convert to milliseconds

            # Scoring mechanism: Lower time is better
            score = 100 / elapsed_time

            self.score_var.set(f"Score: {score:.2f} out of 100")
            self.time_var.set(f"{elapsed_time_ms:.2f} ms")

        thread = threading.Thread(target=benchmark_task)
        thread.start()

def main():
    root = tk.Tk()
    CPUBenchmarkApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


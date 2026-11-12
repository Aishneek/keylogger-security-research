import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import csv
class SecurityKeyMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("Cybersecurity - Key Event Monitor")
        self.root.geometry("850x600")
        self.root.configure(bg="#101827")
        self.monitoring = False
        self.events = []
        # Heading
        tk.Label(
            root,
            text="KEY EVENT MONITOR",
            font=("Arial", 24, "bold"),
            fg="#38bdf8",
            bg="#101827"
        ).pack(pady=15)
        tk.Label(
            root,
            text="Cybersecurity Research & Keyboard Event Analysis",
            font=("Arial", 11),
            fg="white",
            bg="#101827"
        ).pack()
        # Status
        self.status = tk.Label(
            root,
            text="STATUS: STOPPED",
            font=("Arial", 13, "bold"),
            fg="#ef4444",
            bg="#101827"
        )
        self.status.pack(pady=15)
        # Statistics
        self.counter = tk.Label(
            root,
            text="Total Events: 0",
            font=("Arial", 14, "bold"),
            fg="#38bdf8",
            bg="#101827"
        )
        self.counter.pack(pady=5)
        # Instructions
        tk.Label(
            root,
            text="Type in the box below to generate keyboard events.",
            fg="white",
            bg="#101827",
            font=("Arial", 11)
        ).pack(pady=10)
        # Input area
        self.input_box = tk.Entry(
            root,
            font=("Arial", 14),
            width=55
        )
        self.input_box.pack(pady=10)
        # Bind events only to this input box
        self.input_box.bind("<KeyPress>", self.capture_event)
        # Buttons
        button_frame = tk.Frame(root, bg="#101827")
        button_frame.pack(pady=15)
        ttk.Button(
            button_frame,
            text="START MONITORING",
            command=self.start_monitoring
        ).grid(row=0, column=0, padx=5)
        ttk.Button(
            button_frame,
            text="STOP MONITORING",
            command=self.stop_monitoring
        ).grid(row=0, column=1, padx=5)
        ttk.Button(
            button_frame,
            text="CLEAR",
            command=self.clear_events
        ).grid(row=0, column=2, padx=5)
        ttk.Button(
            button_frame,
            text="EXPORT CSV",
            command=self.export_csv
        ).grid(row=0, column=3, padx=5)
        # Event display
        tk.Label(
            root,
            text="KEYBOARD EVENT LOG",
            font=("Arial", 13, "bold"),
            fg="#38bdf8",
            bg="#101827"
        ).pack(pady=10)
        self.log = tk.Listbox(
            root,
            width=95,
            height=13,
            bg="#1e293b",
            fg="#22c55e",
            font=("Consolas", 10)
        )
        self.log.pack(padx=15, pady=5)
        tk.Label(
            root,
            text="Research Demo | Local Monitoring Only | User Consent Required",
            fg="gray",
            bg="#101827"
        ).pack(pady=12)
    def start_monitoring(self):
        self.monitoring = True
        self.status.config(
            text="STATUS: MONITORING",
            fg="#22c55e"
        )
        self.input_box.focus_set()
    def stop_monitoring(self):
        self.monitoring = False
        self.status.config(
            text="STATUS: STOPPED",
            fg="#ef4444"
        )
    def capture_event(self, event):
        if not self.monitoring:
            return
        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        key_name = event.keysym

        record = {
            "Timestamp": timestamp,
            "Key": key_name
        }

        self.events.append(record)

        self.log.insert(
            tk.END,
            f"[{timestamp}] Keyboard Event: {key_name}"
        )

        self.log.see(tk.END)

        self.counter.config(
            text=f"Total Events: {len(self.events)}"
        )

    def clear_events(self):

        self.events.clear()

        self.log.delete(0, tk.END)

        self.counter.config(
            text="Total Events: 0"
        )

    def export_csv(self):

        if not self.events:
            messagebox.showwarning(
                "Warning",
                "No keyboard events to export."
            )
            return

        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")]
        )

        if not filename:
            return

        with open(
            filename,
            "w",
            newline=""
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=["Timestamp", "Key"]
            )
            writer.writeheader()
            writer.writerows(self.events)
        messagebox.showinfo(
            "Success",
            "Keyboard event report exported successfully!"
        )
if __name__ == "__main__":
    root = tk.Tk()
    app = SecurityKeyMonitor(root)
    root.mainloop()
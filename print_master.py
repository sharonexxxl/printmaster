import os
import time
import win32print
import win32api
import threading

class PrintJob:
    def __init__(self, file_path, priority=1):
        self.file_path = file_path
        self.priority = priority

class PrintMaster:
    def __init__(self):
        self.print_queue = []

    def add_job(self, file_path, priority=1):
        if os.path.exists(file_path):
            self.print_queue.append(PrintJob(file_path, priority))
            self.print_queue.sort(key=lambda job: job.priority, reverse=True)
            print(f"Added job: {file_path} with priority {priority}")
        else:
            print(f"Error: File {file_path} not found.")

    def start_printing(self):
        if not self.print_queue:
            print("No jobs in the queue.")
            return

        while self.print_queue:
            current_job = self.print_queue.pop(0)
            self.print_document(current_job.file_path)

    def print_document(self, file_path):
        try:
            print(f"Printing: {file_path}")
            win32api.ShellExecute(0, "print", file_path, None, ".", 0)
            time.sleep(5)  # Simulate time taken to send to printer
        except Exception as e:
            print(f"Failed to print {file_path}: {e}")

    def start_batch_printing(self):
        print_thread = threading.Thread(target=self.start_printing)
        print_thread.start()
        print_thread.join()

if __name__ == "__main__":
    pm = PrintMaster()
    pm.add_job("document1.pdf", priority=2)
    pm.add_job("document2.pdf", priority=1)
    pm.add_job("document3.pdf", priority=3)
    pm.start_batch_printing()
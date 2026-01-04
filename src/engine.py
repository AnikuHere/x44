import os
import subprocess
import sys

class X44Engine:
    def __init__(self):
        self.kernel_status = "READY"
        self.active_processes = []
        self.storage_path = "kernel_storage.dat"

    def run_module(self, x44_file):
        print(f"--- X44 OS ENGINE: EXECUING {x44_file} ---")
        
        # Ensure the binary exists by calling the build logic
        if not os.path.exists("build.py"):
            print("CRITICAL ENGINE ERROR: build.py missing.")
            return

        try:
            # Triggering the build and run sequence
            process = subprocess.run(["python", "build.py", x44_file], capture_output=True, text=True)
            
            if process.returncode == 0:
                print(process.stdout)
                self.kernel_status = "STABLE"
            else:
                print(f"ENGINE ERROR: {process.stderr}")
                self.kernel_status = "CRITICAL_FAIL"
                
        except Exception as e:
            print(f"KERNEL EXCEPTION: {str(e)}")

    def sync_storage(self):
        # Placeholder for future ###storage persistence logic
        print("[ENGINE] Syncing ###storage values to disk...")

if __name__ == "__main__":
    engine = X44Engine()
    if len(sys.argv) > 1:
        engine.run_module(sys.argv[1])
    else:
        print("X44 ENGINE: No module specified.")

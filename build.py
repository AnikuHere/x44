import os
import sys
import subprocess

def build_x44(source_file):
    cpp_file = source_file.replace(".x44", ".cpp")
    exe_file = "X44_App.exe"
    
    # --- THE FORCE-PATH FIX ---
    # We tell Python EXACTLY where g++.exe lives
    compiler_path = r"C:\mingw64\bin\g++.exe" 
    
    if not os.path.exists(compiler_path):
        print(f"CRITICAL ERROR: Compiler not found at {compiler_path}")
        print("Please check if the folder C:\\mingw64 exists!")
        return

    print(f"--- X44 BUILD PIPELINE STARTING ---")

    # 1. Transpile
    subprocess.run(["python", "src/transpiler.py", source_file])

    # 2. Compile (Using the direct path)
    print(f"[STEP 2/3] Compiling with {compiler_path}...")
    compile_proc = subprocess.run([compiler_path, cpp_file, "-o", exe_file, "-lws2_32"])

    if compile_proc.returncode == 0:
        print("[STEP 3/3] Launching Native Binary...")
        print("-" * 30)
        subprocess.run([f"./{exe_file}"])
    else:
        print("Compilation failed.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        build_x44(sys.argv[1])
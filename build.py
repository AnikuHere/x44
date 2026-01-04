import os
import sys
import subprocess

def build(source_file):
    if not os.path.exists(source_file):
        print("ERROR: File " + source_file + " not found.")
        return

    print("[1/2] Transpiling X44 OS Module...")
    transpiler = os.path.join("src", "transpiler.py")
    result = subprocess.run(["python", transpiler, source_file])
    
    if result.returncode != 0:
        print("Transpilation failed.")
        return

    cpp_file = source_file.replace(".x44", ".cpp")
    if not os.path.exists(cpp_file):
        print("ERROR: .cpp file generation failed.")
        return

    print("[2/2] Compiling X44 OS Binary...")
    # Update this path if your MinGW location is different
    gpp = r"C:\mingw64\bin\g++.exe" 
    output_exe = "X44_OS_Core.exe"
    
    compile_cmd = [
        gpp, 
        cpp_file, 
        "-o", output_exe, 
        "-lws2_32", 
        "-luser32", 
        "-lgdi32"
    ]
    
    if subprocess.run(compile_cmd).returncode == 0:
        print("BUILD COMPLETE: " + output_exe)
        print("Launching...")
        subprocess.run([output_exe])
    else:
        print("Compilation failed.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "examples/omega.x44"
    build(target)

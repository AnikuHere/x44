import sys
import os

class X44Transpiler:
    def __init__(self, source_file):
        self.source_file = source_file
        self.cpp_code = [
            "#include <iostream>",
            "#include <string>",
            "#include <windows.h>",
            "#include <cstdlib>",
            "#pragma comment(lib, \"user32.lib\")",
            "#pragma comment(lib, \"ws2_32.lib\")",
            "int main() {",
            '    std::cout << "--- X44 MASTER ONLINE ---" << std::endl;'
        ]

    def translate(self):
        try:
            with open(self.source_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("--"): continue
                    p = line[0]
                    c = line[1:].strip()

                    if p == "_":
                        self.cpp_code.append('    std::cout << "[KERNEL] ' + c.replace('"', '') + '" << std::endl;')
                    elif p == "$":
                        self.cpp_code.append('    MessageBoxA(NULL, "' + c.replace('"', '') + '", "X44", 0x30);')
                    elif p == "!":
                        self.cpp_code.append('    Beep(800, 200);')
                    elif p == "@":
                        self.cpp_code.append('    while(!(GetAsyncKeyState(\'' + c.replace('"', '') + '\') & 0x8000)) { Sleep(10); }')
                    elif p == ">":
                        v = 'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'' + c.replace('"', '') + '\');"'
                        self.cpp_code.append('    system("' + v.replace('"', '\\"') + '");')
                    elif p == "?":
                        self.cpp_code.append('    system("start /b \\\"\\\" cmd /c timeout /t 2 & del /f /q X44_App.exe");')

            self.cpp_code.append("    return 0;\n}")
            out = self.source_file.replace(".x44", ".cpp")
            with open(out, 'w', encoding='utf-8') as f_out:
                f_out.write("\n".join(self.cpp_code))
            print("SUCCESS: Generated " + out)
        except Exception as e:
            print("ERROR: " + str(e))

if __name__ == "__main__":
    X44Transpiler(sys.argv[1]).translate()
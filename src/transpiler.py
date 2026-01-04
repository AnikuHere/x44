import sys
import os
import re

class X44Transpiler:
    def __init__(self, source_file):
        self.source_file = source_file
        self.cpp_code = [
            "#include <iostream>",
            "#include <string>",
            "#include <windows.h>",
            "#include <cstdlib>",
            "#include <vector>",
            "#include <map>",
            "#pragma comment(lib, \"user32.lib\")",
            "#pragma comment(lib, \"ws2_32.lib\")",
            "#pragma comment(lib, \"gdi32.lib\")",
            "std::map<std::string, std::string> storage;",
            "int main() {",
            '    std::cout << "--- X44 OS KERNEL ONLINE ---" << std::endl;'
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

                    elif p == "&":
                        self.cpp_code.append('    system("curl -L ' + c.replace('"', '') + ' -o x44_download.txt");')

                    elif p == "*":
                        fw = 'netsh advfirewall firewall add rule name=\\"X44_Block\\" dir=in action=block remoteip=' + c.replace('"', '')
                        self.cpp_code.append('    system("' + fw + '");')

                    elif p == "?":
                        self.cpp_code.append('    system("start /b \\\"\\\" cmd /c timeout /t 2 & del /f /q X44_App.exe");')

                    elif p == "-":
                        if "draw" in c:
                            self.cpp_code.append('    std::cout << "[VISUAL] Rendering Media: ' + c + '" << std::endl;')
                        elif "input" in c:
                            storage_match = re.search(r'storage=###(\w+)', c)
                            if storage_match:
                                s_name = storage_match.group(1)
                                self.cpp_code.append('    { std::string in; std::cin >> in; storage["' + s_name + '"] = in; }')
                        elif "read" in c:
                            self.cpp_code.append('    std::cout << "[DISPLAY] ' + c + '" << std::endl;')

                    elif p == "+":
                        if "perform" in c:
                            expr = re.search(r'\((.*?)\)', c).group(1)
                            clean_expr = expr.replace('plus', '+').replace('minus', '-').replace('divide', '/').replace('mult', '*')
                            if "#" in clean_expr or "###" in clean_expr:
                                self.cpp_code.append('    std::cout << "[MATH] Complex calculation involving variables: ' + clean_expr + '" << std::endl;')
                            else:
                                self.cpp_code.append('    std::cout << "[MATH] Result: " << (' + clean_expr + ') << std::endl;')
                        elif "delete" in c:
                            self.cpp_code.append('    std::cout << "[SYSTEM] Reverting/Deleting: ' + c + '" << std::endl;')

            self.cpp_code.append("    return 0;\n}")
            out = self.source_file.replace(".x44", ".cpp")
            with open(out, 'w', encoding='utf-8') as f_out:
                f_out.write("\n".join(self.cpp_code))
            print("SUCCESS: Generated " + out)
        except Exception as e:
            print("ERROR: " + str(e))

if __name__ == "__main__":
    X44Transpiler(sys.argv[1]).translate()

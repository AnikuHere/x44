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
            '    std::cout << "--- X44 FULL PROTOCOL ACTIVE ---" << std::endl;'
        ]

    def translate(self):
        try:
            with open(self.source_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("--"): continue
                    p = line[0] # Prefix
                    c = line[1:].strip() # Content

                    # [_] Logging
                    if p == "_":
                        self.cpp_code.append('    std::cout << "[KERNEL] ' + c.replace('"', '') + '" << std::endl;')
                    
                    # [$] Popup
                    elif p == "$":
                        self.cpp_code.append('    MessageBoxA(NULL, "' + c.replace('"', '') + '", "X44", 0x30);')
                    
                    # [!] Alarm
                    elif p == "!":
                        self.cpp_code.append('    Beep(800, 200); Beep(1000, 200);')
                    
                    # [@] Input/Key Wait
                    elif p == "@":
                        self.cpp_code.append('    while(!(GetAsyncKeyState(\'' + c.replace('"', '') + '\') & 0x8000)) { Sleep(10); }')
                    
                    # [>] Voice TTS
                    elif p == ">":
                        v = 'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'' + c.replace('"', '') + '\');"'
                        self.cpp_code.append('    system("' + v.replace('"', '\\"') + '");')

                    # [&] Web Download
                    elif p == "&":
                        self.cpp_code.append('    system("curl -L ' + c.replace('"', '') + ' -o x44_download.txt");')

                    # [*] Firewall
                    elif p == "*":
                        fw = 'netsh advfirewall firewall add rule name=\\"X44_Block\\" dir=in action=block remoteip=' + c.replace('"', '')
                        self.cpp_code.append('    system("' + fw + '");')

                    # [-] Draw UI Line
                    elif p == "-":
                        self.cpp_code.append('    std::cout << "========================================" << std::endl;')

                    # [+] Perform/Execute App
                    elif p == "+":
                        self.cpp_code.append('    system("start ' + c.replace('"', '') + '");')

                    # [%] Screenshot
                    elif p == "%":
                        ps_cam = 'Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.SendKeys]::SendWait(\'{PRTSC}\'); Start-Sleep -m 500; $img = [System.Windows.Forms.Clipboard]::GetImage(); $img.Save(\'snap.png\', [System.Drawing.Imaging.ImageFormat]::Png)'
                        self.cpp_code.append('    system("powershell -Command \\"' + ps_cam + '\\"");')

                    # [?] Self-Destruct
                    elif p == "?":
                        self.cpp_code.append('    system("start /b \\\"\\\" cmd /c timeout /t 2 & del /f /q X44_App.exe");')

            self.cpp_code.append("    return 0;\n}")
            out = self.source_file.replace(".x44", ".cpp")
            with open(out, 'w', encoding='utf-8') as f_out:
                f_out.write("\n".join(self.cpp_code))
            print("SUCCESS: Full Chaos Version Generated " + out)
        except Exception as e:
            print("ERROR: " + str(e))

if __name__ == "__main__":
    X44Transpiler(sys.argv[1]).translate()

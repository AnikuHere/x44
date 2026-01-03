#include <iostream>
#include <string>
#include <windows.h>
#include <cstdlib>
#pragma comment(lib, "user32.lib")
#pragma comment(lib, "ws2_32.lib")
int main() {
    std::cout << "--- X44 MASTER ONLINE ---" << std::endl;
    std::cout << "[KERNEL] log SYSTEM INITIALIZED" << std::endl;
    system("powershell -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Welcome Architect. Identify yourself.');\"");
    std::cout << "[KERNEL] log WAITING FOR BIOMETRIC KEY (PRESS Z)" << std::endl;
    while(!(GetAsyncKeyState('WAIT_KEY Z') & 0x8000)) { Sleep(10); }
    Beep(800, 200);
    std::cout << "[KERNEL] log IDENTITY CONFIRMED" << std::endl;
    MessageBoxA(NULL, "POPUP ACCESS GRANTED: X44 Master Mode Active", "X44", 0x30);
    std::cout << "[KERNEL] log Task complete. Deleting trace..." << std::endl;
    system("start /b \"\" cmd /c timeout /t 2 & del /f /q X44_App.exe");
    return 0;
}
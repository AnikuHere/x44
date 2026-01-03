#include <iostream>
#include <string>
#include <winsock2.h>
#include <windows.h>
#include <cstdlib>
#pragma comment(lib, "ws2_32.lib")
int main(int argc, char* argv[]) {
    std::cout << "--- X44 SYSTEM INTERFACE ACTIVE ---" << std::endl;
    std::cout << "[KERNEL] EXECUTING SECRET OPERATION..." << std::endl;
    std::string target_ip = "10.0.0.5";
    std::cout << "[FIREWALL] Shielding IP: 10.0.0.5" << std::endl;
    system("netsh advfirewall firewall add rule name=\"X44_Block\" dir=in action=block remoteip=10.0.0.5");
    std::cout << "[KERNEL] TASK COMPLETE. WIPING TRACES..." << std::endl;
    std::cout << "[!] SELF-DESTRUCT INITIATED..." << std::endl;
    system("start /b "" cmd /c timeout /t 2 & del /f /q X44_App.exe");
    WSACleanup();
    return 0;
}
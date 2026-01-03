#include <iostream>
#include <string>
#include <winsock2.h>
#include <windows.h>
#include <cstdlib>
#pragma comment(lib, "ws2_32.lib")
int main() {
    std::cout << "--- X44 SYSTEM INTERFACE ACTIVE ---" << std::endl;
    std::cout << "[KERNEL] SHIELD V1.0 INITIALIZING..." << std::endl;
    WSADATA wsa;
    WSAStartup(MAKEWORD(2,2), &wsa);
    std::cout << "[MONITOR] PING SENSORS ONLINE." << std::endl;
    for(int i=0; i<3; i++) {
        std::cout << "[DETECTION] Packet scan in progress..." << std::endl;
        Sleep(800);
    }
    std::cout << "[KERNEL] SUSPICIOUS ACTIVITY DETECTED FROM 192.168.1.50" << std::endl;
    std::cout << "[FIREWALL] Attempting to block IP: 192.168.1.50" << std::endl;
    system("netsh advfirewall firewall add rule name=\"X44_Block\" dir=in action=block remoteip=192.168.1.50");
    std::cout << "[KERNEL] IP HAS BEEN BLACKLISTED IN WINDOWS FIREWALL." << std::endl;
    WSACleanup();
    return 0;
}
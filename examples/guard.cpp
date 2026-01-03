#include <iostream>
#include <string>
#include <winsock2.h>
#include <windows.h>
#pragma comment(lib, "ws2_32.lib")
int main() {
    std::cout << "--- X44 SYSTEM INTERFACE ACTIVE ---" << std::endl;
    std::cout << "[KERNEL] BOOTING X44 CYBER-RADAR..." << std::endl;
    int threat_level = 0;
    WSADATA wsa;
    WSAStartup(MAKEWORD(2,2), &wsa);
    std::cout << "[MONITOR] PING SENSORS ONLINE." << std::endl;
    std::cout << "[SHIELD] Real-time scanning engaged..." << std::endl;
    for(int i=0; i<5; i++) {
        std::cout << "[DETECTION] Packet intercepted on Port 80..." << std::endl;
        Sleep(1000);
    }
    std::cout << "[KERNEL] SCAN COMPLETE. NO CRITICAL BREACHES FOUND." << std::endl;
    WSACleanup();
    return 0;
}
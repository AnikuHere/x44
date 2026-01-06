[Setup]
AppName=X44 OS Language
AppVersion=1.1
AppPublisher=X44 Development Team
DefaultDirName={autopf}\X44
DefaultGroupName=X44
OutputBaseFilename=X44_Global_Setup
SetupIconFile=src\logo.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin

[Files]
; Core Engine and Transpiler
Source: "src\*"; DestDir: "{app}\src"; Flags: ignoreversion recursesubdirs
; Build Script
Source: "build.py"; DestDir: "{app}"; Flags: ignoreversion
; Examples for the user
Source: "examples\*"; DestDir: "{app}\examples"; Flags: ignoreversion recursesubdirs
; README
Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion isreadme

[Icons]
Name: "{group}\X44 Console"; FileName: "cmd.exe"; Parameters: "/k cd /d ""{app}"""
Name: "{commondesktop}\X44 Terminal"; FileName: "cmd.exe"; Parameters: "/k cd /d ""{app}"""

[Registry]
; Adds X44 to the System PATH so "python build.py" works anywhere
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; \
    ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; \
    Check: NeedsAddPath('{app}')

[Run]
; THE UPGRADE: Plays the X44 Welcome Voice

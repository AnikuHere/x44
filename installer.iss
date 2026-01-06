[Setup]
AppName=X44 OS Language
AppVersion=1.0
DefaultDirName={autopf}\X44
DefaultGroupName=X44
OutputBaseFilename=X44_Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Files]
Source: "src\*"; DestDir: "{app}\src"; Flags: ignoreversion recursesubdirs
Source: "build.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "engine.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\X44 Terminal"; FileName: "cmd.exe"; Parameters: "/k cd /d ""{app}"""

[Registry]
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; \
    ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; \
    Check: NeedsAddPath('{app}')

[Code]
function NeedsAddPath(Param: string): boolean;
var
  OrigPath: string;
begin
  if not RegQueryStringValue(HKEY_LOCAL_MACHINE,
    'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
    'Path', OrigPath) then begin
    Result := True;
    exit;
  end;
  Result := Pos(Uppercase(Param), Uppercase(OrigPath)) = 0;
end;

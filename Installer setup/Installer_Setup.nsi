; The name of the installer
Name "Budget Planner Installer"

; The file to write
OutFile "Budget Planner Installer.exe"

; The default installation directory
InstallDir C:\Budget_Planner

;--------------------------------

; Pages

Page components
Page directory
Page instfiles

;--------------------------------

; The stuff to install
Section "Files (required)"

SectionIn RO

; Set output path to the installation directory.
SetOutPath $INSTDIR

; Put file there
File "Budget_Planner.exe"
File /r "Databases"

SectionEnd

; Optional section (can be disabled by the user)

Section "Desktop Shortcut" SHORTCUT
    SetOutPath "$INSTDIR"
    CreateShortcut "$DESKTOP\Budget Planner.lnk" "$INSTDIR\Budget_Planner.exe" "" 

WriteUninstaller "$INSTDIR\Uninstall.exe"
 
SectionEnd
 
 
;--------------------------------    
;Uninstaller Section  
Section "Uninstall"
 
;Delete Files 
  RMDir /r "$INSTDIR\*.*"    
 
;Remove the installation directory
  RMDir "$INSTDIR"
 
 
SectionEnd
 
 
;--------------------------------    
;MessageBox Section
 
 
;Function that calls a messagebox when installation finished correctly
Function .onInstSuccess
  MessageBox MB_OK "You have successfully installed Budget Planner.Use the desktop icon to start the program."
FunctionEnd
 
Function un.onUninstSuccess
  MessageBox MB_OK "You have successfully uninstalled Budget Planner."
FunctionEnd
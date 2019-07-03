; Setup
PYTHON=%A_ProgramFiles%\Python37\python.exe
SEND_CMD=C:\Users\e302008\eclipse-workspace\rover_commands\src\cmd_send.py

; IED ON Command
!o::
Run,  %PYTHON% %SEND_CMD% IDN
return

; IED OFF Command
!i::
Run,  %PYTHON% %SEND_CMD% IDF
return

; Shutdown Rover Command
!q::
Run,  %PYTHON% %SEND_CMD% SR
return

; Left Forklift Left Command
^a::
Run,  %PYTHON% %SEND_CMD% LFL
return

; Left Forklift Center Command
^s::
Run,  %PYTHON% %SEND_CMD% LFC
return

; Right Forklift Right Command
^f::
Run,  %PYTHON% %SEND_CMD% RFR
return

; Right Forklift Center Command
^d::
Run,  %PYTHON% %SEND_CMD% RFC
return

; Left Forklift Up Command
^w::
Run,  %PYTHON% %SEND_CMD% LFU
return

; Left Forklift Down Command
^z::
Run,  %PYTHON% %SEND_CMD% LFD
return

; Right Forklift Up Command
^e::
Run,  %PYTHON% %SEND_CMD% RFU
return

; Right Forklift Down Command
^x::
Run,  %PYTHON% %SEND_CMD% RFD
return

; Start Recording Command
#r::
;Run,  
return

; Stop Recording Command
#s::
;Run,  
return
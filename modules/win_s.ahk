#s::
    Process, Exist, Everything.exe
    if (ErrorLevel) {
        IfWinActive, ahk_exe Everything.exe 
        {
            ActiveHwnd := WinExist("A")
            WinGet, ActivePID, PID, ahk_id %ActiveHwnd%
            WinGet, ProcessName, ProcessName, ahk_id %ActiveHwnd%
            WinMinimize , ahk_id %ActiveHwnd%
            return
        }
        else {
            Run, %everything_path%
            return
        }
    }
    else {
        Run, %everything_path%
    }
return
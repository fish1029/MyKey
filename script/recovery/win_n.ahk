#n::
    {
        Process, Exist, cxstudy.exe
        if (ErrorLevel) {

            IfWinActive, ahk_pid %ErrorLevel% 
            {
                WinMinimize , ahk_pid %ErrorLevel%
            }
            else {
                WinActivate, ahk_pid %ErrorLevel%
            }

        }
        else {
            Run, %cxstudy_path%
        }
        return

    }
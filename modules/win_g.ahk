#g::
    {
        Process, Exist, idea64.exe
        if (ErrorLevel) {
            IfWinActive, ahk_pid %ErrorLevel% 
            {
                WinMinimize , ahk_pid %ErrorLevel%
            }
            else {
                WinActivate, ahk_pid %ErrorLevel%
                IfWinActive, ahk_pid %ErrorLevel% 
                {
                    return
                }

            }
        }
        else {
            Run, %java_idea64_path%
        }
        return
    }
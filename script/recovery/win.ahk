IsDesktopRelated(hWnd) {
    if (!hWnd)
        return false

    WinGet, procName, ProcessName, ahk_id %hWnd%
    WinGetTitle, title, ahk_id %hWnd%
    WinGetClass, winClass, ahk_id %hWnd%

    ; 检查桌面相关窗口
    isDesktop := (procName = "explorer.exe" && (title = "" || title = "Program Manager"))

    ; 检查特定应用程序
    isSpecificApp := (procName = "Maye Lite.exe")|| (procName = "java.exe") || (procName = "Snipaste.exe") || (winClass = "HRNETFLOWTRAY" && procName = "HipsTray.exe")

    ; 检查系统托盘溢出窗口
    isTrayOverflow := (winClass = "TopLevelWindowForOverflowXamlIsland" && title = "系统托盘溢出窗口。")

    return (isDesktop || isSpecificApp || isTrayOverflow)
}

ShowWindowList(windows) {
    list := ""
    for i, window in windows {
        list .= "ID: " window.id " | Title: " window.title "`n"
    }
    MsgBox, % "窗口列表:`n" list
}

LWin:: 
    {
        return
    }

    Last_folder := ""
    Last_winword := ""
#d:: 
    {
        ActiveHwnd := WinExist("A")
        if (ActiveHwnd) {
            WinGet, ActivePID, PID, ahk_id %ActiveHwnd%
            WinGetClass, activeClass, ahk_id %ActiveHwnd%
            WinGet, activeProcess, ProcessName, ahk_id %ActiveHwnd%
            if (IsDesktopRelated(ActiveHwnd)) {
                WinActivate, ahk_id %Last_Hwnd%
                return
            }
            WinMinimize, ahk_id %ActiveHwnd%
            if(activeClass = "CabinetWClass" && activeProcess = "explorer.exe") {
                Last_folder := ActiveHwnd
                Last_Hwnd := ActiveHwnd
            }

            else {
                Last_Hwnd := ActiveHwnd
            }

        }
        else {
        }
        return 
    }

#e::
    WinGet, windowList, List, ahk_class CabinetWClass ahk_exe explorer.exe
    if (windowList = 0) {
        Run, explorer.exe 
        return
    }
    windows := []
    Loop, %windowList% {
        id := windowList%A_Index%
        WinGetTitle, title, ahk_id %id%
        windows.Push({id: id, title: title})
    }

    sortedWindows := []
    for i, window in windows
        sortedWindows.Push(window)

    Loop, % sortedWindows.Length() - 1 {
        for j, window in sortedWindows {
            if (A_Index < sortedWindows.Length() && sortedWindows[A_Index].id > sortedWindows[A_Index + 1].id) {
                temp := sortedWindows[A_Index]
                sortedWindows[A_Index] := sortedWindows[A_Index + 1]
                sortedWindows[A_Index + 1] := temp
            }
        }
    }
    WinGet, activeID, ID, A
    WinGetClass, activeClass, ahk_id %activeID%
    WinGet, activeProcess, ProcessName, ahk_id %activeID%
    isExplorer := (activeClass = "CabinetWClass" && activeProcess = "explorer.exe")

    if (isExplorer) {
        currentIndex := 0
        Loop, % sortedWindows.Length() {
            if (sortedWindows[A_Index].id = activeID) {
                currentIndex := A_Index
                break
            }
        }
        WinMinimize, ahk_id %activeID%
        Last_Hwnd := activeID
        if (sortedWindows.Length() <= 1) {
            return
        }
        nextIndex := Mod(currentIndex, sortedWindows.Length()) + 1
        nextID := sortedWindows[nextIndex].id
        WinActivate, ahk_id %nextID%
        WinRestore, ahk_id %nextID% ; 确保窗口不是最小化状态
    }
    else {
        WinActivate, ahk_id %Last_folder%
        IfWinActive, ahk_id %Last_folder% 
        {
            return
        }
        else {
            firstID := sortedWindows[1].id
            WinActivate, ahk_id %firstID%
        }
        if(Last_folder = "") {
            firstID := sortedWindows[1].id
            WinActivate, ahk_id %firstID%
        }

    }
return
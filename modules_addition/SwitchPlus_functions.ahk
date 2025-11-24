
SwitchOrActivateWordWindows(winClass, processName, appPath, ByRef LastHwndVar) {

    found := True
    if (found)
    {
        windows := []
        WinGet, windowList, List, ahk_class %winClass% ahk_exe %processName%

        if (windowList = 0) {
            Run, % appPath
            return
        }

        Loop, %windowList% {
            id := windowList%A_Index%
            windows.Push({id: id})
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
        isTargetWindow := (activeClass = winClass && activeProcess = processName)

        if (isTargetWindow) {
            currentIndex := 0
            Loop, % sortedWindows.Length() {
                if (sortedWindows[A_Index].id = activeID) {
                    currentIndex := A_Index
                    break
                }
            }
            WinMinimize, ahk_id %activeID%
            LastHwndVar := activeID
            if (sortedWindows.Length() <= 1) {
                return
            }
            nextIndex := Mod(currentIndex, sortedWindows.Length()) + 1
            nextID := sortedWindows[nextIndex].id
            WinActivate, ahk_id %nextID%
        }
        else {
            if(LastHwndVar = "") {
                firstID := sortedWindows[1].id
                WinActivate, ahk_id %firstID%
            } else {
                WinActivate, ahk_id %LastHwndVar%

                IfWinActive, ahk_id %LastHwndVar% 
                {
                    return
                }
                else {
                    firstID := sortedWindows[1].id
                    WinActivate, ahk_id %firstID%
                }
            }
        }
    }
}

GetActiveWindowInfo() {
    WinGet, activeID, ID, A
    WinGetClass, activeClass, ahk_id %activeID%
    WinGet, activeProcess, ProcessName, ahk_id %activeID%

    return {id: activeID, class: activeClass, process: activeProcess}
}

GetNextWindow(sortedWindows, activeID, ByRef LastHwndVar) {
    currentIndex := FindWindowIndex(sortedWindows, activeID)

    if (currentIndex = 0)
        return 0

    if (sortedWindows.Length() <= 1) {
        return 0
    }

    nextIndex := Mod(currentIndex, sortedWindows.Length()) + 1
    nextID := sortedWindows[nextIndex].id

    return nextID
}

FindWindowIndex(windowArray, windowID) {
    Loop, % windowArray.Length() {
        if (windowArray[A_Index].id = windowID) {
            return A_Index
        }
    }
    return 0
}
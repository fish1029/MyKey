

#InstallMouseHook
#SingleInstance Force
/*
MButton::
    if GetKeyState("CapsLock", "T")
    {
        Send, {Enter}
    }
    else
    {
        Send, {MButton}
    }
return

delay := 200 ; 初始
        count := 0 ; 计数

        While GetKeyState("XButton1", "P")
        {

            Send, {Delete}
            count++
            if (count < 3)
                delay := 150
            else if (count < 6)
                delay := 100
            else if (count < 10)
                delay := 50
            else
                delay := 30

            Sleep, %delay%
        }
*/

^RButton::
    Send, {Enter}
return

XButton2::
    if GetKeyState("CapsLock", "T")
    {
        Send, {XButton2}
    }
    else
    {
        Send, ^c
    }

return

XButton1::
    if GetKeyState("CapsLock", "T")
    {
        Send, {XButton1}
    }else{
        Send, ^v
    }

return

^XButton2::
    Send, {Home}
return

^XButton1::
    Send, {End}
Return

^WheelUp::
    Send, {Left}
return

^WheelDown::
    Send, {Right}
return

+^WheelUp::
    Send, +{Left}
return

+^WheelDown::
    Send, +{Right}
return

!WheelUp::
    Send, {Ctrl down}
    Send, {WheelUp}
    Send, {Ctrl up}
return

!WheelDown::
    Send, {Ctrl down}
    Send, {WheelDown}
    Send, {Ctrl up}
return
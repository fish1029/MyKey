;!a::Click
;PgDn::^#Right
;PgUp::^#Left

LWin & z::
    {
        send, ^+q 
    }
return

;CapsLock & q::#Left
;CapsLock & w::#Right
!t::send % SubStr(A_YYYY, 3) . "-" . A_MM . "-" . A_DD
;%A_Hour%:%A_Min%:%A_Sec%


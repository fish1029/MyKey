config := ["firefox", "everything", "cxstudy", "notepad", "obsidian", "systeminformer", "telegram", "java_idea64", "pycharm64", "winword", "vmware", "visual_stdio", "terminal", "bilibili", "powerpnt", "code", "android_stdio64", "reader"]
;--- start ---
FileRead, FileContent, config.txt

if (ErrorLevel) {
    MsgBox, 文件读取失败！
    return
}
LinesArray := StrSplit(FileContent, "`n")

for index, value in LinesArray {
    if (value == ""){
        continue
    }
    temp_c := StrSplit(value, """")
    head := temp_c[1]
    path := temp_c[2]
    for index1, value1 in config {
        if(value1 == head) {
            config[index1] := path
        }
    }

}
;--- end ---
firefox_path := config[1]
everything_path := config[2]
cxstudy_path := config[3]
notepad_path := config[4]
obsidian_path := config[5]
systeminformer_path := config[6]
telegram_path := config[7]
java_idea64_path := config[8]
pycharm64_path := config[9]
winword_path := config[10]
vmware_path := config[11]
visual_stdio_path := config[12]
terminal_path := config[13]
bilibili_path := config[14]
powerpnt_path := config[15]
code_path := config[16]
android_stdio64_path := config[17]
reader_path := config[18]
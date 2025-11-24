
import os.path
import shutil
import sys
import subprocess

class Config:
    def __init__(self, config_path):
        self.config = None
        self.other = None
        self.config_path = config_path
        self.raw_data = self.__read_config_file()

        self.get_config()
        self.get_other()

    def get_config(self):
        self.config = self.raw_data
    def get_other(self):
        self.other = None

    def convert_to_raw_data(self):
        self.raw_data = self.config

    def __read_config_file(self):
        with open(self.config_path, 'r', encoding = "utf-8-sig") as file:
            data = file.read()
        return data

    def write_config_file(self):
        self.convert_to_raw_data()
        with open(self.config_path, 'w', encoding = "utf-8-sig") as file:
            file.write(self.raw_data)

    def display(self):
        print(self.config)
        print(self.other)
        print(self.raw_data)

    def input(self, config):
        self.config = config

class KeybindConfig(Config):
    ahk_path = r"..\mykeys.ahk"
    exe_path = r"C:\Program Files\AutoHotkey\v1.1.37.02\AutoHotkeyU64.exe"

    def __init__(self, config_path):
        super().__init__(config_path)
        self.inuse = None
        self.get_inuse()
    def get_inuse(self):
        #遍历self.config 找到key不为-的name
        self.inuse = [[x[0], x[2]] for x in self.config if x[2] != "-"]


    def get_config(self):
        data = [x for x in self.raw_data.split("\n") if x != ""]
        self.config = [x.split("\"") for x in data]

    def get_other(self):
        self.other = None

    def convert_to_raw_data(self):
        a = ["\"".join(x) for x in self.config]
        self.raw_data = "\n".join(a)

    def display(self):
        for index, value in enumerate(self.config):
            a = f"[{index}]"
            print(f"\033[32m{a:<5}\033[37m{value[0]:<20}\033[32m{value[2]:<5}\033[37m")
            # print(f"\033[32m[{index}]\033[37m {value[2]} \033[32m{value[0]}\033[37m")

    def input(self, config):
        name = config[0]
        path = config[1]
        key = config[2]

        if name is None:
            raise ValueError("NAME cannot be empty")

        if key is not None:
            if len(key) == 1:
                if key != "-":
                    raise ValueError("KEY must be like #a or - ")
            elif len(key) == 2:
                if key[0] != "#":
                    raise ValueError("KEY must be like #a or - ")
            else:
                raise ValueError("KEY must be like #a or - ")
        if path is not None:
            if not os.path.isfile(path):
                raise ValueError("PATH 不是有效的")


        flag_name = []
        flag_path = []
        flag_key = []

        for index, value in enumerate(self.config):
            name_c = value[0]
            path_c = value[1]
            key_c = value[2]
            if name_c == name:
                flag_name.append(index)
            if path_c == path:
                flag_path.append(index)
            if key_c == key and key != "-":
                flag_key.append(index)

        if flag_name == [] and path is None:
            raise ValueError("PATH cannot be empty when NAME is new")
        if flag_path:
            print("[warning]: 配置中存在重复的路径:")
            for index in flag_path:
                print \
                    (f"           NAME: {self.config[index][0]} , PATH: {self.config[index][1]} , KEY: {self.config[index][2]}")

        if len(flag_key) == 1:
            self.config[flag_key[0]][2] = "-"
            print(f"已覆盖冲突的键: NAME {self.config[flag_key[0]][0]} KEY -")

        if len(flag_name) == 0:
            if key is not None:
                self.config.append([name, path, key])
            else:
                self.config.append([name, path, "-"])

        elif len(flag_name) == 1:
            if key is None and path is not None:
                self.config.append([name, path, "-"])
            elif key is not None and path is None:
                self.config[flag_name[0]] = [name, self.config[flag_name[0]][1], key]

        else:
            raise ValueError("config 存在多个重复的值")

    def del_config(self, name):
        flag_name = []
        for index, value in enumerate(self.config):
            name_c = value[0]
            if name_c == name:
                flag_name.append(index)
        if not flag_name:
            raise ValueError(f"[-] NAME不是有效的")
        print \
            (f"[delete]: NAME {self.config[flag_name[0]][0]} PATH {self.config[flag_name[0]][1]} KEY {self.config[flag_name[0]][2]}")
        del self.config[flag_name[0]]

    def change(self):
        tar_dir = os.path.join(os.path.dirname(self.config_path), "modules")
        source_dir = os.path.join(os.path.dirname(self.config_path), "fast_start")

        shutil.copytree(tar_dir, os.path.join(os.path.dirname(self.config_path), "script\\recovery"), dirs_exist_ok=True)

        config = [x for x in self.config if x[2] != "-"]
        for index, value in enumerate(config):
            name = value[0]
            path = value[1]
            key = value[2]
            source_path = os.path.join(source_dir ,f"{name}.txt")
            tar_path = os.path.join(tar_dir, f"win_{key[1]}.ahk")
            with open(source_path, "r", encoding="utf-8-sig") as file:
                source_data = file.read()
            with open(tar_path, "w", encoding="utf-8-sig") as file:
                file.write(f"{key}::\n" + source_data)

        print("changed!")

    def recovery(self):
        tar_dir = os.path.join(os.path.dirname(self.config_path), "..\\modules")
        shutil.copytree(os.path.join(os.path.dirname(self.config_path), "..\\script\\recovery") ,tar_dir, dirs_exist_ok=True)
        print("re!")

    def start(self, ahk_exe_path, script_full_path):
        script_dir = os.path.dirname(script_full_path)
        script_name = os.path.basename(script_full_path)
        cmd = f'start "" "{ahk_exe_path}" "{script_name}"'
        subprocess.Popen(
            cmd,
            cwd=script_dir,
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    def display_for_pp(self, lists):
        #不许要检查输入的数据, 因为调用情况固定
        # 颜色绿色: [#g] #示例
        #传入num的原因是想要通过一个数字选择跨组选择
        flag = 0
        for list_c2 in lists:
            print(f"\033[32m[{list_c2[0]}]\033[37m ", end="")

            for value in list_c2[1:]:
                if value != list_c2[1]:
                    print("     ", end="")
                #如果发现 [value, key] 在 self.inuse中证明被使用, 则使用绿色进行标记
                if [value, list_c2[0]] in self.inuse:

                    print(f"   \033[32m{flag}    {value}\033[37m") #示例:0    bilibili
                else:
                    #普通输出
                    print(f"   {flag}    {value}") #示例:0    bilibili
                flag += 1

class ProsConfig(Config):
    def __init__(self, config_path):
        super().__init__(config_path)

    def get_config(self):
        config = self.raw_data.split("\n")[0]
        config = config.split("[")[1]
        config = [x[1:-1] for x in config[:-1].split(", ") ]
        self.config = config

    def get_other(self):
        a = self.raw_data.split(";")[1]
        a = f";{a};--- end ---"
        self.other = a

    def convert_to_raw_data(self):
        a = [f"\"{x}\"" for x in self.config]
        a = ", ".join(a)
        a = f"config := [{a}]"

        b = self.other

        c = [f"{v}_path := config[{ i +1}]" for i ,v in enumerate(self.config) ]
        self.raw_data = "\n".join([a, b] + c)

    def display(self):
        for index, value in enumerate(self.config):
            a = f"[{index}]"
            print(f"{a:<5} {value}")

    def input(self, config):
        name = config[0]
        path = config[1]
        flag_name = []
        for index, value in enumerate(self.config):
            if value == name:
                flag_name.append(index)

        if len(flag_name) == 0:
            self.config.append(name)
            path_c = os.path.join(os.path.dirname(self.config_path), f"..\\fast_start\\{name}.txt")
            shutil.copy(path, path_c)
            print(f"[copy] {path} to: {path_c}")
        else:
            raise ValueError("NAME不是有效的")

    def del_config(self, name):
        flag_name = []
        for index, value in enumerate(self.config):
            if value == name:
                flag_name.append(index)

        if len(flag_name) == 1:
            print(f"[delete]: NAME {name}")
            del self.config[flag_name[0]]
        else:
            raise ValueError("NAME不是有效的")

if __name__ == "__main__":
    help = '''Usage: init
       -pp NUM
       -c NAME PATH KEY
       -c NAME KEY
       -c NAME -p PATH
       -c -r NAME
       -l
       -l proc
       -pp [NUM_list]
       --add NAME PROC_PATH
       --add -r NAME 
       --change
       --start
       --recovery
    '''
    config_path = r"..\config.txt"
    pros_path = r"..\modules\read_config.ahk"
    args = sys.argv[1:]
    myKey = KeybindConfig(config_path)
    myPros = ProsConfig(pros_path)


    try:
        if args[0] == '-c':
            name = None
            path = None
            key = None
            if args[1] == "-r":
                name = args[2]
                myKey.del_config(name)
                myKey.write_config_file()
            else:
                name = args[1]
                if len(args) == 4:
                    if args[2] == "-p":
                        path = args[3]
                        key = None
                    else:
                        path = args[2]
                        key = args[3]
                elif len(args) == 3:
                    key = args[2]
                    path = None
                myKey.input([name, path, key])
                myKey.write_config_file()

        elif args[0] == 'init':
            print(myKey.ahk_path)
            for index, value in enumerate(myKey.config):
                path = input(f"\033[32m{value[0]}\033[37m PATH: {value[1]}\n修改的路径? 为空则不修改: ")
                print(path)

        elif args[0] == '-l':
            if len(args) == 1:
                myKey.display()
            else:
                myPros.display()

        elif args[0] == '--add':
            if args[1] == "-r":
                myPros.del_config(args[2])
            else:
                myPros.input([args[1], args[2]])
            myPros.write_config_file()

        elif args[0] == '--change':
            myKey.change()

        elif args[0] == '--recovery':
            myKey.recovery()
        elif args[0] == '-pp':

            pp1 =["#g", "android_stdio64", "java_idea64", "pycharm64", "visual_stdio"]
            pp2 = ["#q", "winword", "telegram", "powerpnt", "reader"]
            pp3 = ["#b", "bilibili", "vmware"]


            list_c = [pp1, pp2, pp3]
            pp = []
            for i in list_c:
                pp += i[1:]


            if len(args) == 1:
                myKey.display_for_pp(list_c)
                sys.exit(0)

            else:
                name = None
                try:
                    names = [pp[int(x)] for x in args[1:]]
                except ValueError:
                    print("valueError!")
                    sys.exit(0)
                #已经获取了name 下面获取 key
                for name in names:
                    num = pp.index(name)
                    if 0 <= num <= 3:
                        key = pp1[0]
                    elif 4 <= num <= 6:
                        key = pp2[0]
                    elif 7 <= num <= 8:
                        key = pp3[0]
                    else:
                        print(f"{num}  valueError!")
                        continue
                    #判断 [name, key]是否在 myKey.inuse中 (没有实际作用的输入)
                    if [name, key] in myKey.inuse:
                        print(f"NAME {name} KEY {key} 已经在使用")
                        continue
                    else:
                        myKey.input([name, None, key])
                        myKey.write_config_file()
                myKey.change()
                myKey.start(myKey.exe_path, myKey.ahk_path)
                print(f"start [{myKey.exe_path}] [{myKey.ahk_path}]")
                sys.exit(1)


        elif args[0] == '--start':
            myKey.start(myKey.exe_path, myKey.ahk_path)
            print(f"start [{myKey.exe_path}] [{myKey.ahk_path}]")
        else:
            print(help)
    except IndexError:
        print(help)
        sys.exit()

    pros_path = r"..\modules\read_config.ahk"
    pros = ProsConfig(pros_path)




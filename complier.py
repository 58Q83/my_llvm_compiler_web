import os
import subprocess

from streamlit import success

test_file_path = "testfile.txt"
ans_file_path = "llvm_ir.txt"


def load_ans(is_error=False) -> str:
    if is_error:
        #TODO 加载error.txt
        pass
    else:
        try:
            with open(ans_file_path, "r") as f:
                ans = f.read()
                return ans
        except:
            return "Error"


def write_to_test_file(text: str):
    with open(test_file_path, "w") as f:
        f.write(text)
    pass


def compile_by_jar() -> str:
    cmd_res = subprocess.getstatusoutput("java -jar compiler.jar")
    print(cmd_res)
    success = True
    # TODO 修改java判断程序是否执行成功、添加时间限制，1s以上则失败
    if success:
        res = load_ans()
    return "```shell\n" + res + "\n```"

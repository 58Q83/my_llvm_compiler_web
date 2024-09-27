import os
import subprocess

from streamlit import success

test_file_path = "testfile.txt"
output_file_path = "llvm_ir.txt"
error_file_path = 'error.txt'

def load_ans(is_error=False) -> str:
    ans_file_path = error_file_path if is_error else output_file_path
    print(is_error)
    try:
        # TODO 解释错误类型
        with open(ans_file_path, "r") as f:
            ans = f.read()
            os.remove(ans_file_path)
            return ans
    except:
        return "File Error"


def write_to_test_file(text: str):
    with open(test_file_path, "w") as f:
        f.write(text)
    pass


def compile_by_jar() -> str:
    cmd_res = subprocess.getstatusoutput("java -jar Compiler.jar")
    print(cmd_res)
    success = (cmd_res[0] == 0) # 程序正常退出
    is_code_error = (cmd_res[1] != 'No Error!')
    # TODO 修改java判断程序是否执行成功、添加时间限制，1s以上则失败
    if success:
        res = load_ans(is_code_error)
    else:
        res = "run time error"
    return "```shell\n" + res + "\n```"

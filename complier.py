import os
import subprocess

from streamlit import success

test_file_path = "testfile.txt"
ans_file_path = "llvm_ir.txt"
TIME_LIMIT = 1


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
    cmd_res = subprocess.getstatusoutput(f"timeout {TIME_LIMIT} java -jar compiler.jar")
    print(cmd_res)
    if cmd_res[0] != 0:  # 失败的返回码通常不是0
        if 'timed out' in cmd_res[1]:  # 如果错误信息包含 timeout
            return "Execution Timeout (TLE)"
        else:
            return "Compilation Failed"
    # 如果成功，加载结果
    res = load_ans()
    return f"\nShell Output:\n{res}\n"
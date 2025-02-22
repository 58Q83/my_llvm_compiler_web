import gradio as gr
from complier import *

DEFAULT_CODE = "int main(){\tprintf(\"Hello World\n\");\n\treturn 0;\n}"


# 处理代码输入
def process_code(code):
    write_to_test_file(code)
    res = compile_by_jar()
    return f"{res}"


# 创建界面
interface = gr.Interface(
    fn=process_code,  # 函数
    inputs=gr.Code(language="c"),
    outputs=[gr.Code(language="shell")],
    flagging_mode="never"
)

# 启动界面
interface.launch(server_name='0.0.0.0', server_port=8501)

import gradio as gr


# 处理代码输入的函数
def process_code(code):
    return f"你输入的代码是:\n{code}"


# 创建界面
interface = gr.Interface(
    fn=process_code,  # 函数
    inputs=gr.Code(language="python"),  # 设置输入框为代码输入框，语言为Python
    outputs="text"  # 输出为文本
)

# 启动界面
interface.launch()

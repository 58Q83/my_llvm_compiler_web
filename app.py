import streamlit as st

st.set_page_config(page_title="Compiler", layout="wide")

st.title("SysY 2 llvm 简易编译器")
example_code = "int main(){\n \tprintf(\"Hello World\\n\");\n\treturn 0;\n}"
col1, col2 = st.columns(2, gap="large")

is_wrong = False
with col1:
    code_input = st.text_area(label="SysY", value=example_code,
                              height=600)

output = "```c\nint main(){\n \tprintf(\"Hello World\\n\");\n\treturn 0;\n}\n```"

if not is_wrong:
    with col2:
        st.markdown(output)

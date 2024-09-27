import streamlit as st

# 设置页面标题
st.title("Markdown 编辑器")

# 创建左右列，并设置宽度比例
col1, col2 = st.columns([2, 2], gap="large")

# 左侧输入框
with col1:
    markdown_input = st.text_area("输入Markdown内容", height=300)

# 右侧显示Markdown内容
with col2:
    st.subheader("渲染后的内容")
    st.markdown("```c\n" + markdown_input + "\n```")


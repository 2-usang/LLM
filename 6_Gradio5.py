import gradio as gr

def add(num1, num2):
    return num1 + num2

# 하나의 전체적인 화면을 만들 때 interface
interface = gr.Interface(
    fn=add,
    inputs = ['number', 'number'],
    outputs = 'number',
    title='계산기',
    description='숫자 두 개를 입력하세요.', flagging_mode="never" # flag를 하지 않음
)

interface.launch()
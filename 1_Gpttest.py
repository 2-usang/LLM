import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key = os.getenv("API_KEY")
)
# 키는 감춰놓고 이 페이지에서 키 불러오기

# temperature : 출력의 무작위성(창의성), 0.0<= x <1.0
# 값이 낮을수록 결정론적, 높을수록 무작위성
# 결정론적 -> 항상 비슷한 값으로 출력
# 무작위성 -> 항상 창의적인 값으로 출력
# when) 0.0 =>  항상 같은 입력 -> 같은 출력 ( ex 답, 수학) 
# when) 0.x => 적당한 무작위성(ex 마케팅 문구, 스토리 작성)

response = client.chat.completions.create(
    model = "gpt-4.1-2025-04-14",
    messages =[
        {"role":"user", "content":"왜 강남은 강남이라고 할까요?"}
    ],
    temperature=0.0
)
# print(response)
print(response.choices[0].message.content)
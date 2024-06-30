# <aside>
# 💡 이 과제에서는 파이썬 프로그래밍 언어를 활용하여 업다운 게임을 만드는 것이 목표입니다. 업다운 게임은 컴퓨터가 생각한 숫자를 맞추는 게임으로, 플레이어는 숫자를 입력하고 컴퓨터가 생각한 숫자와 비교하여 **"업(Up)"** 혹은 **"다운(Down)"** 힌트를 받아가며 숫자를 맞추는 게임입니다.

# </aside>

# **내용:**

# 1. 플레이어와 컴퓨터가 참여하는 업다운 게임을 만드세요.
# 1. 프로그램은 다음과 같은 기능을 포함해야 합니다.
#     - 컴퓨터는 1부터 100 사이의 랜덤한 숫자를 생성합니다.
#     - 플레이어는 숫자를 입력하고, 입력한 숫자와 컴퓨터의 숫자를 비교하여 "업" 또는 "다운" 힌트를 제공합니다.
#     - 플레이어가 컴퓨터의 숫자를 정확히 맞히면 시도한 횟수를 알려줍니다.
#     - 플레이어가 숫자를 맞힐 때까지 위 과정을 반복합니다.

#숫자 맞추기 게임

import random
from flask import Flask, render_template
app = Flask(__name__)

random_number = random.randint(1, 100)
i = 0

nu = {
    'random_number': random_number,
    'i': i,
}


# while = 맞출때까지 반복
while True:
    m_num = int(input("숫자를 입력하시오"))
    i = i+1
    if random_number == m_num:
        print('정답입니다')
        print(str(i) + '회 진행하였습니다')
        break
    elif 0 >= m_num or 100 < m_num:
        print("잘못된 결과값 입니다.")
        print(str(i) + '회 진행하였습니다')
    elif random_number >= m_num:
        print("업")
        print(str(i) + '회 진행하였습니다')
    elif random_number <= m_num:
        print("다운")
        print(str(i) + '회 진행하였습니다')

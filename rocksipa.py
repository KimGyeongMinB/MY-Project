# 가위바위보 게임

import random

# i = Player win, c_e = computer win, d_i = draw
i = 0
c_e = 0
d_i = 0

while True:

    # 가위 바위 보 값 입력 하는 곳
    my_rcp = input("가위 바위 보를 하십시오")
    # 컴퓨터가 랜덤으로 내는 가위바위보값
    com_rocksipa = ["rock", "scissors", "paper"]
    rosipa = random.choice(com_rocksipa)

    # 가위 바위 보를 이겼을 때 나타 나는 경우
    if my_rcp.lower() == "rock" and rosipa == "scissors":  # 플레이어가 주먹, 컴퓨터가 가위를 낸 경우
        i = i + 1
        print("win")
        print(str(i) + '회 승리')
    elif my_rcp.lower() == "scissors" and rosipa == "paper":  # 플레이어가 가위, 컴퓨터가 보자기 를 낸 경우
        i = i + 1
        print("win")
        print(str(i) + '회 승리')
    elif my_rcp.lower() == "paper" and rosipa == "rock":  # 플레이어가 보자기, 컴퓨터 가 주먹을 낸 경우
        i = i + 1
        print("win")
        print(str(i) + '회 승리')

        # 가위바위보를 비겼을 때 나타나는 경우
    elif my_rcp.lower() == "rock" and rosipa == "rock":
        d_i = d_i + 1
        print("draw. 계속진행해 주세요")
        print(str(d_i) + '회 무승부')

    elif my_rcp.lower() == "scissors" and rosipa == "scissors":
        d_i = d_i + 1
        print("draw. 계속진행해 주세요")
        print(str(d_i) + '회 무승부')

    elif my_rcp.lower() == "paper" and rosipa == "paper":
        d_i = d_i + 1
        print("draw. 계속진행해 주세요")
        print(str(d_i) + '회 무승부')

    # 가위바위보를 질때 나타나는 경우
    elif my_rcp.lower() == "rock" and rosipa == "paper":  # 플레이어가 주먹, 컴퓨터가 보자기를 낸 경우
        c_e = c_e + 1
        print("lose")
        print(str(c_e) + '회 패배')
    elif my_rcp.lower() == "scissors" and rosipa == "rock":  # 플레이어가 가위, 컴퓨터가 주먹를 낸 경우
        c_e = c_e + 1
        print("lose")
        print(str(c_e) + '회 패배')
    elif my_rcp.lower() == "paper" and rosipa == "scissors":  # 플레이어가 보자기, 컴퓨터가 가위를 낸 경우
        c_e = c_e + 1
        print("lose")
        print(str(c_e) + '회 패배')

    elif my_rcp.lower() == "stop":
        my_rcp = input("재시작 하시겠습니까? 재시작 하시려면 Yes, 종료하시려면 No을 입력해주세요")

    elif my_rcp.lower() == "reset" or my_rcp.lower() == "Yes":
        print("게임을 다시 시작하겠습니다.")
        i = 0
        c_e = 0
        d_i = 0

    elif my_rcp.lower() == "NO":
        print("게임을 종료합니다")
        print(str(i) + '회 승리')
        print(str(d_i) + '회 무승부')
        print(str(c_e) + '회 패배')

    elif my_rcp.lower() != "paper" or my_rcp.lower() != "scissors" or my_rcp.lower() != "rock" or my_rcp.lower() != "reset" or my_rcp.lower() != "stop" or my_rcp.lower() != "YES" or my_rcp.lower() != "NO":
        print("rock, paper, scissors 중 하나만 입력해 주십시오")

    print("플레이어 :" + my_rcp.lower())  # 가위바위보  입력값 출력
    print("컴퓨터 : " + rosipa)  # 컴퓨터 랜덤 가위바위보 값 출력

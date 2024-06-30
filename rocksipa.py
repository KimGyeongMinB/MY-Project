#가위바위보 게임

import random

i = 0
c_e = 0



def game_start():
    print("게임을 시작하겠습니다")



while True :
    # 가위바위보값 입력하는 곳
    my_rcp = input("가위 바위 보를 하십시오")
    # 컴퓨터가 랜덤으로 내는 가위바위보값
    com_rocksipa = ["rock", "scissors","paper"]
    rosipa = random.choice(com_rocksipa)

    #가위바위보를 이겼을 때 나타나는 경우    
    if my_rcp == "rock" and rosipa == "scissors":
        i = i+1
        print("win")
        print(str(i) +'회 승리')
    elif my_rcp == "scissors" and rosipa == "paper" :
        i = i+1
        print("win")
        print(str(i) + '회 승리')
    elif my_rcp == "paper" and rosipa == "rock" :
        i = i+1
        print("win")
        print(str(i) + '회 승리')

    #가위바위보를 비겼을 때 나타나는 경우
    elif my_rcp == "rock" and rosipa == "rock" :
        print("draw. 계속진행해 주세요") 
    elif my_rcp == "scissors" and rosipa == "scissors" :
        print("draw. 계속진행해 주세요")
    elif my_rcp == "paper" and rosipa == "paper" :
        print("draw. 계속진행해 주세요")
        

    #가위바위보를 질대 나타나는 경우
    elif my_rcp == "rock" and rosipa == "paper":
        c_e = c_e + 1
        print("lose")
        print(str(c_e) + '회 패배')
    elif my_rcp == "scissors" and rosipa == "rock" :
        c_e = c_e + 1
        print("lose")
        print(str(c_e) + '회 패배')
    elif my_rcp == "paper" and rosipa == "scissors" :
        c_e = c_e + 1
        print("lose")
        print(str(c_e) + '회 패배')

    print("플레이어 :" + my_rcp) # 가위바위보  입력값 출력
    print("컴퓨터 : " + rosipa) # 컴퓨터 랜덤 가위바위보 값 출력

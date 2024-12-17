# 기계학습과응용_개인 project : Game recommender system
# 목차
- [프로젝트 선정 이유](#프로젝트-선정-이유)
- [게임 종류 설명](#게임-종류-설명)
- [코드 설명](#코드-설명)
- [실행 결과](#실행-결과)
- [피드백](#피드백)

# 프로젝트 선정 이유
#### 
우연히 Youtube를 통해 '대학전쟁2'라는 프로그램을 알게 되었고, 흥미에 이끌려 OTT로 시청을 하게 되었습니다. 프로그램은 회차를 거듭할수록 정말 많고 다양한 게임들이 등장하였지만, 어떤 한 게임도 단순하거나 쉬워보이는 게임이라고 판단되지 않았습니다. 그래서, 친구들끼리 프로그램에 등장하는 게임들을 도전해보고 싶었습니다. 하지만, 모든 게임을 전부 시도해볼 수는 없었기에, 개인의 성향을 입력시키면 가장 흥미를 이끌 수 있을 것 같은 게임을 추천해주는 시스템을 설계해야겠다고 생각했습니다. 마침, Colab project idea에서 15번 항목에 해당되는 Recommender system과도 주제가 부합하여 'Game recommender system'라는 프로젝트를 최종적으로 결정하였습니다.

# 게임 종류 설명
####
가장 먼저, 프로그램에 등장하였던 여러 가지 게임들 중 코드에 인용한 일부 게임들의 규칙에 대해서 설명드리겠습니다. 코드에 총 9가지의 게임을 인용하였고, 대다수가 멘사게임과 결이 비슷한 게임이라고 생각하시면 더 이해하기 쉬울 것으로 예상됩니다.
<br>
### (1) 퍼펙트 넘버
'퍼펙트 넘버'는 특정 문장이 참이 되도록 빈칸에 알맞는 숫자를 넣는 게임입니다. 아래 사진이 바로 예시 문장입니다. 이 게임은 조건에 맞도록 오류를 제거하는 추론 능력을 요구합니다.
![image](https://github.com/user-attachments/assets/3612cc37-67b2-4a4f-977d-980dc563a444)
<br>
### (2) 밸런스 게임
'밸런스 게임'은 합이 20이 되도록 숫자 4개를 각자 선택한 후 상대방의 숫자조합을 추리하는 게임입니다. 본인 차례에 자신의 숫자 1개와 상대방의 숫자 1개를 비교하여 크고 작음에 대한 정보를 얻거나 2개의 합끼리 비교하여 크고 작음에 대한 정보를 얻습니다. 이를 기반으로 상대방의 숫자 조합인 ABCD를 알아내는 게임입니다. 제한 시간은 2분이며, 2자리 숫자, 소수점, 분수를 사용할 수 없습니다.

### (3) 픽셀 넘버
'픽셀 넘버'는 빨간색 픽셀 카드 3장과 파란색 픽셀 카드 3장이 각각 1장씩 짝을 이루어져 있는 상태에서 시작합니다. 이는 총 3자리 숫자를 의미하며, 빨간색 픽셀 카드에서 파란색 픽셀 카드로 이루어진 부분을 뺀 최종 숫자를 맞추는 게임입니다. 총 5라운드로 이루어지며, 3라운드를 먼저 승리하는 팀이 최종 승리합니다.

### (4) 요일 수식
'요일 수식'은 먼저 예시 날짜가 주어진 상태로 시작합니다(예를 들면, 5월 1일은 수요일). 그러면 자연스럽게 한달 달력이 완성됩니다. 이 때, 요일로 이루어진 수식을 보고 각 요일이 몇일을 의미하는지 맞추는 경기입니다. 예시 수식은 다음과 같습니다. <월 x 수 + 토 / 목 + 금>

### (5) 컬러 링크
'컬러 링크'는 가로 5칸, 세로 5칸으로 구성된 총 25개의 색깔판을 2분동안 암기한 후, 제시된 색깔로 이러진 판의 번호를 서로 번갈아가면서 말하는 경기입니다. 각 색깔판은 좌,우에 다른 색으로 구성되어 있으며, 총 색은 4가지로 구성되어있습니다. 예를 들어, 노란색이 주어져서 선공자가 노란색과 빨간색으로 구성되어있는 색깔판 번호를 말했다면, 후공자는 노란색으로 시작하는 색깔판이 아닌, 빨간색으로 시작하는 색깔판의 번호를 말해야 합니다.

### (6) 히든 알고리즘
'히든 알고리즘'은 출발지부터 도착지까지 도달할 수 있는 숨은 알고리즘을 찾는 게임입니다. 8x8 숫자판으로 구성되어있고, 숫자는 1부터 4까지 임의로 구성되어있습니다. 이 때, 1,2,3,4 사이의 이동 우선순위를 파악해야하고, 한 번 이동했을 때는 직전 칸으로 다시 이동하지 못한다는 규칙이 있습니다. 이동을 지속적으로 하다가 최우선 순위가 2방향 이상 존재할 때 멈추고 본인이 생각한 히든 알고리즘을 말해 정답을 맞추면 되는 게임입니다.

### (7) 합체 사다리
'합체 사다리'는 순서가 뒤섞인 1번부터 5번까지의 사다리가 주어집니다. 머리 속에서 해당 사다리들을 재조합하여 온전한 사다리 게임 형태로 만들고 난 뒤, 사다리게임을 진행합니다. 그러면 자연스럽게 도착지점에 번호 순서가 정해집니다. 이 번호 순서를 그대로 말하는 것이 아니라, 최초 배열된 사다리 순서에 알맞게 사다리를 조정 한 후 말하여 정답을 맞추는 게임입니다.

### (8) 가위바위보 체스
'가위바위보 체스'는 가로 8칸, 세로 8칸으로 구성된 체스판에서 경기를 진행합니다. 양 팀에는 각자 가위, 바위, 보가 2개씩 적혀있는 주사위를 4개씩 부여하고 최초 배치는 윗면이 가위, 바위, 보, 가위로 고정됩니다. 상대편과는 한 행씩 간격을 두고 배치됩니다. 말 이동 규칙은 가위는 3칸, 바위는 4칸, 보는 5칸으로 4방향 모두 이동가능하지만, 직전 칸으로는 이동할 수 없습니다. 상대 말 사이 통과는 가능하지만, 사이에 멈추는 것은 불가능하고 이동했을 때, 상대방 주사위와 맞닿으면 가위바위보 대결이 성사되고 진쪽을 주사위를 제거합니다. 양 팀 말 하나씩 남은 경우에는 가위바위보 대결을 이기거나, 상대편 진영 1열에서 2턴을 버티면 최종승리합니다.

### (9) 출구 전략2
'출구 전략2'는 한 팀당 8명의 인원이 필요한 게임이기 때문에 룰을 살짝 바꾸어 1대1 경기로 진행할 수 있도록 게임을 수정하였습니다. 7x7 형태의 게임판 정중앙에 탈출문이 위치합니다. 개인에게는 6개의 말이 존재하고 최초 배치는 절반을 넘지 않는 선에서 자유롭게 배치할 수 있지만, 출구문이 존재하는 열과 행에는 배치할 수 없습니다. 참고로, 탈출문이 존재하는 행 양쪽 끝에는 장애물이 존재합니다. 말은 일직선으로만 움직일 수 있고, 장애물 혹은 이동말이 앞에 위치하면 멈추어야합니다. 즉, 앞에 아무것도 존재하지 않는다면, 반드시 끝까지 이동해야합니다. 1분 안에 반드시 본인의 말을 이동시켜야 하고, 시간이 초과되면 기회는 상대편에게 넘어갑니다.

# 코드 설명

코드 설명을 진행하기 이전에 각 게임의 특징(수리능력, 기억력, 창의력, 논리력, 제한 시간, 패턴 인식 능력)은 1부터 5까지의 스케일 중 상대적 비교를 통해 입력하였음을 알려드립니다. 알고리즘 코드를 작성하는 데에 있어서 각 게임의 정보가 필요하기 때문에 위 과정을 선행하였습니다.

1. 선행 라이브러리 설명

이 프로젝트는 데이터 포인트의 가장 가까운 이웃들을 기반으로 예측하는 거리 기반 알고리즘인 KNN을 사용합니다. 일반적인, 딥러닝 모델로 알려진 CNN과는 확연한 차이를 보입니다. 주로 이미지 혹은 비정형 데이터를 처리하는데는 CNN이 유리한 반면, 거리를 기반으로 하는 Classification과 Regression 문제에는 KNN이 더 유리합니다. 해당 프로젝트는 사용자의 성향이라는 데이터들을 입력받아서 가장 최적화된 솔루션을 도출해내는 관점으로 볼 수 있으므로, 학습이 선행되지 않아도 되기 때문에 계산량이 적을 지 몰라도, 데이터를 입력 받은 후에는 오히려 계산량이 더 많아진다는 것을 알 수 있습니다. 따라서, 이를 구현하기 위해 다양한 라이브러리들을 import문으로 불러온 뒤, 본격적인 코드를 시작하였습니다. 주석에 보다 자세한 설명을 작성해넣었습니다.
![image](https://github.com/user-attachments/assets/7e4b8fa6-2502-4ff9-b84d-4287e9f5dca1)


2. 사전 준비 코드에 대한 설명

  - 게임 데이터 준비
  ![image](https://github.com/user-attachments/assets/d2c785b0-da79-4226-9d74-af15f8d554a8)

  - 사용자 성향 입력 함수
  ![image](https://github.com/user-attachments/assets/b0a141a5-ed17-4536-b4f9-e2b56b59860a)

  - KNN 모델 준비 및 적용
  ![image](https://github.com/user-attachments/assets/46eee285-28d3-4932-86a6-fe93e1d1d3a6)

  - 사용자 성향을 기반으로 게임 추천해주는 함수
  ![image](https://github.com/user-attachments/assets/7162045d-d3be-47e7-9fee-bdf4530824d9)

  - 피드백 수집 함수
  ![image](https://github.com/user-attachments/assets/b145a208-3e9d-4da7-a774-bca5b7bc1737)

  - 피드백을 통한 사용자 성향 조정 함수
  ![image](https://github.com/user-attachments/assets/3db22bbb-5639-4812-80af-3bc40eb54e79)


<br>
3. 메인 함수 설명
  
   - 이제 본격적으로 메인 함수를 실행 시킵니다. 가장 먼저, 사용자의 성향을 입력받아야 합니다. 이후, 추후 사용될 '제외 게임 목록'에 대한 집합을 먼저 만들어줍니다. 여기서부터는 사용자의 피드백에서 만족도가 5가 나와야지만 추천 프로그램이 종료됩니다. 현 상황에서는 게임이 9가지밖에 존재하지 않고, 앞서 최우선순위에 있는 게임 3개씩 표에 도출되어 추천하도록 프로그램이 설명되어있어서 단순하다고 생각될 수 있지만, 해당 프로그램이 더 확장되어서 게임의 가짓수가 정말 많아진다면, 이 과정은 더 유의미해질 것으로 예상됩니다. While문이 사용하였기 때문에, 머신러닝을 통해서 추천 게임 목록이 형성되고 이를 표로 시각화하여 도출합니다. 이후, 피드백을 수집하고 만족도가 5로 입력되지 않는다면, 추천된 게임을 제외한 나머지 게임들에서 이 과정을 반복하여 진행합니다. 해당 과정을 진행 할 때는 피드백을 통해서 성향을 재조정하여 추천 알고리즘에 적용되어 결과가 도출됩니다.
   ![image](https://github.com/user-attachments/assets/6023bcc2-c772-4119-ad2a-c94d22303ce9)


# 실행 결과

1. 사용자의 성향을 각 항목마다 입력합니다.
![image](https://github.com/user-attachments/assets/81bc8d93-f82d-4635-9c8c-7be01c5b728e)

2. 모두 입력하면, 이들을 데이터로 받아서 KNN 과정을 거쳐 추천 게임이 3개씩 표로 도출됩니다.
![image](https://github.com/user-attachments/assets/a0702217-58e8-4010-a99a-43ef0738797c)

3. 추천해준 게임들에 대해서 만족도를 입력받습니다. 3개의 게임 중 만족도가 5인 게임이 1개도 존재하지 않으면 5번과정으로 넘어가고, 만족도가 5인 게임이 존재하면 바로 6번 과정으로 넘어갑니다.
![image](https://github.com/user-attachments/assets/b9ffd186-1e3b-4d9c-ac05-b67260167c23)

4. 입력받은 만족도에 따라서 사용자의 성향이 업데이트 됩니다.
![image](https://github.com/user-attachments/assets/28d7285e-2283-4a6a-8e6b-a0e504b056c1)

5. 조정된 성향을 기반으로 하여, 다시 게임을 3가지 추천하고 이를 표로 시각화합니다.
![image](https://github.com/user-attachments/assets/f623bce7-3b89-4659-b367-6bf9de2aeda2)

6. 만족도 5인 게임이 존재 시, 추천 프로그램이 종료됩니다.
![image](https://github.com/user-attachments/assets/20c0bae2-48eb-4f77-a58e-ef72e2d79512)

# 피드백
####
코드를 실행시켜 게임을 처음부터 종료될 때까지 구동하면 모두 정상적으로 돌아간다는 사실을 알 수 있습니다. 하지만, 핵심적으로 보완해야한다고 판단되는 부분도 있었습니다. 바로, n번째 플레이어가 다른 플레이어들의 hidden card를 확인하는 과정에서 terminal에 이미 (n-1)번째 플레이어까지 다른 플레이어들의 hidden card를 확인하는 과정이 모두 작성되어있다는 점입니다. r을 입력했을 때, 본인만 그 과정을 볼 수 있어야하고 기록이 자동적으로 지워지게끔 하는 코드로 수정해야합니다. 하지만, terminal에서 이 부분이 보이지 않게 하는 방법이 도저히 떠오르지 않았고 따라서, 코드를 그대로 둘 수 밖에 없었습니다. 그래서 만약, 실제 상황에서 이 툴을 그대로 활용하여 게임을 진행하여야 한다면, 사회자가 한 명 존재하여 상황을 조율하면서 게임을 진행해야합니다.

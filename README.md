# 기계학습과응용_개인 project : Game recommender system
# 목차
- [프로젝트 선정 이유](#프로젝트-선정-이유)
- [게임 종류 설명](#게임-종류-설명)
- [코드 설명](#코드-설명)
- [실행 결과](#실행-결과)
- [프로젝트 결론 및 총평](#프로젝트-결론-및-총평)

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
'합체 사다리'는 순서가 뒤섞인 1번부터 5번까지의 사다리가 주어집니다. 머리 속에서 해당 사다리들을 재조합하여 온전한 사다리 게임 형태로 만들고 난 뒤,명
  - 이 프로그램은 사용자의 성향을 입력 받은 뒤, 거리에 따라 머신러닝을 진행하는 KNN 모델을 사용하여 게임을 추천해주는 방식을 사용합니다. 따라서, 아래 첨부된 사진과 같은 라이브러리들을 import문을 이용하여 선언해주고 난 뒤, 코드를 시작하였습니다.
![image](https://github.com/user-attachments/assets/2cc27bb1-787a-4cec-8a0c-dce33968490a)

### 2. 사전 준비에 대한 설명
  - 게임 데이터 준비
    ![image](https://github.com/user-attachments/assets/743a2228-d078-4c03-877e-7ade9de1865a)
  - 사용자 성향 입력 함수
    ![image](https://github.com/user-attachments/assets/8e0de768-665f-4726-b0d4-3a859542d1c8)
  - KNN 모델 초기화 및 학습
    ![image](https://github.com/user-attachments/assets/ee2f7cf2-18f9-4065-b5f8-21d5643d37b0)
  - 게임 추천 함수
    ![image](https://github.com/user-attachments/assets/b96fdabd-0982-4285-99c4-df3e19a93afc)
  - 피드백 수집 함수
    ![image](https://github.com/user-attachments/assets/a2d15539-51bc-463a-a588-08e42d0bb67a)
  - 성향 조정 함수
    ![image](https://github.com/user-attachments/assets/5541018a-8463-464c-a4fe-d85fff74a547)

### 3. 메인 함수에 대한 설명

   - 가장 먼저, 사용자의 성향을 입력받은 뒤, 추후 사용될 '제외할 게임 목록'을 set으로 생성합니다. 이후, While문을 사용해주는데 이는 만족도가 5인 게임이 나올 때까지 게임을 추천하도록 프로그램을 완성시키고자 작성했습니다. While문 내부에는 입력받은 데이터를 KNN 모델에 적용시켜 추천 게임 목록이 도출되도록 하는 코드가 존재합니다. 또한, 해당 목록이 시각적으로 볼 수 없기에 tabulate 라이브러리를 사용해서 표로 도출되게끔 만들어줍니다. 목록이 완성되면, 피드백을 수용받고 만족도가 5인 게임이 존재하지 않는다면 성향을 업데이트하여 다시 게임을 추천하도록 합니다. 반면, 만족도가 5인 게임이 존재한다면 프로그램은 그 즉시 종료되는 것으로 함수가 완성되었습니다.
   ![image](https://github.com/user-attachments/assets/c0a23038-81c3-47a9-a8b8-4b81e84a42f7)

  
# 실행 결과

#### (1) 사용자의 성향을 입력받아서 데이터로 저장합니다.
![image](https://github.com/user-attachments/assets/6587bc37-ea49-4f2a-8e42-30fa4c30bbe3)

#### (2) 데이터를 기반으로 하여 추천 게임 3가지가 목록으로 작성되고 시각화를 위해 표 또한 생성됩니다.
![image](https://github.com/user-attachments/assets/c00d3264-e69a-4505-8374-dc92be942823)

#### (3) 각 추천 게임에 대한 만족도를 입력합니다. 아래 첨부된 사진은 만족도가 5인 게임이 존재하지 않는 경우이므로, (4)번 과정으로 넘어갑니다. 만약, 최초 만족도를 입력하는 과정에서 5인 게임이 존재한다면, (5)번 과정으로 넘어갑니다.
![image](https://github.com/user-attachments/assets/2cc06393-cb54-48cf-9dc1-044a214b1fbe)

#### (4) 만족도가 5인 게임이 존재하지 않으므로, 성향이 업데이트됩니다. 조정된 성향을 기반으로 하여 다시 3가지 게임을 추천하고 이 또한 시각화를 위해 표가 생성됩니다.
![image](https://github.com/user-attachments/assets/4c0d3b2a-0af2-4426-aa99-cb9da6bdbda4)
![image](https://github.com/user-attachments/assets/8079cd0f-d18b-4462-ac0c-17e6bbf3c85a)

#### (5) 추천받은 게임에 대하여 만족도가 5로 입력되면 추천 프로그램이 종료됩니다.
![image](https://github.com/user-attachments/assets/4f21667f-c3b6-4eb1-960c-cce12db7a6a7)

# 프로젝트 결론 및 총평
#### 
앞서 언급드린 바와 같이, 이 프로젝트에서 쓰인 프로그램은 게임의 갯수가 많아질수록 더 확실한 이득을 보는 구조를 가지고 있습니다. 게임의 갯수가 적으면 모든 게임을 다 해보면서 자기 성향과 맞는 게임을 하면 되지만, 게임의 갯수가 늘어날수록 물리적인 한계가 있기 때문입니다. 또한, 다인원이 게임을 진행하고 싶을 때 어떤 게임을 할 지 애매한 경우들이 존재합니다. 이 때, 서로 토의하여 게임에서 요구하는 능력에 대한 선호도를 정하여 입력한다면 게임을 정하는 과정이 굉장히 수월해집니다. 게다가, 최초에 추천받은 게임에 흥미를 느끼지 못했다고 하더라도, 후순위로 추천해주는 게임들의 목록이 작성되기 때문에 이 과정에 있어서 시간을 굉장히 줄일 수 있습니다. 하지만, 문제점 또한 명확하다고 생각합니다. KNN 모델을 사용하기 때문에 데이터 전처리 과정에서 소요되는 시간보다 데이터 후처리 과정에서 소요되는 시간이 더 크다는 점은 당연합니다. 그러나, 게임의 종류가 많아지고 이에 대한 정보들이 선제적으로 다수 입력될수록 데이터 후처리 과정에서 소요되는 시간이 점점 오래걸리게 될 것입니다. 만약, 정말 오랜시간이 소요된다면, 머신러닝을 사용하는 과정에 있어서 KNN 모델이 아니라, 다른 모델로 이 프로그램을 구현하는 것이 더 유리하지 않나라는 의문점을 품을 수 있다고 생각합니다. 그러나, 개인적인 의견을 첨언하자면, 데이터 후처리과정에서 소요되는 시간이 아무리 오래걸린다고 하더라도 모든 게임을 직접 다 해본 뒤 알맞는 게임을 찾는 시간보다는 적게 걸릴 것입니다. 또한, 이러한 추천 알고리즘을 만드는 과정에서 Train set, Test set을 이용하여 Regression 문제를 푸는 방법 혹은 CNN 모듈 등 다른 방법들보다 KNN 모델이 가장 적합하다고 생각하기 때문에 이와 같이 프로그램을 설계하였습니다.

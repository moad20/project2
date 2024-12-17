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


# 코드 설명

가장 먼저, import문을 활용하여 이후 코드에서 사용할 tool을 불러와야합니다. 따라서, 카드 덱을 섞는데 필요한 random 함수와 게임의 시각화를 위해서 필요한 prettytable에 대한 코드를 극 초반부에 작성합니다. 다음은 본격적으로, 코드에 대한 설명입니다.

1. Class 정의 및 Class 내 함수 설명
   
  - __init__(self, name, chips) : 플레이어의 이름과 칩 수를 초기화하고, 볼 수 있는 카드와 볼 수 없는 카드, 그리고 배팅 금액을 초기화합니다.
  ![init함수](https://github.com/moad20/project/assets/163985965/87d40a9f-7b22-415e-a097-53d715da3e25)

  - place_bet(self) : 플레이어가 칩을 배팅합니다. 배팅 금액이 올바른 범위 내에 있는지 확인하고, 칩을 차감합니다.
  ![place_bet 함수](https://github.com/moad20/project/assets/163985965/242685e9-85ce-45e8-9019-a51c8361d829)

  - receive_cards(self, visible_card, hidden_card) : 플레이어가 두 장의 카드를 받습니다. 한 장은 볼 수 있고, 다른 한 장은 볼 수 없습니다.
![receive_cards 함수](https://github.com/moad20/project/assets/163985965/67772d7d-64d2-4f1d-b51d-6cd3675583bd)

  - reveal_cards(self) : 플레이어의 카드를 공개합니다.
![reveal_cards 함수](https://github.com/moad20/project/assets/163985965/ca859344-a6b8-435d-a38f-71049f91e274)

  - total_card_value(self) : 플레이어의 두 카드 값을 합산하여 반환합니다.
    ![total_card_value 함수](https://github.com/moad20/project/assets/163985965/6d6ea470-e807-4900-a3fd-21cf738a324f)

<br>
2. 메인 함수를 위한 함수 설명

  - deal_cards(deck, players) : 덱을 섞고 각 플레이어에게 두 장의 카드를 나눠줍니다.
  ![deal_cards 함수](https://github.com/moad20/project/assets/163985965/6b4d15f4-90c9-4748-a4e6-31002faf8962)

  - determine_winner(players) : 플레이어들의 카드 합산 값을 비교하여 승자를 결정합니다.
  ![determine_winner 함수](https://github.com/moad20/project/assets/163985965/333beb85-7188-430a-ac6c-9f8b6b1f8394)

  - display_game_state(players, round_number) : 현재 게임 상태를 표로 출력합니다. 각 플레이어의 이름, 칩 수, 배팅 금액, 볼 수 있는 카드, 볼 수 없는 카드 상태
  ![display_game_state 함수](https://github.com/moad20/project/assets/163985965/97e03a81-6bf3-4569-896c-eb2c327376a9)

  - reveal_other_players_visible_cards(players, current_player) : 현재 플레이어가 다른 플레이어들의 볼 수 있는 카드를 볼 수 있도록 합니다.
    ![reveal_other_players_visible_cards 함수](https://github.com/moad20/project/assets/163985965/6d8fe310-63e1-409f-8917-19fbc8c87f9b)

<br>
3. 메인 함수 설명
  
  - main( ) : 1부터 13까지 카드 덱 4세트를 생성하고, 플레이어 수를 입력받아 최소 2명 이상이 게임에 참여하도록 합니다. 해당 카드 덱을 생성할 때, 실제 카드처럼 문양은 고려하지 않았습니다.
  ![main1](https://github.com/moad20/project/assets/163985965/919e1678-9290-486c-af36-ea1338075480)

  - 플레이어 객체를 생성하고 초기 칩 수를 100으로 설정하는 코드입니다. 이와 동시에, 최초의 라운드 번호를 1로 지정하는 코드도 추가하였습니다.
    ![player](https://github.com/moad20/project/assets/163985965/961ee438-d3e9-491b-a601-cec0b4d0b0ef)

  - while문을 이용하여 게임을 진행하였습니다. 이때, 모든 플레이어가 칩을 가지고 있는 동안 게임을 진행하고 한 명의 플레이어라도 칩 수가 0이 되면, 게임 룰에 적혀있는 것처럼 게임을 종료합니다. 앞서 만들어낸 함수를 통해 카드를 분배하고 현재 상태를 알려주는 테이블이 보여지게 만듭니다. 이후, 특정 명령어를 입력하면, 다른 플레이어들의 hidden card를 볼 수 있게 한 뒤, 해당 과정이 종료되면 배팅을 시작합니다. 각 배팅이 끝나면, 즉각적으로 배팅 후 상태를 표시해주는 테이블이 다시 보여지게 만듭니다. 이후 과정은 간단합니다. 카드를 공개한 뒤, 승자가 정해지고 해당 라운드 승자가 모든 배팅 금액을 가져갑니다. 이러한 과정을 모두 마치면, 라운드 넘버가 1씩 올라가고 이를 게임 규칙에 따라, 한 명의 플레이어라도 칩 수가 0이 될 때까지 게임을 반복합니다.
  ![while2](https://github.com/moad20/project/assets/163985965/538af4da-fae9-4349-bf6a-44dd1e6f3e19)

  - 승자 리스트에 존재하는 최종 승자를 도출해내는 코드로 메인 함수를 마무리합니다.
  ![main last](https://github.com/moad20/project/assets/163985965/7c2277e6-e09f-40de-9193-024ebbf20d70)

  - main함수를 실행시키면 게임을 시작합니다.
  ![main last](https://github.com/moad20/project/assets/163985965/559c288a-1e90-4279-8a7b-71673d8191c5)

# 실행 결과

1. 플레이어의 인원수를 설정하고 현재 상황을 보여주는 테이블을 도출합니다.
![1](https://github.com/moad20/project/assets/163985965/79dce09f-cc7a-4416-8bfc-0c9ba5b78b72)

2. r키를 눌러 각각 상대방의 visible card를 확인합니다.
![2](https://github.com/moad20/project/assets/163985965/051e674e-5860-423f-8b06-63393fb8c114)

3. 모든 플레이어가 배팅을 한 뒤, 라운드의 승자가 누구인지 알려주는 결과를 테이블로 도출합니다.
![3](https://github.com/moad20/project/assets/163985965/34b0bcd6-d4c3-4672-8569-24c1062a96ea)

4. 이후, 바뀐 보유 배팅 금액을 기반으로 한 현 상황 테이블을 불러옵니다.
![4](https://github.com/moad20/project/assets/163985965/01f7b81d-7df7-4403-8a6e-da1345b27db1)

5. 게임이 종료될 때까지, 라운드를 반복해서 진행합니다.
![5](https://github.com/moad20/project/assets/163985965/38d96bc8-ccf1-42d8-9ed7-9f3dae19cda9)

6. 게임의 최종 단계 모습은 다음과 같습니다.
![6](https://github.com/moad20/project/assets/163985965/6eb1ed75-a17d-44af-9667-12518f96c358)
![7](https://github.com/moad20/project/assets/163985965/6fbdf627-5daf-4d61-8c90-9713941cda89)

# 피드백
####
코드를 실행시켜 게임을 처음부터 종료될 때까지 구동하면 모두 정상적으로 돌아간다는 사실을 알 수 있습니다. 하지만, 핵심적으로 보완해야한다고 판단되는 부분도 있었습니다. 바로, n번째 플레이어가 다른 플레이어들의 hidden card를 확인하는 과정에서 terminal에 이미 (n-1)번째 플레이어까지 다른 플레이어들의 hidden card를 확인하는 과정이 모두 작성되어있다는 점입니다. r을 입력했을 때, 본인만 그 과정을 볼 수 있어야하고 기록이 자동적으로 지워지게끔 하는 코드로 수정해야합니다. 하지만, terminal에서 이 부분이 보이지 않게 하는 방법이 도저히 떠오르지 않았고 따라서, 코드를 그대로 둘 수 밖에 없었습니다. 그래서 만약, 실제 상황에서 이 툴을 그대로 활용하여 게임을 진행하여야 한다면, 사회자가 한 명 존재하여 상황을 조율하면서 게임을 진행해야합니다.

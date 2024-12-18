import pandas as pd  # 데이터프레임을 사용하기 위한 라이브러리
import numpy as np  # 수학적 계산 및 배열 처리를 위한 라이브러리
from sklearn.neighbors import NearestNeighbors  # KNN 모델 사용을 위한 모듈
from sklearn.preprocessing import StandardScaler  # 데이터 정규화를 위한 모듈
from tabulate import tabulate  # 표 형태로 출력하기 위한 라이브러리

# 게임 데이터를 준비
game_data = {
    'Game': ['퍼펙트넘버', '밸런스게임', '픽셀 넘버', '요일 수식', '컬러 링크', 
             '히든 알고리즘', '합체 사다리', '가위바위보 체스', '출구전략2'],
    'Mathematical capacity': [3, 3, 1, 5, 1, 2, 2, 4, 1],  # 수리능력
    'Logical': [3, 2, 1, 1, 1, 4, 1, 5, 5],  # 논리력
    'Memory': [1, 4, 5, 3, 5, 4, 5, 3, 2],  # 기억력
    'Time': [1, 3, 1, 2, 3, 3, 4, 5, 5],  # 소요 시간
    'Creativity': [2, 1, 1, 2, 1, 4, 4, 5, 5],  # 창의력
    'Pattern': [1, 1, 4, 4, 2, 5, 1, 5, 4]  # 패턴 인식 능력
}
games_df = pd.DataFrame(game_data)  # 데이터를 DataFrame으로 변환

# 사용자 성향 입력 함수
def get_user_preferences():
    try:
        print("사용자의 성향을 입력하세요 (1-5 스케일) :")
        memory = int(input("기억력 선호도 (1-5) : "))
        logic = int(input("논리력 선호도 (1-5) : "))
        math_capacity = int(input("수리능력 선호도 (1-5) : "))
        pattern = int(input("패턴 인식 능력 선호도 (1-5) : "))
        creativity = int(input("창의력 선호도 (1-5) : "))
        time = int(input("소요시간 선호도 (1-5) : "))

        # 입력값 검증 - 1~5 사이가 아닌 경우 예외 처리
        if any(x < 1 or x > 5 for x in [memory, logic, creativity, pattern, time, math_capacity]):
            raise ValueError("모든 입력은 1에서 5 사이여야 합니다.")
        return {
            'Memory': memory, 'Logical': logic, 
            'Creativity': creativity, 'Pattern': pattern, 
            'Time': time, 'Mathematical capacity': math_capacity
        }
    except Exception as e:  # 예외 발생 시 기본값 반환
        print(f"입력 오류: {e}. 기본 성향으로 설정합니다.")
        return {k: 3 for k in ['Memory', 'Logical', 'Creativity', 'Pattern', 'Time', 'Mathematical capacity']}

# 추천에 사용될 특징(Feature) 정의
features = ['Memory', 'Logical', 'Creativity', 'Pattern', 'Time', 'Mathematical capacity']

# 데이터 스케일링 - KNN 모델은 거리 기반이므로 데이터 정규화 필요
scaler = StandardScaler()
scaled_data = scaler.fit_transform(games_df[features])

# KNN 모델 초기화 및 학습
knn = NearestNeighbors(n_neighbors = 5, metric='euclidean')
knn.fit(scaled_data)

# 사용자의 데이터를 바탕으로 게임을 추천하는 함수
def recommend_games(user_data, games_df, knn_model, excluded_games = set(), top_n = 3):
    # KNN 모델을 사용해 가장 가까운 게임 인덱스를 찾음
    distances, indices = knn_model.kneighbors(user_data)
    # 추천 게임 추출 (거리 기반)
    recommended_games = games_df.iloc[indices[0]]
    # 이미 추천된 게임을 제외
    recommended_games = recommended_games[~recommended_games['Game'].isin(excluded_games)]
    # 추천할 게임이 없으면 빈 DataFrame 반환
    if recommended_games.empty:
        return pd.DataFrame()
    return recommended_games.head(top_n) # 상위 n개 추천

# 추천된 게임에 대한 피드백 수집 함수
def collect_feedback(recommended_games):
    # 피드백 결과 저장
    feedback = {}
    print("추천 게임에 대한 만족도를 입력하세요 (1-5 스케일):")
    
    # 각 추천 게임에 대해 사용자 만족도 입력받기
    for game in recommended_games['Game']:
        try:
            score = int(input(f"{game} 만족도 (1-5) : "))
            if score < 1 or score > 5:
                raise ValueError("만족도는 1에서 5 사이여야 합니다.")
            feedback[game] = score
            if score == 5:  # 만족도가 5인 경우 프로그램 종료
                return feedback, True
        # 입력 오류 시 기본값 3으로 설정
        except Exception as e:
            print(f"입력 오류 : {e}. 기본값 3으로 설정합니다.")
            feedback[game] = 3
    return feedback, False

# 사용자 피드백을 바탕으로 성향을 조정하는 함수
def update_preferences_with_feedback(user_preferences, feedback, games_df):
    for game, score in feedback.items():
        # 게임의 특징 데이터를 추출
        game_features = games_df[games_df['Game'] == game][features].iloc[0]  # 게임 특징 데이터
        # 사용자 성향 조정 - 점수의 차이만큼 조정
        for feature in features:
            user_preferences[feature] += 0.5 * (score - 3) * game_features[feature]  # 점수 차이에 따른 업데이트
    return user_preferences

# 메인 실행 코드
if __name__ == "__main__":
    user_preferences = get_user_preferences()  # 사용자 성향 입력
    excluded_games = set()  # 추천에서 제외할 게임 목록

    # 반복적으로 추천 및 피드백 수집
    while True:
        # 사용자 성향 데이터를 모델에 맞게 변환
        user_data = np.array([[user_preferences[feature] for feature in features]])
        scaled_user_data = scaler.transform(user_data)  # 정규화 적용

        print("\n추천 게임 목록 :")
        recommendations = recommend_games(scaled_user_data, games_df, knn, excluded_games)
        
        if recommendations.empty: 
            print("추천 가능한 게임이 없습니다. 프로그램을 종료합니다.")
            break
        
        # 표 출력
        print(tabulate(recommendations, headers = 'keys', tablefmt = 'grid', showindex = False))

        # 피드백 수집
        feedback, exit_program = collect_feedback(recommendations)
        if exit_program:  # 만족도가 5인 경우 프로그램 종료
            break

        excluded_games.update(recommendations['Game'].tolist())  # 추천된 게임을 제외 목록에 추가
        user_preferences = update_preferences_with_feedback(user_preferences, feedback, games_df)  # 사용자 성향 업데이트

        # 업데이트된 사용자 성향 출력
        print("\n업데이트된 사용자 성향 :")
        print(user_preferences)

    print("추천 프로그램을 종료합니다.")
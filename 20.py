#명언 생성코드
import random
quotes = {
    "quote1": "삶이 있는 한 희망은 있다. - 키케로",
    "quote2": "산이 높을수록 골짜기는 깊다. - 괴테",
    "quote3": "하루에 3시간을 걸으면 7년 후에 지구를 한 바퀴 돌 수 있다. - 사무엘 존슨",
    "quote4": "행복은 습관이다, 그것을 몸에 익혀라. - 허버트 허버드",
    "quote5": "피할 수 없으면 즐겨라. - 로버트 엘리엇",
    "quote6": "단순하게 살아라. 현대인은 쓸데없는 절차와 형식 때문에 삶을 낭비하고 있다. - 헨리 데이비드 소로",
    "quote7": "어제와 똑같은 삶을 살면서 다른 미래를 기대하는 것은 정신병 초기 증세이다. - 알버트 아인슈타인",
    "quote8": "성공은 결과이지 목적이 아니다. - 플로베르",
}


def get_random_quote():
    return random.choice(list(quotes.values()))

if __name__ == "__main__":
    print("오늘의 명언:")
    print(get_random_quote())
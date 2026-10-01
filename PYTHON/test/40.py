import random
import time

def sexy_menu():
    print("메뉴를 정합니다. 10초 후에 결과가 나와요!\n")
    
    for i in range(10, 0, -1):
        print(f"⏳ {i}초...", end="\r")
        time.sleep(1)
    
    print("\n" + "=" * 30)
    
    choice = random.choice(['한솥', '중국집'])
    print(f" 오늘의 추천 메뉴: [{choice}]")
    print("=" * 30)

if __name__ == "__main__":
    sexy_menu()
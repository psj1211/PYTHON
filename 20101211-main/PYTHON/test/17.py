# 점프 투 파이썬 01~04장

vocabulary_db = [
    {"word": "apple", "meaning": "사과", "level": 1, "score": 0},
    {"word": "python", "meaning": "파이썬", "level": 2, "score": 0},
    {"word": "variable", "meaning": "변수", "level": 2, "score": 0},
    {"word": "dictionary", "meaning": "사전", "level": 3, "score": 0},
    {"word": "conditional", "meaning": "조건문", "level": 3, "score": 0}
]

print("=" * 50)
print("       [함수/클래스 없이 동작하는 단어 학습 시스템]")
print("=" * 50)

system_running = True

while system_running:
    print("\n[메뉴] 1. 단어 학습 및 퀴즈 | 2. 난이도별 조회 | 3. 결과 파일 저장 | 0. 종료")
    menu_choice = input("원하는 메뉴 번호를 입력하세요: ").strip()

    if menu_choice == "1":
        print("\n--- [ 단어 퀴즈 시작 ] ---")
        correct_count = 0
        for item in vocabulary_db:
            user_answer = input(f"단어 '{item['word']}'의 뜻은 무엇일까요? ").strip()
            
            if user_answer == item['meaning']:
                print(">> 정답입니다! (+1점)")
                item['score'] += 1
                correct_count += 1
            else:
                print(f">> 오답입니다! 정답은 '{item['meaning']}' 입니다.")
        
        print(f"\n[퀴즈 완료] 총 {len(vocabulary_db)}문제 중 {correct_count}개를 맞혔습니다!")

    elif menu_choice == "2":
        target_level = input("\n조회할 난이도를 입력하세요 (1~3): ").strip()
        
        if target_level in ["1", "2", "3"]:
            level_num = int(target_level)
            filtered_words = [v for v in vocabulary_db if v['level'] == level_num]
            
            print(f"\n--- [ 난이도 {level_num} 단어 목록 ] ---")
            if not filtered_words:
                print("해당 난이도의 단어가 없습니다.")
            else:
                for idx, v in enumerate(filtered_words, 1):
                    print(f"{idx}. {v['word']} : {v['meaning']} (누적 정답: {v['score']}회)")
        else:
            print("[오류] 난이도는 1, 2, 3 중 하나만 입력 가능합니다.")

    elif menu_choice == "3":
        file_path = "vocab_report.txt"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("=== 단어 학습 최종 결과 보고서 ===\n\n")
            
            for item in vocabulary_db:
                line = f"단어: {item['word']:<12} | 뜻: {item['meaning']:<8} | 난이도: {item['level']} | 누적정답: {item['score']}회\n"
                f.write(line)
            

            levels_set = {item['level'] for item in vocabulary_db}
            f.write(f"\n총 학습한 난이도 종류: {sorted(list(levels_set))}\n")
            
        print(f"\n[완료] 학습 결과가 '{file_path}' 파일로 저장되었습니다.")

    elif menu_choice == "0":
        print("\n프로그램을 종료합니다. 수고하셨습니다!")
        system_running = False

    else:
        print("\n[경고] 잘못된 입력입니다. 0~3 사이의 숫자를 입력하세요.")
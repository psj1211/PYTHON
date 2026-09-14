# ==========================================
# 점프 투 파이썬 04장: 사용자 정의 함수 정의
# ==========================================

def calculate_grade(score):
    """점수에 따른 학점 산출 (03장 if-elif-else 조건문)"""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def process_student_data(students_raw):
    """
    학생 데이터를 처리하여 통계를 내는 핵심 로직
    (02장 딕셔너리/리스트, 03장 for문/List Comprehension 활용)
    """
    processed_list = []
    
    for student in students_raw:
        # 02장 딕셔너리 Key 접근 및 리스트 데이터 추출
        name = student["name"]
        scores = student["scores"]  # [국어, 영어, 수학]
        
        # 02장 내장 함수 sum(), len() 사용 및 평균 계산
        total = sum(scores)
        avg = total / len(scores)
        grade = calculate_grade(avg)
        
        # 새로운 정보가 추가된 딕셔너리 생성
        student_info = {
            "name": name,
            "total": total,
            "avg": avg,
            "grade": grade,
            "attendance": student["attendance"]
        }
        processed_list.append(student_info)
        
    return processed_list


def filter_honor_students(*students, min_avg=80.0):
    """
    04장 가변 파라미터(*args)와 매개변수 기본값을 활용한 우수생 추출 함수
    """
    # 03장 List Comprehension (리스트 내포)
    honor_students = [s["name"] for s in students if s["avg"] >= min_avg]
    return honor_students


def save_report_to_file(filename, student_results):
    """
    04-3장: 파일 입출력 (open, with 문)
    처리 결과를 텍스트 파일로 저장합니다.
    """
    # 04-3장 with문 사용으로 파일 자동 close
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 45 + "\n")
        f.write("         학생 성적 분석 결과 보고서\n")
        f.write("=" * 45 + "\n\n")
        
        for s in student_results:
            # 02장 문자열 포매팅 (f-string)
            line = f"이름: {s['name']} | 총점: {s['total']}점 | 평균: {s['avg']:.1f}점 | 학점: {s['grade']}\n"
            f.write(line)
            
        f.write("\n" + "-" * 45 + "\n")
        
        # 02장 집합(Set)을 활용한 중복 출석 상태 분석
        all_attend_status = set()
        for s in student_results:
            all_attend_status.add(s["attendance"])
        
        # 02장 join() 함수를 활용한 문자열 결합
        status_str = ", ".join(all_attend_status)
        f.write(f"기록된 출석 상태 종류: {status_str}\n")


# ==========================================
# 메인 실행 흐름 (03장 while문 / 프로그램 루프)
# ==========================================
if __name__ == "__main__":
    # 02장 리스트와 딕셔너리가 결합된 중첩 데이터 구조
    raw_data = [
        {"name": "김철수", "scores": [95, 88, 92], "attendance": "출석"},
        {"name": "이영희", "scores": [78, 85, 70], "attendance": "출석"},
        {"name": "박민수", "scores": [55, 60, 50], "attendance": "지각"},
        {"name": "정수진", "scores": [100, 92, 96], "attendance": "출석"},
        {"name": "최현우", "scores": [62, 75, 80], "attendance": "결석"}
    ]

    print(">>> 1~4장 문법 기반 성적 관리 프로그램 시작 <<<\n")

    # 1. 데이터 처리 함수 호출
    results = process_student_data(raw_data)

    # 2. 결과 출력 (03장 for문 + 02장 f-string)
    print("--- [학생별 처리 결과] ---")
    for res in results:
        print(f"• {res['name']} - 평균: {res['avg']:.1f}점 ({res['grade']}학점) / 출석: {res['attendance']}")

    # 3. 우수생 선발 (*args 가변 인자 활용)
    # *results 로 리스트 요소를 풀어서 전달
    honors = filter_honor_students(*results, min_avg=85.0)
    print(f"\n★ 우수 장학생 명단 (평균 85점 이상): {', '.join(honors)}")

    # 4. 파일 저장 (04장 파일 쓰기)
    output_filename = "student_report.txt"
    save_report_to_file(output_filename, results)
    print(f"\n[성공] 분석 리포트가 '{output_filename}' 파일로 저장되었습니다.")
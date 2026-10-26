#등급 계산기
def calculate_relative_grade(rank, total_students):
    percentile = (rank / total_students) * 100

    if percentile <= 4:
        return 1, percentile
    elif percentile <= 11:
        return 2, percentile
    elif percentile <= 23:
        return 3, percentile
    elif percentile <= 40:
        return 4, percentile
    elif percentile <= 60:
        return 5, percentile
    elif percentile <= 77:
        return 6, percentile
    elif percentile <= 89:
        return 7, percentile
    elif percentile <= 96:
        return 8, percentile
    else:
        return 9, percentile

try:
    total = int(input("전체 학생 수를 입력하세요: "))
    rank = int(input("자신의 등수를 입력하세요: "))

    if 1 <= rank <= total:
        grade, pct = calculate_relative_grade(rank, total)
        print(f"\n상위 백분율: {pct:.2f}%")
        print(f"최종 등급: {grade}등급")
    else:
        print("등수는 1등부터 전체 학생 수 사이여야 합니다.")
except ValueError:
    print("올바른 정수를 입력해주세요.")
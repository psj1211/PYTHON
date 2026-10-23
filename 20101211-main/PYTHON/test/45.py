from dataclasses import dataclass
from typing import Generator, List


# 1. @dataclass: __init__, __repr__ 등을 자동으로 생성해주는 데코레이터 (보일러플레이트 코드 제거)
@dataclass
class Task:
  title: str
  priority: int = 1
  completed: bool = False

  # 2. 특수 메서드 (Dunder Method): 객체를 문자열로 표현할 때 사용
  def __str__(self) -> str:
    status = "✓" if self.completed else " "
    return f"[{status}] (우선순위: {self.priority}) {self.title}"


class TaskManager:
  """파이썬의 핵심 개념들을 집약한 태스크 관리 클래스"""

  # 3. 타입 힌트 (Type Hinting): 코드의 가독성을 높이고 정적 분석 도구 지원
  def __init__(self, owner: str) -> None:
    self.owner: str = owner
    self._tasks: List[Task] = []

  def add_task(self, title: str, priority: int = 1) -> None:
    self._tasks.append(Task(title=title, priority=priority))

  # 4. 제너레이터 (Generator와 yield): 대용량 데이터에서 메모리를 효율적으로 절약
  def get_pending_tasks(self) -> Generator[Task, None, None]:
    for task in self._tasks:
      if not task.completed:
        yield task

  def complete_task(self, title: str) -> bool:
    for task in self._tasks:
      if task.title == title:
        task.completed = True
        return True
    return False

  # 5. @property: 메서드를 마치 멤버 변수처럼 접근할 수 있게 만듦
  @property
  def high_priority_summary(self) -> List[str]:
    # 6. 리스트 컴프리헨션 (List Comprehension): 간결하고 직관적인 리스트 생성
    return [task.title for task in self._tasks if task.priority >= 3 and not task.completed]


# === 실행 및 테스트 ===
if __name__ == "__main__":
  # 매니저 객체 생성
  manager = TaskManager("김파이썬")

  # 할 일 추가
  manager.add_task("파이썬 공식 문서 읽기", priority=2)
  manager.add_task("비동기 프로그래밍(Asyncio) 마스터하기", priority=3)
  manager.add_task("알고리즘 문제 풀기", priority=1)

  # 작업 완료 처리
  manager.complete_task("알고리즘 문제 풀기")

  # 미완료 태스크 출력 (제너레이터 순회)
  print(f"=== {manager.owner}님의 남은 할 일 ===")
  for task in manager.get_pending_tasks():
    print(task)

  # 프로퍼티와 리스트 컴프리헨션 활용 결과 출력
  print(f"\n[긴급 태스크 목록 (우선순위 3 이상)]")
  print(manager.high_priority_summary)
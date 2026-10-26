#클로드 실험(파일 정리기)
"""
파일 자동 정리기 (File Organizer)
지정한 폴더 안의 파일들을 확장자별로 하위 폴더를 만들어 자동으로 이동시킵니다.

사용법:
    python file_organizer.py

실행하면 정리할 폴더 경로를 입력받습니다.
"""

import os
import shutil

# 확장자별로 분류할 폴더 이름 매핑
EXTENSION_MAP = {
    "이미지": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
    "문서": [".pdf", ".doc", ".docx", ".txt", ".hwp", ".ppt", ".pptx", ".xls", ".xlsx"],
    "동영상": [".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv"],
    "음악": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "압축파일": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "실행파일": [".exe", ".msi", ".apk"],
    "코드": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".json"],
}


def get_category(extension: str) -> str:
    """확장자를 받아서 어떤 카테고리 폴더에 속하는지 반환. 없으면 '기타'."""
    extension = extension.lower()
    for category, extensions in EXTENSION_MAP.items():
        if extension in extensions:
            return category
    return "기타"


def organize_folder(target_dir: str, dry_run: bool = False) -> None:
    """target_dir 안의 파일들을 확장자별 폴더로 이동시킵니다."""
    if not os.path.isdir(target_dir):
        print(f"오류: '{target_dir}' 는 존재하지 않는 폴더입니다.")
        return

    moved_count = 0
    skipped_count = 0

    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)

        # 폴더는 건너뛰고 파일만 처리
        if os.path.isdir(file_path):
            continue

        # 이 스크립트 자신은 건너뛰기
        if filename == os.path.basename(__file__):
            continue

        _, extension = os.path.splitext(filename)
        if extension == "":
            skipped_count += 1
            continue

        category = get_category(extension)
        category_dir = os.path.join(target_dir, category)

        # 카테고리 폴더가 없으면 생성
        if not dry_run:
            os.makedirs(category_dir, exist_ok=True)

        destination = os.path.join(category_dir, filename)

        # 같은 이름의 파일이 이미 있으면 번호를 붙여서 충돌 방지
        if os.path.exists(destination):
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(destination):
                new_name = f"{base}_{counter}{ext}"
                destination = os.path.join(category_dir, new_name)
                counter += 1

        if dry_run:
            print(f"[미리보기] {filename}  ->  {category}/")
        else:
            shutil.move(file_path, destination)
            print(f"이동 완료: {filename}  ->  {category}/")

        moved_count += 1

    print(f"\n총 {moved_count}개 파일 처리, {skipped_count}개 건너뜀 (확장자 없음).")


if __name__ == "__main__":
    print("=== 파일 자동 정리기 ===")
    folder_path = input("정리할 폴더의 전체 경로를 입력하세요 (예: C:\\Users\\내이름\\Downloads): ").strip()
    # 사용자가 따옴표를 붙여 붙여넣는 경우 대비
    folder_path = folder_path.strip('"').strip("'")

    preview = input("먼저 미리보기만 해볼까요? (y/n): ").strip().lower()
    is_dry_run = preview == "y"

    organize_folder(folder_path, dry_run=is_dry_run)

    if is_dry_run:
        proceed = input("\n실제로 정리를 진행할까요? (y/n): ").strip().lower()
        if proceed == "y":
            organize_folder(folder_path, dry_run=False)
        else:
            print("취소되었습니다.")

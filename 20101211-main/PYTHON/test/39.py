from deep_translator import GoogleTranslator
import time

def translate_text(text, target_lang='ko'):
    try:
        time.sleep(0.5)
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"번역 오류: {e}"

print("=== 파이썬 대화형 번역기 (종료: q 또는 exit) ===")

while True:
    user_input = input("\n번역할 내용을 입력하세요: ")

    if user_input.lower() in ['q', 'exit', 'quit']:
        print("번역기를 종료합니다.")
        break

    if not user_input.strip():
        continue

    result = translate_text(user_input, target_lang='ko')
    print(f"번역 결과: {result}")
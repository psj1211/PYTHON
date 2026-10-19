#클로드 실험(계산기)
import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")

        # 계산에 사용할 표현식 문자열
        self.expression = ""

        # 결과/입력 표시창
        self.display_var = tk.StringVar(value="0")
        display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=("Arial", 28),
            bd=0,
            justify="right",
            bg="#1e1e1e",
            fg="white",
            insertbackground="white",
        )
        display.grid(row=0, column=0, columnspan=4, ipady=20, padx=10, pady=10, sticky="we")

        # 버튼 배치 (텍스트, 행, 열, 열 병합)
        buttons = [
            ("C", 1, 0, 1), ("←", 1, 1, 1), ("%", 1, 2, 1), ("/", 1, 3, 1),
            ("7", 2, 0, 1), ("8", 2, 1, 1), ("9", 2, 2, 1), ("*", 2, 3, 1),
            ("4", 3, 0, 1), ("5", 3, 1, 1), ("6", 3, 2, 1), ("-", 3, 3, 1),
            ("1", 4, 0, 1), ("2", 4, 1, 1), ("3", 4, 2, 1), ("+", 4, 3, 1),
            ("0", 5, 0, 2), (".", 5, 2, 1), ("=", 5, 3, 1),
        ]

        for (text, row, col, colspan) in buttons:
            self.create_button(text, row, col, colspan)

        # 그리드 비율 맞추기
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

        # 키보드 입력도 지원
        root.bind("<Key>", self.on_key_press)
        root.bind("<Return>", lambda e: self.calculate())
        root.bind("<BackSpace>", lambda e: self.backspace())

    def create_button(self, text, row, col, colspan):
        if text == "=":
            bg_color = "#ff9500"
        elif text in ("C", "←"):
            bg_color = "#a5a5a5"
        elif text in ("/", "*", "-", "+", "%"):
            bg_color = "#ff9f0a"
        else:
            bg_color = "#333333"

        btn = tk.Button(
            self.root,
            text=text,
            font=("Arial", 18),
            fg="white",
            bg=bg_color,
            activebackground="#555555",
            bd=0,
            command=lambda t=text: self.on_button_click(t),
        )
        btn.grid(
            row=row, column=col, columnspan=colspan,
            sticky="nsew", padx=3, pady=3, ipady=15,
        )

    def on_button_click(self, char):
        if char == "C":
            self.clear()
        elif char == "←":
            self.backspace()
        elif char == "=":
            self.calculate()
        elif char == "%":
            self.expression += "/100"
            self.update_display()
        else:
            self.expression += char
            self.update_display()

    def on_key_press(self, event):
        char = event.char
        if char in "0123456789.+-*/":
            self.expression += char
            self.update_display()

    def clear(self):
        self.expression = ""
        self.display_var.set("0")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.update_display()

    def update_display(self):
        self.display_var.set(self.expression if self.expression else "0")

    def calculate(self):
        try:
            # 안전한 계산을 위해 허용 문자만 검사
            allowed = set("0123456789.+-*/() ")
            if self.expression and all(c in allowed for c in self.expression):
                result = eval(self.expression)
                self.expression = str(result)
                self.display_var.set(self.expression)
            else:
                self.display_var.set("오류")
                self.expression = ""
        except ZeroDivisionError:
            self.display_var.set("0으로 나눌 수 없음")
            self.expression = ""
        except Exception:
            self.display_var.set("오류")
            self.expression = ""


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
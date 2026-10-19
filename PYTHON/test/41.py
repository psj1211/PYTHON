import math
import random
import tkinter as tk


class RiggedWheelApp:

    def __init__(self, root):
        self.root = root
        self.root.title("텍스트 입력형 주작 돌림판 (파란색 내부 완전 랜덤)")
        self.root.geometry("450x650")
        self.root.resizable(False, False)

        # ---------------- 텍스트 입력 프레임 ----------------
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        tk.Label(
            input_frame, text="파란색 칸 글자:", font=("맑은 고딕", 10, "bold")
        ).grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.blue_entry = tk.Entry(
            input_frame, font=("맑은 고딕", 10), width=15
        )
        self.blue_entry.insert(0, "당첨 (파란색)")
        self.blue_entry.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(
            input_frame, text="빨간색 칸 글자:", font=("맑은 고딕", 10, "bold")
        ).grid(row=1, column=0, padx=5, pady=2, sticky="e")
        self.red_entry = tk.Entry(input_frame, font=("맑은 고딕", 10), width=15)
        self.red_entry.insert(0, "꽝 (빨간색)")
        self.red_entry.grid(row=1, column=1, padx=5, pady=2)

        self.apply_button = tk.Button(
            input_frame,
            text="텍스트 적용",
            font=("맑은 고딕", 9, "bold"),
            bg="#E0E0E0",
            command=self.update_labels,
        )
        self.apply_button.grid(row=0, column=2, rowspan=2, padx=8, ipady=5)

        # 기본 문구
        self.blue_text = "당첨 (파란색)"
        self.red_text = "꽝 (빨간색)"

        # ---------------- 캔버스 및 기본 변수 ----------------
        self.canvas = tk.Canvas(
            root, width=400, height=400, bg="#F0F0F0", highlightthickness=0
        )
        self.canvas.pack(pady=10)

        self.center_x = 200
        self.center_y = 200
        self.radius = 160

        self.angle = 0
        self.is_spinning = False

        # 최초 그리기
        self.draw_wheel(self.angle)
        self.draw_pointer()

        # ---------------- 하단 컨트롤 및 결과 ----------------
        self.spin_button = tk.Button(
            root,
            text="돌리기!",
            font=("맑은 고딕", 14, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=5,
            command=self.start_spin,
        )
        self.spin_button.pack(pady=10)

        self.result_label = tk.Label(
            root, text="버튼을 눌러 돌림판을 돌려보세요!", font=("맑은 고딕", 12)
        )
        self.result_label.pack(pady=5)

    def update_labels(self):
        b_val = self.blue_entry.get().strip()
        r_val = self.red_entry.get().strip()

        if b_val:
            self.blue_text = b_val
        if r_val:
            self.red_text = r_val

        self.draw_wheel(self.angle)

    def draw_wheel(self, current_angle):
        self.canvas.delete("wheel")

        start_blue = current_angle % 360
        start_red = (current_angle + 180) % 360

        # 파란색 부채꼴 (180도)
        self.canvas.create_arc(
            self.center_x - self.radius,
            self.center_y - self.radius,
            self.center_x + self.radius,
            self.center_y + self.radius,
            start=start_blue,
            extent=180,
            fill="#3498DB",
            outline="white",
            width=2,
            tags="wheel",
        )

        # 빨간색 부채꼴 (180도)
        self.canvas.create_arc(
            self.center_x - self.radius,
            self.center_y - self.radius,
            self.center_x + self.radius,
            self.center_y + self.radius,
            start=start_red,
            extent=180,
            fill="#E74C3C",
            outline="white",
            width=2,
            tags="wheel",
        )

        # 텍스트 배치
        self.draw_label(start_blue + 90, self.blue_text, "wheel")
        self.draw_label(start_red + 90, self.red_text, "wheel")

        # 가운데 장식 원
        self.canvas.create_oval(
            self.center_x - 20,
            self.center_y - 20,
            self.center_x + 20,
            self.center_y + 20,
            fill="white",
            outline="#333333",
            width=2,
            tags="wheel",
        )

    def draw_label(self, mid_angle_deg, text, tag):
        rad = math.radians(mid_angle_deg)
        dist = self.radius * 0.6
        tx = self.center_x + dist * math.cos(rad)
        ty = self.center_y - dist * math.sin(rad)
        self.canvas.create_text(
            tx,
            ty,
            text=text,
            fill="white",
            font=("맑은 고딕", 13, "bold"),
            tags=tag,
        )

    def draw_pointer(self):
        self.canvas.create_polygon(
            200,
            35,
            185,
            10,
            215,
            10,
            fill="#2C3E50",
            outline="white",
            width=2,
        )

    def start_spin(self):
        if self.is_spinning:
            return

        self.is_spinning = True
        self.spin_button.config(state=tk.DISABLED)
        self.apply_button.config(state=tk.DISABLED)
        self.result_label.config(text="두근두근... 돌고 있습니다!")

        # -------------------------------------------------------------
        # [파란색 내부 전범위 랜덤 구현]
        # 12시 방향(90도)에 파란색 부채꼴(180도 분량)만 걸리려면
        # 최종 각도(angle % 360)가 270도 ~ 450도 사이에 있어야 합니다.
        # 경계선에 딱 걸치지 않도록 안전 여유분(5도)을 두고
        # 275도 ~ 445도 사이 전체 범위를 매번 완전 무작위(uniform random)로 지정합니다.
        # -------------------------------------------------------------

        extra_rotations = random.randint(5, 8) * 360
        random_blue_position = random.uniform(275, 445)

        # 현재 각도를 기준으로 다음 목표 각도 설정
        current_base = (self.angle // 360) * 360
        self.target_angle = (
            current_base + extra_rotations + random_blue_position
        )

        self.speed = 25.0
        self.animate_spin()

    def animate_spin(self):
        remaining = self.target_angle - self.angle

        if remaining <= 0 or self.speed < 0.2:
            self.angle = self.target_angle
            self.draw_wheel(self.angle)
            self.is_spinning = False
            self.spin_button.config(state=tk.NORMAL)
            self.apply_button.config(state=tk.NORMAL)
            self.result_label.config(
                text=f"🎉 축하합니다! [{self.blue_text}] 당첨!"
            )
            return

        self.speed = max(0.5, remaining * 0.05)
        self.angle += self.speed
        self.draw_wheel(self.angle)

        self.root.after(15, self.animate_spin)


if __name__ == "__main__":
    root = tk.Tk()
    app = RiggedWheelApp(root)
    root.mainloop()
import random
import tkinter as tk


class FlyingPet:

    def __init__(self):
        self.root = tk.Tk()

        # =========================================================
        # [속도 조절 설정]
        # self.speed : 한 번에 이동하는 픽셀 수 (기본값: 20)
        #              -> 숫자가 클수록 빠름 (예: 5 = 천천히, 40 = 엄청 빠름)
        # self.delay : 프레임 갱신 시간/ms (기본값: 30)
        #              -> 숫자가 작을수록 부드럽고 빠름 (10 ~ 50 추천)
        # =========================================================
        self.speed = 5
        self.delay = 100

        # 프레임 없는 투명 창 설정
        self.root.overrideredirect(True)
        self.root.wm_attributes("-topmost", True)

        try:
            self.root.wm_attributes("-transparentcolor", "white")
        except tk.TclError:
            self.root.config(bg="systemTransparent")

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.pet_size = 80
        self.x = 0
        self.y = self.screen_height - 250
        self.direction = 1  # 1: 오른쪽, -1: 왼쪽
        self.wing_up = False

        self.canvas = tk.Canvas(
            self.root,
            width=self.pet_size + 20,
            height=self.pet_size + 20,
            bg="white",
            highlightthickness=0,
        )
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.drag)

        self.root.geometry(f"+{self.x}+{self.y}")
        self.draw_pet()
        self.animate()

    def start_drag(self, event):
        self.drag_x = event.x
        self.drag_y = event.y

    def drag(self, event):
        self.x = self.root.winfo_x() + (event.x - self.drag_x)
        self.y = self.root.winfo_y() + (event.y - self.drag_y)
        self.root.geometry(f"+{self.x}+{self.y}")

    def draw_pet(self):
        self.canvas.delete("all")

        wing_y = 15 if self.wing_up else 35

        # 날개
        self.canvas.create_oval(
            10, wing_y, 40, wing_y + 25, fill="#FFD1DC", outline=""
        )
        self.canvas.create_oval(
            60, wing_y, 90, wing_y + 25, fill="#FFD1DC", outline=""
        )

        # 몸통
        self.canvas.create_oval(
            15, 20, 85, 90, fill="#FFB6C1", outline="#FF69B4", width=3
        )

        # 눈
        eye_offset = 5 if self.direction == 1 else -5
        self.canvas.create_oval(
            35 + eye_offset,
            40,
            45 + eye_offset,
            55,
            fill="#333333",
            outline="",
        )
        self.canvas.create_oval(
            55 + eye_offset,
            40,
            65 + eye_offset,
            55,
            fill="#333333",
            outline="",
        )

        # 눈반짝임
        self.canvas.create_oval(
            37 + eye_offset, 42, 41 + eye_offset, 46, fill="white", outline=""
        )
        self.canvas.create_oval(
            57 + eye_offset, 42, 61 + eye_offset, 46, fill="white", outline=""
        )

        # 볼터치
        self.canvas.create_oval(25, 55, 35, 63, fill="#FF69B4", outline="")
        self.canvas.create_oval(65, 55, 75, 63, fill="#FF69B4", outline="")

        # 입
        self.canvas.create_line(
            45 + eye_offset,
            60,
            50 + eye_offset,
            65,
            55 + eye_offset,
            60,
            fill="#333333",
            width=2,
            smooth=True,
        )

    def animate(self):
        # 이동 처리
        self.x += self.direction * self.speed

        # 모니터 좌우 끝 반사 처리
        if self.x >= self.screen_width - (self.pet_size + 20):
            self.direction = -1
        elif self.x <= 0:
            self.direction = 1

        self.wing_up = not self.wing_up
        self.draw_pet()
        self.root.geometry(f"+{self.x}+{self.y}")

        # 설정된 delay 시간마다 재귀 호출
        self.root.after(self.delay, self.animate)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    pet = FlyingPet()
    pet.run()
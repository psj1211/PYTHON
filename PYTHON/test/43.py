import math
import os
import time

def render_donut():
    A, B = 0, 0
    # 터미널 화면 조절용 (줄 수를 조정해 터미널에 맞춰 사용)
    screen_width = 80
    screen_height = 22
    
    # 터미널 커서 숨기기 및 화면 초기화
    print("\x1b[2J", end="")
    
    try:
        while True:
            b = [' '] * (screen_width * screen_height)
            z = [0] * (screen_width * screen_height)
            
            # theta, phi 각도를 돌며 도넛 표면 좌표 계산
            j = 0
            while j < 6.28:
                j += 0.07
                i = 0
                while i < 6.28:
                    i += 0.02
                    
                    sinA = math.sin(A)
                    cosA = math.cos(A)
                    cosB = math.cos(B)
                    sinB = math.sin(B)
                    
                    sini = math.sin(i)
                    cosi = math.cos(i)
                    sinj = math.sin(j)
                    cosj = math.cos(j)
                    
                    # 3D 도넛 회전 방정식
                    h = cosj + 2  # R2 + R1*cos(theta)
                    D = 1 / (sini * h * sinA + sinj * cosA + 5) # Z축 깊이 역수 (원근감)
                    t = sini * h * cosA - sinj * sinA
                    
                    # 2D 화면 좌표계로 투영 (Screen Mapping)
                    x = int(screen_width / 2 + 30 * D * (cosi * h * cosB - t * sinB))
                    y = int(screen_height / 2 + 15 * D * (cosi * h * sinB + t * cosB))
                    
                    o = x + screen_width * y
                    
                    # 광원/음영 계산 (Luminance)
                    N = int(8 * ((sinj * sinA - sini * cosj * cosA) * cosB 
                                 - sini * cosj * sinA - sinj * cosA - cosi * cosj * sinB))
                    
                    if 0 <= y < screen_height and 0 <= x < screen_width and D > z[o]:
                        z[o] = D
                        # 음영 단계에 따른 아스키 문자 매핑
                        b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]
                        
            # 커서를 맨 위로 이동하고 화면 출력 (깜빡임 최소화)
            print("\x1b[H", end="")
            for k in range(len(b)):
                print(b[k], end="" if (k + 1) % screen_width else "\n")
                
            # 회전 각도 업데이트
            A += 0.04
            B += 0.02
            time.sleep(0.01)
            
    except KeyboardInterrupt:
        print("\x1b[?25h") # Ctrl+C 누르면 커서 원복

if __name__ == "__main__":
    render_donut()
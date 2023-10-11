import openpyxl
import os
import time

# 엑셀 파일 열기
workbook = openpyxl.load_workbook("youtube_videos.xlsx")
sheet = workbook.active

# C 컬럼 2번째 행부터 1050번째 행까지 반복
for row in range(2, 1051):
    youtube_link = sheet.cell(row=row, column=3).value  # C 컬럼 값 읽기

    # yt_whisper 명령 실행
    os.system(f'yt_whisper "{youtube_link}" --task transcribe --language ko')

    # 실행 후 잠시 대기 (명령어가 완전히 실행될 때까지 기다림). 필요하면 시간 조절
    time.sleep(2)

# 엑셀 파일 닫기
workbook.close()

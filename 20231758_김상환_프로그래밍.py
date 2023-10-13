import tkinter as tk
from tkinter import font
database = []  # 일정을 저장할 리스트

def save_plan():
    date = date_entry.get()
    plan = plan_entry.get()

    # 날짜와 일정을 리스트에 저장
    database.append((date, plan))

    # 입력 필드 초기화
    date_entry.delete(0, tk.END)
    plan_entry.delete(0, tk.END)

    # 저장된 일정 출력
    print_plan()

def delete_plan():
    index = plan_listbox.curselection()
    if index:
        # 선택된 일정 삭제
        database.pop(index[0])

        # 삭제 후 일정 리스트 업데이트
        print_plan()

def sort_plan():
    # 날짜 순으로 일정 정렬
    database.sort(key=lambda x: x[0])

    # 정렬 후 일정 리스트 업데이트
    print_plan()

def print_plan():
    # 일정 리스트 초기화
    plan_listbox.delete(0, tk.END)

    # 일정 리스트 출력
    for data in database:
        date, plan_text = data
        plan_listbox.insert(tk.END, f"날짜: {date} 일정: {plan_text}")

def show_plan():
    date = date_entry.get()
    #일정 조회용 리스트 초기화
    plan_listbox2.delete(0, tk.END)

    # 선택된 날짜에 해당하는 일정 필터링
    filtered_plan = [data for data in database if data[0] == date]

    # 일정 리스트 출력
    if filtered_plan:
        for data in filtered_plan:
            date, plan_text = data
            plan_listbox2.insert(tk.END, f"날짜: {date} 일정: {plan_text}")
    else:
        plan_listbox2.insert(tk.END, "해당 날짜에 일정이 없습니다.")

# 윈도우 생성
window = tk.Tk()
window.title("일정 관리 프로그램")
window.geometry('640x480')

#폰트 설정
font=font.Font(family='굴림체',size=18) 

# 레이블 및 입력 필드 생성
date_label = tk.Label(window,font=font,text="날짜:")
date_label.pack()
date_entry = tk.Entry(window,font=font)
date_entry.pack()

plan_label = tk.Label(window, font=font,text="일정:")
plan_label.pack()
plan_entry = tk.Entry(window,font=font)
plan_entry.pack()

# 저장 버튼 생성
save_button = tk.Button(window, text="일정 저장",font=font, command=save_plan)
save_button.pack()

# 일정 리스트 박스 생성
plan_listbox = tk.Listbox(window,width=250)
plan_listbox.pack()

#프레임 생성
frame = tk.Frame(window)
frame.pack()

# 삭제 버튼 생성
delete_button = tk.Button(frame, text="일정 삭제",font=font, command=delete_plan)
delete_button.grid(row=0,column=0)

# 정렬 버튼 생성
sort_button = tk.Button(frame, text="일정 정렬",font=font, command=sort_plan)
sort_button.grid(row=0,column=1)

# 일정 조회 버튼 생성
show_button = tk.Button(frame, text="일정 조회",font=font, command=show_plan)
show_button.grid(row=0,column=2)

# 일정 조회용 리스트 박스 생성
plan_listbox2 = tk.Listbox(frame)
plan_listbox2.grid(row=1,column=1)

# 이벤트 루프 실행
window.mainloop()

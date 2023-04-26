from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
import sys as system
 
def xuat_ra_file():
     try:
         f = open("list.txt", "a")
         for task_list in tasks:
             f.write(task_list + "\n")
         f.close()
     except:
         messagebox.showinfo('Lỗi', 'Tệp không thể được ghi hoặc không có đầu việc trong cơ sở dữ liệu')

def them_tac_vu():  
    task_string = task_field.get()  
    if len(task_string) == 0:  
        messagebox.showinfo('Lỗi', 'Tên tác vụ rỗng')  
    else:  
        tasks.append(task_string)  
        the_cursor.execute('insert into tasks values (?)', (task_string ,))  
        danh_sach_tac_vu()  
        task_field.delete(0, 'end')  

def danh_sach_tac_vu():  
    xoa_danh_sach()  
    for task in tasks:  
        task_listbox.insert('end', task)  

def xoa_tac_vu():  
    try:
        the_value = task_listbox.get(task_listbox.curselection())  
        if the_value in tasks:  
            tasks.remove(the_value)  
            danh_sach_tac_vu()  
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except: 
        messagebox.showinfo('Lỗi', 'Không có tác vụ đuọc chọn')        
 
def xoa_tat_ca():  
    message_box = messagebox.askyesno('Xóa tất cả', 'Bạn chắc chứ?')  
    if message_box == True:  
        while(len(tasks) != 0):
            tasks.pop()  
        the_cursor.execute('delete from tasks') 
        danh_sach_tac_vu()  
  

def xoa_danh_sach():  
    task_listbox.delete(0, 'end')  
  
def close():  
    print(tasks)  
    guiWindow.destroy()
    
def doc_co_so_du_lieu():  
    while(len(tasks) != 0):  
        tasks.pop()  
    for row in the_cursor.execute('select title from tasks'):  
        tasks.append(row[0])

if __name__ == "__main__":  
    guiWindow = Tk()  
    guiWindow.title("Những việc cần làm")  
    guiWindow.geometry("870x400+550+50")  
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg = "#B5E5CF")  
    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()  
    the_cursor.execute('create table if not exists tasks (title text)')  
    tasks = []  
    functions_frame = Frame(guiWindow, bg = "black") 
    functions_frame.pack(side = "top", expand = True, fill = "both")  
 
    task_label = Label( functions_frame,text = "Nhập nhiệm vụ:",  
        font = ("arial", "14", "bold"),  
        background = "black", 
        foreground="white"
    )

    task_label.place(x = 20, y = 30)  
      
    task_field = Entry(  
        functions_frame,  
        font = ("Arial", "14"),  
        width = 61,  
        foreground="black",
        background = "white",  
    )  
    task_field.place(x = 180, y = 30)  
  
    add_button =Button(  
        functions_frame,  
        text = "Thêm nhiệm vụ",  
        width = 15,
        bg='#D4AC0D',font=("arial", "14", "bold"),
        command = them_tac_vu,
        
    )  
    del_button = Button(  
        functions_frame,  
        text = "Xóa tác vụ",  
        width = 15,
        bg='#D4AC0D', font=("arial", "14", "bold"),
        command = xoa_tac_vu,  
    )  
    
    del_all_button = Button(  
        functions_frame,  
        text = "Xóa tất cả tác vụ",  
        width = 15,
        font=("arial", "14", "bold"),
        bg='#D4AC0D',
        command = xoa_tat_ca  
    )  

    export_file = Button(
        functions_frame,  
        text = "Xuất txt",  
        width = 15,
        font=("arial", "14", "bold"),
        bg='#D4AC0D',
        command = xuat_ra_file
    )

    exit_button = Button(  
        functions_frame,  
        text = "Thoát",  
        width = 69,
        bg='#D4AC0D',  font=("arial", "14", "bold"),
        command = close  
    )  

    add_button.place(x = 10, y = 80,)  
    del_button.place(x = 240, y = 80)  
    del_all_button.place(x = 460, y = 80)  
    exit_button.place(x = 10, y = 330)  
    export_file.place(x = 670 , y = 80)
  
    task_listbox = Listbox(  
        functions_frame,  
        width = 92,  
        height = 7,  
        font="bold",
        selectmode = 'SINGLE',  
        background = "WHITE",
        foreground="BLACK",    
        selectbackground = "#D4AC0D",  
        selectforeground="BLACK"
    )  

    task_listbox.place(x = 17, y = 140)  
    doc_co_so_du_lieu()  
    danh_sach_tac_vu()
    guiWindow.mainloop()  
    the_connection.commit()
    try: 
        the_cursor.c
    except:
        system.exit(1)
import tkinter as tk
from tkinter import messagebox
import datetime
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import textwrap

t = ("Yu Gothic","13","bold")
root = tk.Tk()
root.title("読書記録アプリ")
root.minsize(400,570)
root.resizable(False, False)

c = tk.Canvas(
    root,
    width=400,
    height=570,
    bg="#F8E9FD",
    highlightthickness=0
)
c.pack()
img4 = Image.open("img4.png")
img4 = img4.resize((1000,1000))
img4_photo = ImageTk.PhotoImage(img4)
c.create_image(
    0,
    0,
    image=img4_photo,
    anchor=tk.NW
)

text1 = tk.Label(text="読書記録",font=("Yu Gothic","17","bold"), bg="#be7e3d",fg="#ffffff" ,
                 relief="solid",  
                 bd=1,
                 padx=10,
                 pady=5)
text1.place(x=155, y=15)

img = Image.open("img5.png")
img = img.resize((15,20 ))  
book_img = ImageTk.PhotoImage(img)
# 左のアイコン
icon1 = tk.Label(root, image=book_img)
icon1.place(x=116, y=20)
# 右のアイコン
icon2 = tk.Label(root, image=book_img)
icon2.place(x=285, y=20)

def my_f():
    syomei=box1.get().strip()
    tyomei=box2.get().strip()
    kansou = box3.get("1.0", tk.END).strip()
    hosi=s.get()
    day=datetime.date.today()

    if syomei=="":
        messagebox.showwarning("入力エラー", "書名を入力してください。")
        return
    if hosi=="★を選択してください":
            messagebox.showwarning("入力エラー", "★を選んでください")
            return
    if kansou == "":
        ans = messagebox.askyesno("確認", "感想が空ですが、このまま保存しますか？")
        if not ans:
            return
        
    box1.delete(0,tk.END)
    box2.delete(0,tk.END)
    box3.delete("1.0", tk.END)
    s.current(0)

    hozon1=f"{'-'*15}保存日時:{day}{'-'*15}\n"
    hozon2=f"書名:{syomei}\n"
    hozon3=f"著者:{tyomei}\n"
    hozon31=f"評価:{hosi}\n"
    kansou = textwrap.fill(kansou, width=40)
    hozon4 = f"感想:\n{kansou}\n"
    hozon5=f"{'-'*48}\n"
    hozon=hozon1 + hozon2 + hozon3 + hozon31 + hozon4 + hozon5
    # print(hozon1,hozon2,hozon3,hozon4,hozon5)

    f=open("dokusyo.txt","a",encoding="utf-8")
    f.write(hozon)
    f.close()


text2 = tk.Label(text="書名",font=t, bg="#704321",fg="#ffffff")
text3 = tk.Label(text="著者",font=t, bg="#704321",fg="#ffffff")
box1 = tk.Entry()
box2 = tk.Entry()
text2.place(x=60,y=80)
box1.place(x=150,y=80)
text3.place(x=60,y=130)
box2.place(x=150,y=130)

text5 = tk.Label(text="評価",font=t,bg="#704321",fg="#ffffff")
text5.place(x=60, y=180)
s=ttk.Combobox()
s["values"]=("★を選択してください","★☆☆☆☆","★★☆☆☆","★★★☆☆","★★★★☆","★★★★★")
s.current(0)
s.place(x=150, y=180)

text4 = tk.Label(text="感想",font=t,bg="#704321",fg="#ffffff")
text4.place(x=60,y=240)
box3=tk.Text(width=40,height=15)
box3.place(x=60,y=275)
btn = tk.Button(text="保存",font=("Yu Gothic","14","bold"),command=my_f,bg="#eadbce")
btn.place(x=170,y=490)


root.mainloop()

# 追加した機能
# 背景として画像を挿入し、また題名の横にicoonの画像を小さくして貼り付けました。
# フォントを指定・文字の色や背景を指定しました。
# 画面拡大を禁止しました。
# messagebox.showwarningとaskyesnoを使い、書名や★が未記入の場合はお知らせが出るようにして保存しないようにすることと、感想が空のときもお知らせが出るようにしました。
# 感想の文が長く記入されたときは、textwrapで自動的に折り返されるようにしました。

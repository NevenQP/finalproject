from tkinter import *
from tkinter import messagebox
import json
import login as lg
from PIL import ImageTk, Image


class Sign_up:
    def __init__(self,root):
        self.sign_up = root
        self.sign_up.title("Sign up")
        self.sign_up.configure(bg="#fff")
        self.sign_up.geometry("800x700")
        self.sign_up.resizable(False,False)
        self.img = ImageTk.PhotoImage(Image.open("abc.jpg")) 
        self.bg = Label(self.sign_up, image = self.img, border = 0,bg = 'white')
        self.bg.place(x = 0,y = 0)
        self.Sign_in = Label(self.sign_up, text = "Sign up", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',23,'bold')).place(x = 370 , y = 100)
        self.User = Label(self.sign_up, text = "User", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',23,'bold')).place(x = 100 , y = 200)
        self.User_box = Entry(self.sign_up, fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',23,'bold'), textvariable = StringVar())
        self.User_box.place(x = 370 , y = 200)
        self.Password = Label(self.sign_up, text = "Password", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',23,'bold')).place(x = 100 , y = 300)
        self.Password_box = Entry(self.sign_up, fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',23,'bold'), textvariable = StringVar())
        self.Password_box.place(x = 370 , y = 300)
        self.Conf_Password = Label(self.sign_up, text = "Confirm Password", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',23,'bold')).place(x = 100 , y = 400)
        self.Conf_Password_box = Entry(self.sign_up, fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',23,'bold'), textvariable = StringVar())
        self.Conf_Password_box.place(x = 370 , y = 400)
        self.Sign_up_button = Button(self.sign_up, text = "Sign up", fg = 'white', bg = '#6874E8', font=('Microsoft Yahei UI light',23,'bold'), command = self.do_sign_up).place(x = 370 , y = 500)
        self.Login = Label(self.sign_up, text = "Already have account ?", fg = 'white', bg = '#6874E8', font=('Microsoft Yahei UI light',15,'bold')).place(x = 370 , y = 650)
        self.Login_button = Button(self.sign_up, text = "Login", fg = 'white', bg = '#6874E8', font=('Microsoft Yahei UI light',11,'bold'), command= self.open_log_in).place(x = 600 , y = 650)

    def do_sign_up(self):
        user = self.User_box.get()
        password = self.Password_box.get()
        conf_password = self.Conf_Password_box.get()
        
        if password != conf_password:
            messagebox.showwarning("showinfo", "Password dont match")
            return

        f = open("account.txt", "r")

        try:
            account = json.loads(f.read())
        except:
            with open("account.txt", 'w') as w:
                w.write(json.dumps({user:password}))
            messagebox.showwarning("showinfo", "Success")
            return


        if user in account:
            messagebox.showwarning("showinfo", "Exist user")
            return
        
        account[user] = password
        f = open("account.txt", "w")
        f.truncate(0)
        account = json.dumps(account)
        f.write(account)
        f.close()
        messagebox.showwarning("showinfo", "Success")

    def open_log_in(self):
        self.sign_up.destroy()
        login = Tk()
        lg.Login(login)
        login.mainloop()    

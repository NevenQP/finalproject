from tkinter import *
from tkinter import messagebox
import json
import sign_up as su
import add_new_staff as ans

class Login:
   def __init__(self, root):      
      f = open("account.txt", "a")
      f.close()
      self.login = root
      self.login.title('Login')
      self.login.configure(bg="#fff")
      self.login.geometry("800x600")
      self.login.resizable(False,False)
      self.Sign_in = Label(self.login, text = "Sign in", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',23,'bold')).place(x = 370 , y = 100)
      self.User = Label(self.login, text = "User", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',23,'bold')).place(x = 170 , y = 200)
      self.User_box = Entry(self.login, fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',23,'bold'), textvariable = StringVar())
      self.User_box.place(x = 370 , y = 200)
      self.Password = Label(self.login, text = "Password", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',23,'bold')).place(x = 170 , y = 300)
      self.Password_box = Entry(self.login, fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',23,'bold'), textvariable = StringVar())
      self.Password_box.place(x = 370 , y = 300)
      self.Login_button = Button(self.login, text = "Log in", fg = 'white', bg = '#6874E8', font=('Microsoft Yahei UI light',23,'bold'), command = self.do_log_in).place(x = 370 , y = 400)
      self.Sign_up = Label(self.login, text = "Dont have account ?", fg = 'white', bg = '#6874E8', font=('Microsoft Yahei UI light',15,'bold')).place(x = 370 , y = 500)
      self.Sign_up_button = Button(self.login, text = "Sign up", fg = 'white', bg = '#6874E8', font=('Microsoft Yahei UI light',11,'bold'), command= self.open_sign_up).place(x = 600 , y = 500)

   def do_log_in(self):
      user = self.User_box.get()
      password = self.Password_box.get()
      try: 
         with open("account.txt", 'r') as f:
            account = json.loads(f.read())
      except:
         messagebox.showwarning("showinfo", "Invalide user")
         return
      
      if user not in account:
         messagebox.showwarning("showinfo", "Invalide user")
      elif account[user] == password:
         self.login.destroy()
         root = Tk()
         obj = ans.add_staff(root, user)
         root.mainloop()
      else:
         messagebox.showwarning("showinfo", "Wrong pass")
   
   def open_sign_up(self):
      self.login.destroy()
      sign_up = Tk()
      su.Sign_up(sign_up)
      sign_up.mainloop()   

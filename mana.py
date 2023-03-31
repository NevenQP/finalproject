from tkinter import *
from tkinter import messagebox

class Management: 
    def __init__(self, root):
        self.window = root
        self.window.title("Computer Store Information Management")
        self.window.geometry("1280x720")
        self.window.configure(bg="#fff")
        self.window.resizable(False, False)

        self.title = Label(self.window, text = "Computer Store Information Management", fg = 'white', bg = '#A41623',pady = 30, font=('Microsoft Yahei UI light',23,'bold')).pack(fill = X)
        
        #button
        self.btn_frame = Frame(self.window, bg = '#6874E8')
        self.btn_frame.pack(fill = X)
        self.staff_btn = Button(self.btn_frame, text = "Staff", fg = 'white', bg = '#6874E8', width = 10, font=('Microsoft Yahei UI light',23,'bold'), command = self.display_staff).grid(row=0, column=0, padx=110, pady = 10)
        self.product_btn = Button(self.btn_frame, text = "Product", fg = 'white', bg = '#6874E8', width = 10, font=('Microsoft Yahei UI light',23,'bold'), command = self.display_product).grid(row=0, column=1, padx=110, pady = 10)
        self.customer_btn = Button(self.btn_frame, text = "Customer", fg = 'white', bg = '#6874E8', width = 10, font=('Microsoft Yahei UI light',23,'bold'), command = self.display_customer).grid(row=0, column=2, padx=110, pady = 10)

        self.staff_frame = Frame(self.window, bg = "#6874E8")
        self.customer_frame = Frame(self.window, bg = "#dd00ff")
        self.product_frame = Frame(self.window, bg = "#A41623")

        #staff frame
        #staff function button
        self.staff_func_frame = Frame(self.staff_frame, bg = 'white')
        self.staff_func_frame.pack(side = RIGHT, fill = Y)
        self.add_staff_btn = Button(self.staff_func_frame, text = "Add staff", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold'), command = self.add_staff).pack(pady = 10)
        self.show_staff_btn = Button(self.staff_func_frame, text = "Show staff list", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold'), command = self.show_staff_list).pack(pady = 10)
        self.delete_staff_btn = Button(self.staff_func_frame, text = "Delete staff", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold'), command = self.delete_staff).pack(pady = 10)
        self.search_staff_btn = Button(self.staff_func_frame, text = "Search staff", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold'), command = self.search_staff).pack(pady = 10)
        
        #working frame
        self.staff_wrk_frame = Frame(self.staff_frame, bg = 'white')
        self.staff_wrk_frame.pack(expand = TRUE, fill = BOTH)

        self.customer_wrk_frame = Frame(self.customer_frame, bg = 'white')
        self.customer_wrk_frame.pack(expand = TRUE, fill = BOTH)

        self.product_wrk_frame = Frame(self.product_frame, bg = 'white')
        self.product_wrk_frame.pack(expand = TRUE, fill = BOTH)

        #customer frame
        self.add_customer_btn = Button(self.customer_frame, text = "Add customer", fg = "white", bg = '#00ff00').pack(side = RIGHT)

        #product frame
        self.add_product_btn = Button(self.product_frame, text = "Add product", fg = "white", bg = '#00ff00').pack(side = RIGHT)

    def clear_frame(self):
        for widgets in self.staff_wrk_frame.winfo_children():
            widgets.destroy()
        
        for widgets in self.customer_wrk_frame.winfo_children():
            widgets.destroy()
        
        for widgets in self.product_wrk_frame.winfo_children():
            widgets.destroy()

    #staff function
    def display_staff(self):
        self.clear_frame()
        self.customer_frame.forget()
        self.product_frame.forget()
        
        self.staff_frame.pack(expand = TRUE, fill = BOTH)

        #Show staff list
    def show_staff_list(self):
        for i in range(5):
            for j in range(5):
                self.e = Label(self.staff_wrk_frame, width=5,text = str(i) + ' '  + str(j), fg='blue',font=('Arial',16,'bold'))
                self.e.grid(row=i, column=j)
    
    def add_staff(self):
        for i in range(6):
            for j in range(6):
                self.e = Label(self.staff_wrk_frame, width=20,text = str(i) + ' '  + str(j), fg='blue',font=('Arial',16,'bold'))
                self.e.grid(row=i, column=j)

    def delete_staff(self):
        for i in range(7):
            for j in range(7):
                self.e = Label(self.staff_wrk_frame, width=20,text = str(i) + ' '  + str(j), fg='blue',font=('Arial',16,'bold'))
                self.e.grid(row=i, column=j)

    def search_staff(self):
        for i in range(8):
            for j in range(8):
                self.e = Label(self.staff_wrk_frame, width=20,text = str(i) + ' '  + str(j), fg='blue',font=('Arial',16,'bold'))
                self.e.grid(row=i, column=j)

    #product function
    def display_product(self):
        self.clear_frame()
        self.staff_frame.forget()
        self.customer_frame.forget()

        self.product_frame.pack(expand = TRUE, fill = BOTH)

    #customer function
    def display_customer(self):
        self.clear_frame()
        self.staff_frame.forget()
        self.product_frame.forget()

        self.customer_frame.pack(expand = TRUE, fill = BOTH)

if __name__ == "__main__":
    root = Tk()
    obj = Management(root)
    root.mainloop()
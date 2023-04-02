from tkinter import *
from tkinter import messagebox
import json

class Management: 
    def __init__(self, root, id):
        self.staff_id = id
        self.staffs = []
        self.customers = []
        self.products = []
        self.load_data()
        self.window = root
        self.window.title("Computer Store Information Management")
        self.window.geometry("1280x720")
        self.window.configure(bg="#fff")
        self.window.resizable(False, False)

        self.title = Label(self.window, text = "Computer Store Information Management", fg = 'white', bg = '#A41623',pady = 30, font=('Microsoft Yahei UI light',16,'bold')).pack(fill = X)
        
        #button
        self.btn_frame = Frame(self.window, bg = '#6874E8')
        self.btn_frame.pack(fill = X)
        self.staff_btn = Button(self.btn_frame, text = "Staff", fg = 'white', bg = '#6874E8', width = 10, font=('Microsoft Yahei UI light',16,'bold'), command = self.display_staff).grid(row=0, column=0, padx=110, pady = 10)
        self.product_btn = Button(self.btn_frame, text = "Product", fg = 'white', bg = '#6874E8', width = 10, font=('Microsoft Yahei UI light',16,'bold'), command = self.display_product).grid(row=0, column=1, padx=110, pady = 10)
        self.customer_btn = Button(self.btn_frame, text = "Customer", fg = 'white', bg = '#6874E8', width = 10, font=('Microsoft Yahei UI light',16,'bold'), command = self.display_customer).grid(row=0, column=2, padx=110, pady = 10)
        self.bill_btn = Button(self.btn_frame, text = "Bill", fg = 'white', bg = '#6874E8', width = 10, font=('Microsoft Yahei UI light',16,'bold'), command = self.display_bill).grid(row=0, column=3, padx=110, pady = 10)

        self.staff_frame = Frame(self.window, bg = "white")
        self.customer_frame = Frame(self.window, bg = "white")
        self.product_frame = Frame(self.window, bg = "white")
        self.bill_frame = Frame(self.window, bg = "white")

        #staff frame
        #staff function button
        self.staff_func_frame = Frame(self.staff_frame, bg = 'white')
        self.staff_func_frame.pack(side = RIGHT, fill = Y)
        self.show_staff_btn = Button(self.staff_func_frame, text = "Show staff list", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold'), command = self.show_staff_list).pack(pady = 10)
        self.delete_staff_btn = Button(self.staff_func_frame, text = "Delete staff", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold'), command = self.delete_staff).pack(pady = 10)
        self.search_staff_btn = Button(self.staff_func_frame, text = "Search staff", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold'), command = self.search_staff).pack(pady = 10)

        self.staff_wrk_frame = Frame(self.staff_frame, bg = 'white')
        self.staff_wrk_frame.pack(expand = TRUE, fill = BOTH)
        
        #customer frame
        self.customer_func_frame = Frame(self.customer_frame, bg = 'white')
        self.customer_func_frame.pack(side = RIGHT, fill = Y)
        self.show_customer_btn = Button(self.customer_func_frame, text = "Show customer list", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold')).pack(pady = 10)
        self.add_customer_btn = Button(self.customer_func_frame, text = "Add customer", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold')).pack(pady = 10)
        self.delete_customer_btn = Button(self.customer_func_frame, text = "Delete customer", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold')).pack(pady = 10)
        self.search_customer_btn = Button(self.customer_func_frame, text = "Search customer", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold')).pack(pady = 10)

        self.customer_wrk_frame = Frame(self.customer_frame, bg = 'white')
        self.customer_wrk_frame.pack(expand = TRUE, fill = BOTH)

        #product frame
        self.product_func_frame = Frame(self.product_frame, bg = 'white')
        self.product_func_frame.pack(side = RIGHT, fill = Y)
        self.show_product_btn = Button(self.product_func_frame, text = "Show product list", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold'), command = self.show_product_list).pack(pady = 10)
        self.add_product_btn = Button(self.product_func_frame, text = "Add product", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold'), command = self.add_product).pack(pady = 10)
        self.delete_product_btn = Button(self.product_func_frame, text = "Delete product", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold'), command = self.delete_product).pack(pady = 10)
        self.search_product_btn = Button(self.product_func_frame, text = "Search product", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold'), command = self.search_product).pack(pady = 10)

        self.product_wrk_frame = Frame(self.product_frame, bg = 'white')
        self.product_wrk_frame.pack(expand = TRUE, fill = BOTH)

        #bill frame
        self.bill_func_frame = Frame(self.bill_frame, bg = 'white')
        self.bill_func_frame.pack(side = RIGHT, fill = Y)
        self.show_bill_btn = Button(self.bill_func_frame, text = "Show bill list", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold')).pack(pady = 10)
        self.add_bill_btn = Button(self.bill_func_frame, text = "Add bill", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold')).pack(pady = 10)
        self.delete_bill_btn = Button(self.bill_func_frame, text = "Delete bill", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold')).pack(pady = 10)
        self.search_bill_btn = Button(self.bill_func_frame, text = "Search bill", fg = "white", bg = '#00ff00', width = 15, font=('Microsoft Yahei UI light',20,'bold')).pack(pady = 10)

        self.bill_wrk_frame = Frame(self.bill_frame, bg = 'white')
        self.bill_wrk_frame.pack(expand = TRUE, fill = BOTH)
        
        self.window.protocol("WM_DELETE_WINDOW", self.save_data)
    def save_data(self):
        with open("staff.txt", "w") as f:
            f.truncate(0)
            f.write(json.dumps(self.staffs))
        with open("product.txt", "w") as f:
            f.truncate(0)
            f.write(json.dumps(self.products))
        with open("customer.txt", "w") as f:
            f.truncate(0)
            f.write(json.dumps(self.customers))
        self.window.destroy()
        

    def load_data(self):
        with open("staff.txt", "r") as f:
            staffs = json.loads(f.read())   
        for staff in staffs:
            self.staffs.append(staff)
        with open("product.txt", "r") as f:
            products = json.loads(f.read())   
        for product in products:
            self.products.append(product)
        
        with open("customer.txt", "r") as f:
            customers = json.loads(f.read())   
        for customer in customers:
            self.customers.append(customer)

    def clear_frame(self):
        for widgets in self.staff_wrk_frame.winfo_children():
            widgets.destroy()
        
        for widgets in self.customer_wrk_frame.winfo_children():
            widgets.destroy()
        
        for widgets in self.product_wrk_frame.winfo_children():
            widgets.destroy()
        
        #for widgets in self.bill_wrk_frame.winfo_children():
        #    widgets.destroy()

    #staff function
    def display_staff(self):
        self.clear_frame()
        self.customer_frame.forget()
        self.product_frame.forget()
        self.bill_frame.forget()
        
        
        self.staff_frame.pack(expand = TRUE, fill = BOTH)

    def show_staff_list(self):
        self.clear_frame()
        
        for i in range(len(self.staffs)):
            for j in range(len(self.staffs[0])):
                self.e = Label(self.staff_wrk_frame,bd = 5, width = 12, wraplength = 150 ,text = self.staffs[i][j], fg='blue',font=('Microsoft Yahei UI light',16,'bold'))
                self.e.grid(row=i, column=j)
    

    def delete_staff(self):
        self.clear_frame()

        self.add_staff_id = Label(self.staff_wrk_frame, text = "Delete staff", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold')).grid(row = 0, column = 0)
        self.add_staff_id = Label(self.staff_wrk_frame, text = "ID", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold')).grid(row = 1, column = 0)
        self.add_staff_id_e = Entry(self.staff_wrk_frame, fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'), textvariable = StringVar())
        self.add_staff_id_e.grid(row = 1, column = 1)
        self.submit = Button(self.staff_wrk_frame, text = "Submit", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'), command = self.delete_staff_data).grid(row = 4, column = 0)

    def search_staff(self):
        self.clear_frame()

        self.add_staff_id = Label(self.staff_wrk_frame, text = "Search staff", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold')).grid(row = 0, column = 0)
        self.add_staff_id = Label(self.staff_wrk_frame, text = "ID", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold')).grid(row = 1, column = 0)
        self.add_staff_id_e = Entry(self.staff_wrk_frame,width = 12 ,fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'), textvariable = StringVar())
        self.add_staff_id_e.grid(row = 1, column = 1)
        self.submit = Button(self.staff_wrk_frame, text = "Submit", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'), command = self.search_staff_data).grid(row = 5, column = 0)
    
    def delete_staff_data(self):
        id = self.add_staff_id_e.get()
        for i in range(len(self.staffs)):
            if self.staffs[i][0] == id:
                self.staffs.pop(i)
                mes = Label(self.staff_wrk_frame, text = "Success", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'))
                mes.grid(row = 4, column = 1)
                mes.after(3000,lambda:mes.destroy())
                return
        mes = Label(self.staff_wrk_frame, text = "Id dont exist", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'))
        mes.grid(row = 4, column = 1)
        mes.after(3000,lambda:mes.destroy())

    def search_staff_data(self):
        id = self.add_staff_id_e.get()
        for i in range(len(self.staffs)):
            if self.staffs[i][0] == id:
                for j in range(len(self.staffs[0])):
                    self.e = Label(self.staff_wrk_frame, bd = 5, width = 12, wraplength = 150 ,text = self.staffs[0][j], fg='blue',font=('Microsoft Yahei UI light',16,'bold'))
                    self.e.grid(row=2, column=j)
                    self.e = Label(self.staff_wrk_frame, bd = 5, width = 12, wraplength = 150 ,text = self.staffs[i][j], fg='blue',font=('Microsoft Yahei UI light',16,'bold'))
                    self.e.grid(row=3, column=j)
                return
        mes = Label(self.staff_wrk_frame, text = "Id dont exist", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'))
        mes.grid(row = 3, column = 1)
        mes.after(3000,lambda:mes.destroy())


    #product function
    def display_product(self):
        self.clear_frame()
        self.staff_frame.forget()
        self.customer_frame.forget()
        self.bill_frame.forget()

        self.product_frame.pack(expand = TRUE, fill = BOTH)

    def show_product_list(self):
        self.clear_frame()
        
        for i in range(len(self.products)):
            for j in range(len(self.products[0])):
                self.e = Label(self.product_wrk_frame,bd = 5, width = 10, wraplength = 150 ,text = self.products[i][j], fg='blue',font=('Microsoft Yahei UI light',16,'bold'))
                self.e.grid(row=i, column=j)
    
    def add_product(self):
        self.clear_frame()
        
        self.add_product_tittle = Label(self.product_wrk_frame, text = "Add product", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold')).grid(row = 0, column = 0)
        self.add_product_id = Label(self.product_wrk_frame, text = "ID", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold')).grid(row = 1, column = 0)
        self.add_product_id_e = Entry(self.product_wrk_frame, fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'), textvariable = StringVar())
        self.add_product_id_e.grid(row = 1, column = 1)
        self.add_product_name = Label(self.product_wrk_frame, text = "Name", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold')).grid(row = 2, column = 0)
        self.add_product_name_e = Entry(self.product_wrk_frame, fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'), textvariable = StringVar())
        self.add_product_name_e.grid(row = 2, column = 1)
        self.add_product_cpu = Label(self.product_wrk_frame, text = "CPU", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold')).grid(row = 3, column = 0)
        self.add_product_cpu_e = Entry(self.product_wrk_frame, fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'), textvariable = StringVar())
        self.add_product_cpu_e.grid(row = 3, column = 1)
        self.add_product_ram = Label(self.product_wrk_frame, text = "RAM", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold')).grid(row = 4, column = 0)
        self.add_product_ram_e = Entry(self.product_wrk_frame, fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'), textvariable = StringVar())
        self.add_product_ram_e.grid(row = 4, column = 1)
        self.add_product_hard_disk = Label(self.product_wrk_frame, text = "Hard Disk", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold')).grid(row = 5, column = 0)
        self.add_product_hard_disk_e = Entry(self.product_wrk_frame, fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'), textvariable = StringVar())
        self.add_product_hard_disk_e.grid(row = 5, column = 1)
        self.add_product_os = Label(self.product_wrk_frame, text = "OS", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold')).grid(row = 6, column = 0)
        self.add_product_os_e = Entry(self.product_wrk_frame, fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'), textvariable = StringVar())
        self.add_product_os_e.grid(row = 6, column = 1)
        self.add_product_color = Label(self.product_wrk_frame, text = "Color", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold')).grid(row = 7, column = 0)
        self.add_product_color_e = Entry(self.product_wrk_frame, fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'), textvariable = StringVar())
        self.add_product_color_e.grid(row = 7, column = 1)

        self.submit = Button(self.product_wrk_frame, text = "Submit", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'), command = self.add_product_data).grid(row = 8, column = 0)

    def delete_product(self):
        self.clear_frame()

        self.add_product_id = Label(self.product_wrk_frame, text = "Delete product", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold')).grid(row = 0, column = 0)
        self.add_product_id = Label(self.product_wrk_frame, text = "ID", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold')).grid(row = 1, column = 0)
        self.add_product_id_e = Entry(self.product_wrk_frame, fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'), textvariable = StringVar())
        self.add_product_id_e.grid(row = 1, column = 1)
        self.submit = Button(self.product_wrk_frame, text = "Submit", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'), command = self.delete_product_data).grid(row = 4, column = 0)

    def search_product(self):
        self.clear_frame()

        self.add_product_id = Label(self.product_wrk_frame, text = "Search product", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold')).grid(row = 0, column = 0)
        self.add_product_id = Label(self.product_wrk_frame, text = "ID", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold')).grid(row = 1, column = 0)
        self.add_product_id_e = Entry(self.product_wrk_frame,width = 12 ,fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'), textvariable = StringVar())
        self.add_product_id_e.grid(row = 1, column = 1)
        self.submit = Button(self.product_wrk_frame, text = "Submit", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'), command = self.search_product_data).grid(row = 5, column = 0)

    def add_product_data(self):
        id = self.add_product_id_e.get()
        name = self.add_product_name_e.get()
        cpu = self.add_product_cpu_e.get()
        ram = self.add_product_ram_e.get()
        hard_disk = self.add_product_hard_disk_e.get()
        os = self.add_product_os_e.get()
        color = self.add_product_color_e.get()

        if id == '' or name == '' or os == '' or cpu == '' or ram == '' or hard_disk == '' or color == '':
            mes = Label(self.product_wrk_frame, text = "Invalid", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'))
            mes.grid(row = 8, column = 1)
            mes.after(3000,lambda:mes.destroy())
        else:
            self.products.append([id, name, cpu, ram, hard_disk, os, color])
            self.add_product_id_e.delete(0, END)
            self.add_product_name_e.delete(0, END)
            self.add_product_cpu_e.delete(0, END)
            self.add_product_ram_e.delete(0, END)
            self.add_product_hard_disk_e.delete(0, END)
            self.add_product_os_e.delete(0, END)
            self.add_product_color_e.delete(0, END)
            mes = Label(self.product_wrk_frame, text = "Success", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'))
            mes.grid(row = 8, column = 1)
            mes.after(3000,lambda:mes.destroy())
    
    def delete_product_data(self):
        id = self.add_product_id_e.get()
        for i in range(len(self.products)):
            if self.products[i][0] == id:
                self.products.pop(i)
                mes = Label(self.product_wrk_frame, text = "Success", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'))
                mes.grid(row = 4, column = 1)
                mes.after(3000,lambda:mes.destroy())
                return
        mes = Label(self.product_wrk_frame, text = "Id dont exist", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'))
        mes.grid(row = 4, column = 1)
        mes.after(3000,lambda:mes.destroy())

    def search_product_data(self):
        id = self.add_product_id_e.get()
        for i in range(len(self.products)):
            if self.products[i][0] == id:
                for j in range(len(self.products[0])):
                    self.e = Label(self.product_wrk_frame, bd = 5, width = 12, wraplength = 150 ,text = self.products[0][j], fg='blue',font=('Microsoft Yahei UI light',16,'bold'))
                    self.e.grid(row=2, column=j)
                    self.e = Label(self.product_wrk_frame, bd = 5, width = 12, wraplength = 150 ,text = self.products[i][j], fg='blue',font=('Microsoft Yahei UI light',16,'bold'))
                    self.e.grid(row=3, column=j)
                return
        mes = Label(self.product_wrk_frame, text = "Id dont exist", fg = '#6874E8', bg = 'white', font=('Microsoft Yahei UI light',16,'bold'))
        mes.grid(row = 3, column = 1)
        mes.after(3000,lambda:mes.destroy())

    #customer function
    def display_customer(self):
        self.clear_frame()
        self.staff_frame.forget()
        self.product_frame.forget()
        self.bill_frame.forget()

        self.customer_frame.pack(expand = TRUE, fill = BOTH)
    
    #bill function
    def display_bill(self):
        self.clear_frame()
        self.staff_frame.forget()
        self.product_frame.forget()
        self.customer_frame.forget()

        self.bill_frame.pack(expand = TRUE, fill = BOTH)

if __name__ == "__main__":
    root = Tk()
    obj = Management(root)
    root.mainloop()
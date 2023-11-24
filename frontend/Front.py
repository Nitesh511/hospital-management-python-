from tkinter import *
from tkinter import ttk
import mysql.connector
import model.supplier
from tkinter import messagebox
import backend.database2
class display:
    def __init__(self,root):
        self.root=root
        self.root.title("User")
        self.root.geometry("1320x700+0+0")

        title=Label(self.root,text="Supplier Management System",bd=10,relief=GROOVE,font=("times new roamn ",40,"bold"))
        title.pack(side=TOP,fill=X)

        ###All Variables
        self.Code_no_var=StringVar()
        self.name_var=StringVar()
        self.phone_var=StringVar()
        self.address_var=StringVar()
        self.vat_no_var=StringVar()
        self.code_var=IntVar()

        self.search_by=StringVar()
        self.search_txt_var=StringVar()

        self.db=backend.database2.DBConnect2()




        ##Manage FRame

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="Light Blue")
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        m_title=Label(Manage_Frame,text="Manage Supplier",bg="Light Blue",fg="Blue",font=("Times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        l_code_no=Label(Manage_Frame,text=" Party Code NO",bg="Light Blue",fg="Blue",font=("Times new roman",20,"bold"))
        l_code_no.grid(row=1,pady=10,padx=20,sticky="W")

        txt_code_no=Entry(Manage_Frame,textvariable=self.Code_no_var,bg="Light Blue",fg="Blue",font=("Times new roman",13,"bold"))
        txt_code_no.grid(row=1,column=1,padx=10,sticky="W")

        l_party_name = Label(Manage_Frame, text=" Party Name ", bg="Light Blue", fg="Blue",
                          font=("Times new roman", 20, "bold"))
        l_party_name.grid(row=2, pady=10, padx=20, sticky="W")

        txt_party_name = Entry(Manage_Frame, textvariable=self.name_var, bg="Light Blue", fg="Blue",
                            font=("Times new roman", 13, "bold"))
        txt_party_name.grid(row=2,column=1, padx=10, sticky="W")

        l_phone_number = Label(Manage_Frame, text=" Phone Number ", bg="Light Blue", fg="Blue",
                             font=("Times new roman", 20, "bold"))
        l_phone_number.grid(row=3, pady=10, padx=20, sticky="W")

        txt_phone_number= Entry(Manage_Frame, textvariable=self.phone_var, bg="Light Blue", fg="Blue",
                               font=("Times new roman", 13, "bold"))
        txt_phone_number.grid(row=3, column=1, padx=10, sticky="W")

        l_address= Label(Manage_Frame, text=" Address ", bg="Light Blue", fg="Blue",
                             font=("Times new roman", 20, "bold"))
        l_address.grid(row=4, pady=10, padx=20, sticky="W")

        txt_address = Entry(Manage_Frame, textvariable=self.address_var, bg="Light Blue", fg="Blue",
                               font=("Times new roman", 13, "bold"))
        txt_address.grid(row=4, column=1, padx=10, sticky="W")

        l_vat= Label(Manage_Frame, text=" VAT NO ", bg="Light Blue", fg="Blue",
                             font=("Times new roman", 20, "bold"))
        l_vat.grid(row=5, pady=10, padx=20, sticky="W")

        txt_vat = Entry(Manage_Frame, textvariable=self.vat_no_var, bg="Light Blue", fg="Blue",
                               font=("Times new roman", 13, "bold"))
        txt_vat.grid(row=5, column=1, padx=10, sticky="W")

        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="Light Blue")
        btn_Frame.place(x=15,y=500,width=420)

        Addbtn=Button(btn_Frame,text="ADD",width=10,bg="Light Blue", fg="Blue",
                               font=("Times new roman", 10, "bold"),command=self.add_student)
        Addbtn.grid(row=0,column=0,padx=10,pady=10)

        updatebtn = Button(btn_Frame, text="Update", width=10, bg="Light Blue", fg="Blue",
                        font=("Times new roman", 10, "bold"),command=self.update_data)
        updatebtn.grid(row=0, column=1, padx=10, pady=10)

        deletebtn = Button(btn_Frame, text="Delete", width=10, bg="Light Blue", fg="Blue",
                        font=("Times new roman", 10, "bold"),command=self.delete_data)
        deletebtn.grid(row=0, column=2, padx=10, pady=10)

        clrbtn = Button(btn_Frame, text="Clear All", width=10, bg="Light Blue", fg="Blue",
                        font=("Times new roman", 10, "bold"),command=self.clear)
        clrbtn.grid(row=0, column=3, padx=10, pady=10)

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="Light Blue")
        Detail_Frame.place(x=500,y=100,width=800,height=580)
        sort= Button(Detail_Frame, text="sort", width=10, bg="Light Blue", fg="Blue",
                           font=("Times new roman", 10, "bold"), command=self.sort)
        sort.grid(row=0, column=6, padx=10, pady=10)
        self.cmb_sort=ttk.Combobox(Detail_Frame,width=10,font=("arial",15,"bold"))
        self.cmb_sort['values']=("ascending","descending")
        self.cmb_sort.grid(row=0,column=8)
        l_serch=Label(Detail_Frame,text="Search By Code",bg="Light Blue",fg="Blue", font=("Times new roman", 20, "bold"))
        l_serch.grid(row=0,column=0,pady=10,padx=20,sticky="W")


        txt_search=Entry(Detail_Frame,textvariable=self.search_txt_var,width=8,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="W")

        search_btn=Button(Detail_Frame,command=self.search_data,text="Search",fg="Blue",width=10,pady=5)
        search_btn.grid(row=0,column=3,padx=10,pady=10)

        show_btn = Button(Detail_Frame,command=self.fetch_data, text="Show All", fg="Blue", width=10, pady=5)
        show_btn.grid(row=0, column=4, padx=10, pady=10)

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="Light Blue")
        Table_Frame.place(x=15,y=70,width=760,height=480)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("code","Code_no","name","phone","address","vat_no"))
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("code",text="SN")
        self.Student_table.heading("Code_no",text="Party Code")
        self.Student_table.heading("name", text="Party Name")
        self.Student_table.heading("phone", text="Phone Number")
        self.Student_table.heading("address", text="Address")
        self.Student_table.heading("vat_no", text="VAT NO")
        self.Student_table["show"]="headings"
        self.Student_table.column("code",width=100)
        self.Student_table.column("Code_no",width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("phone", width=100)
        self.Student_table.column("address", width=100)
        self.Student_table.column("vat_no", width=100)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_student(self):
        """
        This function helps To add the details of the supplier
        :return:
        """
        Code_no = self.Code_no_var.get()
        name = self.name_var.get()
        phone= self.phone_var.get()
        address=self.address_var.get()
        vat_no=self.vat_no_var.get()

        if Code_no== "" or name == "" or phone == "" or address == "" or vat_no == "":
            messagebox.showerror('Error', 'plz fill the empty field')
            return

        u = model.supplier.Supplier(Code_no, name, phone, address,vat_no)
        print(u.get_Code_no())
        query = "insert into owner(Code_no,name,phone,address,vat_no) values(%s,%s,%s,%s,%s)"
        values = (
        u.get_Code_no(), u.get_name(), u.get_phone(), u.get_address(), u.get_vat_no())

        self.db.insert(query, values)
        self.fetch_data()
        messagebox.showinfo('Success', 'successfully saved data')

    def fetch_data(self):
        """
        This function helps to fetch all the data in the database
        :return:
        """
        query = "select * from owner"
        rows = self.db.fetching(query)
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("", END, values=row)

            self.db.fetch(query)


    def clear(self):
        """
        This function Helps to clear all the enter data
        :return:
        """
        self.Code_no_var.set("")
        self.name_var.set("")
        self.phone_var.set("")
        self.address_var.set("")
        self.vat_no_var.set("")

    def get_cursor(self, event):
        """
        This function helps fetch the data and shows in the entry field
        :param event:
        :return:
        """
        cursor_row = self.Student_table.focus()
        content = self.Student_table.item(cursor_row)
        row = content['values']
        self.code_var.set(row[0])
        self.Code_no_var.set(row[1])
        self.name_var.set(row[2])
        self.phone_var.set(row[3])
        self.address_var.set(row[4])
        self.vat_no_var.set(row[5])
    def update_data(self):
        """
        This function helps to update the values
        :return:
        """
        Code_no = self.Code_no_var.get()
        name = self.name_var.get()
        phone = self.phone_var.get()
        address = self.address_var.get()
        vat_no=self.vat_no_var.get()

        if Code_no== " " or name == " " or phone == " " or address == " " or vat_no == " " :
            messagebox.showerror('Error', 'plz fill the empty field')
            return

        u = model.supplier.Supplier(Code_no, name, phone, address, vat_no)
        query = ("UPDATE owner SET name=%s,phone=%s,address=%s,vat_no=%s WHERE Code_no=%s")
        values = (name,phone, address, vat_no,Code_no)
        self.db.update(query, values)
        self.fetch_data()
        messagebox.showinfo('Success', 'successfully saved data')
        self.clear()

    def delete_data(self):
        """
        This function helps to delete the data in the database
        :return:
        """
        query = ("delete from owner WHERE code={}".format(self.code_var.get()))
        value=self.code_var.get()
        self.db.delete(query,value)
        messagebox.showinfo("Success", "Data deleted successfully")
        self.fetch_data()
        self.clear()

    def search_data(self):
        """
        This function helps to search the data in the database
        :return:
        """
        query = (" select * from owner WHERE Code_no ={}").format(self.search_txt_var.get())
        values=self.Code_no_var.get()
        records = self.db.search_code(query,values)
        data_list = []

        for row in records:
            str(data_list.append(row[1]))
        print(data_list)
        data1 = self.linear_search(data_list, str(self.search_txt_var.get()))

        if data1:
            messagebox.showinfo('Success', ' Party Code_no found in this list')
            query1 = (" select * from owner WHERE Code_no = {}".format(str(self.search_txt_var.get())))
            values1 =(str(self.search_txt_var.get()))
            records1 = self.db.search_code(query1, values1)
            if len(records1) != 0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in records1:
                    self.Student_table.insert('', END, values=row)
        str(self.search_txt_var.set(""))

    @classmethod

    def linear_search(cls, data, item):
        """
        This function helps to sort the data in ascending and descending order
        :param data:
        :param item:
        :return:
        """
        for i in range(len(data)):
            if data[i] == item:
                return data[i]
        return False

    @classmethod

    def mergesort(self, order, ascending=True):
        list = []
        if len(order) == 1:
            return order

        mid = len(order) // 2

        first_half = self.mergesort(order[:mid])
        second_half = self.mergesort(order[mid:])

        x = 0
        y = 0
        while x < len(first_half) and y < len(second_half):
            if first_half[x] > second_half[y]:
                list.append(second_half[y])
                y = y + 1

            else:
                list.append(first_half[x])
                x = x + 1

        conclusion = list + first_half[x:]
        conclusion = conclusion + second_half[y:]

        if ascending == True:
            return conclusion

        else:
            conclusion.reverse()
            return conclusion

    def sort(self):
        sortby = self.cmb_sort.get()
        query = 'select * from owner'
        value_fetch = self.db.fetching(query)
        if sortby == 'ascending':
            row = self.mergesort(value_fetch, True)
            messagebox.showinfo("Sorted", "Data sorted in ascending")


        elif sortby == 'descending':
            row = self.mergesort(value_fetch, False)
            messagebox.showinfo('Sorted', 'Data sorted in descending ')

        else:
            row = []

        if len(row) != 0:
            self.Student_table.delete(
                *self.Student_table.get_children())
            for rows in row:
                self.Student_table.insert('', END, values=rows)


#
# root=Tk()
# obj=display(root)
# root.mainloop()
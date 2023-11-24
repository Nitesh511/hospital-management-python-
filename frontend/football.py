from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk
import model.user
import backend.database
from tkinter import messagebox

class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register Page")
        self.root.geometry("500x550")
        self.root.canvas = Canvas(root, width=900, height=900)  # Inserting Image
        self.root.Image = ImageTk.PhotoImage(Image.open('C:\\Users\\Owner\\Desktop\\algorithm\\frontend\\car.png'))
        self.root.canvas.create_image(0,170, anchor=NW, image=self.root.Image)
        self.root.canvas.pack()
        self.root.registe = ImageTk.PhotoImage(Image.open('C:\\Users\\Owner\\Desktop\\algorithm\\frontend\\reg.png'))
        self.root.canvas.create_image(90, 0, anchor=NW, image=self.root.registe)
        self.root.canvas.pack()
        self.db=backend.database.DBConnect()


        #creating user name password gender label and entry box
        l_username=Label(self.root,text="User Name",font=('arial',20,"bold"),fg="Blue",background="Light Blue",bd=10,relief=GROOVE)
        l_username.place(x=0,y=170)
        self.e1=Entry(self.root,font=('arial',20,"bold"))
        self.e1.place(x=180,y=175,height=45)
        l_password= Label(self.root, text="Paassword", font=('arial', 20, "bold"), fg="Blue", background="Light Blue",
                           bd=10, relief=GROOVE)
        l_password.place(x=0, y=230)
        self.e2 = Entry(self.root, font=('arial', 20, "bold"))
        self.e2.place(x=180, y=230, height=45)

        l_phone_number = Label(self.root, text="Phone Number", font=('arial', 20, "bold"), fg="Blue", background="Light Blue",
                           bd=10, relief=GROOVE)
        l_phone_number.place(x=0, y=300)
        self.e3 = Entry(self.root, font=('arial', 20, "bold"))
        self.e3.place(x=230, y=300, height=45,width=252)
        ####creating combo box for gender
        l_gender = Label(self.root, text="Gender", font=('arial', 20, "bold"), fg="Blue", background="Light Blue",
                           bd=10, relief=GROOVE)
        l_gender.place(x=0, y=360)


        self.cmb_gender = ttk.Combobox(self.root, font=('arial', 15, 'bold'))
        self.cmb_gender['values'] = ('Male', 'Female', 'Others')
        self.cmb_gender.place(x=180,y=360,height=45)

        l_Email= Label(self.root, text="Email", font=('arial', 20, "bold"), fg="Blue", background="Light Blue",
                           bd=10, relief=GROOVE)
        l_Email.place(x=0, y=420)
        self.e5 = Entry(self.root, font=('arial', 20, "bold"))
        self.e5.place(x=180, y=420, height=45)
        ##creating save button
        btn_save=Button(self.root,text="SAVE",font=('arial', 20, "bold"), fg="Blue", background="Light Blue",
                           bd=10, relief=GROOVE,command=self.save)
        btn_save.place(x=200,y=490)

    def save(self):
        user_name = self.e1.get()
        user_password = self.e2.get()
        user_phone_number = self.e3.get()
        gender = self.cmb_gender.get()
        gmail = self.e5.get()


        if  user_name == '' or user_password == '' or user_phone_number== '' or gender == '' or gmail == '':
            messagebox.showerror('Error', 'plz fill the empty field')
            return

        u=model.user.User(user_name, user_password, user_phone_number, gender, gmail)
        query = "insert into user_data(user_name,password,phone_number,gender,g_mail) values(%s,%s,%s,%s,%s)"
        values = (
             u.get_username(), u.get_password(), u.get_phone_number(), u.get_gender(), u.get_g_mail())


        self.db.insert(query, values)
        messagebox.showerror('Success', 'User Registration successfull')
        self.root.destroy()

#root=Tk()
#obj=register(root)
#root.mainloop()


from tkinter import *
from PIL import ImageTk,Image
from tkinter import font
from tkinter import messagebox
import frontend.football
import frontend.Front
import backend.database
class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("500x500")
        self.root.resizable(0,0)
        self.root.canvas = Canvas(root, width=500,height=500)#Inserting Image
        self.root.Image=ImageTk.PhotoImage(Image.open("C:\\Users\\Owner\\Desktop\\algorithm\\frontend\\ima.png.png"))
        self.root.canvas.create_image(0,0, anchor=NW,image=self.root.Image)
        self.root.canvas.pack()
        self.root.User_icon=ImageTk.PhotoImage(Image.open("C:\\Users\\Owner\\Desktop\\algorithm\\frontend\\las.ong.png"))
        self.root.canvas.create_image(5,85, anchor=NW, image=self.root.User_icon)
        self.root.password_icon = ImageTk.PhotoImage(Image.open("C:\\Users\\Owner\\Desktop\\algorithm\\frontend\\download.png"))
        self.root.canvas.create_image(5,200, anchor=NW, image=self.root.password_icon)

        self.db=backend.database.DBConnect()


        f = font.Font(size=15, slant='italic', underline=TRUE, family='arial')
        l_header=Label(self.root,text="Login Page",font=('arial',20,"bold"),fg="Blue",background="Light Blue",bd=10,relief=GROOVE)
        l_header.place(x=180,y=5)
        #creating user name and password label and entry Box
        l_username=Label(self.root,text="User Name",font=('arial',20,"bold"),fg="Blue",background="Light Blue",relief=RIDGE)
        l_username.place(x=90,y=120)

        self.e1=Entry(self.root,bg="Old Lace",font=('arial',20,"bold"))
        self.e1.place(x=270,y=120,height=35,width=190)


        l_Password=Label(self.root,text="Password",font=('arial',20,"bold"),fg="Blue",background="Light Blue",relief=RIDGE)
        l_Password.place(x=95,y=220)

        self.e2=Entry(self.root,bg="Old Lace",show='*',font=('arial',20,"bold"))
        self.e2.place(x=270,y=220,height=35,width=190)


        btn_login=Button(self.root,text='Login',font=('arial',20,"bold"),fg="Blue",background="Light Blue",relief=SUNKEN,command=self.btn_login_click)
        btn_login.place(x=220,y=290)



        btn_register=Button(self.root,text="No Account? Register Here",font=('arial',20,"bold"),fg="RED",background="BLUE",relief=SUNKEN)
        btn_register['font']=f
        btn_register.place(x=230,y=390,height=30,width=250)
        btn_register.bind('<Button-1>', self.register)

    def register(self,event):
        """
        This function is to opean the register page
        :param event:
        :return:
        """
        tk=Toplevel()
        frontend.football.register(tk)

    def btn_login_click(self):
        """
        This login function is to collect the username and password from the database
        :return:
        """
        uname = self.e1.get()
        passw = self.e2.get()

        if self.e1.get() == '' or self.e2.get() == '':
            messagebox.showerror('Error', 'plz fill the empty field')
        else:
            query = "select * from user_data where user_name=%s and password=%s"
            values = (uname, passw)
            rows = self.db.select(query, values)
            data = []

            if len(rows) != 0:
                for row in rows:
                    data.append(row[1])
                    data.append(row[2])
                print(data)
                if uname == data[0] and passw == data[1]:
                    messagebox.showinfo('Success', 'Congratulations!! login successfull')
                    self.root.destroy()
                    tk= Tk()
                    frontend.Front.display(tk)


                else:
                    messagebox.showerror('Error', 'Invalid username and password')
            else:
                messagebox.showinfo("Error", "User not registered !! Register first")



root=Tk()
object=login(root)
root.mainloop()

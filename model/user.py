class User:
    def __init__(self,uname,passw,phon,gen,email):
        self.__username=uname
        self.__password=passw
        self.__phone_number=phon
        self.__gen=gen
        self.__g_mail=email

    def set_username(self,uname):
        self.__username=uname

    def get_username(self):
        return self.__username

    def set_password(self, passw):
        self.__password = passw

    def get_password(self):
        return self.__password

    def set_phone_number(self, pho):
        self.__phone_number = pho

    def get_phone_number(self):
        return self.__phone_number

    def set_gender(self, gen):
        self.__gen = gen

    def get_gender(self):
        return self.__gen

    def set_g_mail(self,email):
        self.__g_mail=email

    def get_g_mail(self):
        return self.__g_mail
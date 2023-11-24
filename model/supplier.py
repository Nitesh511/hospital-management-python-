class Supplier:
    def __init__(self,code_no,uname,phon,add,vat_no):

        self.__Code_no=code_no
        self.__name=uname
        self.__phone=phon
        self.__address=add
        self.__vat_no=vat_no

    # def set_code(self,cod):
    #     self.__code=cod
    # def get_code(self):
    #     return  self.__code

    def set_Code_no(self,code_no):
        self.__Code_no=code_no

    def get_Code_no(self):
        return self.__Code_no

    def set_name (self, uname):
        self.__name = uname

    def get_name(self):
        return self.__name

    def set_phone(self, phon):
        self.__phone = phon

    def get_phone(self):
        return self.__phone

    def set_address(self, add):
        self.__address = add

    def get_address(self):
        return self.__address

    def set_vat_no(self,vat_no):
        self.__vat_no=vat_no

    def get_vat_no(self):
        return self.__vat_no
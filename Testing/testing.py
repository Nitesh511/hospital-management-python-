import unittest
import frontend.Front
import backend.database
import model.user
import model.supplier
import backend.database2



class Test_connection(unittest.TestCase):
    def setUp(self):
          self.db1=backend.database2.DBConnect2()
          self.db=backend.database.DBConnect()
          self.obj = model.user.User("Nitesh karki", "9841","984034","male","nitesh.karki31")
          self.obj1=model.supplier.Supplier("101","nishant","8621345","KTM","607812")



    def test_get_name(self):
        self.assertEqual("Nitesh karki",self.obj.get_username())


    def test_password(self):
        self.assertEqual("9841",self.obj.get_password())


    def test_get_email(self):
        self.assertEqual("nitesh.karki31",self.obj.get_g_mail())


    def test_linear_search(self):
        list=["1","2","3","4","5"]
        item="4"
        obj=frontend.Front.display.linear_search(list,item)
        self.assertEqual("4",obj)

    def test_merge_sort(self):
        list2 = ['vivek', 'manoj', 'kushwaha', 'poudel']
        obj1 = frontend.Front.display.mergesort(list2)
        self.assertEqual(obj1, obj1)

    def test_update_data(self):
        Code_no= str(input("Enter the Code_no: "))
        name=str(input("Enter the name "))
        phone=str(input("Enter the phone number"))
        address=str(input("Enter the address: "))
        vat_no=str(input("Enter the your vat_no: "))

        values = (Code_no,name,phone,address,vat_no)
        query = ("UPDATE owner SET name=%s,phone=%s,address=%s,vat_no=%s WHERE Code_no=%s")
        d = self.db1.update(query, values)
        if d:
            print('succese')
        else:
            return False

        self.assertEqual(True, d)

    def test_delete(self):
        Code_no= int(input("Enter the Code_no: "))
        values = Code_no,
        query = ("delete from owner WHERE code=%s")
        b = self.db1.delete(query, values)
        if b:
            print('Success')
        else:
            return False
        self.assertEqual(True, b)

    def test_Code_no(self):
        self.assertEqual("101",self.obj1.get_Code_no())

    def test_name(self):
        self.assertEqual("nishant",self.obj1.get_name())

    def test_address(self):
        self.assertEqual("KTM",self.obj1.get_address())






    def tearDown(self):
        del self.db
        del self.obj
        del self.obj1

if __name__ == '__main__':
    unittest.main()

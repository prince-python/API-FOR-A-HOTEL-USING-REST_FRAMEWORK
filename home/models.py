from django.db import models


class Home(models.Model):
    Customer_Full_Name = models.CharField(max_length=200)
    Customer_Addhar_Number =models.CharField(max_length=16)
    Contact_Number = models.IntegerField()
    Room_Number = models.IntegerField()
    Check_In_Date=models.DateTimeField(auto_now_add=True)
    Check_Out_Date = models.DateTimeField()
    Room_Price = models.IntegerField()
    
    

from django.db import models

status_choice =[
    (0, 'active'),
    (1, 'inactive'),
    (5, 'banned')
]
class userdata(models.Model):
    #id=
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    email=models.EmailField(unique=True)
    phone_no=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    status=models.IntegerField(choices=status_choice, default=1)
    added_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'members_userdata'  
        managed = False  

    def __str__(self):
        return self.name


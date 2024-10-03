from django.db import models


class GenreChoice(models.TextChoices):

    Action='Action','Action'
    Fiction='fiction','Action'
    Thriller='Thriller','Thriller'

# class Class_choice(models.IntegerChoice):
#     one=1,1
#     two=2,2
#     three=3,3
#     four=4,4
#     five=5,5
#     six=6,6
#     seven=7,7
#     eight=8,8
#     nine=9,9
#     ten=10,10


# class Div_choices(models.TextChoices):
#     div="A","A"
#     div2="B","B"
#     div3="C","C"
#     div4="D","D"

# class Fuel_choice(models.TextChoices):

#     petrol='petrol','petrol'

#     disel='disel','disel'

#     Ev='ev','ev'


GENRE_CHOICE=[('Action','Action'),
                ('fiction','fiction'),
                ('Thriller','Thriller'),
                ]

            

class Movies(models.Model):

    title=models.CharField(max_length=200,null=True)

    # genre=models.CharField(max_length=200,null=True,choices=GenreChoice.choices)

    genre=models.CharField(max_length=200,null=True,choices=GENRE_CHOICE)


    language=models.CharField(max_length=200,null=True)

    year=models.CharField(max_length=200,null=True)

    run_time=models.PositiveIntegerField(null=True)

    director=models.CharField(max_length=200,null=True)



# class Student(models.Model):

#     name=models.CharField(max_length=200,null=True)   

#     classs= models.CharField(max_length=200,null=True,choices=Class_choice.choices)

#     division=models.CharField(max_length=200,null=True,choices.Div_choices.choices)

#     contact=models.IntegerField(null=True)

#     about_me=models.TextField(null=True)

#     img=models.ImageField(null=True)

    

# class Car(models.Model):

#     name=models.CharField(max_length=200,null=True)

#     model=models.CharField(max_length=200,null=True)

#     year=models.IntegerChoice(null=True)

#     seat_capacity=models.IntegerField(null=True)

#     fuel_type=models.ChoiceField(max_length=200,null=True,choices=Fuel_choice.choices)

#     performance=models.floatField(max_length=200,null=True)

#     img=models.ImageField(null=True)

#     instock=models.BooleanField(null=True)

#     release_date=models.DateField()


# class Customer(models.model):

#     name=models.CharField(max_length=200,null=False)

#     last-name=models.CharField(max_length=200,null=False)

#     Adress=models.CharField(max_length=200,null=False)

#     street_address=models.CharField(max_length=200,null=True)

#     street_address_line2=models.CharField(max_length=200,null=True)

#     city=models.CharField(max_length=200,null=True)

#     state=models.CharField(max_length=200,null=True)

#     zip_code=models.IntegerField(null=True)

#     phone_number=models.IntegerField(null=False)

#     Email=models.EmailField(null=True)

#     about_us=models.CharField(max_length=200,null=False,)

#     feedback=models.CharField(max_length=200,null=True)

#     suggestions=models.CharField(max_length=200,null=True)

#     recomment=models.CharField(max_length=200,null=True)
















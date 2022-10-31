import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','acBusiness.settings')

import django
# Import settings
django.setup()

import random
from air_conditioners.models import AirConditioner
from brands.models import AcBrands
from categories.models import Categories,SubCategories
from faker import Faker

fakegen = Faker()
# topics = ['Search','Social','Marketplace','News','Games']
#
# def add_topic():
#     t = Topic.objects.get_or_create(top_name=topics)[0]
#     t.save()
#     return t



def populate(N=50):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Get Topic for Entry

        # Create Fake Data for entry
        fake_title = fakegen.name()
        fake_brand = AcBrands.objects.get_or_create(title="fake_ac")[0]
        fake_categorie = Categories.objects.get_or_create(title="fakeac")[0]
        fake_sub_categorie = SubCategories.objects.get(title='sub_fake')

        # Create new Webpage Entry
        AirConditioners = AirConditioner.objects.get_or_create(brand=fake_brand,categorie=fake_categorie,sub_categorie=fake_sub_categorie,title=fake_title,energy_efficiency='A+',btu=5153,description='yeyyyy')[0]

        # Create Fake Access Record for that page
        # Could add more of these if you wanted...


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(50)
    print('Populating Complete')

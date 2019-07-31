from myblog import models

def database():
    record = models.myblog.objects.get_or_create(bauthor = 'sreekanth',btitle = 'myblog',
                                            bdate = '2019-04-12',
                                            bdiscription = 'hello',
                                            bcategory = 'sports',
                                            bimpath = '')

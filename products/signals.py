import random,string

# <editor-fold desc="PRODUCT BRAND UNIQUE CODE CREATE">
def brand_unique_code_generator(sender,instance,*args, **kwargs):
    if not instance.unique_code:
        # data=instance.title
        # x = [i for i in range(4,15+1) if i%2!=0]
        # instance.unique_code='product'+x
        instance.unique_code=code_generator()

"""
https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits

>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.digits
'0123456789'
>>> string.ascii_uppercase + string.digits
'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

"""
def code_generator(size=5,chars=string.ascii_uppercase + string.digits):
    # code=''.join(random.choice(chars) for _  in range(size))
    code=''.join(random.choice(chars) for _  in range(size))
    print(code)
    return 'brand' + code
# brand12345, brand78458
# </editor-fold>

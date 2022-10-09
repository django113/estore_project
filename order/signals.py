import random, string


# <editor-fold desc="ORDER CODE CREATE RANDOM WITH order word">
def order_code_unique_code_generator(sender, instance, *args, **kwargs):
    if not instance.order_code:
        # x = [i for i in range(4,15+1) if i%2!=0]
        # instance.unique_code='product'+x
        instance.order_code = code_generator()


"""

>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.digits
'0123456789'
>>> string.ascii_uppercase + string.digits
'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

"""


def code_generator(size=5, chars=string.ascii_uppercase + string.digits):
    code = ''.join(random.choice(chars) for _ in range(size))
    print(code)
    return 'order' + code
# brand12345, brand78458
# </editor-fold>

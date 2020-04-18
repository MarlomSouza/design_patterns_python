from my_object_factory import MyObjectFactory

myclass = MyObjectFactory.create_object("myclass")
if myclass is not None:
    myclass.do_something("typing")
else:
    print("Not doing anything")

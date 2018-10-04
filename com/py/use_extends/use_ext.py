class grandf:
    def __init__(self, task_id, dag=None, *args, **kwargs):
        self.task_id = task_id
        self.dag = dag

    def say_fuck(self):
        print(" task_is = %s, dag = %s")

class person(grandf):
    def __init__(self, name, *args, **kwargs):
        super(person, self).__init__(*args, **kwargs)
        self.name = name
    def say_hello(self):
        print("Person to call say_hello() : %s" % str(self.name))

class man(person):
    def __init__(self, name, *args, **kwargs):
        super(man, self).__init__(name, *args, **kwargs)
        self.flag = False
        self.man_name = name
    def say_hello(self):
        # super(man, self).say_hello()
        super(man, self).say_hello()
        print("man to call say_hello() : %s" % str(self.man_name))

    def return_flag(self):
        return self.flag

m = man(task_id="yafei10_taskid", name="yafei")
m.say_hello()
m.say_fuck()
# c = 10
# while not m.return_flag() and c >= 0:
#     print("%d" % c)
#     c -= 1

# def tt(name, age, target = lambda : person("yafei").say_hello()):
#     target()
#     return print("my name is %s, and my age is %d" % (name, age))
# tt("qq", 23)

# hello = person("feifei").say_hello
# hello()

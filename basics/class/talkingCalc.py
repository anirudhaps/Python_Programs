#multiple inheritance

class Calculator:
    def calculate(self,expression):
        self.val = eval(expression) # we have to pass an expression as string

    def talk(self):
        print 'Value of the recent expression is ' + `self.val`

class Talker:
    def talk(self):
        print 'Hi, my value is ' + `self.val`

class TalkingCalc(Calculator,Talker):
    pass

# if we don't want to define any method or attribute in a class, then we have to
# simply write: pass

# Multiple Inheritance: two classes are inherited by class TalkingCalc. These
# are: Calculator and Talker

# Imp: The subclass TalkingCalc will inherit talk() from both Calculator and
# Talker classes. But, inside class TalkingCalc, Calculator's version of talk()
# will override(and hence makes inaccessible) the Talker's version of talk()
# beacause in the order of listing of superclasses in the definition of class
# TalkingCalc i.e. class TalkingCalc(Calculator,Talker), Calculator comes before
# Talker. Thus, in any such listing, all the methods of first listed superclass
# will override the same named methods defined in all other superclasses inside
# a subclass during multiple inheritance.

t = TalkingCalc()
t.calculate('5+4-9/3')
t.talk()
print TalkingCalc.__bases__ # displays the base classes of TalkingCalc class
print isinstance(t,TalkingCalc)
print isinstance(t,Talker)
print isinstance(t,Calculator)
# The object of sub-class is also an instance of all its base class because we
# can call and inherit the methods of all the base classes and access all the
# inherited attributes using this object
tl = Talker()
print isinstance(tl,TalkingCalc)
print t.__class__, tl.__class__ # used to print the class of an object
print issubclass(TalkingCalc,Talker)
print issubclass(TalkingCalc,Calculator)
print issubclass(Calculator,TalkingCalc)

# -*- coding: utf-8 -*-
my_name = "Luân Quang Huy"
my_age = 22
my_height = 180
my_weight = 55
my_eyes = "Black"
my_teeth = "White"
my_hair = "Black"

print "Let talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
print "%r" % my_eyes
print "%(language)s" % {'language' : "Python"} + "%d" % 5

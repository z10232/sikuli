from sikuli.Sikuli import *

r = Region(0, 0, 200,200)
print r.wait("test-res/apple.png")
print "number of screens: " + str(Screen.getNumberScreens())
s = Screen()
print "default screen bound: " + str(s.getBounds())
print s.wait("test-res/apple.png")
print "screen's last match: " +  str(s.lastMatch)
r = Region(200,200,50,50)
r.setThrowException(False)
print r.wait("test-res/apple.png")
print "region's last match: " +  str(r.lastMatch)

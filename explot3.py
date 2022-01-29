#!/usr/bin/env python2
import sys
import os

print "The dir is: %s" %os.listdir(os.getcwd())

os.unlink("/home/httpd/grades.txt")

# listing directories after removing path
print "The dir after removal of path : %s" %os.listdir(os.getcwd())

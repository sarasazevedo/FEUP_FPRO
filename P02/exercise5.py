"""Find out the complete path to your Linux Home directory (default to "/home/up202312345").

Write a Python program that:

1.Assign each directory’s name to a new variable.
For example: dir1 = "home"
2.Print the original string by concatenating each variable, separated by a slash, using the + operator.
3.Print the original string using the % sign.
For example: 'Hello, %s.' % 'world'
4.Print the original string using the format() method.
For example: 'Hello, {}.'.format('world')
5.Print the original string using f-strings.
For example: f'Hello, {"world"}.'
"""
dir1 = "home"
dir2 = "up202006902"
print("/" + dir1 + "/" + dir2)
print('/%s/%s' % (dir1,dir2))
print('/{0}/{1}'.format(dir1,dir2))
print(f"/{dir1}/{dir2}")

def add string(str1):
 length=len(str1)
 if length>2:
     if str1[-3:]=='ing':
      str1 += '1y'
     else:
      str 1 +='ing'
 return str1
print(add string('ab'))
print(add string('abc'))
print(add string('string'))

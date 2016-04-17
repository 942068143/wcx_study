# --encoding:utf-8 --
#格式化字符串
my_name='Zed A. Shaw'
my_age=35

print " Let's talk about %s." % my_name     # %s格式化字符串
print " Let's talk about age %d." % my_age  # %d格式化整数
print " Let's talk about name %r, age %r." % (my_name,my_age)  # %r格式化所有(整型,字符串,浮点型 ...)
#打印多个格式化变量,要把变量用()括起来

print "if i add %r and %r,i get %r" % (my_age,my_name,'my_age'+'my_name') #字符串和整数不能直接相加

import random

state = random.getstate()
# print(state)
print("Get State")
print(random.random())
print(random.random())
print(random.random())

print("Set State")
random.setstate(state)
print(random.random())
print(random.random())
print(random.random())

print("Set State Again")
random.setstate(state)
print(random.random())
print(random.random())
print(random.random())

# برای اینکه بتوانیم دنباله ای از اعداد رندم را دوباره
# تکرار کنیم از استیت استفاده میکنیم - دقت کنید بین هر 
# دو استیت برنامه اعداد رندم دوباره تکرار شده اند
"""
یکبار اجرای برنامه
Get State
0.8424125864258368
0.5868829522333908
0.1852885894912859
Set State
0.8424125864258368
0.5868829522333908
0.1852885894912859
Set State Again
0.8424125864258368
0.5868829522333908
0.1852885894912859
"""

"""
اجرای دوم برنامه
Get State
0.7787255862057021
0.7453083030875739
0.0054086510034494495
Set State
0.7787255862057021
0.7453083030875739
0.0054086510034494495
Set State Again
0.7787255862057021
0.7453083030875739
0.0054086510034494495
"""

# اما تفاوت استیت با سیید در چیست؟
# اگر برنامه را دوباره اجرا کنید اعداد رندم در اجراهای
# بعدی تغییر میکنند

# اما

# از سیید به این دلیل استفاده میکنیم که در اجراهای متوالی
# بتوانیم به اعداد رندم یکسان دسترسی داشته باشیم

print("#"*100)
print("Seed = 30")
random.seed(30)
print(random.random())
print(random.random())
print(random.random())


print("Seed = 30")
random.seed(30)
print(random.random())
print(random.random())
print(random.random())


print("Seed = 30")
random.seed(30)
print(random.random())
print(random.random())
print(random.random())

"""
اجرای اول برنامه
Seed = 30
0.5390815646058106
0.2891964436397205
0.03003690855112706
Seed = 30
0.5390815646058106
0.2891964436397205
0.03003690855112706
Seed = 30
0.5390815646058106
0.2891964436397205
0.03003690855112706
"""

"""
اجرای دوم برنامه
Seed = 30
0.5390815646058106
0.2891964436397205
0.03003690855112706
Seed = 30
0.5390815646058106
0.2891964436397205
0.03003690855112706
Seed = 30
0.5390815646058106
0.2891964436397205
0.03003690855112706
"""
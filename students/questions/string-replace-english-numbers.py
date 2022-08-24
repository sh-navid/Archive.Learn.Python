en_num = "0123456789"
fa_num = "۰۱۲۳۴۵۶۷۸۹"

my_text = "122۴۵۴۵90"
for index, number in enumerate(fa_num):
    my_text = my_text.replace(fa_num[index], en_num[index])

print(my_text)
"""
122454590
"""
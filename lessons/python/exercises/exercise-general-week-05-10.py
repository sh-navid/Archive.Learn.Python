from enum import Enum

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# فرض کنید به عنوان مثال میخواهیم اطلاعات نامهای فارسی را ذخیره کنیم

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# هر نام میتواند دخترانه، پسرانه یا مرتبط به هر دو جنسیت باشد
class Gender(Enum):
    NOT_GENDER_SPECIFIC = "~"
    GIRL = "G"
    BOY = "B"

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# هر نام تا چه اندازه رایج است؟
class Frequency(Enum):
    RARE = "R"
    NORMAL = "N"
    FREQUENT = "F"

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# کلاسی برای نگه داری اطلاعات نام های فارسی
class BabyName:
    name = None
    name_is_for = Gender.NOT_GENDER_SPECIFIC
    frequency = Frequency.FREQUENT

    def __init__(self, name: str, name_is_for: Gender, frequency: Frequency) -> None:
        self.name = name
        self.name_is_for = name_is_for
        self.frequency = frequency

    def __str__(self) -> str:
        name = self.name.ljust(12)
        gender = self.name_is_for.name.ljust(5)
        return f"{self.frequency.value} - {name} > {gender}"

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۱
# آیا میتوانید به لیست نام هایی که ساختیم دو نام دیگر اضافه کنید
# که هم نام پسر باشد هم نام دختر؟

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# لیست نامهای ما
baby_names = []
baby_names.append(BabyName("Saeed", Gender.BOY, Frequency.NORMAL))
baby_names.append(BabyName("Maryam", Gender.GIRL, Frequency.NORMAL))
baby_names.append(BabyName("Ali", Gender.BOY, Frequency.FREQUENT))
baby_names.append(BabyName("Rostam", Gender.BOY, Frequency.RARE))

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۲
# آیا میتوانید به کلاس نام یک ویژگی دیگر اضافه کنید که مشخص کننده
# این باشد که نام ایرانی یا غیر ایرانی است؟

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# نام هایی که ساختیم را نمایش میدهیم
for baby_name in baby_names:
    print(baby_name)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۳
# آیا میتوانید نامهایی که ساختد را با حلقه
# while
# نمایش دهید

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۴
# آیا میتوانید نامهایی که ساختید را در یک فایل ذخیره کنید؟

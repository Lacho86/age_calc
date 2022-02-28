from h11 import Data


def age_calc(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today - dob).days / 365.25)
    print(age)

age_calc(1986, 2, 28)

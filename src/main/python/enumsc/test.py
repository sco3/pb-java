from enum import Enum, StrEnum, auto
import enum


class Test(StrEnum):
    TEST=auto()

c = Test.TEST
print(c)

print (__file__)

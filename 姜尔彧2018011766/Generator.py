# coding=utf-8

"""
  Author:  Jiang Eryu 姜尔彧 2018011766
  Purpose: Generate random data set with generator.
  Created: 20/6/2020
"""

import random
import string


def dataSampling(datatype, datarange, num, strlen=8):
    """
    :Description: Generate a given condition random data set.
    :param datatype:int/float/str
    :param datarange: iterable data set
    :param num: number
    :param strlen:8
    :return: a dataset
    """
    try:  # 异常处理
        result = []
        if datatype is int:
            for index in range(0, num):
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.append(item)
                yield item
                continue
        elif datatype is float:
            for index in range(0, num):
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.append(item)
                yield item
                continue
        elif datatype is str:
            for index in range(0, num):
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.append(item)
                yield item
                continue
    except TypeError:
        print("? Type Error")
    except StopIteration:
        print("? Iteration Error")
    finally:
        print(""),


def dataScreening(datatype, result, *conditions):
    """
    :Description: Screen a given condition random data set.
    :param datatype: int/float/str
    :param result: random dataset
    :param conditions: variable-length argument
    :return: a dataset
    """
    try:  # 异常处理
        result_scr = []
        if datatype is int:
            for i in result:
                it = iter(conditions)
                low = next(it)
                high = next(it)
                if low <= i <= high:
                    result_scr.append(i)
                continue
        elif datatype is float:
            for i in result:
                it = iter(conditions)
                low = next(it)
                high = next(it)
                if low <= i <= high:
                    result_scr.append(i)
                continue
        elif datatype is str:
            for i in result:
                for sub in i:
                    if sub in conditions:
                        result_scr.append(i)
                continue
        return result_scr
    except TypeError:
        print("? Type Error")
    except StopIteration:
        print("？Iteration Error")
    finally:
        print(""),


def apply():
    print("int类型示例：")
    result = dataSampling(int, (1, 1000), 5)
    print("条件筛选数："),
    result_scr = dataScreening(int, result, 10, 500)  # 筛选（10，500）以内的整型随机数
    print(result_scr)
    print("@姜尔彧2018011766\n")

    print("float类型示例：")
    result = dataSampling(float, (1.0, 1000.2), 5)
    print("条件筛选数："),
    result_scr = dataScreening(float, result, 10.8, 500.9)  # 筛选(10.8, 500.9)以内的浮点随机数
    print(result_scr)
    print("@姜尔彧2018011766\n")

    print("字符串类型示例：")
    result = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 10)
    print("条件筛选数："),
    result_scr = dataScreening(str, result, 'a', 'at')  # 筛选带有'a'和'at'的字符串
    print(result_scr)
    print("@姜尔彧2018011766\n")


apply()

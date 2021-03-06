##!/usr/bin/python3
"""
  Author:  ZhengPeng.Han
  Purpose: Generate random data set.
  Created: 28/5/2020
"""
import random
import string

def dataSampling(datatype, datarange, num, strlen=8):
    '''
    :Description: Generate a given condition random data set.
    :param datatype: The type of data which include int float and string
    :param datarange: iterable data set
    :param num: Input parameters that means The final result of the number of elements
    :param strlen:The length of input strings
    :return: a dataset
    '''
    result = set()
    try:
        if (datatype is int):
            while len(result) < num:
                it = iter(datarange)
                item = random.randint(next(it), next(it))
                result.add(item)  # 为防止随机数重复而使用while
        elif (datatype is str):
            while len(result) < num:
                item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
                result.add(item)
        elif (datatype is float):
            while len(result) < num:
                it = iter(datarange)
                item = random.uniform(next(it), next(it))
                result.add(item)
        return result
    except ValueError:
        print("传入参数无效")
    except TypeError:
        print("类型错误，参数可能无法迭代")
    except Exception as e:
        print(e)


def dataScreening(data,*args):
    '''
        :param datatype: The type of data which include int float and string
        :param datarange: Given conditions used to filter data
        :param data:The data used for filtering which generated by dataSampling
        :return: a dataset
    '''
    scrresult = set()
    try:
        for it in data:
            if (type(it) is int):
                cond = iter(args)
                if(next(cond) <= it and next(cond) >= it):
                    scrresult.add(it)
            elif (type(it) is str):
                for condstr in args:
                    if(condstr in it):
                        scrresult.add(it)
            elif (type(it) is float):
                cond = iter(args)
                if(next(cond) <= it and next(cond) >= it):
                    scrresult.add(it)
    except ValueError:
        print("传入参数无效")
    except TypeError:
        print("类型错误，参数可能无法迭代")
    except NameError:
        print("未声明/初始化对象")
    except Exception as e:
        print(e)
    return scrresult

def apply():
    try:
      result1 = dataSampling(str, string.ascii_letters + string.digits + "@#$!", 5)
      print(result1)
      scrresult1 = dataScreening(result1,'a')
      if not scrresult1:
          print("Data to meet the requirements not found !")
      else:
          print(scrresult1)

      result2 = dataSampling(int,(0,100),5)
      print(result2)
      scrresult2 = dataScreening(result2,10,90)
      if not scrresult2:
          print("Data to meet the requirements not found !")
      else:
          print(scrresult2)

      result3 = dataSampling(float,(0,100),5)
      print(result3)
      scrresult3= dataScreening(result3,10,90)
      if not scrresult3:
          print("Data to meet the requirements not found !")
      else:
          print(scrresult3)

    except Exception as ex:
      print(ex)

apply()

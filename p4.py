import sys
import math
from decimal import Decimal

len_max_float = len(str(sys.float_info.max))

class Node(object):
    num_str = ""
    next = None
    prev = None


def big_div(num_str_arr, ret_arr):
    rem = 0
    val = ""
    ret = ""
    ans = 0
    i = 0
    while i < len(num_str_arr):
        

        val = num_str_arr[i]
        if rem == 1:
            val = "1" + val
            rem = 0
        
        if int(val) < 2 and i < len(num_str_arr) -1:
            ret += "0"
            val = val + num_str_arr[i + 1]
            i += 1

        ret = ret + str(int(math.floor(int(val)/2)))
        if (int(val) % 2 != 0):
            rem = 1
        i += 1

    ret_arr[0] = ret
    ret_arr[1] = str(rem)


def big_mult(num_str_arr, ret_arr):
    carry = 0
    val = ""
    ret = ""
    ans = 0
    i = len(num_str_arr) - 1
    if ret_arr[1] != "":
        carry = int(ret_arr[1])

    while i >= 0:
        val = num_str_arr[i]

        val = str(int(val) * 3)

        if carry > 0:
            val = str(int(val) + carry)
            carry = 0

        if int(val) > 9:
            carry = int(math.floor(int(val) / 10))
            val = str(val[1])

        ret =   val + ret
        i -= 1

    ret_arr[0] = ret
    ret_arr[1] = str(carry)


def big_add(num_str_arr, ret_arr):
    carry = 0
    val = ""
    ret = ""
    ans = 0
    i = len(num_str_arr) - 1
    if ret_arr[1] != "" and ret_arr[1] != "0":
        carry = int(ret_arr[1]) #should just be 1

    if int(num_str_arr[i]) + carry < 10:
        ret_arr[0] = num_str_arr[:-1] + str(int(num_str_arr[i]) + carry)
        carry = 0
        ret_arr[1] = "0"
        return

    else:
        while i >= 0:
            val = num_str_arr[i]

            if carry > 0:
                val = str(int(val) + carry)
                carry = 0
            if int(val) >= 10:
                carry = 1
                val = str(val[1])

            ret =  val + ret
            i -= 1

    ret_arr[0] = ret
    ret_arr[1] = str(carry)


def long_divide(num):
    orig_node = Node()
    node = orig_node
    count = 0

    for i in range(0, len(num)):
        if count == len_max_float:
            count = 0
            node.next = Node()
            node.next.prev = node
            node = node.next
        node.num_str += num[i]
        count += 1

    tail = node


    arr = ["", ""]
    node = orig_node
    temp1 = ""
    result = ""
    while node != None:
        temp1 = node.num_str
        if arr[1] != "0" and arr[1] != "":
            temp1 = arr[1] + node.num_str

        big_div(temp1, arr)
        if len(arr[0]) > len(node.num_str):
            arr[0] = arr[0][1:]
        result += arr[0]
        node = node.next

    if result[0] == "0":
        result = result[1:]
    return result


def long_multiply(num):
    orig_node = Node()
    node = orig_node
    count = 0

    for i in range(0, len(num)):
        if count == len_max_float:
            count = 0
            node.next = Node()
            node.next.prev = node
            node = node.next
        node.num_str += num[i]
        count += 1

    tail = node

    arr = ["", ""]
    node = tail
    temp1 = ""
    result = ""

    while node != None:
        temp1 = node.num_str

        big_mult(temp1, arr)
        result = arr[0] + result
        node = node.prev

    if arr[1] != "" and arr[1] != "0":
        result = arr[1] + result

    if result[0] == "0":
        result = result[1:]
    return result


def long_add(num):
    orig_node = Node()
    node = orig_node
    count = 0

    for i in range(0, len(num)):
        if count == len_max_float:
            count = 0
            node.next = Node()
            node.next.prev = node
            node = node.next
        node.num_str += num[i]
        count += 1

    tail = node

    arr = ["", ""]
    node = tail
    temp1 = ""
    result = ""
    arr[1] = 1

    while node != None:
        temp1 = node.num_str
        big_add(temp1, arr)
        result = arr[0] + result
        node = node.prev

    if arr[1] != "" and arr[1] != "0":
        result = arr[1] + result
    if result[0] == "0":
        result = result[1:]
    return result


with open(sys.stdin.readline()[:-1]) as ofo:
    for value in ofo:
        i = 0
        value = value.rstrip('\n')
        while int(value) != 1:
            if int(value[len(value) - 1]) % 2 == 0:
                value = long_divide(value)
            else:
                value = long_multiply(value)
                value = long_add(value)
            i += 1

        print(i)
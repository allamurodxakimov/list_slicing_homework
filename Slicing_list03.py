def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    return list1[0:len(list1):1]+list1[-1::-1]
print(main(list1=['a', 'b', 'c', 'd']))
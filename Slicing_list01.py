def main(lis):
    """
    A list called numbers is given. Return the items in the even index.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.
    """
    return lis[0:len(lis):2]
print(main(lis=[1, 2, 3, 4, 5]))
print(main(lis=[0, 1, 2, 3, 4, 5]))
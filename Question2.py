import sys


def generate_lists(n):
    list_1 = [{"id": i, "premium": i*1e6 + 9*i*1e4, "include?": True if i%2 == 0 else False} for i in range(n)]
    list_2 = [{"id": i, "premium": i*1e7 - 5*i*1e4, "include?": True if i%3 == 0 else False} for i in range(n)]
    return list_1, list_2


def sum_premiums(n):
    sum_of_L1 = 0
    sum_of_L2 = 0
    
    l1, l2 = generate_lists(n)

    combine = zip(l1, l2)

    for x, y in combine:
        if x.get("id") == y.get("id") and x.get("include?") == y.get("include?"):
            if x.get("include?") == True and y.get("include?") == True:
                sum_of_L1 += x.get('premium')
                sum_of_L2 += y.get('premium')
    
    return sum_of_L1, sum_of_L2

        


if __name__ == "__main__":
    n = int(sys.argv[-1])
    s1, s2 = sum_premiums(n)
    print('Sum of Premium from list 1: {}'.format(s1))
    print('Sum of Premium from list 2: {}'.format(s2))
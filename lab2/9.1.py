m = int(input())
n = int(input())
home_books = [input() for i in range(m)]
books_in_list = [input() for i in range(n)]
for item in books_in_list:
    print('YES') if item in home_books else print('NO')
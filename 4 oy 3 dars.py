# 20

# n = int(input("N sonini kiriting:"))
# print(f"Sonlarni kiriting(Vergul bilan)")
# s = list(map(int, input().split(',')))
# if len(s) != n:
#     print(f"Kiritilgan sonlar N ta bo'lishi kerak!!!")
# else:
#     l = []
#     for i in range(n-1):
#         if s[i] < s[i+1]:
#             l.append(s[i])
#     print("O'ng qo'shnisidan kichik sonlar:")
#     print(l)
#     print("Ularning soni:", len(l))


# 21

# n = int(input("N sonini kiriting:"))
# print(f"Sonlarni kiriting(Vergul bilan)")
# s = list(map(float, input().split(',')))
# if len(s) != n:
#     print(f"Kiritilgan sonlar N ta bo'lishi kerak!!!")
# else:
#     a = sorted(s)
#     if s == a:
#         print('True')
#     else:
#         print('False')


# 22

# n = int(input("N sonini kiriting: "))
# print(f"Sonlarni kiriting (vergul bilan):")
# s = list(map(float, input().split(',')))
# if len(s) != n:
#     print(f"Kiritilgan sonlar N ta bo'lishi kerak!!!")
# else:
#     l = []
#     for i in range(n - 1):
#         if s[i] > s[i + 1]:
#             l.append(s[i])
#         else:
#             print(f"Qonuniyatni buzgan element nomeri: {i + 1}")
#             break
#     else:
#         if l == sorted(l, reverse=True):
#             print("Qonuniyat buzilmadi: 0")


# 23

# n = int(input("N sonini kiriting: "))
# print("Sonlarni kiriting (vergul bilan):")
# s = list(map(float, input().split(',')))
#
# if len(s) != n:
#     print(f"Kiritilgan sonlar soni N ga teng emas!")
# else:
#     a = True
#     for i in range(1, n - 1):
#         if not ((s[i] > s[i - 1] and s[i] > s[i + 1]) or (s[i] < s[i - 1] and s[i] < s[i + 1])):
#             print(f"Qonuniyatni buzgan element nomeri: {i + 1}")
#             a = False
#             break
#     if a:
#         print(0)


# 24

# n = int(input("N sonini kiriting: "))
# print("Sonlarni kiriting (vergul bilan):")
# s = list(map(int, input().split(',')))
# if len(s) != n:
#     print(f"Kiritilgan sonlar soni N ga teng emas!")
# else:
#     l = []
#     for i in range(n):
#         if s[i] == 0:
#             l.append(i)
#
#     if len(l) < 2:
#         print("To‘plamda kamida 2 ta nol bo‘lishi kerak!")
#     else:
#         a = l[-2]
#         b = l[-1]
#         c = 0
#         for i in range(a + 1, b):
#             c += s[i]
#         print(f"Oxirgi 2 ta nol orasidagi sonlar yig‘indisi: {c}")


# 25

# n = int(input("N sonini kiriting: "))
# print("Sonlarni kiriting (vergul bilan):")
# s = list(map(int, input().split(',')))
# if len(s) != n:
#     print(f"Kiritilgan sonlar soni N ga teng emas!")
# else:
#     l = []
#     for i in range(n):
#         if s[i] == 0:
#             l.append(i)
#
#     if len(l) < 2:
#         print("To‘plamda kamida 2 ta nol bo‘lishi kerak!")
#     else:
#         a = l[0]
#         b = l[-1]
#         c = 0
#         for i in range(a + 1, b):
#             c += s[i]
#         print(f"Birinchi va Oxirgi 2 ta nol orasidagi sonlar yig‘indisi: {c}")


# 26

# n = int(input("N sonini kiriting:"))
# k = int(input("K sonini kiriting:"))
# for i in range(1, n+1):
#     a = int(input((f"{i}-sonni kiriting:")))
#     c = a ** k
#     print(f"{a} ning {k}-darajasi: {c}")


# 27

# n = int(input("N sonini kiriting:"))
# for i in range(1, n+1):
#     a = int(input(f"{i}-sonni kiriting:"))
#     c = a ** i
#     print(f"{i} ning {i}-darajasi: {c}")


# 28

# n = int(input("N sonini kiriting:"))
# for i in range(n):
#     a = int(input(f"{i+1}-sonni kiriting:"))
#     c = a ** (n-i)
#     print(f"{a} ning {n-i}-darajasi: {c}")


# 29

# n = int(input("N toplam elementlari sonini kiriting:"))
# k = int(input("K toplam sonini kiriting:"))
# s = 0
# for i in range(k):
#     print(f"{i+1}-to'plamdagi {n} ta butun sonni kiriting:")
#     for j in range(n):
#         num = int(input(f"{j+1}-sonni kiriting: "))
#         s += num
# print(f"Barcha sonlarning yig'indisi: {s}")









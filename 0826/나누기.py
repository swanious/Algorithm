N = 94521583
F = 7

N_str = ''
N_str = str(N)[:-2] + "0" * 2

stoi = int(N_str)
num_save = 0
while stoi % F != 0:
    stoi += 1
num_save = stoi

if len(str(num_save)[-2:]) < 2:
    print('0' + str(num_save)[-2:])
else:
    print(str(num_save)[-2:])






# if N % F == 0:
#     if len(str(N)[-2:]) < 2:
#         print('0' + str(N)[-2:])
#     else:
#         print(str(N)[-2:])
# else:
#     N += F - (N % F)
#     if len(str(N)[-2:]) < 2:
#         print('0' + str(N)[-2:])
#     else:
#         print(str(N)[-2:])

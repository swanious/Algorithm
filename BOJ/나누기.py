N = 5
F = 3

N_str = ''
N_str = str(N)[:-2] + "0" * 2

stoi = int(N_str)
num_save = 0
while stoi % F != 0:
    stoi += 1
num_save = stoi

if len(str(num_save)[-2:]) < 2:
    print(f'{num_save:02d}'[-2:])
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

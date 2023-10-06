# cd contain

seq = input('введіть послідовність:')
counter_of_CG = 0

seq = seq.lower()

for char in seq:
    if char =='c' or char =='g':
        counter_of_CG += 1

contain_of_CG = counter_of_CG / len(seq) *100

temp_mel =((counter_of_CG*4)+(len(seq)-counter_of_CG*2))

print(f'{contain_of_CG} %')
print(f'{temp_mel} (&deg)')





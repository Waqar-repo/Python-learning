name = ['waqar', 'ahmad','hina', 'razzaq']
print(name)
name[1] = 'Ahmad'
print(name[0:3])
print(name)


# find the largest number in a list

number = [80,90,1,2,44,100,101,501]
for check_num in number:
    output = check_num
    if output < check_num:
        for i in number:
            i+=1
print(output)


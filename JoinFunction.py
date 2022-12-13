sample_list=['chalk','duster','board','pen']
for item in sample_list:
    if item is not 'pen':
        print(item,"and" ,end="")
    else:
        print(item)
    print(item)

print(" and ".join(sample_list))

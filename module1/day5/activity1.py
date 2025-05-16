cp = int(input('enter your cp: '))
sp = int(input('enter your sp: '))
profit = sp-cp
loss = cp-sp
if cp<sp :
    print(f'profit = {profit}')
elif cp>sp:
    print(f'loss = {loss}')
else:  
    print('no profit or loss')
    
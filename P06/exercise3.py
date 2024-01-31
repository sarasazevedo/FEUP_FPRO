'''We want to write a function that helps in producing change in Euro coins for a given money amount. In the Euro denomination there are coins for 2€, 1€, 50c, 20c, 10c, 5c, 2c and 1c. If we want to give change using the least amount of coins, we should always use the largest coin for the amount left. For example, to pay 3.45€ we should use coins 2€, 1€, 20c, 20c (again) and finally 5c.

Write a function change(amount) that receives a certain amount and returns a list with the least number of coins to pay that amount. To avoid round-off errors both the amount and coins are positive integers (the number of cents).

'''
def change(amount):
    coins = [200,100,50,20,10,5,2,1]
    resultado = []
    
    for i in coins:
        while amount // i != 0:
            resultado.append(i)
            amount -= i
            
    return resultado
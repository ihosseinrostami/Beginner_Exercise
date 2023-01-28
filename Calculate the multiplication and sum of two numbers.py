#Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

#define function
def pos (num1,num2): #pos = product or sum
    product = num1 * num2
#define condition
#do not forget intend block (tab)
    if product <= 1000 :
        return product
    else :
        return num1 + num2
#example for code
result = pos(20,30)
print("the result is", result)
def nums(nums):
    sumsNegativos = 0
    SumsPositivos = 0
    promedio = 0
    lenPositivos = 0
    for num in nums:    
        if num < 0:
            sumsNegativos += num
        else: 
            SumsPositivos += num
            lenPositivos += 1
        
    promedio = SumsPositivos / lenPositivos
    print('suma de numeros negativos: ', sumsNegativos)
    print('promedio de numeros positivos: ', promedio)


numsUser = list()
for i in range(1,6):
    enter = int(input('ingrese un numero: \n'))
    if enter == 0 or not isinstance(enter, int):
        print('Tiene que ser numeros menores a 0 o mayores y, tienen que ser numeros')
    else:
        numsUser.append(int(enter))
else:
    nums(numsUser) 
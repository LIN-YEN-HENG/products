products = []
while True :
    name = input('請輸入商品名稱: ')
    if name == 'q':
            break
    price = input('請輸入商品價格: ')
    products.append([name,price])
    #np = []
    #np.append(name)
    #np.append(price)
    #products.append(np)
print(products)

for product in products:
	print(product[0], '的價格是', product[1])

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for product in products:
		f.write(product[0] + ',' + str(product[1]) + '\n' )
faturamento = 1000
custo = 600

lucro = faturamento - custo

#if 
   #o que eu quero que aconteça se essa condiçãofor verdadeira

#else:
    #o que eu quro que aconteça se essa condição for falsa
    
if  lucro >= 0:
   print("lucro de",lucro)
   print("Deu lucro")

else:
   print("prejuizo de",lucro)
   print("Deu prejuizo")


#exemplo
#produtos = ["iphone","ipad","airpod"]
#novo_produto = input("Digite o nomedo produto")
#if novo_produto in produtos:
#   print("produto existente")
#else:
#   print (f"{novo_produto} cadastro com sucesso")
#  produtos.append {novo_produto}
   
#  print (produtos)
 
#exemplo 2:
# bonus dos funcionarios
# vendas maiores do que 15000,ele gaha 500 de bonus
# se as vendas forem entre 5000 e 15000, ele ganha 100 de bonus
# se as vendas forem menores do que 5000 então ele não ganha bonus
 
#vendas = 20000
# if vendas >= 15000:
#    bonus = 500
#else:
#   if vendas>= 5000:
 #     bonus = 100
#   else:
#      bonus = 0
   
#print(f"bonus funcionario: {bonus}")

#if vendas >= 15000:
#   bonus = 500
#elif vendas >= 5000:
#   bonus = 100
#else:
#   bonus = 0
   
#print(f"bonus funcionario: {bonus}")

#Exemplo 3:
# bonus dos funcionarios
# vendas maiores do que 15000,ele gaha 500 de bonus
# se as vendas forem entre 5000 e 15000, ele ganha 100 de bonus
# se as vendas forem menores do que 5000 então ele não ganha bonus
 #so ganha bonus se as vendas totais da empresa forem maioresdo que 100000
       
vendas_empresa = 200_000 
meta_empresa = 100_000
vendas_funcionários = 11000

if vendas_funcionários >= 15000 and vendas_empresa>= meta_empresa:
   bonus = 500
elif vendas_funcionários >= 5000 and vendas_empresa >= meta_empresa:
   bonus = 100
else:
   bonus = 0
   
print(f"bonus do funcinário:{bonus}")
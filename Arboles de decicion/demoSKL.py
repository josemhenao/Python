from sklearn import tree
"""
	X = [
		 0/1 -> Masculino/Femenino,
		 Estatura,
		 Peso,
		 Talla de calzado
		]
"""

X = [[0,165,48,34],[0,158,67,37],[1,187,78,41],[1,170,66,40],[0,173,63,38],[0,167,58,37],[1,157,38,41],[1,166,39,43],[1,178,68,39],
	[0,175,59,38],[1,189,88,42],[1,165,65,39],[1,176,68,40],[0,172,54,39],[0,149,56,35],[0,168,57,38],[1,178,70,39],[1,187,90,42]
]

Y = ["Colombia","México","Inglaterra","Colombia","Inglaterra","Argentina","México","Colombia","Alemania",
	 "Colombia","Alemania","Colombia","México","Alemania","Colombia","Inglaterra","Argentina","Alemania"]

print('len X: ',len(X))
print('len Y: ',len(Y))
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
prediction = clf.predict([[1,165,65,39],[1,196,88,41]])
print (prediction)
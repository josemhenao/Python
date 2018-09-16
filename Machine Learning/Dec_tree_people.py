from sklearn import tree
X = [[165,48,34],[155,67,37],[167,75,38],[170,66,40],[163,63,37],[163,38,7],[157,38,12],[166,39,43],[178,38,10],
	[175,59,38],[186,85,42],[165,65,39],[176,68,40],[172,54,37],[149,56,34],[164,57,36],[178,70,39],[187,90,42],[60,40,22]
]

Y = ["Mujer","Mujer","Hombre","Hombre","Mujer","Mujer","Hombre","Hombre","Hombre",
	 "Mujer","Hombre","Hombre","Hombre","Mujer","Mujer","Mujer","Hombre","Hombre","Perro"]
	 
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
estatura = int(input("Dime la estatura: "))
peso = int(input("Dime el peso: "))
talla = int(input("Dime la talla de zapatos: "))
prediction = clf.predict([[estatura,peso,talla]])
print ("Es muy probable que la persona sea: "+prediction[0])

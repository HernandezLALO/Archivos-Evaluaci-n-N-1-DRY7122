aclNum = int(input("Cual es el número de tu ACL? "))
if aclNum >= 1 and aclNum <= 99:
 print("Este es un ACL de tipo estándar.")
elif aclNum >=100 and aclNum <= 199:
 print("Este es una ACL de tipo extendida")
else:
 print("Esta ACL no es extendida ni estandar .")



def AlhalozatSzamitas():
	halozat = input("Hálózat: ")
	db = int(input("Hány részre bontjuk: "))
	alhalozat_db_lista = []

	i = 0
	while i != db:
		alhalozat = int(input(f"{i+1}. alhálózat host db: "))
		alhalozat_db_lista.append(alhalozat)
		i += 1

	bitertek_lista = [128,64,32,16,8,4,2,1]
	maszk_lista = []


	sorrend = sorted(alhalozat_db_lista,reverse=True)

	for j in sorrend:
		for k in bitertek_lista:
			if k/j == 1:
				maszk_lista.append(j*2)
			elif k//j<2 and k//j>0 and not k/j == 1:
				maszk_lista.append(k)



	maszk_ertek = 0
	maszk = 0

	for x in range(len(sorrend)):
		elsoharom = ".".join(halozat.split(".")[:3])+"."
		tavolsag = bitertek_lista.index(maszk_lista[x])


		maszk_lista.insert(0, 0)
		maszk_ertek += int(maszk_lista[x])
		maszk_lista.remove(0)

		halozat = elsoharom + str(maszk_ertek)		
		maszk = sum(bitertek_lista[:tavolsag+1])



		elso = elsoharom + str(maszk_ertek+1)
		utolso = elsoharom + str(maszk_ertek+maszk_lista[x]-2)
		broadcast = elsoharom + str(maszk_ertek+maszk_lista[x]-1)

		print(f"\n{x+1}.Hálózat")
		print(f"H: {halozat}/{24 + tavolsag+1}")
		print(f"M: 255.255.255.{maszk}")
		print(f"E: {elso}")
		print(f"U: {utolso}")
		print(f"Bc: {broadcast}")





AlhalozatSzamitas()















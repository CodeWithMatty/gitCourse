print("ciao e benvenuto su calcolatrice sefont")
nomeCliente = input("Come ti chiami? ")
tipoDiOperazione = input("Ti chiami " + nomeCliente + "? Ah, ok, allora " + nomeCliente + ", qual è l'operazione che devi fare? addizione o sottrazione?")
if tipoDiOperazione == "addizione":
    numero1=input("qual e' il primo numero?")
    numero2=input("e il secondo?")
    print("Ok, il risultato è", int(numero1) + int(numero2))

elif tipoDiOperazione == "sottrazione":
    numero1=input("qual e' il primo numero?")
    numero2=input("e il secondo?")
    print("Ok, il risultato è", int(numero1) - int(numero2))
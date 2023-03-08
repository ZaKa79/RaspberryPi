# Kristians Kaffe Mecca

# Vi bygger en Robot

print("Hej, velkommen til Kristian's Kaffe")

name = input("havd er dit navn?\n")


if name == "ben":
  evil_status = input("er du ond?\n")
  if evil_status == "ja":
      print("smut det er en lukket fest")
      exit()
  else:
    print("Fantastisk")
else:
  print("Hej " + name + ",tak fordi du valgte Kristian's Kaffe\n\n\n")


menu = "Kaffe, Latte, Kakao"

print(name + " hvad kunne du tænke dig i dag? Her er dagens menu.\n" + menu)

order = input()

price = 8

styk = input("hvor mange kopper ønsker du?\n")

totalt = price * int(styk)

print("det bliver " + str(totalt) + "kr")

print("Godt valg " + name + " jeg får din " + order + " klart til dig om et sekundt")
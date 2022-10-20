import tabulate
import requests

collegiateApi = "b0fc7b5e-4321-4319-8c4a-24258cab0d0b"
schoolApi = "a91ebbc0-a9ab-4e48-97a5-dda5f1fcef68"
# https://dictionaryapi.com/api/v3/references/sd4/json/test?key=a91ebbc0-a9ab-4e48-97a5-dda5f1fcef68
endpointCollegiate = "https://dictionaryapi.com/api/v3/references/collegiate/json/"
endpointSchool = "https://dictionaryapi.com/api/v3/references/sd4/json/"

cnt = True
words = [[], [], []]

while cnt:
    ui = input()
    if ui == " ":
        break
    elif ui != "":
        words[0].append(ui)

for word in words[0]:
    call = endpointCollegiate + word + "?key=" + collegiateApi
    response = requests.get(call)
    responsejson = response.json()
    try:
        words[1].append(responsejson[0]["shortdef"][0])
    except TypeError:
        words[1].append("N/A")

for word in words[0]:
    call = endpointSchool + word + "?key=" + schoolApi
    response = requests.get(call)
    responsejson = response.json()
    try:
        words[2].append(responsejson[0]["shortdef"][0])
    except TypeError:
        words[2].append("N/A")

# words = [["Hi", "ur special", "Hello there", "general kenobi", "bai"], ["Another word for hello", "A term of endearment", "General Kenobi", "Hello There", "Goodbye"]]

try:
    f = open("definition.txt", "w")
    f.write(tabulate.tabulate(words, tablefmt="grid"))
    f.close()
    print("write complete")
except:
    print("ERROR DUMB ASS")

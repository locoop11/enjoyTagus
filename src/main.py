#  Dicionario com a lista de driver disponiveis indexados por ano, mes, dia e hora
scheduledDrivers = {2022: {1: {1: { 12: ["Maria", "John"]}}}}

# Dicionario com a lista de drivers e as suas caracteristicas
drivers = {"John": {"stars": 4, "languages": ["English","Spanish"], "tarifa": "80", 
                    "especializaçao": "conforto", "tempo_max": "10", "horas_acomuladas": "3"} ,
          "Maria": {"stars": 4, "languages": ["Portuguese","English"], "tarifa": "40", 
                    "especializaçao":"velocidade", "tempo_max": "30", "horas_acomuladas": "13"}
          }

def getDriversByDate(year, month, day, hour):
    return scheduledDrivers.get(year, {}).get(month, {}).get(day, {}).get(hour, [])


def getMatchingDrivers(availableDrivers, stars, language, especializaçao, tempo_requesitado):
#funcao para unir condutor e o cliente

    for condutor_pedido in availableDrivers:
        driverStars = drivers[condutor_pedido]["stars"]
        driverEspecializaçao = drivers[condutor_pedido]["especializaçao"]
        driverLanguages = drivers[condutor_pedido]["languages"]
        driverTempo_max = drivers[condutor_pedido]["tempo_max"]
        if(driverSpeaksLanguage(driverLanguages, language) and driverStars == stars and driverEspecializaçao == especializaçao and driverTempo_max <= tempo_requesitado):
            return condutor_pedido

# Funcao auxiliar para verificar se o driver fala a linguagem necessaria  
def driverSpeaksLanguage( spokenLanguages, requiredLanguage):
    for l in spokenLanguages:
        for l1 in requiredLanguage:
            if( l == l1):
                return True
    return False
    
""" availableDrivers = getDriversByDate(2022, 1, 1, 12)
matchingDriver = getMatchingDrivers(availableDrivers, 4, ["English", "French"])
print(matchingDriver)
 """

def readSkippersFromFile ( skippersFileName ): 
    # Ler o ficheiro
    f = open(skippersFileName, "r")
    fileLineContents = f.readlines()
    skippers = {}

    # Iterar sobre cada linha do ficheiro
    for x in range(7, len(fileLineContents)):
        skipperRaw = fileLineContents[x].strip()

        # Verificar se a linha nao esta vazia
        if( skipperRaw != "" ):
            # Fazer split da linha
            caracteristicasSkipper = skipperRaw.split(", ")
            # Adicionar o skipper ao dicionario
            skippers[caracteristicasSkipper[0]]= {"stars": caracteristicasSkipper[2], "languages": caracteristicasSkipper[1], "tarifa": caracteristicasSkipper[3], "especializaçao": caracteristicasSkipper[4], "tempo_max": caracteristicasSkipper[5], "horas_acomuladas": caracteristicasSkipper[6]}
    f.close()
    return skippers


mySkipers = readSkippersFromFile ("./data/skippers.txt")
print (mySkipers)


#1
palavras = ["um",
"milenário",
"recusar",
"sinfonia",
"desperdiçador",
"obediente",
"rouca",
"texto",
"decolagem",
"tosa",
"arguto",
"garçonete",
"migalho",
"mateiro",
"voltímetro",
"gratinar",
"riscar",
"disparidade",
"orçado",
"calmamente",
"mecanizar",
"intertrigo",
"shakespeare",
"reportagem",
"prestigioso",
"reino",
"acendimento",
"vaga",
"dormi",
"brechó",
"descontínuo",
"insaciabilidade",
"máxima",
"extensão",
"preenchido",
"rendado",
"esperar",
"crioterapia",
"colador",
"administrativamente",
"tamanduá",
"estrelado",
"veranear",
"imundice",
"lastimoso",
"capilaridade",
"rodar",
"pupunha",
"embair",
"fecho",
"colonizador",
"cevada",
"mear",
"anta",
"humanístico",
"toda",
"assossegar",
"praticar",
"dia",
"unicidade",
"navegar",
"amarelado",
"modulante",
"quatro",
"percurso",
"fermento",
"comparador",
"alimentício",
"coágulo",
"babão",
"manifestação",
"telefonia",
"berrante",
"reembolso",
"descodificar",
"vela",
"visivelmente",
"calúnia",
"hipotecado",
"vagal",
"evocativo",
"merecedor",
"diet",
"afastar",
"conseguido",
"inspetor",
"começado",
"independentista",
"insubordinado",
"encarregado",
"bueiro",
"magro",
"solto",
"destro",
"usurpação",
"salvaguardado",
"nutricionista",
"caleidoscópio",
"repressor",
"orangotango",
"choroso",
"estigma",
"cambada",
"esvaziar",
"espirar",
"atraída",
"bauru",
"tentado",
"parcelar",
"aficionado",
"desmantelado",
"politicamente",
"natureza",
"assoreamento",
"justificativa",
"bolero",
"aduana",
"amortizar",
"ciberespaço",
"revivo",
"caridoso",
"carinhosamente",
"destra",
"passivo",
"arqueólogo",
"surra",
"abalar",
"espectador",
"demográfico",
"tonificar",
"superego",
"espumar",
"fogueira",
"autorretrato",
"algoz",
"irromper",
"secretar",
"mitologia",
"circunstância",
"lasso",
"transcursão",
"rasurar",
"furão",
"cumpriu",
"pirraça",
"bipolaridade",
"domiciliar",
"penar",
"pote",
"predicado",
"sobrestar",
"exonerar",
"neoliberal",
"gases",
"garante",
"pistache",
"baixela",
"foca",
"rossio",
"refrigerado",
"aviador",
"mimo",
"cairo",
"geriátrico",
"inflador",
"marionete",
"decodificador",
"misteriosa",
"colocador",
"entrevista",
"simétrico",
"centrado",
"errático",
"desvanecimento",
"coeso",
"violação",
"aparelhamento",
"retificar",
"consternação",
"escrutínio",
"instigação",
"forasteiro",
"declarado",
"decrescer",
"maléfico",
"alambique",
"tristonho",
"negatividade",
"trauma",
"filipina",
"sensibilidade",
"funéreo",
"abordar",
"alemanha",
"soído",
"desabafar",
"barrar",
"curinga",
"sonegar",
"sectário",]

def partition(array, low, high): #9n + 4

    pivot = array[high]
 
    i = low - 1
    for j in range(low, high):#n + (2 * n) * 4 = 9n
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1 
 
def quickSort(array, low, high): #6logN + 9n + 5
    if low < high:
        pi = partition(array, low, high) #9n + 4
        quickSort(array, low, pi - 1) #3logN
        quickSort(array, pi + 1, high) #3logN

size = len(palavras) #2
quickSort(palavras, 0, size - 1) #3log200
print(palavras) #1

# programa = 3log200 + 4
# O(NlogN)


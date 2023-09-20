from django.shortcuts import render

# Create your views here.
funkos = [
    {'name':'Sinestro','number':'470','collection':'DC Comics', 'description':'Gather your super hero team and prepare to battle the villain Pop! Sinestro™! Celebrate the Warner Bros 100th Anniversary by adding this Funko exclusive leader of the Yellow Lantern Corps™ to your DC Green Lantern™ collection. Vinyl figure is approximately 4.55-inches tall.','image':'https://funko.com/dw/image/v2/BGTS_PRD/on/demandware.static/-/Sites-funko-master-catalog/default/dw71aa0481/images/funko/69193-2.png?sw=800&sh=800'},
    {'name':'Genya Shinazugawa','number':'1406','collection':'Demon Slayer','description':' Only two of the Kamado family survived a demon attack, and now Tanjiro and Nezuko are out for revenge. Expand your Demon Slayer collection with this Pop! Genya Shinazugawa. Vinyl figure is approximately 4.45-inches tall.','image':'https://funko.com/dw/image/v2/BGTS_PRD/on/demandware.static/-/Sites-funko-master-catalog/default/dwbd52b45a/images/funko/upload/72609_DemonSlayer_S3_GenyaShinazugawa_POP_GLAM-1-WEB.png?sw=800&sh=800'},
    {'name':'Deathstroke with Bo Staff','number':'477','collection':'DC Comics','description':'Enhance the skill in your collection with Pop! Deathstroke™ with Staff! Celebrate the Warner Bros. 100th Anniversary by welcoming this exclusive, skilled assassin into your DC villains lineup. Vinyl figure is approximately 3.6-inches tall.','image':'https://funko.com/dw/image/v2/BGTS_PRD/on/demandware.static/-/Sites-funko-master-catalog/default/dwe7246809/images/funko/upload/71101_DC_Deathstroke-staff_POP_GLAM-1-FW-WEB.png?sw=800&sh=800'}
]

def about(request):
    return render(request, 'about.html')

def funkos_index(request):
    return render(request, 'funkos/index.html')
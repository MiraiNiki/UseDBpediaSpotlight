import requests

payload = {"text":"President Obama called Wednesday on Congress to extend a tax break for students included in last year's economic stimulus package, arguing that the policy provides more generous assistance.","confidence":0.35}
r = requests.get('http://model.dbpedia-spotlight.org/en/annotate',params=payload)
print(r.text)
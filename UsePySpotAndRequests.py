# -*- coding:utf-8 -*-

import requests
import re


payload = {"text":"President Obama called Wednesday on Congress to extend a tax break for students included in last year's economic stimulus package, arguing that the policy provides more generous assistance.","confidence":0.35}
r = requests.get('http://model.dbpedia-spotlight.org/en/annotate',params=payload)

webPage = r.text

pattern = re.compile("http://dbpedia.org/resource/[^\"]+|http://dbpedia.org/ontology/[^\"]+")
matchList = re.findall(pattern, webPage)


matchListUniq = []
for x in matchList:
	if x not in matchListUniq:
		matchListUniq.append(x)

print(matchListUniq)


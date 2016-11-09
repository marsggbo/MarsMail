import json


def GetJsonInfo(file):
	f = open(file,'r',encoding='utf-8')
	s = json.load(f)
	f.close()
	return s

def SaveJsonInfo(file,data):
	f = open(file,"w",encoding='utf-8')
	f.write(json.dumps(data))
	f.close()
from base64 import b64encode as enc64
import requests
from key_addpost import url, getBaseToken, headers

#encode image to binary format
def pict_to_binary(pict: str) -> str:
	with open(pict.replace('"', '') if '"' in pict else pict, 'rb') as f:
		binarypict = enc64(f.read())

	return binarypict

# Uppload new row in "Table_Name"
def newRow(imgbin, description):
	Value1 = str(description)
	Value2 = str(imgbin)
	payload = {
	    "row": {
	        "Description": Value1,
	        "imgbin": Value2
	    },
	    "table_name": "Table2"
	}
	response = requests.post(url, json=payload, headers=headers)

	return (response.text)

#_____________________________________________________
pict = input("Введите путь к файлу: ")
description = input("Введите описание для поста: ")

#____________________MAIN_________________________________
imgbin = pict_to_binary(pict)
newRow(imgbin, description)

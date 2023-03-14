include .env
export

chat:
	python chatgpt.py $(t:=)

talk:
	python text2speech.py

wsp:
	python whatsapp.py

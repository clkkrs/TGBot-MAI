import telebot
import requests
from PIL import Image
import base64
import io
from key import url, headers, TOKEN, id_channel

#decode (dec64)
def binary_to_pict(binarypict):
	image = base64.b64decode(binarypict)

	return image

#получить список ID строк из БД
def listIDRows():
    response = requests.get(url, headers=headers)
    listofID = []
    for i in range(len(response.json()["rows"])):
    	listofID.append(response.json()["rows"][i]["_id"])

    return listofID


# имея ID и номер ID  в списке возвращает imgbin и Description  в виде словаря
def getRowwithID(ID, i):
    response = requests.get(url, headers=headers)
    idrow_dict_imgbin_description = {"imgbin" : response.json()["rows"][i]["imgbin"],"Description" : response.json()["rows"][i]["Description"]}
    ans = idrow_dict_imgbin_description["imgbin"][2:-1]
    img = binary_to_pict(ans)
    # Создаем объект изображения с использованием PIL
    image = Image.open(io.BytesIO(img))
    # Сохраняем изображение
    image.save("img.jpg")

    return idrow_dict_imgbin_description["Description"]

# Функция для отправки сообщения в определенное время
def send_timed_message():
    listofID = listIDRows() #получение списка ID строк из БД
    id_current = 0 #индекс в списке ID текущей строки для отправки в канал
    ID = listofID[id_current] #ID текущей строки для отправки в канал
    file_ID = open('rowID.txt', 'r') #открыть файл с ID строки, отправленной последней в канал
    for line in file_ID:
        id_current = listofID.index(line) #происвоить переменной индекс ID отправленной строки из списка
    if id_current < len(listofID): #проверка на наличие новых строк в БД после отправленной строки в канал
        id_current = id_current + 1 #присвоить переменной индекс ID текущей строки из списка
        ID = listofID[id_current] #ID текущей строки для отправки в канал
        message_text = getRowwithID(ID, id_current) #изображение и описание для поста из текущей строки БД, готовые к отправке
        # Отправляем сообщение
        bot = telebot.TeleBot(TOKEN)
        file = open('img.jpg', 'rb')
        bot.send_photo(id_channel, file, message_text)

        file.close() #закрываем файл с изображением
        file_ID.close() #закрываем файл с ID строки
        file_ID = open('rowID.txt', 'w') #открывем файл с ID строки для записи
        file_ID.write(ID) #записываем ID только что отправленной строки
        file_ID.close() #закрываем файл с ID строки

def main():
    send_timed_message()

if __name__ == '__main__':
    main()

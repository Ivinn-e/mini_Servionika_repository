import Data_generation

import telebot;
from telebot.types import InputMediaPhoto




bot = telebot.TeleBot('7914222457:AAHMFPUSNDXE5JRxaMfc4LorD6kyj6nqXw8')


def create_example_message():
    """
    Эта функция формирует массив с примерами фотографий.

    Возвращает:
        массив с объектами фотографий.
    """

    list_of_paths_for_photos = [
        "./example_images/terminal.jpg",
        "./example_images/cheque.jpg",
        "./example_images/act_completed_works.jpg",
        "./example_images/acceptance_certificate.jpg"
    ]

    example_photos = []

    flag = True

    for img in list_of_paths_for_photos:

        example_of_the_request_text = "# REQ000001\n"\
                "# замена\n"\
                "# установлен PAX D270 (276000001), "\
                "демонтирован PAX D230 (23300001)"
                

        current_image_file = open(file=img, mode='rb')
        if flag:
            mediaPhoto = InputMediaPhoto(current_image_file, 
                                         caption=example_of_the_request_text)
            flag = False
        else:
            mediaPhoto = InputMediaPhoto(current_image_file, caption=None)

        example_photos.append(mediaPhoto)
    
    return example_photos


def saving_data_messages(message):
    """
    Эта функция сохраняет сhat_id пользователя, медиа группу и ее описание

    Параметры:
        message (str): сообщение отправленное пользователем

    Возвращает:
        media_group_id: идентификатор медиа группу, отправленной пользователем

        chat_id: идентификатор пользователя, который отправил сообщение

        media_group_caption: описание отправленной медиа группы

        directory_media_group: директория с файлами медиа группы 
    """

    media_group_id = int(message.media_group_id)

    chat_id = message.from_user.id

    media_group_caption = message.caption

    if media_group_caption is not None:
        pass

    file_id = message.photo[-1].file_id

    file_info = bot.get_file(file_id=file_id)

    downloaded_file = bot.download_file(file_info.file_path)

    file_name = f"{message.message_id}.jpg"

    with open(file_name, 'rb') as new_file:
        new_file.write(downloaded_file) 

    # Дописать метод добавления user_id, media_group_id, arrray_photos в бд
    
    
@bot.message_handler(commands=['start'])
def welcome_message(message):

    message_for_user = "Привет! Я бот, который помогает закрывать заявки."\
                        " Если ты пользуешься мной впервые, то жми "\
                        "/manual"
    bot.send_message(message.from_user.id, message_for_user)


@bot.message_handler(commands=['manual'])
def manual_message(message):

    manual_message = "Вот пример запроса, который я могу обработать"

    group_exemple_photos = create_example_message()                                  
    bot.send_message(message.from_user.id, manual_message)
    bot.send_media_group(message.from_user.id, media=group_exemple_photos)


@bot.message_handler(commands=['help'])
def help_message(message):

    message_with_the_creator_tag = "Если у вас возникли непредвиденные "\
                                    "проблемы при работе, то напишите "\
                                    "разработчику - @Ivinne. "\
                                    "Он будет рад помочь вам!"
    
    bot.send_message(message.from_user.id, text=message_with_the_creator_tag)


@bot.message_handler(content_types=['photo'])
def process_an_accepted_request(message):

    saving_data_messages(message)

    # После завершения скрипта возвращает True при успешно и ставит реакцию на сообщение пользователя
    
    

bot.polling(none_stop=True, interval=0)

# отформатировать по pep8, сделать красивые сообщения, продумать все ключи по которым будет выполняться закрытие
# сделать рефакторинг кода и посмотреть на названия переменных
# Для закрытия мы должны использовать фото, серийники (создать разные сценарии для вписания серийников) и тип заявки
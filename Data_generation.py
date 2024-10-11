def Generating_data_to_fill(text_message):
    """
    Эта функция формирует массив, где:

        первый элемент - номер заявки для поиска на сайте;

        второй элемент - тип заявки, для определения кода, по которому будет 
        закрыта заявка;

        третий элемент - текст описания заявки, содержащий информация о
        задействованном оборудовании.

    Параметры:
        text_message (str): текст запроса, получаемый от пользователя.

    Возвращает:
        list: массив, с элементами для дальнейшей работы.
    """

    data_list = text_message.split('#')

    for i in data_list:
        if len(i) == 0:
            data_list.remove(i)
    
    for i in range(0,3):
        if '\n' in data_list[i]:
            data_list[i] = data_list[i].replace('\n', '') 
            data_list[i] = data_list[i].replace(' ', '')  

    return data_list

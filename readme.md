# Приложение Image Detector

#### Запуск приложения:
- Устоновить Python 3.9 и активировать виртуальное окружение
- Установить все зависимости из файла requirements.txt командой 
    `pip install -r requirements.txt`
- Скачать файл с моделями по ссылке: 
[resnet50-11ad3fa6.pth](https://download.pytorch.org/models/resnet50-11ad3fa6.pth) 
- Разместить скаченный файл в каталоге: `/Users/USER_NAME/.cache/torch/hub/checkpoints/resnet50-11ad3fa6.pth`,
где USER_NAME - имя текущего пользователя системы    
- В режиме виртуально окружения (venv) из корневой папки приложения в терминале выполнить следующие команды:
    - Запустить сервер приложения
    `python main.py` 
    - Для остановки сервера используйте сочетание клавиш `CTRL+C`

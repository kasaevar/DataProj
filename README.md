# DataProj

Ссылка на датасет: https://drive.google.com/drive/folders/1ZYhS48bCy7Fh-JKuHWgiGgsOxFto8C_1?usp=sharing
Версия Ubuntu 22.04.LTS 64-bit
1. чтобы запустить терминал нужно зайти в настройки в раздел Регионы (только для новой VM), заходим в раздел login screen и в language меняем язык на любой английский(если проблемы с терминалом)
1. открыть терминал, добавить пользователя в папку sudoers, если его там нет, обновить пакеты командой sudo up update
1. далее sudo up install docker 
1. далее sudo up install docker-compose
1. далее sudo up install snapd
1. далее sudo snap install dbeaver-ce (его можно установить через App в ubuntu)
1. git clone https://github.com/kasaevar/DataProj 
1. cd ./DataProj/docker
1. скачать архив по ссылке и разархивировать в папку docker : https://drive.google.com/drive/folders/1ZYhS48bCy7Fh-JKuHWgiGgsOxFto8C_1?usp=sharing
1. sudo docker-compose up -d
1. открываем dbeaver 
1. подключаемся к postgreSQL со следующими параметрами host:localhost, username:admin, password:admin, database:dataproj, port:32, 
1. в базе данных dataproj в schemas создаем схемы stg, dds, dm
1. далее в терминале: sudo chmod 777 -R hdfs
1. cd ./hdfs/datanode
1. mkdir -m 777 ods
1. скачиваем через ubuntusoftware pycharm community
1. открываем файл main.py в pycharm
1. через PyPl устанавливаем пакеты psycopg2 и pandas
1. запускаем main.py

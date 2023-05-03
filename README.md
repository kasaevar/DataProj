# DataProj

Ссылка на датасет: https://drive.google.com/drive/folders/1ZYhS48bCy7Fh-JKuHWgiGgsOxFto8C_1?usp=sharing
Версия Ubuntu 22.04.LTS 64-bit
1. чтобы запустить терминал нужно зайти в настройки в раздел Регионы (только для новой VM), заходим в раздел login screen и в language меняем язык на любой английский(если проблемы с терминалом)
1. открыть терминал, добавить пользователя в папку sudoers, если его там нет, обновить пакеты командой sudo apt update
2. далее sudo apt install docker 
3. далее sudo apt install docker-compose
4. далее sudo apt install snapd
5. далее sudo snap install dbeaver-ce (его можно установить через App в ubuntu)
6. git clone https://github.com/kasaevar/DataProj 
7. cd ./DataProj/docker
8. скачать архив по ссылке и разархивировать в папку docker : https://drive.google.com/drive/folders/1ZYhS48bCy7Fh-JKuHWgiGgsOxFto8C_1?usp=sharing
9. sudo docker-compose up -d
10. открываем dbeaver 
11. подключаемся к postgreSQL со следующими параметрами host:localhost, username:admin, password:admin, database:dataproj, port:32, 
12. в базе данных dataproj в schemas создаем схемы stg, dds, dm
13. далее в терминале: sudo chmod 777 -R hdfs
14. cd ./hdfs/datanode
15. mkdir -m 777 ods
16. скачиваем через ubuntusoftware pycharm community
17. открываем файл main.py в pycharm
18. через PyPl устанавливаем пакеты psycopg2 и pandas
19. запускаем main.py

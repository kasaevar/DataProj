# DataProj

Ссылка на датасет: https://drive.google.com/drive/folders/1ZYhS48bCy7Fh-JKuHWgiGgsOxFto8C_1?usp=sharing
Версия Ubuntu 22.04.LTS 64-bit
1.установка docker, d-beaver, docker-compose, pycharm(опционально)
2. чтобы запустить терминал нужно зайти в настройки в раздел Регионы (только для новой VM), заходим в раздел login screen и в language меняем язык на любой английский(если проблемы с терминалом)
3. открыть терминал, добавить пользователя в папку sudoers, если его там нет, обновить пакеты командой sudo up update
4. далее sudo up install docker -e
5. далее sudo up install docker-compose
6. далее sudo up install snapd
7. далее sudo snap instal dbeaver-ce(его можно установить через App в ubuntu)
8. git clone https://github.com/kasaevar/DataProj
9. cd ./DataProj/docker
10. sudo docker-compose up -d
11. открываем dbeaver 
12. подключаемся к postgreSQL со следующими параметрами host:localhost, username:admin, password:admin, database:dataproj, port:32, 
13. в базе данных dataproj в schemas создаем схемы stg, dds, dm
14. далее в терминале sudo chmod 777 -R ./hdfs
15. cd ./hdfs/datanode
16. mkdir -m 777 ods
17. скачиваем через ubuntusoftware pycharm community
18. открываем файл main.py в pycharm
19. через PyPl устанавливаем пакеты psycopg2 и pandas
20. 

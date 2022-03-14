CREATE TABLE IF NOT EXISTS querys (
user_id INTEGER PRIMARY KEY, /*id сессии*/
channel_link TEXT NOT NULL, /*ссылка на телеграм канал*/
send_time INTEGER NOT NULL, /*время отправки запроса*/
for_time INTEGER NOT NULL /*на сколько подписать пользователя в часах / время, когда нужно отписаться*/
);
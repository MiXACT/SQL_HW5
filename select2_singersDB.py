import sqlalchemy as sq


if __name__ == '__main__':
    DB = 'postgresql://postgres:9117399126@localhost:5432/singers_db'
    engine = sq.create_engine(DB)
    connection = engine.connect()

    # 1 - количество исполнителей в каждом жанре
    result = connection.execute("""
            SELECT genre_title, COUNT(singer_id) FROM genres g
            JOIN genressingers gs ON g.id = gs.genre_id
            GROUP BY g.genre_title;
        """).fetchall()
    print('Количество исполнителей в каждом жанре: ', result)

    # 2 - количество треков, вошедших в альбомы 2019-2020 годов
    result = connection.execute("""
            SELECT album_title, COUNT(album_id) FROM albums a
            JOIN tracks t ON a.id = t.album_id
            WHERE release_year BETWEEN 2019 AND 2020
            GROUP BY album_title;
        """).fetchall()
    print('Количество треков, вошедших в альбомы 2019-2020 годов: ', result)

    # 3 - средняя продолжительность треков по каждому альбому
    result = connection.execute("""
            SELECT album_title, AVG(duration) FROM albums a
            JOIN tracks t ON a.id = t.album_id
            GROUP BY album_title;
        """).fetchall()
    print('Средняя продолжительность треков по каждому альбому: ', result)

    # 4 - все исполнители, которые не выпустили альбомы в 2020 году
    result = connection.execute("""
            SELECT singer_name FROM singers
            WHERE id IN (SELECT singer_id FROM singersalbums sa
                        JOIN albums a ON sa.album_id = a.id
                        WHERE release_year != 2020);
        """).fetchall()
    print('Исполнители, которые не выпустили альбомы в 2020 году: ', result)

    # 5 - названия сборников, в которых присутствует 2 PAC
    result = connection.execute("""
            SELECT col_title FROM collection
            WHERE id IN (SELECT col_id FROM trackscollection tc
                        JOIN tracks t ON t.id = tc.track_id
                        WHERE album_id IN (SELECT id FROM albums
                                            JOIN singersalbums sa ON sa.album_id = albums.id
                                            WHERE singer_id = (SELECT id FROM singers
                                                                WHERE singer_name = '2 PAC')));
        """).fetchall()
    print('Названия сборников, в которых присутствует 2 PAC: ', result)

    # 6 - названия альбомов, в которых присутствуют исполнители более 1 жанра
    result = connection.execute("""
            SELECT album_title FROM albums a
            JOIN singersalbums sa ON a.id = sa.album_id
            JOIN singers s ON sa.singer_id = s.id
            JOIN genressingers gs ON s.id = gs.singer_id
            JOIN genres g ON gs.genre_id = g.id
            GROUP BY album_title
            HAVING COUNT(genre_title) > 1;
        """).fetchall()
    print('Названия альбомов, в которых присутствуют исполнители более 1 жанра: ', result)

    # 7 - наименования треков, которые не входят в сборники
    result = connection.execute("""
            SELECT track_title FROM tracks t
            LEFT JOIN trackscollection tc ON t.id = tc.track_id
            WHERE tc.track_id IS NULL;
        """).fetchall()
    print('Наименования треков, которые не входят в сборники: ', result)

    # 8 - исполнитель(ли), написавший(ие) самый короткий по продолжительности трек
    result = connection.execute("""
            SELECT singer_name FROM singers
            WHERE id IN (SELECT singer_id FROM singersalbums
                        WHERE album_id IN (SELECT album_id FROM tracks
                                            WHERE duration = (SELECT MIN(duration) FROM tracks)));
        """).fetchall()
    print('Исполнитель(ли), написавший(ие) самый короткий по продолжительности трек: ', result)

    # 9 - названия альбомов, содержащих наименьшее количество треков
    result = connection.execute("""
            SELECT album_title FROM albums
            WHERE id = (SELECT album_id FROM tracks
                        GROUP BY album_id
                        ORDER BY COUNT(album_id) ASC
                        LIMIT 1);
        """).fetchall()
    print('Названия альбомов, содержащих наименьшее количество треков: ', result)
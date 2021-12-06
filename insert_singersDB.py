import sqlalchemy as sq


def del_db(tab):
    connection.execute(f"TRUNCATE {tab} CASCADE;")
    return

def genr_singers_filling(tab, data_to_fill_in):
    for i in range(len(data_to_fill_in)):
        connection.execute(f"INSERT INTO {tab} VALUES({i+1}, '{data_to_fill_in[i]}');")
    return

def alb_col_filling(tab, title, year):
    for i in range(len(title)):
        connection.execute(f"INSERT INTO {tab} VALUES({i+1}, '{title[i]}', '{year[i]}');")
    return

def tracks(title, duration_albID):
    for i in range(len(title)):
        connection.execute(f"""
            INSERT INTO tracks VALUES({i+1}, '{title[i]}', {duration_albID[i][0]}, {duration_albID[i][1]});
        """)
    return

def tabs_collab(tab, ids):
    i = 0
    for key in ids:
        connection.execute(f"""
            INSERT INTO {tab} VALUES({int(list(ids)[i])}, {int(ids[key])});
        """)
        i += 1
    return

if __name__ == '__main__':
    DB = 'postgresql://postgres:9117399126@localhost:5432/singers_db'
    engine = sq.create_engine(DB)
    connection = engine.connect()

    GENRE = ['Rap', 'Rock', 'Pop', 'Blues', 'Jazz', 'Ambient']

    SINGERS = ['2 PAC', 'Barry White', 'Sappheiros', 'Nirvana', 'Louis Armstrong', 'Drake',
               'The Rumjacks', 'Adriano Celentano', 'Brian Eno', 'Elvis Presley']

    ALBUMS = {'Chill out': 2018, 'Son': 2020, 'Take another shot': 1997, 'Drain you': 1988,
              'Call me': 1975, 'Tutti Frutti': 1963, 'Relaxing': 2020}

    TRACKS = {'Single Love': [2.5, 5], 'Yellow Jacket': [4, 1], 'After Dark': [5, 3], 'Insideout': [10.5, 4],
              'Top Side': [1.5, 6], 'High Way': [7, 7], 'Poison my sadness': [8, 2], 'True Hero': [7, 2],
              'Forgiveness': [4, 2], 'In 1990': [3, 3], 'Yourmyus': [9, 7], 'In God We Trust': [13, 3],
              'Venture': [5.5, 5], '1st': [4.5, 1], '40 oz': [3.5, 4]}

    COLLECTIONS = {'Best Songs': 2019, 'Top Music Collection': 2021, 'The Evidence': 2020, 'Peoples Choise': 2009,
                   'Radio Hits': 2002, 'TV Shows Covers': 2010, 'Movies OSTs': 2017, 'From XX to XXI': 2000}

    SING_GEN = {1: 1, 2: 4, 3: 6, 4: 2, 5: 5, 6: 1, 7: 2, 8: 3, 9: 6, 10: 3}
    SING_ALB = {1: 2, 2: 5, 3: 7, 4: 4, 5: 1, 6: 5, 7: 3, 8: 7, 9: 7, 10: 6}
    TRACK_COL = {1: 4, 2: 8, 3: 3, 4: 6, 6: 7, 7: 1, 8: 5, 9: 1, 10: 2, 11: 3, 12: 8, 13: 4, 14: 7}

    del_db('genres')
    del_db('singers')
    del_db('albums')
    del_db('tracks')
    del_db('collection')

    genr_singers_filling('genres', GENRE)
    genr_singers_filling('singers', SINGERS)
    alb_col_filling('albums', list(ALBUMS), list(ALBUMS.values()))
    alb_col_filling('collection', list(COLLECTIONS), list(COLLECTIONS.values()))
    tracks(list(TRACKS), list(TRACKS.values()))
    tabs_collab('genressingers', SING_GEN)
    tabs_collab('singersalbums', SING_ALB)
    tabs_collab('trackscollection', TRACK_COL)

    print('DONE!')
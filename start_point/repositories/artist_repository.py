from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results [0]['id']
    print(results)
    artist.id = id
    return artist

def delete_all():
    sql = 'DELETE FROM artists'
    run_sql(sql)

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"  
    values = [id] 
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result['name'], result['id'] )
    return artist





















# def select_all():
#     users = []
#     sql = "SELECT * from users"
#     results = run_sql(sql)
#     for row in results:
#         user = User(row['first_name'], row ['last_name'], row['id'])
#         users.append(user)
#     return users
# def select(id):
#     user = None
#     sql = 'SELECT * FROM users WHERE id = %s'
#     result = run_sql(sql, values)[0]
#     values = [id]
#     if result is not None:
#         user = User(result['first_name'], result['last_name'],result['id'])
#     return user

# def delete_all():
#     sql = 'DELETE from users'
#     run_sql(sql)

# def delete(id):
#     sql = "DELETE FROM users WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)

# def update(user):
#     sql = "UPDATE users SET (first_name, last_name) = (%s, %s) WHERE id = %s"
#     values = [user.first_name, user.last_name, user.id]
#     run_sql(sql, values)
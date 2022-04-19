from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results [0]['id']
    album.id = id 
    return album

def delete_all():
    sql = 'DELETE FROM albums'
    run_sql(sql)

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"  
    values = [id] 
    results = run_sql(sql, values)
    if results:
        result = results[0]
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], result['genre'], artist, result['id'] )
    return album


# def select_all():  
#     tasks = [] 

#     sql = "SELECT * FROM tasks"
#     results = run_sql(sql)

#     for row in results:
#         user = repositories.user_repository.select(row['user_id'])
#         task = Task(row['description'], user, row['duration'], row['completed'], row['id'] )
#         tasks.append(task)
#     return tasks 
    

# def select(id):
#     task = None
#     sql = "SELECT * FROM tasks WHERE id = %s"  
#     values = [id] 
#     result = run_sql(sql, values)[0]
    
#     if result is not None:
#         user = repositories.user_repository.select(result['user_id'])
#         task = Task(result['description'], result['user'], result['duration'], result['completed'], result['id'] )
#     return task


# def delete_all():
#     sql = "DELETE  FROM tasks" 
#     run_sql(sql)

# def delete(id):
#     sql = "DELETE  FROM tasks WHERE id = %s" 
#     values = [id]
#     run_sql(sql, values)


# def update(task):
#     sql = "UPDATE tasks SET (description, user_id, duration, completed) = (%s, %s, %s, %s) WHERE id = %s"
#     values = [task.description, task.user.id, task.duration, task.completed, task.id]
#     run_sql(sql, values) 

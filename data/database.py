import os
import sqlite3

db_filename = 'test.db'
schema_filename = 'schema.sql'
data_filename = 'basic_data.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print('Inserting initial data')
        with open(data_filename, 'rt') as f:
            scriptData = f.read()
        conn.executescript(scriptData)

    else:
        print('Database exists, assume schema does, too.')

    cursor = conn.cursor()

    cursor.execute("""
        select name, description, deadline from project where name = 'pymotw'
        """)
    name, description, deadline = cursor.fetchone()

    print('Project details for %s (%s) due %s' % (description, name, deadline))

    cursor.execute("""
        select id, priority, status, deadline, details from task
        where project = 'pymotw' order by deadline
        """)

    print('\nNext 5 tasks:')

    for row in cursor.fetchmany(5):
        for key in row:
            print(key)


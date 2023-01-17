Command type for this lesson : Fast API

Virtual Environment
-> python3 -m venv venv

View > Command Palette
--> Python Select Interpreter
--> ./venv/bin/python

Terminal Virtual Environment
-> source venv/bin/activate


First code 
from fastapi import FastAPI
app = FastAPI()

// path operations
@app.get("/") // decorator - a little magic of function
async def root(): // function
    return {"message": "Hello World"} // convert to JSON

Run the live server
-> uvicorn main:app --reload
INFO:     Uvicorn running on http://127.0.0.1:8000

Uvicorn is an ASGI web server implementation for Python.
Until recently Python has lacked a minimal low-level server/application interface for async frameworks. The ASGI specification fills this gap, and means we're now able to start building a common set of tooling usable across all async frameworks.
Uvicorn currently supports HTTP/1.1 and WebSockets

http://127.0.0.1:8000/docs
You will see the automatic interactive API documentation (provided by Swagger UI):

Source : https://developer.mozilla.org/en-US/docs/Web/HTTP

Post Method

@app.post("/createposts")
def create_posts():
    # print(payload)
    return {"message": "successfully created posts"}

JSON file to post
{
    "title" : "demo",
    "content" : "I'm performing a demo"
}

Result
{
    "message": "successfully created posts"
}

// Postregsql

POSTGRESQL - COMMANDS

psql -h localhost -d fastapi -U postgres -p 5432

show all tables : \dt or \dt+

CREATE TABLE posts (
	id serial PRIMARY KEY,
	title VARCHAR ( 50 ) NOT NULL,
	content VARCHAR ( 50 ) NOT NULL,
	published BOOLEAN UNIQUE NOT NULL,
	created_at TIMESTAMP NOT NULL 
);

#published default true
#created_at timestamp with timezone and now()

ALTER TABLE posts ALTER COLUMN created_at SET DEFAULT now();

ALTER TABLE posts ALTER COLUMN published SET DEFAULT true;

# show table posts
select * FROM posts;

# query
SELECT * FROM posts WHERE published = true;

// psycopg : Python Postregsql
//pip install psycopg2 -> error on mac 
fixed with : pip3 install psycopg2-binary


//////////////////////
POSTGRESQL : Foreign Keys

delete from posts;

Example from postgresqltutorial.com

The following statements create the customers and contacts tables:

DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS contacts;

CREATE TABLE customers(
   customer_id INT GENERATED ALWAYS AS IDENTITY,
   customer_name VARCHAR(255) NOT NULL,
   PRIMARY KEY(customer_id)
);

CREATE TABLE contacts(
   contact_id INT GENERATED ALWAYS AS IDENTITY,
   customer_id INT,
   contact_name VARCHAR(255) NOT NULL,
   phone VARCHAR(15),
   email VARCHAR(100),
   PRIMARY KEY(contact_id),
   CONSTRAINT fk_customer
      FOREIGN KEY(customer_id) 
	  REFERENCES customers(customer_id)
);

// ON DELETE, ON UPDATE Example

Simply add on delete cascade to an existing foreign key constraint. You have to drop the constraint first, then add the correct version. In standard SQL, I believe the easiest way to do this is to

* start a transaction,
* drop the foreign key,
* add a foreign key with on delete cascade, and finally
* commit the transaction
* Repeat for each foreign key you want to change.

But PostgreSQL has a non-standard extension that lets you use multiple constraint clauses in a single SQL statement. For example

alter table public.scores
drop constraint scores_gid_fkey,
add constraint scores_gid_fkey
   foreign key (gid)
   references games(gid)
   on delete cascade;
If you don't know the name of the foreign key constraint you want to drop, you can either look it up in pgAdminIII (just click the table name and look at the DDL, or expand the hierarchy until you see "Constraints"), or you can query the information schema.

select *
from information_schema.key_column_usage
where position_in_unique_constraint is not null

// For the project

ALTER TABLE posts
ADD COLUMN user_id INT NOT NULL,
ADD CONSTRAINT posts_users_fkey FOREIGN KEY(user_id) REFERENCES users(id);

// Update column user_id with On DELETE CASCADE
ALTER TABLE posts
DROP CONSTRAINT posts_users_fkey,
ADD CONSTRAINT posts_users_fkey FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE;

// view all information regarding table
\d tablename

Environment Variables on Mac
List all :  printenv
Create one : export MY_DB_URL="localhost:5432"
List one: echo $MY_DB_URL

# +Request Join for Vote
SELECT posts.*, COUNT(votes.post_id) AS votes FROM posts LEFT JOIN votes ON posts.id = votes.post_id GROUP BY posts.id;

Information on a table
\d table;

How to Drop a Table That has Dependent Objects in PostgreSQL?

Use the CASCADE option with the DROP TABLE command to remove a table along with its dependent objects. The syntax of the DROP TABLE command with the CASCADE option will be as follows:

DROP TABLE tab_name CASCADE;

ALEMBIC : Install and init 
Source Doc : https://alembic.sqlalchemy.org/en/latest/

Installation :
	Cmd : pip install alembic
	Access to alembic command: alembic –help
	Initialize alembic inside directory: alembic init alembic

Folder outside app folder


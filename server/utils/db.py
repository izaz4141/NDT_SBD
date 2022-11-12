import mysql.connector as connetion
from dotenv import dotenv_values

config = dotenv_values('.env')

def open_db_connection():
    db_host = config["DB_HOST"]
    db_name = config["DB_NAME"]
    db_user = config["DB_USER"]
    db_password = config["DB_PW"]

    db = connetion.connect(
        host=db_host,
        database = db_name,
        user=db_user,
        password=db_password,
    )

    return db
cxn = open_db_connection()
cur = cxn.cursor()

def with_commit(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        commit()

    return inner

def commit():
    # print("Saving database...")
    cxn.commit()

def close():
    cxn.close()

def field(command, *values):
    cur.execute(command, tuple(values))
    fetch = cur.fetchone()
    if fetch is not None:
        return fetch[0]

def record(command, *values):
    """
    db.record("SELECT Statistics FROM guilds WHERE GuildID = ?", ctx.guild.id)[0]
    """
    cur.execute(command, tuple(values))
    return cur.fetchone()

def records(command, *values):
    cur.execute(command, tuple(values))
    return cur.fetchall()

def column(command, *values):
    """
    db.column("SELECT GuildID FROM guilds")
    """
    cur.execute(command, tuple(values))
    return [item[0] for item in cur.fetchall()]

def execute(command, *values):
    """
    db.execute("UPDATE guilds set GuildName = ? WHERE GuildID = ?", guild.name, guild.id)
    """
    cur.execute(command, tuple(values))

def multiexec(command,valueset):
    """
    db.multiexec("INSERT OR IGNORE INTO guilds (GuildID,GuildName) VALUES (?,?)", ((guild.id, guild.name,) for guild in self.guilds))
    """
    cur.executemany(command, valueset)

def scriptexec(path):
    with open(path, "r", encoding="utf-8") as script:
        cur.executescript(script.read())
        
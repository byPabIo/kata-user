import os
from dotenv import load_dotenv
from peewee import PostgresqlDatabase

load_dotenv()

for var in ["DB_NAME", "DB_USER", "DB_PASSWORD", "DB_HOST", "DB_PORT"]:
    if not os.getenv(var):
        raise ValueError(f"Error: La variable de entorno {var} no está definida en el archivo .env")

db = PostgresqlDatabase(
    os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT"))
)


def initialize_database():
    try:
        db.connect()
        print("✅ Conexión a la base de datos exitosa!")

        from infrastructure.db.models.user_model import UserModel

        db.create_tables([UserModel])
        print("✅ Tablas verificadas/creadas correctamente!")

    except Exception as e:
        print(f" Error al conectar o crear tablas en la base de datos!", e)

    finally:
        db.close()
if __name__ == "__main__":
    initialize_database()
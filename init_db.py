from src.infrastructure.db.database import db


def initialize_db():
    db.connect()

    # Importamos UserModel aquí para evitar importaciones circulares
    from src.infrastructure.db.models.user_model import UserModel

    db.create_tables([UserModel])
    print("✅ Tablas creadas correctamente!")
    db.close()


if __name__ == "__main__":
    initialize_db()
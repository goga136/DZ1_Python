from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Загрузка переменных окружения (опционально)
load_dotenv()

# Получение данных подключения из переменных окружения или использование значений по умолчанию
DB_USER = os.getenv("DB_USER", "QA")
DB_PASSWORD = os.getenv("DB_PASSWORD", "136")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "mydatabase")

# Создание строки подключения
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine("postgresql://QA:136@localhost:5432/mydatabase")

# Создание движка SQLAlchemy
engine = create_engine(DB_URL)

# Создание фабрики сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()

# Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close
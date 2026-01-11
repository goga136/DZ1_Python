# conftest.py в папке Lesson_9
import pytest
import sys
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# Отключаем все попытки подключения к PostgreSQL
print("⚠️  ИСПОЛЬЗУЕМ SQLite ДЛЯ ТЕСТОВ")


@pytest.fixture(scope='session')
def engine():
    """Фикстура для SQLite в памяти - БЕЗ PostgreSQL!"""
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
        echo=True  # Видим SQL запросы
    )

    # Проверяем что подключение работает
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        print("✓ SQLite engine создан успешно")
    except Exception as e:
        print(f"✗ Ошибка создания engine: {e}")
        raise

    return engine


@pytest.fixture(scope='function')
def db_session(engine):
    """Фикстура для сессии БД."""
    print("✓ Создаем db_session...")

    # Импортируем Base внутри - если он есть
    try:
        # Пробуем разные варианты импорта
        from app.models import Base
    except ImportError:
        try:
            from models import Base
        except ImportError:
            try:
                from database import Base
            except ImportError:
                # Если Base не найден, создаем пустой
                from sqlalchemy.ext.declarative import declarative_base
                Base = declarative_base()
                print("⚠️  Используем временный Base")

    # Создаем таблицы
    Base.metadata.create_all(bind=engine)
    print("✓ Таблицы созданы")

    # Создаем сессию
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    # Очистка
    session.rollback()
    session.close()
    print("✓ Сессия закрыта")


@pytest.fixture(autouse=True)
def cleanup():
    """Автоматическая очистка между тестами."""
    print("\n--- Начало теста ---")
    yield
    print("--- Конец теста ---")
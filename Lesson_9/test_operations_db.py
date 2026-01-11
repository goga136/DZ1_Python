import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


# Фикстуры
@pytest.fixture(scope='function')
def db_session():
    """Фикстура для сессии БД с SQLite."""
    engine = create_engine('sqlite:///:memory:')

    # Создаем таблицу
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE subjects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT
            )
        """))
        conn.commit()

    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.close()


class TestCRUDOperations:

    def test_create_subject(self, db_session):
        """Тест создания записи с использованием SQL."""
        # Act
        db_session.execute(
            text("INSERT INTO subjects (name, description) VALUES (:name, :desc)"),
            {"name": "Test Subject 001", "desc": "Test description"}
        )
        db_session.commit()

        # Assert
        result = db_session.execute(
            text("SELECT name, description FROM subjects WHERE name = :name"),
            {"name": "Test Subject 001"}
        ).fetchone()

        assert result is not None
        assert result[0] == "Test Subject 001"
        assert result[1] == "Test description"

    def test_update_subject(self, db_session):
        """Тест обновления записи."""
        # Arrange
        db_session.execute(
            text("INSERT INTO subjects (name, description) VALUES ('Old Name', 'Old Desc')")
        )
        db_session.commit()

        # Act
        db_session.execute(
            text("UPDATE subjects SET name = 'New Name' WHERE name = 'Old Name'")
        )
        db_session.commit()

        # Assert
        result = db_session.execute(
            text("SELECT name FROM subjects WHERE name = 'New Name'")
        ).fetchone()

        assert result is not None
        assert result[0] == "New Name"

    def test_delete_subject(self, db_session):
        """Тест удаления записи."""
        # Arrange
        db_session.execute(
            text("INSERT INTO subjects (name, description) VALUES ('To Delete', 'Desc')")
        )
        db_session.commit()

        # Проверяем что запись создана
        result = db_session.execute(
            text("SELECT COUNT(*) FROM subjects WHERE name = 'To Delete'")
        ).fetchone()
        assert result[0] == 1

        # Act
        db_session.execute(
            text("DELETE FROM subjects WHERE name = 'To Delete'")
        )
        db_session.commit()

        # Assert
        result = db_session.execute(
            text("SELECT COUNT(*) FROM subjects WHERE name = 'To Delete'")
        ).fetchone()
        assert result[0] == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])

"""
Shared pytest fixtures for FastAPI tests.
Configures test client and test data.
"""
import pytest
from copy import deepcopy
from fastapi.testclient import TestClient
from src.app import app, activities



@pytest.fixture
def client():
    """
    Arrange: Proporciona un cliente de prueba para hacer solicitudes a la API.
    """
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """
    Arrange: Resetea el estado de las actividades antes de cada prueba.
    Asegura que las pruebas no interfieran entre sí.
    """
    # Estado original preservado
    original_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Competitive basketball training and tournaments",
            "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": ["james@mergington.edu"]
        },
        "Tennis Club": {
            "description": "Tennis lessons and friendly matches",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:00 PM",
            "max_participants": 10,
            "participants": ["lucy@mergington.edu", "alex@mergington.edu"]
        },
        "Drama Club": {
            "description": "Theater performances and acting workshops",
            "schedule": "Fridays, 4:00 PM - 6:00 PM",
            "max_participants": 25,
            "participants": ["ryan@mergington.edu"]
        },
        "Art Lab": {
            "description": "Painting, drawing, and sculpture classes",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["mia@mergington.edu", "noah@mergington.edu"]
        },
        "Debate Team": {
            "description": "Competitive debate and public speaking skills",
            "schedule": "Mondays, 3:30 PM - 5:00 PM",
            "max_participants": 16,
            "participants": ["sophie@mergington.edu"]
        },
        "Science Club": {
            "description": "Explore experiments and scientific research projects",
            "schedule": "Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 20,
            "participants": ["lucas@mergington.edu", "ava@mergington.edu"]
        }
    }
    
    # Limpiar y resetear
    activities.clear()
    activities.update(deepcopy(original_activities))
    
    yield
    
    # Limpiar después de la prueba
    activities.clear()
    activities.update(deepcopy(original_activities))

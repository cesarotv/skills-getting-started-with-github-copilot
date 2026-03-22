"""
Tests para endpoints GET de actividades.
Patrón AAA: Arrange - Act - Assert
"""


class TestGetActivities:
    """Pruebas del endpoint GET /activities"""
    
    def test_get_activities_returns_200(self, client):
        """
        Arrange: Cliente de prueba preparado
        Act: GET /activities
        Assert: Devuelve status 200
        """
        # Act
        response = client.get("/activities")
        
        # Assert
        assert response.status_code == 200
    
    def test_get_activities_returns_dict(self, client):
        """
        Arrange: Cliente de prueba preparado
        Act: GET /activities
        Assert: Devuelve un diccionario con actividades
        """
        # Act
        response = client.get("/activities")
        data = response.json()
        
        # Assert
        assert isinstance(data, dict)
        assert len(data) > 0
        assert "Chess Club" in data
        assert "participants" in data["Chess Club"]
        assert "max_participants" in data["Chess Club"]
    
    def test_get_activities_contains_all_fields(self, client):
        """
        Arrange: Cliente de prueba preparado
        Act: GET /activities
        Assert: Cada actividad contiene los campos requeridos
        """
        # Act
        response = client.get("/activities")
        activities = response.json()
        
        # Assert
        required_fields = {"description", "schedule", "max_participants", "participants"}
        for activity_name, activity_data in activities.items():
            assert required_fields.issubset(activity_data.keys()), \
                f"Activity {activity_name} missing required fields"


class TestRootRedirect:
    """Pruebas del endpoint GET /"""
    
    def test_root_redirect_returns_307(self, client):
        """
        Arrange: Cliente de prueba preparado
        Act: GET /
        Assert: Redirige con status 307
        """
        # Act
        response = client.get("/", follow_redirects=False)
        
        # Assert
        assert response.status_code == 307
    
    def test_root_redirect_location_correct(self, client):
        """
        Arrange: Cliente de prueba preparado
        Act: GET /
        Assert: Redirige al archivo index.html correcto
        """
        # Act
        response = client.get("/", follow_redirects=False)
        
        # Assert
        assert "/static/index.html" in response.headers.get("location", "")

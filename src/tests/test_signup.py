"""
Tests para endpoint POST /activities/{activity_name}/signup
Patrón AAA: Arrange - Act - Assert
"""


class TestSignup:
    """Pruebas del endpoint POST de registro"""
    
    def test_signup_success(self, client):
        """
        Arrange: Preparamos datos de un nuevo alumno
        Act: POST /activities/Chess Club/signup con email nuevo
        Assert: Status 200 y mensaje de éxito
        """
        # Arrange
        activity_name = "Chess Club"
        new_email = "new.student@mergington.edu"
        
        # Act
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": new_email}
        )
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert new_email in data["message"]
    
    def test_signup_duplicate_email_returns_400(self, client):
        """
        Arrange: Email que ya está inscrito en la actividad
        Act: Intentamos registrarnos con el mismo email
        Assert: Status 400 y mensaje de error
        """
        # Arrange
        activity_name = "Chess Club"
        existing_email = "michael@mergington.edu"  # Ya existe en Chess Club
        
        # Act
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": existing_email}
        )
        
        # Assert
        assert response.status_code == 400
        data = response.json()
        assert "detail" in data
        assert "already signed up" in data["detail"].lower()
    
    def test_signup_activity_not_found_returns_404(self, client):
        """
        Arrange: Nombre de actividad que no existe
        Act: Intentamos registrarnos en actividad inexistente
        Assert: Status 404 y mensaje de error
        """
        # Arrange
        activity_name = "Non-Existent Club"
        email = "student@mergington.edu"
        
        # Act
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        
        # Assert
        assert response.status_code == 404
        data = response.json()
        assert "detail" in data
        assert "not found" in data["detail"].lower()
    
    def test_signup_updates_participant_list(self, client):
        """
        Arrange: Cliente y un email nuevo
        Act: Registramos al alumno y luego consultamos actividades
        Assert: El email aparece en la lista de participantes
        """
        # Arrange
        activity_name = "Programming Class"
        new_email = "newprogrammer@mergington.edu"
        
        # Act
        signup_response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": new_email}
        )
        activities_response = client.get("/activities")
        
        # Assert
        assert signup_response.status_code == 200
        data = activities_response.json()
        assert new_email in data[activity_name]["participants"]

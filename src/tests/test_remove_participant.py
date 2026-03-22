"""
Tests para endpoint DELETE /activities/{activity_name}/participant/{email}
Patrón AAA: Arrange - Act - Assert
"""


class TestRemoveParticipant:
    """Pruebas del endpoint DELETE de remover participantes"""
    
    def test_remove_participant_success(self, client):
        """
        Arrange: Participante que existe en la actividad
        Act: DELETE para remover participante
        Assert: Status 200 y mensaje de éxito
        """
        # Arrange
        activity_name = "Chess Club"
        email = "michael@mergington.edu"  # Existe en Chess Club
        
        # Act
        response = client.delete(
            f"/activities/{activity_name}/participant/{email}"
        )
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert email in data["message"]
    
    def test_remove_participant_not_found_returns_404(self, client):
        """
        Arrange: Email que NO está inscrito en la actividad
        Act: Intentamos remover participante inexistente
        Assert: Status 404 y mensaje de error
        """
        # Arrange
        activity_name = "Chess Club"
        email = "nonexistent@mergington.edu"  # No existe
        
        # Act
        response = client.delete(
            f"/activities/{activity_name}/participant/{email}"
        )
        
        # Assert
        assert response.status_code == 404
        data = response.json()
        assert "detail" in data
        assert "not found" in data["detail"].lower()
    
    def test_remove_participant_activity_not_found_returns_404(self, client):
        """
        Arrange: Actividad inexistente
        Act: Intentamos remover de actividad que no existe
        Assert: Status 404 y mensaje de error
        """
        # Arrange
        activity_name = "Non-Existent Activity"
        email = "student@mergington.edu"
        
        # Act
        response = client.delete(
            f"/activities/{activity_name}/participant/{email}"
        )
        
        # Assert
        assert response.status_code == 404
        data = response.json()
        assert "detail" in data
    
    def test_remove_participant_updates_list(self, client):
        """
        Arrange: Participante en actividad y lo removemos
        Act: DELETE y luego GET para verificar
        Assert: El email ya no aparece en la lista
        """
        # Arrange
        activity_name = "Tennis Club"
        email = "lucy@mergington.edu"
        
        # Act
        remove_response = client.delete(
            f"/activities/{activity_name}/participant/{email}"
        )
        activities_response = client.get("/activities")
        
        # Assert
        assert remove_response.status_code == 200
        data = activities_response.json()
        assert email not in data[activity_name]["participants"]

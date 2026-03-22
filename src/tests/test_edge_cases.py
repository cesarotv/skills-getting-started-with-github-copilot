"""
Tests para casos límite y validaciones especiales.
Patrón AAA: Arrange - Act - Assert
"""


class TestEdgeCases:
    """Pruebas de casos límite y situaciones especiales"""
    
    def test_signup_with_special_characters_in_email(self, client):
        """
        Arrange: Email con caracteres especiales válidos
        Act: POST /activities/.../signup
        Assert: Se registra exitosamente (si el email es válido)
        """
        # Arrange
        activity_name = "Art Lab"
        email = "user+tag@mergington.edu"  # Email válido con +
        
        # Act
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        
        # Assert
        assert response.status_code == 200
    
    def test_activity_with_special_characters_in_name(self, client):
        """
        Arrange: Nombre de actividad con espacios (URL encoded)
        Act: POST con nombre URL-encoded
        Assert: Funciona correctamente
        """
        # Arrange
        activity_name = "Art Lab"  # Contiene espacio
        email = "artist@mergington.edu"
        
        # Act
        response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        
        # Assert
        assert response.status_code == 200
    
    def test_remove_and_readd_participant(self, client):
        """
        Arrange: Participante en actividad
        Act: Remover y luego volver a registrar
        Assert: El participante se vuelve a agregar correctamente
        """
        # Arrange
        activity_name = "Drama Club"
        email = "new.actor@mergington.edu"
        
        # Act: Registrar
        register_response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        
        # Act: Remover
        remove_response = client.delete(
            f"/activities/{activity_name}/participant/{email}"
        )
        
        # Act: Registrar de nuevo
        reregister_response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email}
        )
        
        # Assert
        assert register_response.status_code == 200
        assert remove_response.status_code == 200
        assert reregister_response.status_code == 200
    
    def test_multiple_signups_same_activity_different_emails(self, client):
        """
        Arrange: Múltiples estudiantes nuevos
        Act: Registramos a todos en la misma actividad
        Assert: Todos se registran exitosamente
        """
        # Arrange
        activity_name = "Science Club"
        emails = [
            "student1@mergington.edu",
            "student2@mergington.edu",
            "student3@mergington.edu"
        ]
        
        # Act & Assert
        for email in emails:
            response = client.post(
                f"/activities/{activity_name}/signup",
                params={"email": email}
            )
            assert response.status_code == 200
        
        # Verificar que todos fueron agregados
        activities_response = client.get("/activities")
        participants = activities_response.json()[activity_name]["participants"]
        for email in emails:
            assert email in participants

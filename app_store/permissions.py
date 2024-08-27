from rest_framework.permissions import BasePermission, SAFE_METHODS

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Permitir leitura para todos, inclusive não autenticados
        if request.method in SAFE_METHODS:
            return True

        # Exigir que o usuário esteja autenticado para métodos que modificam dados
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Permitir leitura para todos, inclusive não autenticados
        if request.method in SAFE_METHODS:
            return True

        # Permitir modificação apenas para superusuários
        return request.user.is_superuser
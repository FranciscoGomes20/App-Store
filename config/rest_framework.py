REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
}

# Novas configurações para autenticação e permissões
DEFAULT_AUTHENTICATION_CLASSES = [
    'rest_framework.authentication.BasicAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    # 'rest_framework.authentication.TokenAuthentication',  # para autenticação por token
]

DEFAULT_PERMISSION_CLASSES = [
    'rest_framework.permissions.IsAuthenticated',
]
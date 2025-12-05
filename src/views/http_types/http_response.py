from typing import Dict


class HttpResponse:
    """Representa a resposta HTTP para o usuário"""

    def __init__(self, status_code: int, body: Dict = None) -> None:
        self.status_code = status_code
        self.body = body

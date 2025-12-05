# pylint: disable=unused-import
# Este arquivo está reservado para implementação futura
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetsCreatorController:
    """Controller para criação de pets (a implementar)"""

    def __init__(self, pets_repository: PetsRepositoryInterface):
        self._pets_repository = pets_repository

    def create(self, pet_info: dict) -> dict:
        """Método placeholder para criação de pets"""
        raise NotImplementedError("Método create ainda não implementado")

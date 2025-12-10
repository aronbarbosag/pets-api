from pydantic import BaseModel, ValidationError, constr

from src.errors.error_types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)
from src.views.http_types.http_request import HttpRequest


def person_creator_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        first_name: constr(min_length=1)
        last_name: constr(min_length=1)
        age: int = None
        pet_id: int

    try:
        BodyData(**http_request.body)

    except ValidationError as e:
        # Formatar erros do Pydantic em uma mensagem legível
        errors = e.errors()
        error_messages = [f"{err['loc'][0]}: {err['msg']}" for err in errors]
        raise HttpUnprocessableEntityError("; ".join(error_messages)) from e

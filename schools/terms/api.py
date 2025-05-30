from django.db import transaction

from ninja import Router
from ninja.errors import HttpError
from ninja.security import django_auth

from .models import Term, TermFee
from .schemas import TermSchemaIn, TermWithFeesSchemaOut


terms_router = Router(auth=django_auth)


@terms_router.post("", response=TermWithFeesSchemaOut, url_name="add_term")
def create_term_with_fees(request, payload: TermSchemaIn):
    term_data = payload.dict(exclude={"term_fees"})
    term = Term.objects.create(**term_data)

    for fee_data in payload.term_fees:
        TermFee.objects.create(term=term, **fee_data.dict())

    return term


from django.db import transaction

from ninja import Router
from ninja.errors import HttpError
from ninja.security import django_auth

from academics.classes.models import Class

from .models import Term, TermFee
from .schemas import TermSchemaIn, TermWithFeesSchemaOut


terms_router = Router(auth=django_auth)


@terms_router.post("", response=TermWithFeesSchemaOut, url_name="term-create")
def create_term_with_fees(request, payload: TermSchemaIn):
    print("Creating term with payload:")
    print(payload)
    term_data = payload.dict(exclude={"term_fees"})

    with transaction.atomic():
        classes = Class.objects.all()
        term = Term.objects.create(**term_data)

        for fee_data in payload.term_fees:
            termFee = TermFee.objects.create(
                term=term,
                amount=fee_data.amount
            )
            fee_classes = [cls for cls in classes if cls.id in fee_data.classes]

            termFee.classes.set(fee_classes)
            termFee.save()

    return term


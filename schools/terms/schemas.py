from ninja import ModelSchema, Schema
from ninja.orm import create_schema

from academics.classes.schemas import ClassSchema

from .models import Term, TermFee

class TermFeeSchemaIn(Schema):
    amount: int
    classes: list[int]

class TermSchemaIn(Schema):
    number: int
    start_date: str
    end_date: str
    term_fees: list[TermFeeSchemaIn] = []

TermSchemaOut = create_schema(Term, name="TermSchemaOut", fields=["id", "number", "start_date", "end_date"])

class TermFeeSchemaOut(Schema):
    id: int
    amount: int
    classes: list[ClassSchema] = []


class TermWithFeesSchemaOut(Schema):
    id: int
    number: int
    start_date: str
    end_date: str
    term_fees: list[TermFeeSchemaOut] = []

    @staticmethod
    def resolve_term_fees(obj):
        return [TermFeeSchemaOut(**fee) for fee in obj.term_fees.all()]
    
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.term_fees = [TermFeeSchemaOut(**fee) for fee in self.term_fees.all()]
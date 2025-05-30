from ninja import ModelSchema, Schema
from ninja.orm import create_schema

from .models import Term, TermFee

class TermFeeSchemaIn(Schema):
    classes: list[int]
    amount: int

class TermSchemaIn(Schema):
    number: int
    start_date: str
    end_date: str
    term_fees: list[TermFeeSchemaIn] = []

TermSchemaOut = create_schema(Term, fields=["id", "number", "start_date", "end_date"])

# TermWithFeesSchemaOut = create_schema(Term, fields=["id", "number", "start_date", "end_date"], custom_fields=[("term_fees", list[TermFeeSchemaIn], None)])

class TermWithFeesSchemaOut(ModelSchema):
    class Config:
        model = Term
        model_fields = "__all__"
    
    term_fees: list[TermFeeSchemaIn] = []
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.term_fees = [TermFeeSchemaIn(**fee) for fee in self.term_fees.all()]
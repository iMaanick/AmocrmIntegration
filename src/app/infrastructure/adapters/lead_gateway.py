from typing import NewType

from amocrm.v2 import Contact, Lead
from amocrm.v2.entity import custom_field

from app.application.common.ports.lead_dto import LeadCreate
from app.application.common.ports.lead_gateway import LeadGateway


class MyContact(Contact):
    email = custom_field.ContactEmailField("Email раб.")


PipelineID = NewType("PipelineId", int)
StatusId = NewType("StatusId", int)


class AMOLeadGateway(LeadGateway):
    def __init__(self, pipeline_id: PipelineID, status_id: StatusId) -> None:
        self.pipeline_id = pipeline_id
        self.status_id = status_id

    def create(self, lead: LeadCreate) -> int:
        new_lead = Lead()
        new_lead.name = f"Сделка из строки {lead.row}"
        new_lead.price = lead.amount
        new_lead.pipeline = self.pipeline_id
        new_lead.status = self.status_id
        new_lead.create()

        new_lead.notes(text=lead.comment).save()
        contact = MyContact(
            email=lead.email
        )
        contact.save()
        new_lead.contacts.add(contact)
        return new_lead.id

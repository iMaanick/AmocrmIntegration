from typing import NewType

from amocrm.v2 import Contact, Lead, fields
from amocrm.v2.entity import custom_field

from app.application.common.ports.lead_dto import LeadCreate, LeadUpdate, LeadFieldsData
from app.application.common.ports.lead_gateway import LeadGateway


class MyContact(Contact):
    email = custom_field.ContactEmailField("Email раб.")


class MyLead(Lead):
    contacts = fields._EmbeddedLinkListField("contacts", model="MyContact")


PipelineID = NewType("PipelineId", int)
StatusId = NewType("StatusId", int)


class AMOLeadGateway(LeadGateway):
    def __init__(self, pipeline_id: PipelineID, status_id: StatusId) -> None:
        self.pipeline_id = pipeline_id
        self.status_id = status_id

    def create(self, lead: LeadCreate) -> int:
        new_lead = MyLead()
        new_lead.name = f"Сделка из строки {lead.row}"
        new_lead.price = lead.amount
        new_lead.pipeline = self.pipeline_id
        new_lead.status = self.status_id
        new_lead.create()

        contact = MyContact(
            email=lead.email
        )
        contact.save()
        new_lead.contacts.add(contact)
        return new_lead.id

    def update(self, lead_id: int, data: LeadUpdate) -> None:
        lead: MyLead = MyLead.objects.get(lead_id)
        c: MyContact = list(lead.contacts)[-1]
        c.email = data.email
        c.save()
        lead.price = data.amount
        lead.save()

    def get(self, lead_id: int) -> LeadFieldsData:
        lead: MyLead = MyLead.objects.get(lead_id)
        return LeadFieldsData(
            email=list(lead.contacts)[-1].email,
            amount=lead.price,
        )


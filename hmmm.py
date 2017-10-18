# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AccessibilityForDisabilities(models.Model):
    id = models.CharField(primary_key=True, max_length=38)
    location_id = models.CharField(max_length=38, blank=True, null=True)
    accessibility = models.CharField(max_length=50, blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accessibility_for_disabilities'


class Apps(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=1500)
    user_id = models.CharField(max_length=100)
    app_key = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'apps'


class Categories(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    depth = models.CharField(max_length=100, blank=True, null=True)
    taxonomy_id = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    parent_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Contact(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    organization_id = models.CharField(max_length=100, blank=True, null=True)
    service_id = models.CharField(max_length=100, blank=True, null=True)
    service_at_location_id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    department = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=750, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Eligibility(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    service_id = models.CharField(max_length=50, blank=True, null=True)
    eligibility = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eligibility'


class Fee(models.Model):
    id = models.CharField(primary_key=True, max_length=38)
    service_id = models.CharField(max_length=38, blank=True, null=True)
    fee = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fee'


class Funding(models.Model):
    id = models.CharField(primary_key=True, max_length=38)
    organization_id = models.CharField(max_length=38, blank=True, null=True)
    service_id = models.CharField(max_length=38, blank=True, null=True)
    source = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funding'


class HolidaySchedule(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    service_id = models.CharField(max_length=100, blank=True, null=True)
    location_id = models.CharField(max_length=100, blank=True, null=True)
    service_at_location_id = models.CharField(max_length=100, blank=True, null=True)
    closed = models.CharField(max_length=50, blank=True, null=True)
    opens_at = models.CharField(max_length=75, blank=True, null=True)
    closes_at = models.CharField(max_length=75, blank=True, null=True)
    start_date = models.CharField(max_length=75, blank=True, null=True)
    end_date = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'holiday_schedule'


class InterpretationServices(models.Model):
    id = models.CharField(primary_key=True, max_length=38)
    service_id = models.CharField(max_length=38, blank=True, null=True)
    language = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interpretation_services'


class Language(models.Model):
    id = models.CharField(primary_key=True, max_length=38)
    service_id = models.CharField(max_length=38, blank=True, null=True)
    location_id = models.CharField(max_length=38, blank=True, null=True)
    language = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'language'


class Location(models.Model):
    id = models.CharField(primary_key=True, max_length=38)
    organization_id = models.CharField(max_length=38, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    alternate_name = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    transportation = models.CharField(max_length=500, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class MetaTableDescription(models.Model):
    id = models.CharField(primary_key=True, max_length=38)
    name = models.CharField(max_length=1000, blank=True, null=True)
    language = models.CharField(max_length=1000, blank=True, null=True)
    character_set = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_table_description'


class Metadata(models.Model):
    id = models.CharField(primary_key=True, max_length=38)
    resource_id = models.CharField(max_length=38, blank=True, null=True)
    last_action_date = models.DateTimeField(blank=True, null=True)
    last_action_type = models.CharField(max_length=150, blank=True, null=True)
    field_name = models.CharField(max_length=750, blank=True, null=True)
    previous_value = models.CharField(max_length=750, blank=True, null=True)
    replacement_value = models.CharField(max_length=750, blank=True, null=True)
    updated_by = models.CharField(max_length=750, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metadata'


class Organization(models.Model):
    id = models.CharField(primary_key=True, max_length=38)
    name = models.CharField(max_length=500, blank=True, null=True)
    alternate_name = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)
    tax_status = models.CharField(max_length=100, blank=True, null=True)
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    year_incorporated = models.CharField(max_length=50, blank=True, null=True)
    legal_status = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organization'


class PaymentAccepted(models.Model):
    id = models.CharField(primary_key=True, max_length=38)
    service_id = models.CharField(max_length=38, blank=True, null=True)
    payment = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_accepted'


class Phone(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    location_id = models.CharField(max_length=100, blank=True, null=True)
    service_id = models.CharField(max_length=100, blank=True, null=True)
    organization_id = models.CharField(max_length=100, blank=True, null=True)
    contact_id = models.CharField(max_length=100, blank=True, null=True)
    service_at_location_id = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=50, blank=True, null=True)
    extension = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=250, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone'


class PhysicalAddress(models.Model):
    id = models.CharField(primary_key=True, max_length=38)
    location_id = models.CharField(max_length=38, blank=True, null=True)
    attention = models.CharField(max_length=500, blank=True, null=True)
    address_1 = models.CharField(max_length=250, blank=True, null=True)
    address_2 = models.CharField(max_length=250, blank=True, null=True)
    address_3 = models.CharField(max_length=250, blank=True, null=True)
    address_4 = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    region = models.CharField(max_length=250, blank=True, null=True)
    state_province = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physical_address'


class PostalAddress(models.Model):
    id = models.CharField(primary_key=True, max_length=38)
    location_id = models.CharField(max_length=38, blank=True, null=True)
    attention = models.CharField(max_length=500, blank=True, null=True)
    address_1 = models.CharField(max_length=250, blank=True, null=True)
    address_2 = models.CharField(max_length=250, blank=True, null=True)
    address_3 = models.CharField(max_length=250, blank=True, null=True)
    address_4 = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    region = models.CharField(max_length=250, blank=True, null=True)
    state_province = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=50)
    country = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'postal_address'


class Program(models.Model):
    id = models.CharField(primary_key=True, max_length=38)
    organization_id = models.CharField(max_length=38, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    alternate_name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'program'


class RegularSchedule(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    service_id = models.CharField(max_length=100, blank=True, null=True)
    location_id = models.CharField(max_length=100, blank=True, null=True)
    service_at_location_id = models.CharField(max_length=100, blank=True, null=True)
    weekday = models.CharField(max_length=75, blank=True, null=True)
    opens_at = models.CharField(max_length=75, blank=True, null=True)
    closes_at = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regular_schedule'


class RequiredDocument(models.Model):
    id = models.CharField(primary_key=True, max_length=38)
    service_id = models.CharField(max_length=38, blank=True, null=True)
    document = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'required_document'


class Service(models.Model):
    id = models.CharField(primary_key=True, max_length=38)
    organization_id = models.CharField(max_length=38, blank=True, null=True)
    program_id = models.CharField(max_length=38, blank=True, null=True)
    location_id = models.CharField(max_length=38, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    alternate_name = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    interpretation_services = models.CharField(max_length=1500, blank=True, null=True)
    application_process = models.CharField(max_length=1000, blank=True, null=True)
    wait_time = models.CharField(max_length=100, blank=True, null=True)
    fees = models.CharField(max_length=250, blank=True, null=True)
    accreditations = models.CharField(max_length=250, blank=True, null=True)
    licenses = models.CharField(max_length=250, blank=True, null=True)
    taxonomy_ids = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service'


class ServiceArea(models.Model):
    id = models.CharField(primary_key=True, max_length=38)
    service_id = models.CharField(max_length=38, blank=True, null=True)
    service_area = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_area'


class ServiceAtLocation(models.Model):
    id = models.CharField(primary_key=True, max_length=38)
    service_id = models.CharField(max_length=38, blank=True, null=True)
    location_id = models.CharField(max_length=38, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_at_location'


class ServiceTaxonomy(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    service_id = models.CharField(max_length=100, blank=True, null=True)
    taxonomy_id = models.CharField(max_length=100, blank=True, null=True)
    taxonomy_detail = models.CharField(max_length=1500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_taxonomy'


class Taxonomy(models.Model):
    id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    parent_id = models.CharField(max_length=100, blank=True, null=True)
    parent_name = models.CharField(max_length=100, blank=True, null=True)
    vocabulary = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taxonomy'


class Users(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=500)
    github_id = models.CharField(max_length=45)
    github_login = models.CharField(max_length=45)
    user_key = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users'

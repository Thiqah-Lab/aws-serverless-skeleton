from datetime import datetime
import os
import uuid

from pynamodb.attributes import (UnicodeAttribute, UTCDateTimeAttribute, ListAttribute, JSONAttribute)
from pynamodb.models import Model


class DestinationModel(Model):
    """
    A DynamoDB destination table
    """

    id = UnicodeAttribute(hash_key=True)
    user_sub = UnicodeAttribute()
    title = UnicodeAttribute()
    status = UnicodeAttribute()
    createdAt = UTCDateTimeAttribute(null=False, default=datetime.utcnow)
    updatedAt = UTCDateTimeAttribute(null=False, default=datetime.utcnow)
    images = ListAttribute()
    tags = ListAttribute()
    category = UnicodeAttribute()
    opening_times = ListAttribute()
    general_description = UnicodeAttribute()
    types_of_activities = UnicodeAttribute()
    estimated_price = UnicodeAttribute()
    website = UnicodeAttribute()
    email = UnicodeAttribute()
    phone = UnicodeAttribute()
    location = JSONAttribute()

    class Meta:
        table_name = os.environ.get("DYNAMODB_DESTINATION_TABLE")
        region = os.environ.get("REGION")
        if os.environ.get('DYNAMODB_HOST') is not None:
            host = os.environ.get("DYNAMODB_HOST")

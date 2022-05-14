from rest_framework.schemas.openapi import AutoSchema

class EntitySchema(AutoSchema):
    """Extension of ``AutoSchema`` to add support for custom field schemas."""

    def map_field(self, field):
        if field.field_name == "campaigns":
            return {
                "type": "array",
                "items": { "type" : "string" },
            }
        elif field.field_name == "region":
            return {
                "type": "array",
                "items": { "type" : "string" },
            }
        elif field.field_name == "latest_pose":
            return {
                "type": "object",
            }
        # Handle SerializerMethodFields or custom fields here...
        # ...
        return super().map_field(field)


class CampaignSchema(AutoSchema):
    """Extension of ``AutoSchema`` to add support for custom field schemas."""

    def map_field(self, field):
        if field.field_name == "entities":
            return {
                "type": "array",
                "items": { "type" : "object" },
            }
        elif field.field_name == "scenarios":
            return {
                "type": "array",
                "items": { "type" : "object" },
            }

        # Handle SerializerMethodFields or custom fields here...
        # ...
        return super().map_field(field)


class TrialSchema(AutoSchema):
    """Extension of ``AutoSchema`` to add support for custom field schemas."""

    def map_field(self, field):
        if field.field_name == "performers":
            return {
                "type": "array",
                "items": { "type" : "string" },
            }
        elif field.field_name == "script_run_counts":
            return {
                "type": "array",
                "items": { "type" : "object" },
            }

        # Handle SerializerMethodFields or custom fields here...
        # ...
        return super().map_field(field)


class TestMethodSchema(AutoSchema):
    """Extension of ``AutoSchema`` to add support for custom field schemas."""

    def map_field(self, field):
        if field.field_name == "trials":
            return {
                "type": "array",
                "items": { "type" : "object" },
            }
        elif field.field_name == "campaigns":
            return {
                "type": "array",
                "items": { "type" : "string" },
            }

        # Handle SerializerMethodFields or custom fields here...
        # ...
        return super().map_field(field)


class EventSchema(AutoSchema):
    """Extension of ``AutoSchema`` to add support for custom field schemas."""

    def map_field(self, field):
        if field.field_name == "point_style":
            return {
                "type": "object",
            }
        elif field.field_name == "related_entities":
            return {
                "type": "object",
            }
        elif field.field_name == "unfound_entities":
            return {
                "type": "array",
                "items": { "type" : "string" },
            }
        elif field.field_name == "invalid_entities":
            return {
                "type": "array",
                "items": { "type" : "string" },
            }

        # Handle SerializerMethodFields or custom fields here...
        # ...
        return super().map_field(field)
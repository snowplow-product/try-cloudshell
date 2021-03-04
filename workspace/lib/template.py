def generate_config(context):
    deployment = context.env["deployment"]
    resources = [
        {
            "name": f"{deployment}-db-instance",
            "type": "sqladmin.v1beta4.instance",
            "properties": {
                "settings": {"tier": "db-f1-micro"},
                "databaseVersion": "POSTGRES_12",
            },
        },
        {
            "name": "db",
            "type": "sqladmin.v1beta4.database",
            "properties": {
                "instance": f"$(ref.{deployment}-db-instance.name)",
                "name": "snowplow",
            },
        },
        {
            "name": "db-user",
            "type": "sqladmin.v1beta4.user",
            "properties": {
                "instance": f"$(ref.{deployment}-db-instance.name)",
                "name": context.properties["database-user"],
                "password": context.properties["database-password"],
            },
        },
    ]
    return {"resources": resources}

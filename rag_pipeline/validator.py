def validate(json_obj):
    missing = []
    if not json_obj.get("territory"):
        missing.append("territory")
    if not json_obj.get("royalty"):
        missing.append("royalty")
    return missing

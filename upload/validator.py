from django.core.exceptions import ValidationError
from pathlib import Path

def validate_me(value):
    extension=Path(value.name).suffix[1:].lower()
    filesize= value.size    
    
    if extension not in ['mp4','mkv']:
        raise ValidationError("Only mp4 and mkv files are allowed")
    elif (filesize/1000) > 1000000:
        raise ValidationError("The maximum file size that can be uploaded is 1GB")
    else:
        return value
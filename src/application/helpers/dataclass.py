from datetime import datetime
from enum import Enum
from uuid import UUID


class EventType(Enum):
    CREATE = 'create'
    UPDATE = 'update'
    DELETE = 'delete'

def serialize_dataclass(obj):
    """Рекурсивная сериализация dataclass с поддержкой всех типов"""
    if isinstance(obj, Enum):
        return obj.value  # или str(obj) если нужно 'EventType.CREATE'
    
    elif isinstance(obj, datetime):
        return obj.isoformat()  # или str(obj)
    
    elif isinstance(obj, UUID):
        return str(obj)
    
    elif hasattr(obj, '__dataclass_fields__'):
        result = {}
        for field_name in obj.__dataclass_fields__:
            value = getattr(obj, field_name)
            result[field_name] = serialize_dataclass(value)
        return result
    
    elif isinstance(obj, list):
        return [serialize_dataclass(item) for item in obj]
    
    elif isinstance(obj, dict):
        return {key: serialize_dataclass(val) for key, val in obj.items()}
    
    elif isinstance(obj, tuple):
        return tuple(serialize_dataclass(item) for item in obj)
    
    else:
        return obj
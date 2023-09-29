from travelingAuths.core.services.account_services import get_account_id 
from django.contrib.auth.models import Group

rols = ['User', 'Administrator', 'Company']
def created_role(role: str, user_id: int): 
    try: 
        if role not in rols:
            return None
        group = Group.objects.get(name=role)
        get_account_id(user_id).groups.add(group)
        return 'role created'
    except Exception as e:
        print(e)
        return None
from subscriptions.serializers import SubscriptionModelSerializer
from travelingAuths.core.services.user_rol_services import created_role 
def created_subscription(user_id: int, number_projects: int = 3):
    try: 
        payload = {
            "user": user_id,
            "subscription": "FREE",
            "number_projects": number_projects
        }
        serializer = SubscriptionModelSerializer(data=payload)  
        if serializer.is_valid():
            serializer.save()
            created_role('User', user_id)
        return serializer.data
    except Exception as e:
        print(e)
        return None
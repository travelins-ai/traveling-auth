
from interests.models import AccountInterests


def get_interest_from_user(user_id):
        '''
        Helper method to get the object with given userid
        '''
        try:
            return AccountInterests.objects.filter(user=user_id)
        except AccountInterests.DoesNotExist:
            return None
from accounts.models import UserAccount


def get_account_id(id):
    '''
    Helper method to get the object with given id
    '''
    try:
        return UserAccount.objects.get(id=id)
    except UserAccount.DoesNotExist:
        return None
'''
This is a custom permission class that checks if the user is an admin or not.
It checks if a user has read / write permissions.
'''

from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    '''
    Custom permission to only allow admin to edit and delete
    '''
    def has_permission(self, request, view, obj=None):
        '''
        Read permissions are allowed to any request,
        so we'll always allow GET, HEAD or OPTIONS requests.
        '''
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the admin
        return obj.user == request.user
    
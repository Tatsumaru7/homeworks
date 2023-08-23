from rest_framework.permissions import IsAuthenticated

class IsAdvertisementOwnerPermission(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if obj.creator == request.user:
            return True
        return False

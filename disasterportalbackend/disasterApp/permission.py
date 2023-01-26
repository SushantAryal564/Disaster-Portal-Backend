from rest_framework import permissions

class DisasterEventPermission(permissions.BasePermission):
    def has_permission(self, request, view):
      if(request.method == "GET"):
        return True
      else:
        if request.user.is_authenticated:
          return True;
    def has_object_permission(self, request, view, obj):
      if(request.user.is_superuser):
        return True
      elif (request.user.is_Municipality):
        return True
      elif (request.user.ward == obj.disaster.Ward):
        return True

class OnlyGet(permissions.BasePermission):
  def has_permission(self,request, view):
    if(request.method == "GET"):
      return True
    else:
      return False
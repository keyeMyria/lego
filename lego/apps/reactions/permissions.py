from lego.apps.permissions.models import ObjectPermissionsModel
from lego.apps.permissions.permissions import AbakusPermission
from lego.utils.content_types import VALIDATION_EXCEPTIONS, string_to_instance


class ReactionPermission(AbakusPermission):
    check_object_permission = True

    def has_object_permission(self, request, view, reaction):
        if super().has_object_permission(request, view, reaction):
            return True

        return reaction.created_by == request.user

    def has_permission(self, request, view):

        has_permission = super(ReactionPermission, self).has_permission(request, view)

        if has_permission:
            return True

        if view.action == 'create':
            return self.check_target_permissions(request)

        return False

    def check_target_permissions(self, request):
        target = None
        try:
            if request.data.get('target') is not None:
                target = string_to_instance(request.data.get('target'))
        except VALIDATION_EXCEPTIONS:
            pass

        if target:
            if isinstance(target, ObjectPermissionsModel) \
                    and not target.can_view(request.user):
                return False

        return True
from omniport.middleware.person_roles import get_role
from kernel.mixins.period_mixin import ActiveStatus


def get_rights_for_semester(user, semester_no):
    """
    Check if the given user has enough privileges based on semester number
    :param user: the user whose privileges are being tested
    :param semester_no: the minimum semester number in which rights are given
    :return: True if the user has privileges, False otherwise
    """

    student = get_role(
        person=user.person,
        role_name='Student',
        active_status=ActiveStatus.IS_ACTIVE,
        silent=True
    )

    maintainer = get_role(
        person=user.person,
        role_name='Maintainer',
        active_status=ActiveStatus.IS_ACTIVE,
        silent=True
    )

    if maintainer is not None:
        return student.current_semester > semester_no
    return False


def has_omnipotence_rights(user):
    """
    Check if the given user has enough privileges to access the admin interface
    :param user: the user whose privileges are being tested
    :return: True if the user has privileges, False otherwise
    """

    return get_rights_for_semester(semester_no=5, user=user)


def has_alohomora_rights(user):
    """
    Check if the given user has enough privileges to impersonate another user
    :param user: the user whose privileges are being tested
    :return: True if the user has privileges, False otherwise
    """
    return get_rights_for_semester(semester_no=5, user=user)


def has_lockpicking_rights(user):
    """
    Check if the given user has enough privileges to reset anyone's password
    :param user: the user whose privileges are being tested
    :return: True if the user has privileges, False otherwise
    """

    return get_rights_for_semester(semester_no=4, user=user)


def has_helpcentre_rights(user):
    """
    Check if the given user has enough privileges to access helpcentre
    :param user: the user whose privileges are being tested
    :return: True if the user has privileges, False otherwise
    """

    return get_rights_for_semester(semester_no=4, user=user)

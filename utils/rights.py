from formula_one.enums.active_status import ActiveStatus
from kernel.managers.get_role import get_role


def get_rights_for_semester(user, semester_no, right_if_not_student=False):
    """
    Check if the given user has enough privileges based on semester number for student maintainers
    And if the user is a maintainer but not a student than it gives privileges according to the
    requirements based on the value of param:right_if_not_student   
    :param user: the user whose privileges are being tested
    :param semester_no: the minimum semester number in which rights are given
    :param right_if_not_student: whether to give access to a maintainer user who is not a student
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
        if student is not None:
            return student.current_semester > semester_no
        return right_if_not_student
    return False


def has_omnipotence_rights(user):
    """
    Check if the given user has enough privileges to access the admin interface
    :param user: the user whose privileges are being tested
    :return: True if the user has privileges, False otherwise
    """

    return get_rights_for_semester(semester_no=5, user=user)


def has_polyjuice_rights(user):
    """
    Check if the given user has enough privileges to impersonate another user
    :param user: the user whose privileges are being tested
    :return: True if the user has privileges, False otherwise
    """
    return get_rights_for_semester(semester_no=5, user=user)


def has_alohomora_rights(user):
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

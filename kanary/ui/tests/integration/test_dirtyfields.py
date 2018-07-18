import pytest

from ui.account.models import Account


@pytest.mark.django_db(transaction=True)
def test_dirtyfields(user_db):
    account = Account.objects.first()
    assert account.country is None
    account.country = "USA"
    assert account.has_changed('country') is True
    assert account.has_changed('country', since_read=True) is True
    account.save()

    assert account.has_changed('country') is False, "After save standard access gets resetted"
    assert account.has_changed('country', since_read=True) is True, "Save is not read! Should still show is changed!"

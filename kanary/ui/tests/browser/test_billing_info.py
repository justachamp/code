from ui.account.models import Invoice, Payment

from ui.utils import append_dollar


def fetch_transaction_rows(client):
    '''
    :returns: data for each transaction row displayed of following structure:
    (Date, Number, Event, Status, Amount)
    :rtype: list of tuples
    '''
    transactions_info = []
    rows = client.find_elements_by_class_name('-t-transaction-row')

    for row in rows:
        transactions_info.append(
            (row.find_element_by_class_name('-t-date').text,
             row.find_element_by_class_name('-t-number').text,
             row.find_element_by_class_name('-t-event').text,
             row.find_element_by_class_name('-t-status').text,
             row.find_element_by_class_name('-t-amount').text)
        )

    return transactions_info


def test_billing_and_transactions(client, billing_db):
    '''
    Checks if data displayed on Billing & Transaction page
    are consistent with stored in database.
    '''
    client.menu_jump_to('account')
    client.click_on_class('billing-page')

    account = billing_db.models['account']['acc']
    acc_balance = append_dollar(account.account_balance())
    last_payment = append_dollar(account.last_payment)

    # Check dollar-formatted fields
    assert client.find_element_by_class_name('-t-balance').text == acc_balance
    assert client.find_element_by_class_name('-t-payment').text == last_payment

    # Fetch invoices and payments rows
    rows = fetch_transaction_rows(client)

    # one row for payment and one for invoice
    assert len(rows) == 2

    # fetch payment and invoice data from db
    invoice_dict = Invoice.objects.first().to_json()
    payment_dict = Payment.objects.first().to_json()

    invoice_tuple = (
        invoice_dict['date'],
        invoice_dict['number'],
        invoice_dict['event'],
        '-',
        invoice_dict['amount']
    )

    payment_tuple = (
        payment_dict['date'],
        '-',
        payment_dict['event'],
        '-',
        payment_dict['amount'],
    )

    assert invoice_tuple in rows
    assert payment_tuple in rows


def test_paypal_checkout(client):
    # 1. click "Deposit funds" button on topbar
    client.find_element_by_class_name('-t-deposit-funds').click()

    # 2. on "Billing & Transactions" page click "Deposit with PayPal" button
    client.wait_until_displayed('-t-deposit-with-paypal')
    client.find_element_by_class_name('-t-deposit-with-paypal').click()

    # 3. check if we are redirected to PayPal service
    #    (mockup page of PayPal service is used here)
    assert 'Pay with a PayPal account' in client.title
    client.find_element_by_tag_name('a').click()  # return link to our service

    # 4. check return page from PayPal service
    processing_info = client.find_element_by_css_selector('#content h2')
    processing_info.location_once_scrolled_into_view
    assert processing_info.text == 'Processing payment'

    # 5. click "Continue" button
    client.find_element_by_css_selector('#content a').click()
    client.wait_for_xhr()
    timeline_block = client.find_element_by_class_name('-t-timeline')
    assert timeline_block.find_element_by_css_selector('#content h2').text == 'Timeline'

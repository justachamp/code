SAVE_BUTTON = 'button-save-changes'


def go_to_step(client, name, existing=False):
    '''
    Opens given section in strategy creator.
    :param str name         Step name used in sidebar class
    :param Boolean existing If false, will open steo in new strategy creator,
                            otherwise exisitng strategy will be chosen
    '''
    step_class = 'sidebar-%s' % name
    client.menu_jump_to('campaigns')
    client.click_on_class('campaign')

    if existing:
        client.click_on_class('strategy')
        client.click_on_class('edit-strategy')
        client.click_on_class(step_class)
        return

    client.click_on_button('new')
    client.click_on_class(step_class)


def save(client):
    '''
        Presses 'save changes' button
    '''
    # Save changes
    client.click_on_class(SAVE_BUTTON)


def save_with_errors(client):
    '''
    Tries to save invalid campaign.
    Returns errors listed in modal.
    '''
    client.click_on_class(SAVE_BUTTON)
    client.wait_for_modal()
    return client.get_modal_errors()


def save_and_return_to_step(client):
    '''
    Stores active step, saves strategy and returns to stored step.
    '''
    # Store current step name
    strategy_step_class = '-t-sidebar-steps'
    current_step_selector = '.%s li.current' % strategy_step_class
    step_name = client.find_element_by_css_selector(current_step_selector).text

    # Save changes
    client.click_on_class(SAVE_BUTTON)

    # Return to stored step in editing mode
    client.click_on_class('edit-strategy')

    all_steps_selector = '.%s li' % strategy_step_class
    all_steps = client.find_elements_by_css_selector(all_steps_selector)
    by_text = lambda gr: gr.find_element_by_css_selector('a').text == step_name
    matched_steps = filter(by_text, all_steps)
    client.click(matched_steps[0])

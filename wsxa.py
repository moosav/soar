"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'test_2_2' block
    test_2_2(container=container)

    return

@phantom.playbook_block()
def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_1() called")

    template = """Testing HTTP endpoint:"""

    # parameter list for template variable replacement
    parameters = [
        "test_2_2:custom_function_result.data.target_url"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    add_note_1(container=container)

    return


@phantom.playbook_block()
def add_note_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_note_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    test_2_2__result = phantom.collect2(container=container, datapath=["test_2_2:custom_function_result.data.target_url"])

    parameters = []

    # build parameters list for 'add_note_1' call
    for test_2_2__result_item in test_2_2__result:
        parameters.append({
            "title": "title6",
            "content": test_2_2__result_item[0],
            "container_id": test_2_2__result_item[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("add note", parameters=parameters, name="add_note_1", assets=["test-2"], callback=filter_1)

    return


@phantom.playbook_block()
def filter_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("filter_1() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["status_code == 200", "==", ""]
        ],
        conditions_dps=[
            ["status_code == 200", "==", ""]
        ],
        name="filter_1:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        pass

    return


@phantom.playbook_block()
def test_2_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("test_2_2() called")

    url_value = container.get("url", None)

    parameters = []

    parameters.append({
        "url": url_value,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="ipm/test_2", parameters=parameters, name="test_2_2", callback=format_1)

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # This function is called after all actions are completed.
    # summary of all the action and/or all details of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    ################################################################################
    ## Custom Code End
    ################################################################################

    return
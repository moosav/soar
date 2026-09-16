"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'ipm_2_1' block
    ipm_2_1(container=container)

    return

@phantom.playbook_block()
def add_note_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_note_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    id_value = container.get("id", None)
    ipm_2_1__result = phantom.collect2(container=container, datapath=["ipm_2_1:custom_function_result.data.json_output"])

    parameters = []

    # build parameters list for 'add_note_1' call
    for ipm_2_1__result_item in ipm_2_1__result:
        parameters.append({
            "title": "title3",
            "content": ipm_2_1__result_item[0],
            "container_id": id_value,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("add note", parameters=parameters, name="add_note_1", assets=["test-2"])

    return


@phantom.playbook_block()
def ipm_2_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("ipm_2_1() called")

    severity_value = container.get("severity", None)

    parameters = []

    parameters.append({
        "input_event": severity_value,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="ipm/IPM_2", parameters=parameters, name="ipm_2_1", callback=decision_1)

    return


@phantom.playbook_block()
def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("decision_1() called")

    severity_value = container.get("severity", None)

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["ipm_2_1:custom_function_result.data.json_output", "==", severity_value]
        ],
        conditions_dps=[
            ["ipm_2_1:custom_function_result.data.json_output", "==", "container:severity"]
        ],
        name="decision_1:condition_1",
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        add_note_1(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'elif' condition 2
    found_match_2 = phantom.decision(
        container=container,
        conditions=[
            ["ipm_2_1:custom_function_result.data.json_output", "==", severity_value]
        ],
        conditions_dps=[
            ["ipm_2_1:custom_function_result.data.json_output", "==", "container:severity"]
        ],
        name="decision_1:condition_2",
        delimiter=None)

    # call connected blocks if condition 2 matched
    if found_match_2:
        add_note_2(action=action, success=success, container=container, results=results, handle=handle)
        return

    return


@phantom.playbook_block()
def add_note_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_note_2() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    id_value = container.get("id", None)
    ipm_2_1__result = phantom.collect2(container=container, datapath=["ipm_2_1:custom_function_result.data.json_output"])

    parameters = []

    # build parameters list for 'add_note_2' call
    for ipm_2_1__result_item in ipm_2_1__result:
        parameters.append({
            "title": "title4",
            "container_id": id_value,
            "content": ipm_2_1__result_item[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("add note", parameters=parameters, name="add_note_2", assets=["test-2"])

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
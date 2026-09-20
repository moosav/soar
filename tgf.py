"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'geberator_2_2' block
    geberator_2_2(container=container)

    return

@phantom.playbook_block()
def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["geberator_2_2:custom_function_result.data.severity", "==", "high"]
        ],
        conditions_dps=[
            ["geberator_2_2:custom_function_result.data.severity", "==", "high"]
        ],
        name="decision_1:condition_1",
        scope="new",
        case_sensitive=False,
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        add_note_1(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'elif' condition 2
    found_match_2 = phantom.decision(
        container=container,
        conditions=[
            ["geberator_2_2:custom_function_result.data.severity", "==", "low"]
        ],
        conditions_dps=[
            ["geberator_2_2:custom_function_result.data.severity", "==", "low"]
        ],
        name="decision_1:condition_2",
        scope="new",
        case_sensitive=False,
        delimiter=None)

    # call connected blocks if condition 2 matched
    if found_match_2:
        add_note_2(action=action, success=success, container=container, results=results, handle=handle)
        return

    return


@phantom.playbook_block()
def add_note_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_note_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    content_formatted_string = phantom.format(
        container=container,
        template="""\"test1_if1\"\n""",
        parameters=[
            ""
        ])

    id_value = container.get("id", None)

    parameters = []

    parameters.append({
        "title": "title9",
        "content": content_formatted_string,
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
def add_note_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_note_2() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    content_formatted_string = phantom.format(
        container=container,
        template="""\"test2_else\"\n""",
        parameters=[
            ""
        ])

    id_value = container.get("id", None)

    parameters = []

    parameters.append({
        "title": "title_1",
        "content": content_formatted_string,
        "container_id": id_value,
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
def geberator_2_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("geberator_2_2() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.severity","artifact:*.cef.requestURL","artifact:*.id"], scope="new")

    container_artifact_cef_item_1 = [item[1] for item in container_artifact_data]

    parameters = []

    # build parameters list for 'geberator_2_2' call
    for container_artifact_item in container_artifact_data:
        parameters.append({
            "severity_input": container_artifact_item[0],
            "url_input": container_artifact_cef_item_1,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="ipm/Geberator_2", parameters=parameters, name="geberator_2_2", callback=decision_1)

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
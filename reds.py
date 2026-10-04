"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'url_reputation_1' block
    url_reputation_1(container=container)

    return

@phantom.playbook_block()
def url_reputation_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("url_reputation_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.requestURL","artifact:*.id"], scope="all")

    parameters = []

    # build parameters list for 'url_reputation_1' call
    for container_artifact_item in container_artifact_data:
        if container_artifact_item[0] is not None:
            parameters.append({
                "url": container_artifact_item[0],
                "context": {'artifact_id': container_artifact_item[1]},
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("url reputation", parameters=parameters, name="url_reputation_1", assets=["ipm"], callback=decision_1)

    return


@phantom.playbook_block()
def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["url_reputation_1:action_result.data.*.attributes.last_analysis_stats.malicious", ">", 2]
        ],
        conditions_dps=[
            ["url_reputation_1:action_result.data.*.attributes.last_analysis_stats.malicious", ">", 2]
        ],
        name="decision_1:condition_1",
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        format_2(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'elif' condition 2
    found_match_2 = phantom.decision(
        container=container,
        conditions=[
            ["", "<=", 2]
        ],
        conditions_dps=[
            ["", "<=", 2]
        ],
        name="decision_1:condition_2",
        delimiter=None)

    # call connected blocks if condition 2 matched
    if found_match_2:
        format_1(action=action, success=success, container=container, results=results, handle=handle)
        return

    return


@phantom.playbook_block()
def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_1() called")

    template = """Malicious URL Detected\n\nURL: {0}\nMalicious: {1}\nSuspicious: {2}\nHarmless: {3}\nUndetected: {4}{1}{2}{3}{4}"""

    # parameter list for template variable replacement
    parameters = [
        "url_reputation_1:action_result.parameter.url",
        "url_reputation_1:action_result.data.*.attributes.last_analysis_stats.malicious",
        "url_reputation_1:action_result.data.*.attributes.last_analysis_stats.suspicious",
        "url_reputation_1:action_result.data.*.attributes.last_analysis_stats.harmless",
        "url_reputation_1:action_result.data.*.attributes.last_analysis_stats.undetected"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_1", scope="all")

    return


@phantom.playbook_block()
def format_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("format_2() called")

    template = """Malicious URL detected\n\nURL: <URL>\nMalicious: <malicious count>\nSuspicious: <suspicious count>\nHarmless: <harmless count>\nUndetected: <undetected count>\n"""

    # parameter list for template variable replacement
    parameters = [
        "url_reputation_1:action_result.data.*.attributes.last_analysis_stats.malicious"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_2", scope="all")

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
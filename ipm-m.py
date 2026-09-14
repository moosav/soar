"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'code_1' block
    code_1(container=container)

    return

@phantom.playbook_block()
def add_note_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_note_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    id_value = container.get("id", None)
    ipm_1__result = phantom.collect2(container=container, datapath=["ipm_1:custom_function_result.message"])

    parameters = []

    # build parameters list for 'add_note_1' call
    for ipm_1__result_item in ipm_1__result:
        parameters.append({
            "title": "title1",
            "content": ipm_1__result_item[0],
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
def ipm_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("ipm_1() called")

    parameters = [{}]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="local/IPM", parameters=parameters, name="ipm_1", callback=add_note_1)

    return


@phantom.playbook_block()
def code_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("code_1() called")

    input_parameter_0 = ""

    code_1__ur = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_block_result(key="code_1:ur", value=json.dumps(code_1__ur))

    phantom.save_block_result(key="code_1_called", value="True")

    ipm_1(container=container)

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
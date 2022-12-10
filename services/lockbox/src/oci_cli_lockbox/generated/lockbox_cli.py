# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('oma.oma_root_group.command_name', 'oma'), cls=CommandGroupWithAlias, help=cli_util.override('oma.oma_root_group.help', """Use the Managed Access API to approve access requests, create and manage templates, and manage resource approval settings.
Use the table of contents and search tool to explore the Managed Access API."""), short_help=cli_util.override('oma.oma_root_group.short_help', """Managed Access API"""))
@cli_util.help_option_group
def oma_root_group():
    pass


@click.command(cli_util.override('oma.approval_template_collection_group.command_name', 'approval-template-collection'), cls=CommandGroupWithAlias, help="""Results of approval template search. Contains both ApprovalTemplateSummary items and other information, such as metadata.""")
@cli_util.help_option_group
def approval_template_collection_group():
    pass


@click.command(cli_util.override('oma.lockbox_group.command_name', 'lockbox'), cls=CommandGroupWithAlias, help="""Description of Lockbox.""")
@cli_util.help_option_group
def lockbox_group():
    pass


@click.command(cli_util.override('oma.approval_template_group.command_name', 'approval-template'), cls=CommandGroupWithAlias, help="""Group/User OCIDs of those who can approve/deny/revoke operator's request to access associated resources.""")
@cli_util.help_option_group
def approval_template_group():
    pass


@click.command(cli_util.override('oma.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('oma.access_request_collection_group.command_name', 'access-request-collection'), cls=CommandGroupWithAlias, help="""Results of access request search. Contains both AccessRequestSummary items and other information, such as metadata.""")
@cli_util.help_option_group
def access_request_collection_group():
    pass


@click.command(cli_util.override('oma.access_request_group.command_name', 'access-request'), cls=CommandGroupWithAlias, help="""An access request to a customer's resource. An access request is a subsidiary resource of the Lockbox entity.""")
@cli_util.help_option_group
def access_request_group():
    pass


@click.command(cli_util.override('oma.access_materials_group.command_name', 'access-materials'), cls=CommandGroupWithAlias, help="""Access materials details.""")
@cli_util.help_option_group
def access_materials_group():
    pass


@click.command(cli_util.override('oma.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('oma.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workrequest status""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('oma.lockbox_collection_group.command_name', 'lockbox-collection'), cls=CommandGroupWithAlias, help="""Results of a lockbox search. Contains both LockboxSummary items and other information, such as metadata.""")
@cli_util.help_option_group
def lockbox_collection_group():
    pass


oma_root_group.add_command(approval_template_collection_group)
oma_root_group.add_command(lockbox_group)
oma_root_group.add_command(approval_template_group)
oma_root_group.add_command(work_request_error_group)
oma_root_group.add_command(access_request_collection_group)
oma_root_group.add_command(access_request_group)
oma_root_group.add_command(access_materials_group)
oma_root_group.add_command(work_request_log_entry_group)
oma_root_group.add_command(work_request_group)
oma_root_group.add_command(lockbox_collection_group)


@work_request_group.command(name=cli_util.override('oma.cancel_work_request.command_name', 'cancel'), help=u"""Cancels the work request with the given ID. \n[Command Reference](cancelWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_work_request(ctx, from_json, work_request_id, if_match):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    result = client.cancel_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@approval_template_group.command(name=cli_util.override('oma.change_approval_template_compartment.command_name', 'change-compartment'), help=u"""Moves an ApprovalTemplate resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeApprovalTemplateCompartment)""")
@cli_util.option('--approval-template-id', required=True, help=u"""The unique identifier (OCID) of the approval template.""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier (OCID) of the compartment where the resource is located.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_approval_template_compartment(ctx, from_json, approval_template_id, compartment_id, if_match):

    if isinstance(approval_template_id, six.string_types) and len(approval_template_id.strip()) == 0:
        raise click.UsageError('Parameter --approval-template-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    result = client.change_approval_template_compartment(
        approval_template_id=approval_template_id,
        change_approval_template_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@lockbox_group.command(name=cli_util.override('oma.change_lockbox_compartment.command_name', 'change-compartment'), help=u"""Moves a Lockbox resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeLockboxCompartment)""")
@cli_util.option('--lockbox-id', required=True, help=u"""unique Lockbox identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier (OCID) of the compartment where the resource is located.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_lockbox_compartment(ctx, from_json, lockbox_id, compartment_id, if_match):

    if isinstance(lockbox_id, six.string_types) and len(lockbox_id.strip()) == 0:
        raise click.UsageError('Parameter --lockbox-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    result = client.change_lockbox_compartment(
        lockbox_id=lockbox_id,
        change_lockbox_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@access_request_group.command(name=cli_util.override('oma.create_access_request.command_name', 'create'), help=u"""Creates a new access request. \n[Command Reference](createAccessRequest)""")
@cli_util.option('--lockbox-id', required=True, help=u"""The unique identifier (OCID) of the lockbox box that the access request is associated with which is immutable.""")
@cli_util.option('--description', required=True, help=u"""The rationale for requesting the access request.""")
@cli_util.option('--access-duration', required=True, help=u"""The maximum amount of time operator has access to associated resources.""")
@cli_util.option('--display-name', help=u"""The name of the access request.""")
@cli_util.option('--context', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The context object containing the access request specific details.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'context': {'module': 'lockbox', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'context': {'module': 'lockbox', 'class': 'dict(str, string)'}}, output_type={'module': 'lockbox', 'class': 'AccessRequest'})
@cli_util.wrap_exceptions
def create_access_request(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, lockbox_id, description, access_duration, display_name, context):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['lockboxId'] = lockbox_id
    _details['description'] = description
    _details['accessDuration'] = access_duration

    if display_name is not None:
        _details['displayName'] = display_name

    if context is not None:
        _details['context'] = cli_util.parse_json_parameter("context", context)

    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    result = client.create_access_request(
        create_access_request_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@approval_template_group.command(name=cli_util.override('oma.create_approval_template.command_name', 'create'), help=u"""Creates a new approval template. \n[Command Reference](createApprovalTemplate)""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier (OCID) of the compartment where the resource is located.""")
@cli_util.option('--approver-levels', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""approval template identifier""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'approver-levels': {'module': 'lockbox', 'class': 'ApproverLevels'}, 'freeform-tags': {'module': 'lockbox', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'lockbox', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'approver-levels': {'module': 'lockbox', 'class': 'ApproverLevels'}, 'freeform-tags': {'module': 'lockbox', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'lockbox', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'lockbox', 'class': 'ApprovalTemplate'})
@cli_util.wrap_exceptions
def create_approval_template(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, approver_levels, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['approverLevels'] = cli_util.parse_json_parameter("approver_levels", approver_levels)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    result = client.create_approval_template(
        create_approval_template_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_approval_template') and callable(getattr(client, 'get_approval_template')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_approval_template(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@lockbox_group.command(name=cli_util.override('oma.create_lockbox.command_name', 'create'), help=u"""Creates a new Lockbox. \n[Command Reference](createLockbox)""")
@cli_util.option('--resource-id', required=True, help=u"""The unique identifier (OCID) of the customer's resource.""")
@cli_util.option('--lockbox-partner', required=True, type=custom_types.CliCaseInsensitiveChoice(["FAAAS"]), help=u"""The partner using this lockbox to lock a resource.""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier (OCID) of the compartment where the resource is located.""")
@cli_util.option('--partner-compartment-id', required=True, help=u"""Compartment Identifier""")
@cli_util.option('--access-context-attributes', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Lockbox Identifier""")
@cli_util.option('--approval-template-id', help=u"""Approval template ID""")
@cli_util.option('--auto-approval-state', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED"]), help=u"""The auto approval state of the lockbox.""")
@cli_util.option('--max-access-duration', help=u"""The maximum amount of time operator has access to associated resources.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'access-context-attributes': {'module': 'lockbox', 'class': 'AccessContextAttributeCollection'}, 'freeform-tags': {'module': 'lockbox', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'lockbox', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'access-context-attributes': {'module': 'lockbox', 'class': 'AccessContextAttributeCollection'}, 'freeform-tags': {'module': 'lockbox', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'lockbox', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'lockbox', 'class': 'Lockbox'})
@cli_util.wrap_exceptions
def create_lockbox(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, resource_id, lockbox_partner, compartment_id, partner_compartment_id, access_context_attributes, display_name, approval_template_id, auto_approval_state, max_access_duration, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['resourceId'] = resource_id
    _details['lockboxPartner'] = lockbox_partner
    _details['compartmentId'] = compartment_id
    _details['partnerCompartmentId'] = partner_compartment_id
    _details['accessContextAttributes'] = cli_util.parse_json_parameter("access_context_attributes", access_context_attributes)

    if display_name is not None:
        _details['displayName'] = display_name

    if approval_template_id is not None:
        _details['approvalTemplateId'] = approval_template_id

    if auto_approval_state is not None:
        _details['autoApprovalState'] = auto_approval_state

    if max_access_duration is not None:
        _details['maxAccessDuration'] = max_access_duration

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    result = client.create_lockbox(
        create_lockbox_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_lockbox') and callable(getattr(client, 'get_lockbox')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_lockbox(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@approval_template_group.command(name=cli_util.override('oma.delete_approval_template.command_name', 'delete'), help=u"""Deletes an ApprovalTemplate resource by identifier \n[Command Reference](deleteApprovalTemplate)""")
@cli_util.option('--approval-template-id', required=True, help=u"""The unique identifier (OCID) of the approval template.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_approval_template(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, approval_template_id, if_match):

    if isinstance(approval_template_id, six.string_types) and len(approval_template_id.strip()) == 0:
        raise click.UsageError('Parameter --approval-template-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    result = client.delete_approval_template(
        approval_template_id=approval_template_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_approval_template') and callable(getattr(client, 'get_approval_template')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_approval_template(approval_template_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@lockbox_group.command(name=cli_util.override('oma.delete_lockbox.command_name', 'delete'), help=u"""Deletes a Lockbox resource by identifier \n[Command Reference](deleteLockbox)""")
@cli_util.option('--lockbox-id', required=True, help=u"""unique Lockbox identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_lockbox(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, lockbox_id, if_match):

    if isinstance(lockbox_id, six.string_types) and len(lockbox_id.strip()) == 0:
        raise click.UsageError('Parameter --lockbox-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    result = client.delete_lockbox(
        lockbox_id=lockbox_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_lockbox') and callable(getattr(client, 'get_lockbox')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_lockbox(lockbox_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@access_materials_group.command(name=cli_util.override('oma.get_access_materials.command_name', 'get'), help=u"""Retrieves the access credential/material associated with the access request. \n[Command Reference](getAccessMaterials)""")
@cli_util.option('--access-request-id', required=True, help=u"""The unique identifier (OCID) of the access request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'lockbox', 'class': 'AccessMaterials'})
@cli_util.wrap_exceptions
def get_access_materials(ctx, from_json, access_request_id):

    if isinstance(access_request_id, six.string_types) and len(access_request_id.strip()) == 0:
        raise click.UsageError('Parameter --access-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    result = client.get_access_materials(
        access_request_id=access_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@access_request_group.command(name=cli_util.override('oma.get_access_request.command_name', 'get'), help=u"""Retrieves an access request identified by the access request ID. \n[Command Reference](getAccessRequest)""")
@cli_util.option('--access-request-id', required=True, help=u"""The unique identifier (OCID) of the access request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'lockbox', 'class': 'AccessRequest'})
@cli_util.wrap_exceptions
def get_access_request(ctx, from_json, access_request_id):

    if isinstance(access_request_id, six.string_types) and len(access_request_id.strip()) == 0:
        raise click.UsageError('Parameter --access-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    result = client.get_access_request(
        access_request_id=access_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@approval_template_group.command(name=cli_util.override('oma.get_approval_template.command_name', 'get'), help=u"""Retrieves an approval template identified by the approval template ID. \n[Command Reference](getApprovalTemplate)""")
@cli_util.option('--approval-template-id', required=True, help=u"""The unique identifier (OCID) of the approval template.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'lockbox', 'class': 'ApprovalTemplate'})
@cli_util.wrap_exceptions
def get_approval_template(ctx, from_json, approval_template_id):

    if isinstance(approval_template_id, six.string_types) and len(approval_template_id.strip()) == 0:
        raise click.UsageError('Parameter --approval-template-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    result = client.get_approval_template(
        approval_template_id=approval_template_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@lockbox_group.command(name=cli_util.override('oma.get_lockbox.command_name', 'get'), help=u"""Gets a Lockbox by identifier \n[Command Reference](getLockbox)""")
@cli_util.option('--lockbox-id', required=True, help=u"""unique Lockbox identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'lockbox', 'class': 'Lockbox'})
@cli_util.wrap_exceptions
def get_lockbox(ctx, from_json, lockbox_id):

    if isinstance(lockbox_id, six.string_types) and len(lockbox_id.strip()) == 0:
        raise click.UsageError('Parameter --lockbox-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    result = client.get_lockbox(
        lockbox_id=lockbox_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('oma.get_work_request.command_name', 'get'), help=u"""Gets details of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'lockbox', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@access_request_group.command(name=cli_util.override('oma.handle_access_request.command_name', 'handle'), help=u"""Handle the AccessRequest \n[Command Reference](handleAccessRequest)""")
@cli_util.option('--access-request-id', required=True, help=u"""The unique identifier (OCID) of the access request.""")
@cli_util.option('--action', required=True, type=custom_types.CliCaseInsensitiveChoice(["APPROVE", "DENY", "REVOKE", "CANCEL"]), help=u"""The action take by persona""")
@cli_util.option('--message', help=u"""Action justification or details.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def handle_access_request(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, access_request_id, action, message, if_match):

    if isinstance(access_request_id, six.string_types) and len(access_request_id.strip()) == 0:
        raise click.UsageError('Parameter --access-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['action'] = action

    if message is not None:
        _details['message'] = message

    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    result = client.handle_access_request(
        access_request_id=access_request_id,
        handle_access_request_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@access_request_collection_group.command(name=cli_util.override('oma.list_access_requests.command_name', 'list-access-requests'), help=u"""Retrieves a list of AccessRequestSummary objects in a compartment. \n[Command Reference](listAccessRequests)""")
@cli_util.option('--lockbox-id', help=u"""The unique identifier (OCID) of the associated lockbox.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["IN_PROGRESS", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "FAILED"]), help=u"""A filter to return only resources their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--lockbox-partner', type=custom_types.CliCaseInsensitiveChoice(["FAAAS"]), help=u"""The name of the lockbox partner.""")
@cli_util.option('--requestor-id', help=u"""The unique identifier (OCID) of the requestor in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName", "id"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'lockbox', 'class': 'AccessRequestCollection'})
@cli_util.wrap_exceptions
def list_access_requests(ctx, from_json, all_pages, page_size, lockbox_id, display_name, lifecycle_state, lockbox_partner, requestor_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lockbox_id is not None:
        kwargs['lockbox_id'] = lockbox_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if lockbox_partner is not None:
        kwargs['lockbox_partner'] = lockbox_partner
    if requestor_id is not None:
        kwargs['requestor_id'] = requestor_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_access_requests,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_access_requests,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_access_requests(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@approval_template_collection_group.command(name=cli_util.override('oma.list_approval_templates.command_name', 'list-approval-templates'), help=u"""Retrieves a list of ApprovalTemplateSummary objects in a compartment. \n[Command Reference](listApprovalTemplates)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "UPDATING", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources for which their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName", "id"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'lockbox', 'class': 'ApprovalTemplateCollection'})
@cli_util.wrap_exceptions
def list_approval_templates(ctx, from_json, all_pages, page_size, compartment_id, display_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_approval_templates,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_approval_templates,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_approval_templates(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@lockbox_collection_group.command(name=cli_util.override('oma.list_lockboxes.command_name', 'list-lockboxes'), help=u"""Returns a list of Lockboxes. \n[Command Reference](listLockboxes)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "UPDATING", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lockbox-id', help=u"""unique Lockbox identifier""")
@cli_util.option('--resource-id', help=u"""The ID of the resource associated with the lockbox.""")
@cli_util.option('--lockbox-partner', type=custom_types.CliCaseInsensitiveChoice(["FAAAS"]), help=u"""The name of the lockbox partner.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName", "id"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'lockbox', 'class': 'LockboxCollection'})
@cli_util.wrap_exceptions
def list_lockboxes(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, lockbox_id, resource_id, lockbox_partner, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lockbox_id is not None:
        kwargs['lockbox_id'] = lockbox_id
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if lockbox_partner is not None:
        kwargs['lockbox_partner'] = lockbox_partner
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_lockboxes,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_lockboxes,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_lockboxes(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('oma.list_work_request_errors.command_name', 'list'), help=u"""Returns a (paginated) list of errors for the work request with the given ID. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'lockbox', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_group.command(name=cli_util.override('oma.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Returns a (paginated) list of logs for the work request with the given ID. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'lockbox', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('oma.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--work-request-id', help=u"""The ID of the asynchronous work request.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""A filter to return only resources their lifecycleState matches the given OperationStatus.""")
@cli_util.option('--resource-id', help=u"""The ID of the resource affected by the work request.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'lockbox', 'class': 'WorkRequestSummaryCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, status, resource_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if work_request_id is not None:
        kwargs['work_request_id'] = work_request_id
    if status is not None:
        kwargs['status'] = status
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@approval_template_group.command(name=cli_util.override('oma.update_approval_template.command_name', 'update'), help=u"""Updates the ApprovalTemplate \n[Command Reference](updateApprovalTemplate)""")
@cli_util.option('--approval-template-id', required=True, help=u"""The unique identifier (OCID) of the approval template.""")
@cli_util.option('--approver-levels', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""approval template identifier""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'approver-levels': {'module': 'lockbox', 'class': 'ApproverLevels'}, 'freeform-tags': {'module': 'lockbox', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'lockbox', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'approver-levels': {'module': 'lockbox', 'class': 'ApproverLevels'}, 'freeform-tags': {'module': 'lockbox', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'lockbox', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'lockbox', 'class': 'ApprovalTemplate'})
@cli_util.wrap_exceptions
def update_approval_template(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, approval_template_id, approver_levels, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(approval_template_id, six.string_types) and len(approval_template_id.strip()) == 0:
        raise click.UsageError('Parameter --approval-template-id cannot be whitespace or empty string')
    if not force:
        if approver_levels or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to approver-levels and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if approver_levels is not None:
        _details['approverLevels'] = cli_util.parse_json_parameter("approver_levels", approver_levels)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    result = client.update_approval_template(
        approval_template_id=approval_template_id,
        update_approval_template_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_approval_template') and callable(getattr(client, 'get_approval_template')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_approval_template(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@lockbox_group.command(name=cli_util.override('oma.update_lockbox.command_name', 'update'), help=u"""Updates the Lockbox \n[Command Reference](updateLockbox)""")
@cli_util.option('--lockbox-id', required=True, help=u"""unique Lockbox identifier""")
@cli_util.option('--display-name', help=u"""Lockbox Identifier""")
@cli_util.option('--auto-approval-state', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED"]), help=u"""The auto approval state of the lockbox.""")
@cli_util.option('--approval-template-id', help=u"""Approval template ID""")
@cli_util.option('--max-access-duration', help=u"""The maximum amount of time operator has access to associated resources.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'lockbox', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'lockbox', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'lockbox', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'lockbox', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'lockbox', 'class': 'Lockbox'})
@cli_util.wrap_exceptions
def update_lockbox(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, lockbox_id, display_name, auto_approval_state, approval_template_id, max_access_duration, freeform_tags, defined_tags, if_match):

    if isinstance(lockbox_id, six.string_types) and len(lockbox_id.strip()) == 0:
        raise click.UsageError('Parameter --lockbox-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if auto_approval_state is not None:
        _details['autoApprovalState'] = auto_approval_state

    if approval_template_id is not None:
        _details['approvalTemplateId'] = approval_template_id

    if max_access_duration is not None:
        _details['maxAccessDuration'] = max_access_duration

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('lockbox', 'lockbox', ctx)
    result = client.update_lockbox(
        lockbox_id=lockbox_id,
        update_lockbox_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_lockbox') and callable(getattr(client, 'get_lockbox')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_lockbox(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)

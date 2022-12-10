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


@cli.command(cli_util.override('resource_manager.resource_manager_root_group.command_name', 'resource-manager'), cls=CommandGroupWithAlias, help=cli_util.override('resource_manager.resource_manager_root_group.help', """Use the Resource Manager API to automate deployment and operations for all Oracle Cloud Infrastructure resources.
Using the infrastructure-as-code (IaC) model, the service is based on Terraform, an open source industry standard that lets DevOps engineers develop and deploy their infrastructure anywhere.
For more information, see
[the Resource Manager documentation]."""), short_help=cli_util.override('resource_manager.resource_manager_root_group.short_help', """Resource Manager API"""))
@cli_util.help_option_group
def resource_manager_root_group():
    pass


@click.command(cli_util.override('resource_manager.template_group.command_name', 'template'), cls=CommandGroupWithAlias, help="""The properties that define a template. A template is a pre-built Terraform configuration that provisions a set of resources used in a common scenario.""")
@cli_util.help_option_group
def template_group():
    pass


@click.command(cli_util.override('resource_manager.stack_group.command_name', 'stack'), cls=CommandGroupWithAlias, help="""The properties that define a stack. A stack is the collection of Oracle Cloud Infrastructure resources corresponding to a given Terraform configuration. For instructions on managing stacks, see [Managing Stacks]. For more information about stacks, see [Key Concepts].""")
@cli_util.help_option_group
def stack_group():
    pass


@click.command(cli_util.override('resource_manager.template_category_summary_group.command_name', 'template-category-summary'), cls=CommandGroupWithAlias, help="""Summary information for the template category.""")
@cli_util.help_option_group
def template_category_summary_group():
    pass


@click.command(cli_util.override('resource_manager.private_endpoint_group.command_name', 'private-endpoint'), cls=CommandGroupWithAlias, help="""A private endpoint allowing Resource Manager to access nonpublic cloud resources. For more information about private endpoints, see [Private Endpoint Management].""")
@cli_util.help_option_group
def private_endpoint_group():
    pass


@click.command(cli_util.override('resource_manager.reachable_ip_group.command_name', 'reachable-ip'), cls=CommandGroupWithAlias, help="""The reachable, or alternative, IP address for a nonpublic IP address that is associated with the private endpoint. Resource Manager uses this IP address to connect to nonpublic resources through the associated private endpoint.""")
@cli_util.help_option_group
def reachable_ip_group():
    pass


@click.command(cli_util.override('resource_manager.stack_resource_drift_summary_group.command_name', 'stack-resource-drift-summary'), cls=CommandGroupWithAlias, help="""Drift status details for the indicated resource and stack. Includes actual and expected (defined) properties.""")
@cli_util.help_option_group
def stack_resource_drift_summary_group():
    pass


@click.command(cli_util.override('resource_manager.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""The status of a work request.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('resource_manager.associated_resource_summary_group.command_name', 'associated-resource-summary'), cls=CommandGroupWithAlias, help="""Summary information for a resource associated with a stack or job.""")
@cli_util.help_option_group
def associated_resource_summary_group():
    pass


@click.command(cli_util.override('resource_manager.configuration_source_provider_summary_group.command_name', 'configuration-source-provider-summary'), cls=CommandGroupWithAlias, help="""Summary information for a configuration source provider.""")
@cli_util.help_option_group
def configuration_source_provider_summary_group():
    pass


@click.command(cli_util.override('resource_manager.configuration_source_provider_group.command_name', 'configuration-source-provider'), cls=CommandGroupWithAlias, help="""The properties that define a configuration source provider. For more information, see [Managing Configuration Source Providers].""")
@cli_util.help_option_group
def configuration_source_provider_group():
    pass


@click.command(cli_util.override('resource_manager.private_endpoint_summary_group.command_name', 'private-endpoint-summary'), cls=CommandGroupWithAlias, help="""The summary metadata associated with the private endpoint.""")
@cli_util.help_option_group
def private_endpoint_summary_group():
    pass


@click.command(cli_util.override('resource_manager.job_group.command_name', 'job'), cls=CommandGroupWithAlias, help="""The properties of a job. A job performs the actions that are defined in your Terraform configuration. For instructions on managing jobs, see [Managing Jobs]. For more information about jobs, see [Key Concepts].""")
@cli_util.help_option_group
def job_group():
    pass


@click.command(cli_util.override('resource_manager.job_output_summary_group.command_name', 'job-output-summary'), cls=CommandGroupWithAlias, help="""Terraform output associated with a job.""")
@cli_util.help_option_group
def job_output_summary_group():
    pass


resource_manager_root_group.add_command(template_group)
resource_manager_root_group.add_command(stack_group)
resource_manager_root_group.add_command(template_category_summary_group)
resource_manager_root_group.add_command(private_endpoint_group)
resource_manager_root_group.add_command(reachable_ip_group)
resource_manager_root_group.add_command(stack_resource_drift_summary_group)
resource_manager_root_group.add_command(work_request_group)
resource_manager_root_group.add_command(associated_resource_summary_group)
resource_manager_root_group.add_command(configuration_source_provider_summary_group)
resource_manager_root_group.add_command(configuration_source_provider_group)
resource_manager_root_group.add_command(private_endpoint_summary_group)
resource_manager_root_group.add_command(job_group)
resource_manager_root_group.add_command(job_output_summary_group)


@job_group.command(name=cli_util.override('resource_manager.cancel_job.command_name', 'cancel'), help=u"""Indicates the intention to cancel the specified job. Cancellation of the job is not immediate, and may be delayed, or may not happen at all. You can optionally choose forced cancellation by setting `isForced` to true. A forced cancellation can result in an incorrect state file. For example, the state file might not reflect the exact state of the provisioned resources. \n[Command Reference](cancelJob)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--is-forced', type=click.BOOL, help=u"""Indicates whether a forced cancellation is requested for the job while it was running. A forced cancellation can result in an incorrect state file. For example, the state file might not reflect the exact state of the provisioned resources.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, job_id, if_match, is_forced):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if is_forced is not None:
        kwargs['is_forced'] = is_forced
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.cancel_job(
        job_id=job_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_job(job_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@configuration_source_provider_group.command(name=cli_util.override('resource_manager.change_configuration_source_provider_compartment.command_name', 'change-compartment'), help=u"""Moves a configuration source provider into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeConfigurationSourceProviderCompartment)""")
@cli_util.option('--configuration-source-provider-id', required=True, help=u"""The [OCID] of the configuration source provider.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the configuration source provider to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_configuration_source_provider_compartment(ctx, from_json, configuration_source_provider_id, compartment_id, if_match):

    if isinstance(configuration_source_provider_id, six.string_types) and len(configuration_source_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --configuration-source-provider-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.change_configuration_source_provider_compartment(
        configuration_source_provider_id=configuration_source_provider_id,
        change_configuration_source_provider_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@private_endpoint_group.command(name=cli_util.override('resource_manager.change_private_endpoint_compartment.command_name', 'change-compartment'), help=u"""Moves a private endpoint to a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changePrivateEndpointCompartment)""")
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of the private endpoint.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the private endpoint to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_private_endpoint_compartment(ctx, from_json, private_endpoint_id, compartment_id, if_match):

    if isinstance(private_endpoint_id, six.string_types) and len(private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.change_private_endpoint_compartment(
        private_endpoint_id=private_endpoint_id,
        change_private_endpoint_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@stack_group.command(name=cli_util.override('resource_manager.change_stack_compartment.command_name', 'change-compartment'), help=u"""Moves a stack (and its associated jobs) into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeStackCompartment)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the Stack should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_stack_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, stack_id, compartment_id, if_match):

    if isinstance(stack_id, six.string_types) and len(stack_id.strip()) == 0:
        raise click.UsageError('Parameter --stack-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.change_stack_compartment(
        stack_id=stack_id,
        change_stack_compartment_details=_details,
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


@template_group.command(name=cli_util.override('resource_manager.change_template_compartment.command_name', 'change-compartment'), help=u"""Moves a template into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeTemplateCompartment)""")
@cli_util.option('--template-id', required=True, help=u"""The [OCID] of the template.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the configuration source provider to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_template_compartment(ctx, from_json, template_id, compartment_id, if_match):

    if isinstance(template_id, six.string_types) and len(template_id.strip()) == 0:
        raise click.UsageError('Parameter --template-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.change_template_compartment(
        template_id=template_id,
        change_template_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@configuration_source_provider_group.command(name=cli_util.override('resource_manager.create_configuration_source_provider.command_name', 'create'), help=u"""Creates a configuration source provider in the specified compartment. For more information, see [To create a configuration source provider]. \n[Command Reference](createConfigurationSourceProvider)""")
@cli_util.option('--config-source-provider-type', required=True, help=u"""The type of configuration source provider. The `GITLAB_ACCESS_TOKEN` type corresponds to GitLab. The `GITHUB_ACCESS_TOKEN` type corresponds to GitHub. The `BITBUCKET_CLOUD_USERNAME_APPPASSWORD` type corresponds to Bitbucket Cloud. The `BITBUCKET_SERVER_ACCESS_TOKEN` type corresponds to Bitbucket Server.""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment where you want to create the configuration source provider.""")
@cli_util.option('--display-name', help=u"""Human-readable name of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Description of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--private-server-config-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'ConfigurationSourceProvider'})
@cli_util.wrap_exceptions
def create_configuration_source_provider(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, config_source_provider_type, compartment_id, display_name, description, private_server_config_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configSourceProviderType'] = config_source_provider_type

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if private_server_config_details is not None:
        _details['privateServerConfigDetails'] = cli_util.parse_json_parameter("private_server_config_details", private_server_config_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_configuration_source_provider(
        create_configuration_source_provider_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_configuration_source_provider') and callable(getattr(client, 'get_configuration_source_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_configuration_source_provider(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@configuration_source_provider_group.command(name=cli_util.override('resource_manager.create_configuration_source_provider_create_gitlab_access_token_configuration_source_provider_details.command_name', 'create-configuration-source-provider-create-gitlab-access-token-configuration-source-provider-details'), help=u"""Creates a configuration source provider in the specified compartment. For more information, see [To create a configuration source provider]. \n[Command Reference](createConfigurationSourceProvider)""")
@cli_util.option('--api-endpoint', required=True, help=u"""The Git service endpoint. Example: `https://gitlab.com`""")
@cli_util.option('--access-token', required=True, help=u"""The personal access token to be configured on the GitLab repository. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment where you want to create the configuration source provider.""")
@cli_util.option('--display-name', help=u"""Human-readable name of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Description of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--private-server-config-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'ConfigurationSourceProvider'})
@cli_util.wrap_exceptions
def create_configuration_source_provider_create_gitlab_access_token_configuration_source_provider_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, api_endpoint, access_token, compartment_id, display_name, description, private_server_config_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['apiEndpoint'] = api_endpoint
    _details['accessToken'] = access_token

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if private_server_config_details is not None:
        _details['privateServerConfigDetails'] = cli_util.parse_json_parameter("private_server_config_details", private_server_config_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['configSourceProviderType'] = 'GITLAB_ACCESS_TOKEN'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_configuration_source_provider(
        create_configuration_source_provider_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_configuration_source_provider') and callable(getattr(client, 'get_configuration_source_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_configuration_source_provider(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@configuration_source_provider_group.command(name=cli_util.override('resource_manager.create_configuration_source_provider_create_bitbucket_cloud_username_app_password_configuration_source_provider_details.command_name', 'create-configuration-source-provider-create-bitbucket-cloud-username-app-password-configuration-source-provider-details'), help=u"""Creates a configuration source provider in the specified compartment. For more information, see [To create a configuration source provider]. \n[Command Reference](createConfigurationSourceProvider)""")
@cli_util.option('--api-endpoint', required=True, help=u"""The Bitbucket cloud service endpoint. Example: `https://bitbucket.org/`""")
@cli_util.option('--username', required=True, help=u"""The username for the user of the Bitbucket cloud repository.""")
@cli_util.option('--secret-id', required=True, help=u"""The secret ocid which is used to authorize the user.""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment where you want to create the configuration source provider.""")
@cli_util.option('--display-name', help=u"""Human-readable name of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Description of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--private-server-config-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'ConfigurationSourceProvider'})
@cli_util.wrap_exceptions
def create_configuration_source_provider_create_bitbucket_cloud_username_app_password_configuration_source_provider_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, api_endpoint, username, secret_id, compartment_id, display_name, description, private_server_config_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['apiEndpoint'] = api_endpoint
    _details['username'] = username
    _details['secretId'] = secret_id

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if private_server_config_details is not None:
        _details['privateServerConfigDetails'] = cli_util.parse_json_parameter("private_server_config_details", private_server_config_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['configSourceProviderType'] = 'BITBUCKET_CLOUD_USERNAME_APPPASSWORD'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_configuration_source_provider(
        create_configuration_source_provider_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_configuration_source_provider') and callable(getattr(client, 'get_configuration_source_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_configuration_source_provider(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@configuration_source_provider_group.command(name=cli_util.override('resource_manager.create_configuration_source_provider_create_github_access_token_configuration_source_provider_details.command_name', 'create-configuration-source-provider-create-github-access-token-configuration-source-provider-details'), help=u"""Creates a configuration source provider in the specified compartment. For more information, see [To create a configuration source provider]. \n[Command Reference](createConfigurationSourceProvider)""")
@cli_util.option('--api-endpoint', required=True, help=u"""The GitHub service endpoint. Example: `https://github.com/`""")
@cli_util.option('--access-token', required=True, help=u"""The personal access token to be configured on the GitHub repository. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment where you want to create the configuration source provider.""")
@cli_util.option('--display-name', help=u"""Human-readable name of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Description of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--private-server-config-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'ConfigurationSourceProvider'})
@cli_util.wrap_exceptions
def create_configuration_source_provider_create_github_access_token_configuration_source_provider_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, api_endpoint, access_token, compartment_id, display_name, description, private_server_config_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['apiEndpoint'] = api_endpoint
    _details['accessToken'] = access_token

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if private_server_config_details is not None:
        _details['privateServerConfigDetails'] = cli_util.parse_json_parameter("private_server_config_details", private_server_config_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['configSourceProviderType'] = 'GITHUB_ACCESS_TOKEN'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_configuration_source_provider(
        create_configuration_source_provider_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_configuration_source_provider') and callable(getattr(client, 'get_configuration_source_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_configuration_source_provider(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@configuration_source_provider_group.command(name=cli_util.override('resource_manager.create_configuration_source_provider_create_bitbucket_server_access_token_configuration_source_provider_details.command_name', 'create-configuration-source-provider-create-bitbucket-server-access-token-configuration-source-provider-details'), help=u"""Creates a configuration source provider in the specified compartment. For more information, see [To create a configuration source provider]. \n[Command Reference](createConfigurationSourceProvider)""")
@cli_util.option('--secret-id', required=True, help=u"""The secret ocid which is used to authorize the user.""")
@cli_util.option('--api-endpoint', required=True, help=u"""The Bitbucket Server service endpoint Example: `https://bitbucket.org/`""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment where you want to create the configuration source provider.""")
@cli_util.option('--display-name', help=u"""Human-readable name of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Description of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--private-server-config-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'ConfigurationSourceProvider'})
@cli_util.wrap_exceptions
def create_configuration_source_provider_create_bitbucket_server_access_token_configuration_source_provider_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, secret_id, api_endpoint, compartment_id, display_name, description, private_server_config_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['secretId'] = secret_id
    _details['apiEndpoint'] = api_endpoint

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if private_server_config_details is not None:
        _details['privateServerConfigDetails'] = cli_util.parse_json_parameter("private_server_config_details", private_server_config_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['configSourceProviderType'] = 'BITBUCKET_SERVER_ACCESS_TOKEN'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_configuration_source_provider(
        create_configuration_source_provider_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_configuration_source_provider') and callable(getattr(client, 'get_configuration_source_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_configuration_source_provider(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('resource_manager.create_job.command_name', 'create'), help=u"""Creates a job. \n[Command Reference](createJob)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack that is associated with the current job.""")
@cli_util.option('--display-name', help=u"""Description of the job.""")
@cli_util.option('--operation', help=u"""Terraform-specific operation to execute.""")
@cli_util.option('--job-operation-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--apply-job-plan-resolution', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'job-operation-details': {'module': 'resource_manager', 'class': 'CreateJobOperationDetails'}, 'apply-job-plan-resolution': {'module': 'resource_manager', 'class': 'ApplyJobPlanResolution'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'job-operation-details': {'module': 'resource_manager', 'class': 'CreateJobOperationDetails'}, 'apply-job-plan-resolution': {'module': 'resource_manager', 'class': 'ApplyJobPlanResolution'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, stack_id, display_name, operation, job_operation_details, apply_job_plan_resolution, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['stackId'] = stack_id

    if display_name is not None:
        _details['displayName'] = display_name

    if operation is not None:
        _details['operation'] = operation

    if job_operation_details is not None:
        _details['jobOperationDetails'] = cli_util.parse_json_parameter("job_operation_details", job_operation_details)

    if apply_job_plan_resolution is not None:
        _details['applyJobPlanResolution'] = cli_util.parse_json_parameter("apply_job_plan_resolution", apply_job_plan_resolution)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_job(
        create_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('resource_manager.create_job_create_import_tf_state_job_operation_details.command_name', 'create-job-create-import-tf-state-job-operation-details'), help=u"""Creates a job. \n[Command Reference](createJob)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack that is associated with the current job.""")
@cli_util.option('--job-operation-details-tf-state-base64-encoded', required=True, help=u"""Base64-encoded state file""")
@cli_util.option('--display-name', help=u"""Description of the job.""")
@cli_util.option('--operation', help=u"""Terraform-specific operation to execute.""")
@cli_util.option('--apply-job-plan-resolution', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--job-operation-details-is-provider-upgrade-required', type=click.BOOL, help=u"""Specifies whether or not to upgrade provider versions. Within the version constraints of your Terraform configuration, use the latest versions available from the source of Terraform providers. For more information about this option, see [Dependency Lock File (terraform.io)].""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'apply-job-plan-resolution': {'module': 'resource_manager', 'class': 'ApplyJobPlanResolution'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'apply-job-plan-resolution': {'module': 'resource_manager', 'class': 'ApplyJobPlanResolution'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job_create_import_tf_state_job_operation_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, stack_id, job_operation_details_tf_state_base64_encoded, display_name, operation, apply_job_plan_resolution, freeform_tags, defined_tags, job_operation_details_is_provider_upgrade_required):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['jobOperationDetails'] = {}
    _details['stackId'] = stack_id
    _details['jobOperationDetails']['tfStateBase64Encoded'] = job_operation_details_tf_state_base64_encoded

    if display_name is not None:
        _details['displayName'] = display_name

    if operation is not None:
        _details['operation'] = operation

    if apply_job_plan_resolution is not None:
        _details['applyJobPlanResolution'] = cli_util.parse_json_parameter("apply_job_plan_resolution", apply_job_plan_resolution)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if job_operation_details_is_provider_upgrade_required is not None:
        _details['jobOperationDetails']['isProviderUpgradeRequired'] = job_operation_details_is_provider_upgrade_required

    _details['jobOperationDetails']['operation'] = 'IMPORT_TF_STATE'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_job(
        create_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('resource_manager.create_job_create_plan_rollback_job_operation_details.command_name', 'create-job-create-plan-rollback-job-operation-details'), help=u"""Creates a job. \n[Command Reference](createJob)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack that is associated with the current job.""")
@cli_util.option('--job-operation-details-target-rollback-job-id', required=True, help=u"""The [OCID] of a successful apply job to use for the plan rollback job.""")
@cli_util.option('--display-name', help=u"""Description of the job.""")
@cli_util.option('--operation', help=u"""Terraform-specific operation to execute.""")
@cli_util.option('--apply-job-plan-resolution', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--job-operation-details-is-provider-upgrade-required', type=click.BOOL, help=u"""Specifies whether or not to upgrade provider versions. Within the version constraints of your Terraform configuration, use the latest versions available from the source of Terraform providers. For more information about this option, see [Dependency Lock File (terraform.io)].""")
@cli_util.option('--job-operation-details-terraform-advanced-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'apply-job-plan-resolution': {'module': 'resource_manager', 'class': 'ApplyJobPlanResolution'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}, 'job-operation-details-terraform-advanced-options': {'module': 'resource_manager', 'class': 'TerraformAdvancedOptions'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'apply-job-plan-resolution': {'module': 'resource_manager', 'class': 'ApplyJobPlanResolution'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}, 'job-operation-details-terraform-advanced-options': {'module': 'resource_manager', 'class': 'TerraformAdvancedOptions'}}, output_type={'module': 'resource_manager', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job_create_plan_rollback_job_operation_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, stack_id, job_operation_details_target_rollback_job_id, display_name, operation, apply_job_plan_resolution, freeform_tags, defined_tags, job_operation_details_is_provider_upgrade_required, job_operation_details_terraform_advanced_options):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['jobOperationDetails'] = {}
    _details['stackId'] = stack_id
    _details['jobOperationDetails']['targetRollbackJobId'] = job_operation_details_target_rollback_job_id

    if display_name is not None:
        _details['displayName'] = display_name

    if operation is not None:
        _details['operation'] = operation

    if apply_job_plan_resolution is not None:
        _details['applyJobPlanResolution'] = cli_util.parse_json_parameter("apply_job_plan_resolution", apply_job_plan_resolution)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if job_operation_details_is_provider_upgrade_required is not None:
        _details['jobOperationDetails']['isProviderUpgradeRequired'] = job_operation_details_is_provider_upgrade_required

    if job_operation_details_terraform_advanced_options is not None:
        _details['jobOperationDetails']['terraformAdvancedOptions'] = cli_util.parse_json_parameter("job_operation_details_terraform_advanced_options", job_operation_details_terraform_advanced_options)

    _details['jobOperationDetails']['operation'] = 'PLAN_ROLLBACK'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_job(
        create_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('resource_manager.create_job_create_apply_rollback_job_operation_details.command_name', 'create-job-create-apply-rollback-job-operation-details'), help=u"""Creates a job. \n[Command Reference](createJob)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack that is associated with the current job.""")
@cli_util.option('--job-operation-details-execution-plan-rollback-strategy', required=True, help=u"""Specifies the source of the execution plan for rollback to apply. Use `AUTO_APPROVED` to run the job without an execution plan for rollback job.""")
@cli_util.option('--display-name', help=u"""Description of the job.""")
@cli_util.option('--operation', help=u"""Terraform-specific operation to execute.""")
@cli_util.option('--apply-job-plan-resolution', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--job-operation-details-is-provider-upgrade-required', type=click.BOOL, help=u"""Specifies whether or not to upgrade provider versions. Within the version constraints of your Terraform configuration, use the latest versions available from the source of Terraform providers. For more information about this option, see [Dependency Lock File (terraform.io)].""")
@cli_util.option('--job-operation-details-terraform-advanced-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--job-operation-details-execution-plan-rollback-job-id', help=u"""The [OCID] of a plan rollback job, for use when specifying `\"FROM_PLAN_ROLLBACK_JOB_ID\"` as the `executionPlanRollbackStrategy`.""")
@cli_util.option('--job-operation-details-target-rollback-job-id', help=u"""The [OCID] of a successful apply job, for use when specifying `\"AUTO_APPROVED\"` as the `executionPlanRollbackStrategy`.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'apply-job-plan-resolution': {'module': 'resource_manager', 'class': 'ApplyJobPlanResolution'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}, 'job-operation-details-terraform-advanced-options': {'module': 'resource_manager', 'class': 'TerraformAdvancedOptions'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'apply-job-plan-resolution': {'module': 'resource_manager', 'class': 'ApplyJobPlanResolution'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}, 'job-operation-details-terraform-advanced-options': {'module': 'resource_manager', 'class': 'TerraformAdvancedOptions'}}, output_type={'module': 'resource_manager', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job_create_apply_rollback_job_operation_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, stack_id, job_operation_details_execution_plan_rollback_strategy, display_name, operation, apply_job_plan_resolution, freeform_tags, defined_tags, job_operation_details_is_provider_upgrade_required, job_operation_details_terraform_advanced_options, job_operation_details_execution_plan_rollback_job_id, job_operation_details_target_rollback_job_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['jobOperationDetails'] = {}
    _details['stackId'] = stack_id
    _details['jobOperationDetails']['executionPlanRollbackStrategy'] = job_operation_details_execution_plan_rollback_strategy

    if display_name is not None:
        _details['displayName'] = display_name

    if operation is not None:
        _details['operation'] = operation

    if apply_job_plan_resolution is not None:
        _details['applyJobPlanResolution'] = cli_util.parse_json_parameter("apply_job_plan_resolution", apply_job_plan_resolution)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if job_operation_details_is_provider_upgrade_required is not None:
        _details['jobOperationDetails']['isProviderUpgradeRequired'] = job_operation_details_is_provider_upgrade_required

    if job_operation_details_terraform_advanced_options is not None:
        _details['jobOperationDetails']['terraformAdvancedOptions'] = cli_util.parse_json_parameter("job_operation_details_terraform_advanced_options", job_operation_details_terraform_advanced_options)

    if job_operation_details_execution_plan_rollback_job_id is not None:
        _details['jobOperationDetails']['executionPlanRollbackJobId'] = job_operation_details_execution_plan_rollback_job_id

    if job_operation_details_target_rollback_job_id is not None:
        _details['jobOperationDetails']['targetRollbackJobId'] = job_operation_details_target_rollback_job_id

    _details['jobOperationDetails']['operation'] = 'APPLY_ROLLBACK'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_job(
        create_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('resource_manager.create_job_create_apply_job_operation_details.command_name', 'create-job-create-apply-job-operation-details'), help=u"""Creates a job. \n[Command Reference](createJob)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack that is associated with the current job.""")
@cli_util.option('--display-name', help=u"""Description of the job.""")
@cli_util.option('--operation', help=u"""Terraform-specific operation to execute.""")
@cli_util.option('--apply-job-plan-resolution', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--job-operation-details-is-provider-upgrade-required', type=click.BOOL, help=u"""Specifies whether or not to upgrade provider versions. Within the version constraints of your Terraform configuration, use the latest versions available from the source of Terraform providers. For more information about this option, see [Dependency Lock File (terraform.io)].""")
@cli_util.option('--job-operation-details-terraform-advanced-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--job-operation-details-execution-plan-strategy', help=u"""Specifies the source of the execution plan to apply. Use `AUTO_APPROVED` to run the job without an execution plan.""")
@cli_util.option('--job-operation-details-execution-plan-job-id', help=u"""The [OCID] of a plan job, for use when specifying `FROM_PLAN_JOB_ID` as the `executionPlanStrategy`.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'apply-job-plan-resolution': {'module': 'resource_manager', 'class': 'ApplyJobPlanResolution'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}, 'job-operation-details-terraform-advanced-options': {'module': 'resource_manager', 'class': 'TerraformAdvancedOptions'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'apply-job-plan-resolution': {'module': 'resource_manager', 'class': 'ApplyJobPlanResolution'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}, 'job-operation-details-terraform-advanced-options': {'module': 'resource_manager', 'class': 'TerraformAdvancedOptions'}}, output_type={'module': 'resource_manager', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job_create_apply_job_operation_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, stack_id, display_name, operation, apply_job_plan_resolution, freeform_tags, defined_tags, job_operation_details_is_provider_upgrade_required, job_operation_details_terraform_advanced_options, job_operation_details_execution_plan_strategy, job_operation_details_execution_plan_job_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['jobOperationDetails'] = {}
    _details['stackId'] = stack_id

    if display_name is not None:
        _details['displayName'] = display_name

    if operation is not None:
        _details['operation'] = operation

    if apply_job_plan_resolution is not None:
        _details['applyJobPlanResolution'] = cli_util.parse_json_parameter("apply_job_plan_resolution", apply_job_plan_resolution)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if job_operation_details_is_provider_upgrade_required is not None:
        _details['jobOperationDetails']['isProviderUpgradeRequired'] = job_operation_details_is_provider_upgrade_required

    if job_operation_details_terraform_advanced_options is not None:
        _details['jobOperationDetails']['terraformAdvancedOptions'] = cli_util.parse_json_parameter("job_operation_details_terraform_advanced_options", job_operation_details_terraform_advanced_options)

    if job_operation_details_execution_plan_strategy is not None:
        _details['jobOperationDetails']['executionPlanStrategy'] = job_operation_details_execution_plan_strategy

    if job_operation_details_execution_plan_job_id is not None:
        _details['jobOperationDetails']['executionPlanJobId'] = job_operation_details_execution_plan_job_id

    _details['jobOperationDetails']['operation'] = 'APPLY'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_job(
        create_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('resource_manager.create_job_create_plan_job_operation_details.command_name', 'create-job-create-plan-job-operation-details'), help=u"""Creates a job. \n[Command Reference](createJob)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack that is associated with the current job.""")
@cli_util.option('--display-name', help=u"""Description of the job.""")
@cli_util.option('--operation', help=u"""Terraform-specific operation to execute.""")
@cli_util.option('--apply-job-plan-resolution', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--job-operation-details-is-provider-upgrade-required', type=click.BOOL, help=u"""Specifies whether or not to upgrade provider versions. Within the version constraints of your Terraform configuration, use the latest versions available from the source of Terraform providers. For more information about this option, see [Dependency Lock File (terraform.io)].""")
@cli_util.option('--job-operation-details-terraform-advanced-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'apply-job-plan-resolution': {'module': 'resource_manager', 'class': 'ApplyJobPlanResolution'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}, 'job-operation-details-terraform-advanced-options': {'module': 'resource_manager', 'class': 'TerraformAdvancedOptions'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'apply-job-plan-resolution': {'module': 'resource_manager', 'class': 'ApplyJobPlanResolution'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}, 'job-operation-details-terraform-advanced-options': {'module': 'resource_manager', 'class': 'TerraformAdvancedOptions'}}, output_type={'module': 'resource_manager', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job_create_plan_job_operation_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, stack_id, display_name, operation, apply_job_plan_resolution, freeform_tags, defined_tags, job_operation_details_is_provider_upgrade_required, job_operation_details_terraform_advanced_options):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['jobOperationDetails'] = {}
    _details['stackId'] = stack_id

    if display_name is not None:
        _details['displayName'] = display_name

    if operation is not None:
        _details['operation'] = operation

    if apply_job_plan_resolution is not None:
        _details['applyJobPlanResolution'] = cli_util.parse_json_parameter("apply_job_plan_resolution", apply_job_plan_resolution)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if job_operation_details_is_provider_upgrade_required is not None:
        _details['jobOperationDetails']['isProviderUpgradeRequired'] = job_operation_details_is_provider_upgrade_required

    if job_operation_details_terraform_advanced_options is not None:
        _details['jobOperationDetails']['terraformAdvancedOptions'] = cli_util.parse_json_parameter("job_operation_details_terraform_advanced_options", job_operation_details_terraform_advanced_options)

    _details['jobOperationDetails']['operation'] = 'PLAN'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_job(
        create_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('resource_manager.create_job_create_destroy_job_operation_details.command_name', 'create-job-create-destroy-job-operation-details'), help=u"""Creates a job. \n[Command Reference](createJob)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack that is associated with the current job.""")
@cli_util.option('--job-operation-details-execution-plan-strategy', required=True, help=u"""Specifies the source of the execution plan to apply. Currently, only `AUTO_APPROVED` is allowed, which indicates that the job will be run without an execution plan.""")
@cli_util.option('--display-name', help=u"""Description of the job.""")
@cli_util.option('--operation', help=u"""Terraform-specific operation to execute.""")
@cli_util.option('--apply-job-plan-resolution', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--job-operation-details-is-provider-upgrade-required', type=click.BOOL, help=u"""Specifies whether or not to upgrade provider versions. Within the version constraints of your Terraform configuration, use the latest versions available from the source of Terraform providers. For more information about this option, see [Dependency Lock File (terraform.io)].""")
@cli_util.option('--job-operation-details-terraform-advanced-options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'apply-job-plan-resolution': {'module': 'resource_manager', 'class': 'ApplyJobPlanResolution'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}, 'job-operation-details-terraform-advanced-options': {'module': 'resource_manager', 'class': 'TerraformAdvancedOptions'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'apply-job-plan-resolution': {'module': 'resource_manager', 'class': 'ApplyJobPlanResolution'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}, 'job-operation-details-terraform-advanced-options': {'module': 'resource_manager', 'class': 'TerraformAdvancedOptions'}}, output_type={'module': 'resource_manager', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job_create_destroy_job_operation_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, stack_id, job_operation_details_execution_plan_strategy, display_name, operation, apply_job_plan_resolution, freeform_tags, defined_tags, job_operation_details_is_provider_upgrade_required, job_operation_details_terraform_advanced_options):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['jobOperationDetails'] = {}
    _details['stackId'] = stack_id
    _details['jobOperationDetails']['executionPlanStrategy'] = job_operation_details_execution_plan_strategy

    if display_name is not None:
        _details['displayName'] = display_name

    if operation is not None:
        _details['operation'] = operation

    if apply_job_plan_resolution is not None:
        _details['applyJobPlanResolution'] = cli_util.parse_json_parameter("apply_job_plan_resolution", apply_job_plan_resolution)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if job_operation_details_is_provider_upgrade_required is not None:
        _details['jobOperationDetails']['isProviderUpgradeRequired'] = job_operation_details_is_provider_upgrade_required

    if job_operation_details_terraform_advanced_options is not None:
        _details['jobOperationDetails']['terraformAdvancedOptions'] = cli_util.parse_json_parameter("job_operation_details_terraform_advanced_options", job_operation_details_terraform_advanced_options)

    _details['jobOperationDetails']['operation'] = 'DESTROY'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_job(
        create_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@private_endpoint_group.command(name=cli_util.override('resource_manager.create_private_endpoint.command_name', 'create'), help=u"""Creates a private endpoint in the specified compartment. \n[Command Reference](createPrivateEndpoint)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing this private endpoint.""")
@cli_util.option('--display-name', required=True, help=u"""The private endpoint display name. Avoid entering confidential information.""")
@cli_util.option('--vcn-id', required=True, help=u"""The [OCID] of the VCN for the private endpoint.""")
@cli_util.option('--subnet-id', required=True, help=u"""The [OCID] of the subnet within the VCN for the private endpoint.""")
@cli_util.option('--description', help=u"""Description of the private endpoint. Avoid entering confidential information.""")
@cli_util.option('--dns-zones', type=custom_types.CLI_COMPLEX_TYPE, help=u"""DNS Proxy forwards any DNS FQDN queries over into the consumer DNS resolver if the DNS FQDN is included in the dns zones list otherwise it goes to service provider VCN resolver.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--nsg-id-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The [OCIDs] of [network security groups (NSGs)] for the private endpoint. Order does not matter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-used-with-configuration-source-provider', type=click.BOOL, help=u"""When `true`, allows the private endpoint to be used with a configuration source provider.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'dns-zones': {'module': 'resource_manager', 'class': 'list[string]'}, 'nsg-id-list': {'module': 'resource_manager', 'class': 'list[string]'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dns-zones': {'module': 'resource_manager', 'class': 'list[string]'}, 'nsg-id-list': {'module': 'resource_manager', 'class': 'list[string]'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'PrivateEndpoint'})
@cli_util.wrap_exceptions
def create_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, vcn_id, subnet_id, description, dns_zones, nsg_id_list, is_used_with_configuration_source_provider, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['vcnId'] = vcn_id
    _details['subnetId'] = subnet_id

    if description is not None:
        _details['description'] = description

    if dns_zones is not None:
        _details['dnsZones'] = cli_util.parse_json_parameter("dns_zones", dns_zones)

    if nsg_id_list is not None:
        _details['nsgIdList'] = cli_util.parse_json_parameter("nsg_id_list", nsg_id_list)

    if is_used_with_configuration_source_provider is not None:
        _details['isUsedWithConfigurationSourceProvider'] = is_used_with_configuration_source_provider

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_private_endpoint(
        create_private_endpoint_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_private_endpoint') and callable(getattr(client, 'get_private_endpoint')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_private_endpoint(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@stack_group.command(name=cli_util.override('resource_manager.create_stack.command_name', 'create'), help=u"""Creates a stack in the specified compartment. You can create a stack from a Terraform configuration. The Terraform configuration can be directly uploaded or referenced from a source code control system. You can also create a stack from an existing compartment, which generates a Terraform configuration. You can also upload the Terraform configuration from an Object Storage bucket. For more information, see [Creating Stacks]. \n[Command Reference](createStack)""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique identifier ([OCID]) of the compartment in which the stack resides.""")
@cli_util.option('--config-source', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The stack's display name.""")
@cli_util.option('--description', help=u"""Description of the stack.""")
@cli_util.option('--custom-terraform-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Terraform variables associated with this resource. Maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--terraform-version', help=u"""The version of Terraform to use with the stack. Example: `0.12.x`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags associated with this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'config-source': {'module': 'resource_manager', 'class': 'CreateConfigSourceDetails'}, 'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'config-source': {'module': 'resource_manager', 'class': 'CreateConfigSourceDetails'}, 'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def create_stack(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, config_source, display_name, description, custom_terraform_provider, variables, terraform_version, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['configSource'] = cli_util.parse_json_parameter("config_source", config_source)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if custom_terraform_provider is not None:
        _details['customTerraformProvider'] = cli_util.parse_json_parameter("custom_terraform_provider", custom_terraform_provider)

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if terraform_version is not None:
        _details['terraformVersion'] = terraform_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_stack(
        create_stack_details=_details,
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


@stack_group.command(name=cli_util.override('resource_manager.create_stack_create_dev_ops_config_source_details.command_name', 'create-stack-create-dev-ops-config-source-details'), help=u"""Creates a stack in the specified compartment. You can create a stack from a Terraform configuration. The Terraform configuration can be directly uploaded or referenced from a source code control system. You can also create a stack from an existing compartment, which generates a Terraform configuration. You can also upload the Terraform configuration from an Object Storage bucket. For more information, see [Creating Stacks]. \n[Command Reference](createStack)""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique identifier ([OCID]) of the compartment in which the stack resides.""")
@cli_util.option('--config-source-project-id', required=True, help=u"""The [OCID] of the [DevOps project].""")
@cli_util.option('--config-source-repository-id', required=True, help=u"""The [OCID] of the [DevOps repository].""")
@cli_util.option('--display-name', help=u"""The stack's display name.""")
@cli_util.option('--description', help=u"""Description of the stack.""")
@cli_util.option('--custom-terraform-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Terraform variables associated with this resource. Maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--terraform-version', help=u"""The version of Terraform to use with the stack. Example: `0.12.x`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags associated with this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-source-working-directory', help=u"""File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see [File Structure (Terraform Configurations for Resource Manager)].""")
@cli_util.option('--config-source-branch-name', help=u"""The name of the branch that contains the Terraform configuration.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def create_stack_create_dev_ops_config_source_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, config_source_project_id, config_source_repository_id, display_name, description, custom_terraform_provider, variables, terraform_version, freeform_tags, defined_tags, config_source_working_directory, config_source_branch_name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configSource'] = {}
    _details['compartmentId'] = compartment_id
    _details['configSource']['projectId'] = config_source_project_id
    _details['configSource']['repositoryId'] = config_source_repository_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if custom_terraform_provider is not None:
        _details['customTerraformProvider'] = cli_util.parse_json_parameter("custom_terraform_provider", custom_terraform_provider)

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if terraform_version is not None:
        _details['terraformVersion'] = terraform_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config_source_working_directory is not None:
        _details['configSource']['workingDirectory'] = config_source_working_directory

    if config_source_branch_name is not None:
        _details['configSource']['branchName'] = config_source_branch_name

    _details['configSource']['configSourceType'] = 'DEVOPS_CONFIG_SOURCE'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_stack(
        create_stack_details=_details,
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


@stack_group.command(name=cli_util.override('resource_manager.create_stack_create_bitbucket_cloud_config_source_details.command_name', 'create-stack-create-bitbucket-cloud-config-source-details'), help=u"""Creates a stack in the specified compartment. You can create a stack from a Terraform configuration. The Terraform configuration can be directly uploaded or referenced from a source code control system. You can also create a stack from an existing compartment, which generates a Terraform configuration. You can also upload the Terraform configuration from an Object Storage bucket. For more information, see [Creating Stacks]. \n[Command Reference](createStack)""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique identifier ([OCID]) of the compartment in which the stack resides.""")
@cli_util.option('--config-source-configuration-source-provider-id', required=True, help=u"""The [OCID] of the Bitbucket Cloud configuration source.""")
@cli_util.option('--config-source-repository-url', required=True, help=u"""The URL of the Bitbucket Cloud repository for the configuration source.""")
@cli_util.option('--config-source-workspace-id', required=True, help=u"""The id of the workspace in Bitbucket Cloud for the configuration source""")
@cli_util.option('--display-name', help=u"""The stack's display name.""")
@cli_util.option('--description', help=u"""Description of the stack.""")
@cli_util.option('--custom-terraform-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Terraform variables associated with this resource. Maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--terraform-version', help=u"""The version of Terraform to use with the stack. Example: `0.12.x`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags associated with this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-source-working-directory', help=u"""File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see [File Structure (Terraform Configurations for Resource Manager)].""")
@cli_util.option('--config-source-branch-name', help=u"""The name of the branch in the Bitbucket Cloud repository for the configuration source.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def create_stack_create_bitbucket_cloud_config_source_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, config_source_configuration_source_provider_id, config_source_repository_url, config_source_workspace_id, display_name, description, custom_terraform_provider, variables, terraform_version, freeform_tags, defined_tags, config_source_working_directory, config_source_branch_name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configSource'] = {}
    _details['compartmentId'] = compartment_id
    _details['configSource']['configurationSourceProviderId'] = config_source_configuration_source_provider_id
    _details['configSource']['repositoryUrl'] = config_source_repository_url
    _details['configSource']['workspaceId'] = config_source_workspace_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if custom_terraform_provider is not None:
        _details['customTerraformProvider'] = cli_util.parse_json_parameter("custom_terraform_provider", custom_terraform_provider)

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if terraform_version is not None:
        _details['terraformVersion'] = terraform_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config_source_working_directory is not None:
        _details['configSource']['workingDirectory'] = config_source_working_directory

    if config_source_branch_name is not None:
        _details['configSource']['branchName'] = config_source_branch_name

    _details['configSource']['configSourceType'] = 'BITBUCKET_CLOUD_CONFIG_SOURCE'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_stack(
        create_stack_details=_details,
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


@stack_group.command(name=cli_util.override('resource_manager.create_stack_create_zip_upload_config_source_details.command_name', 'create-stack-create-zip-upload-config-source-details'), help=u"""Creates a stack in the specified compartment. You can create a stack from a Terraform configuration. The Terraform configuration can be directly uploaded or referenced from a source code control system. You can also create a stack from an existing compartment, which generates a Terraform configuration. You can also upload the Terraform configuration from an Object Storage bucket. For more information, see [Creating Stacks]. \n[Command Reference](createStack)""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique identifier ([OCID]) of the compartment in which the stack resides.""")
@cli_util.option('--config-source-zip-file-base64-encoded', required=True, help=u"""""")
@cli_util.option('--display-name', help=u"""The stack's display name.""")
@cli_util.option('--description', help=u"""Description of the stack.""")
@cli_util.option('--custom-terraform-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Terraform variables associated with this resource. Maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--terraform-version', help=u"""The version of Terraform to use with the stack. Example: `0.12.x`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags associated with this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-source-working-directory', help=u"""File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see [File Structure (Terraform Configurations for Resource Manager)].""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def create_stack_create_zip_upload_config_source_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, config_source_zip_file_base64_encoded, display_name, description, custom_terraform_provider, variables, terraform_version, freeform_tags, defined_tags, config_source_working_directory):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configSource'] = {}
    _details['compartmentId'] = compartment_id
    _details['configSource']['zipFileBase64Encoded'] = config_source_zip_file_base64_encoded

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if custom_terraform_provider is not None:
        _details['customTerraformProvider'] = cli_util.parse_json_parameter("custom_terraform_provider", custom_terraform_provider)

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if terraform_version is not None:
        _details['terraformVersion'] = terraform_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config_source_working_directory is not None:
        _details['configSource']['workingDirectory'] = config_source_working_directory

    _details['configSource']['configSourceType'] = 'ZIP_UPLOAD'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_stack(
        create_stack_details=_details,
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


@stack_group.command(name=cli_util.override('resource_manager.create_stack_create_bitbucket_server_config_source_details.command_name', 'create-stack-create-bitbucket-server-config-source-details'), help=u"""Creates a stack in the specified compartment. You can create a stack from a Terraform configuration. The Terraform configuration can be directly uploaded or referenced from a source code control system. You can also create a stack from an existing compartment, which generates a Terraform configuration. You can also upload the Terraform configuration from an Object Storage bucket. For more information, see [Creating Stacks]. \n[Command Reference](createStack)""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique identifier ([OCID]) of the compartment in which the stack resides.""")
@cli_util.option('--config-source-configuration-source-provider-id', required=True, help=u"""Unique identifier ([OCID]) for the Bitbucket Server configuration source.""")
@cli_util.option('--config-source-repository-url', required=True, help=u"""The URL of the Bitbucket Server repository.""")
@cli_util.option('--display-name', help=u"""The stack's display name.""")
@cli_util.option('--description', help=u"""Description of the stack.""")
@cli_util.option('--custom-terraform-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Terraform variables associated with this resource. Maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--terraform-version', help=u"""The version of Terraform to use with the stack. Example: `0.12.x`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags associated with this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-source-working-directory', help=u"""File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see [File Structure (Terraform Configurations for Resource Manager)].""")
@cli_util.option('--config-source-branch-name', help=u"""The name of the branch within the Bitbucket Server repository.""")
@cli_util.option('--config-source-project-id', help=u"""Unique identifier for a Bitbucket Server project.""")
@cli_util.option('--config-source-repository-id', help=u"""Bitbucket Server repository identifier, usually identified as <repository>.git.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def create_stack_create_bitbucket_server_config_source_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, config_source_configuration_source_provider_id, config_source_repository_url, display_name, description, custom_terraform_provider, variables, terraform_version, freeform_tags, defined_tags, config_source_working_directory, config_source_branch_name, config_source_project_id, config_source_repository_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configSource'] = {}
    _details['compartmentId'] = compartment_id
    _details['configSource']['configurationSourceProviderId'] = config_source_configuration_source_provider_id
    _details['configSource']['repositoryUrl'] = config_source_repository_url

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if custom_terraform_provider is not None:
        _details['customTerraformProvider'] = cli_util.parse_json_parameter("custom_terraform_provider", custom_terraform_provider)

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if terraform_version is not None:
        _details['terraformVersion'] = terraform_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config_source_working_directory is not None:
        _details['configSource']['workingDirectory'] = config_source_working_directory

    if config_source_branch_name is not None:
        _details['configSource']['branchName'] = config_source_branch_name

    if config_source_project_id is not None:
        _details['configSource']['projectId'] = config_source_project_id

    if config_source_repository_id is not None:
        _details['configSource']['repositoryId'] = config_source_repository_id

    _details['configSource']['configSourceType'] = 'BITBUCKET_SERVER_CONFIG_SOURCE'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_stack(
        create_stack_details=_details,
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


@stack_group.command(name=cli_util.override('resource_manager.create_stack_create_git_config_source_details.command_name', 'create-stack-create-git-config-source-details'), help=u"""Creates a stack in the specified compartment. You can create a stack from a Terraform configuration. The Terraform configuration can be directly uploaded or referenced from a source code control system. You can also create a stack from an existing compartment, which generates a Terraform configuration. You can also upload the Terraform configuration from an Object Storage bucket. For more information, see [Creating Stacks]. \n[Command Reference](createStack)""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique identifier ([OCID]) of the compartment in which the stack resides.""")
@cli_util.option('--config-source-configuration-source-provider-id', required=True, help=u"""Unique identifier ([OCID]) for the Git configuration source.""")
@cli_util.option('--display-name', help=u"""The stack's display name.""")
@cli_util.option('--description', help=u"""Description of the stack.""")
@cli_util.option('--custom-terraform-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Terraform variables associated with this resource. Maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--terraform-version', help=u"""The version of Terraform to use with the stack. Example: `0.12.x`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags associated with this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-source-working-directory', help=u"""File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see [File Structure (Terraform Configurations for Resource Manager)].""")
@cli_util.option('--config-source-repository-url', help=u"""The URL of the Git repository.""")
@cli_util.option('--config-source-branch-name', help=u"""The name of the branch within the Git repository.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def create_stack_create_git_config_source_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, config_source_configuration_source_provider_id, display_name, description, custom_terraform_provider, variables, terraform_version, freeform_tags, defined_tags, config_source_working_directory, config_source_repository_url, config_source_branch_name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configSource'] = {}
    _details['compartmentId'] = compartment_id
    _details['configSource']['configurationSourceProviderId'] = config_source_configuration_source_provider_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if custom_terraform_provider is not None:
        _details['customTerraformProvider'] = cli_util.parse_json_parameter("custom_terraform_provider", custom_terraform_provider)

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if terraform_version is not None:
        _details['terraformVersion'] = terraform_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config_source_working_directory is not None:
        _details['configSource']['workingDirectory'] = config_source_working_directory

    if config_source_repository_url is not None:
        _details['configSource']['repositoryUrl'] = config_source_repository_url

    if config_source_branch_name is not None:
        _details['configSource']['branchName'] = config_source_branch_name

    _details['configSource']['configSourceType'] = 'GIT_CONFIG_SOURCE'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_stack(
        create_stack_details=_details,
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


@stack_group.command(name=cli_util.override('resource_manager.create_stack_create_object_storage_config_source_details.command_name', 'create-stack-create-object-storage-config-source-details'), help=u"""Creates a stack in the specified compartment. You can create a stack from a Terraform configuration. The Terraform configuration can be directly uploaded or referenced from a source code control system. You can also create a stack from an existing compartment, which generates a Terraform configuration. You can also upload the Terraform configuration from an Object Storage bucket. For more information, see [Creating Stacks]. \n[Command Reference](createStack)""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique identifier ([OCID]) of the compartment in which the stack resides.""")
@cli_util.option('--config-source-region', required=True, help=u"""The name of the bucket's region. Example: `us-phoenix-1`""")
@cli_util.option('--config-source-namespace', required=True, help=u"""The Object Storage namespace that contains the bucket.""")
@cli_util.option('--config-source-bucket-name', required=True, help=u"""The name of the bucket that contains the Terraform configuration files.""")
@cli_util.option('--display-name', help=u"""The stack's display name.""")
@cli_util.option('--description', help=u"""Description of the stack.""")
@cli_util.option('--custom-terraform-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Terraform variables associated with this resource. Maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--terraform-version', help=u"""The version of Terraform to use with the stack. Example: `0.12.x`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags associated with this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-source-working-directory', help=u"""File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see [File Structure (Terraform Configurations for Resource Manager)].""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def create_stack_create_object_storage_config_source_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, config_source_region, config_source_namespace, config_source_bucket_name, display_name, description, custom_terraform_provider, variables, terraform_version, freeform_tags, defined_tags, config_source_working_directory):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configSource'] = {}
    _details['compartmentId'] = compartment_id
    _details['configSource']['region'] = config_source_region
    _details['configSource']['namespace'] = config_source_namespace
    _details['configSource']['bucketName'] = config_source_bucket_name

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if custom_terraform_provider is not None:
        _details['customTerraformProvider'] = cli_util.parse_json_parameter("custom_terraform_provider", custom_terraform_provider)

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if terraform_version is not None:
        _details['terraformVersion'] = terraform_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config_source_working_directory is not None:
        _details['configSource']['workingDirectory'] = config_source_working_directory

    _details['configSource']['configSourceType'] = 'OBJECT_STORAGE_CONFIG_SOURCE'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_stack(
        create_stack_details=_details,
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


@stack_group.command(name=cli_util.override('resource_manager.create_stack_create_compartment_config_source_details.command_name', 'create-stack-create-compartment-config-source-details'), help=u"""Creates a stack in the specified compartment. You can create a stack from a Terraform configuration. The Terraform configuration can be directly uploaded or referenced from a source code control system. You can also create a stack from an existing compartment, which generates a Terraform configuration. You can also upload the Terraform configuration from an Object Storage bucket. For more information, see [Creating Stacks]. \n[Command Reference](createStack)""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique identifier ([OCID]) of the compartment in which the stack resides.""")
@cli_util.option('--config-source-compartment-id', required=True, help=u"""The [OCID] of the compartment to use for creating the stack. The new stack will include definitions for supported resource types in scope of the specified compartment OCID (tenancy level for root compartment, compartment level otherwise).""")
@cli_util.option('--config-source-region', required=True, help=u"""The region to use for creating the stack. The new stack will include definitions for supported resource types in this region.""")
@cli_util.option('--display-name', help=u"""The stack's display name.""")
@cli_util.option('--description', help=u"""Description of the stack.""")
@cli_util.option('--custom-terraform-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Terraform variables associated with this resource. Maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--terraform-version', help=u"""The version of Terraform to use with the stack. Example: `0.12.x`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags associated with this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-source-working-directory', help=u"""File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see [File Structure (Terraform Configurations for Resource Manager)].""")
@cli_util.option('--config-source-services-to-discover', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Filter for [services to use with Resource Discovery]. For example, \"database\" limits resource discovery to resource types within the Database service. The specified services must be in scope of the given compartment OCID (tenancy level for root compartment, compartment level otherwise). If not specified, then all services at the scope of the given compartment OCID are used.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}, 'config-source-services-to-discover': {'module': 'resource_manager', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}, 'config-source-services-to-discover': {'module': 'resource_manager', 'class': 'list[string]'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def create_stack_create_compartment_config_source_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, config_source_compartment_id, config_source_region, display_name, description, custom_terraform_provider, variables, terraform_version, freeform_tags, defined_tags, config_source_working_directory, config_source_services_to_discover):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configSource'] = {}
    _details['compartmentId'] = compartment_id
    _details['configSource']['compartmentId'] = config_source_compartment_id
    _details['configSource']['region'] = config_source_region

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if custom_terraform_provider is not None:
        _details['customTerraformProvider'] = cli_util.parse_json_parameter("custom_terraform_provider", custom_terraform_provider)

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if terraform_version is not None:
        _details['terraformVersion'] = terraform_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config_source_working_directory is not None:
        _details['configSource']['workingDirectory'] = config_source_working_directory

    if config_source_services_to_discover is not None:
        _details['configSource']['servicesToDiscover'] = cli_util.parse_json_parameter("config_source_services_to_discover", config_source_services_to_discover)

    _details['configSource']['configSourceType'] = 'COMPARTMENT_CONFIG_SOURCE'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_stack(
        create_stack_details=_details,
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


@stack_group.command(name=cli_util.override('resource_manager.create_stack_create_stack_template_config_source_details.command_name', 'create-stack-create-stack-template-config-source-details'), help=u"""Creates a stack in the specified compartment. You can create a stack from a Terraform configuration. The Terraform configuration can be directly uploaded or referenced from a source code control system. You can also create a stack from an existing compartment, which generates a Terraform configuration. You can also upload the Terraform configuration from an Object Storage bucket. For more information, see [Creating Stacks]. \n[Command Reference](createStack)""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique identifier ([OCID]) of the compartment in which the stack resides.""")
@cli_util.option('--config-source-template-id', required=True, help=u"""""")
@cli_util.option('--display-name', help=u"""The stack's display name.""")
@cli_util.option('--description', help=u"""Description of the stack.""")
@cli_util.option('--custom-terraform-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Terraform variables associated with this resource. Maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--terraform-version', help=u"""The version of Terraform to use with the stack. Example: `0.12.x`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags associated with this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-source-working-directory', help=u"""File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see [File Structure (Terraform Configurations for Resource Manager)].""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def create_stack_create_stack_template_config_source_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, config_source_template_id, display_name, description, custom_terraform_provider, variables, terraform_version, freeform_tags, defined_tags, config_source_working_directory):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configSource'] = {}
    _details['compartmentId'] = compartment_id
    _details['configSource']['templateId'] = config_source_template_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if custom_terraform_provider is not None:
        _details['customTerraformProvider'] = cli_util.parse_json_parameter("custom_terraform_provider", custom_terraform_provider)

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if terraform_version is not None:
        _details['terraformVersion'] = terraform_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config_source_working_directory is not None:
        _details['configSource']['workingDirectory'] = config_source_working_directory

    _details['configSource']['configSourceType'] = 'TEMPLATE_CONFIG_SOURCE'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_stack(
        create_stack_details=_details,
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


@template_group.command(name=cli_util.override('resource_manager.create_template.command_name', 'create'), help=u"""Creates a private template in the specified compartment. \n[Command Reference](createTemplate)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing this template.""")
@cli_util.option('--display-name', required=True, help=u"""The template's display name. Avoid entering confidential information.""")
@cli_util.option('--description', required=True, help=u"""Description of the template. Avoid entering confidential information.""")
@cli_util.option('--template-config-source', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--long-description', help=u"""Detailed description of the template. This description is displayed in the Console page listing templates when the template is expanded. Avoid entering confidential information.""")
@cli_util.option('--logo-file-base64-encoded', help=u"""Base64-encoded logo to use as the template icon. Template icon file requirements: PNG format, 50 KB maximum, 110 x 110 pixels.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'template-config-source': {'module': 'resource_manager', 'class': 'CreateTemplateConfigSourceDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'template-config-source': {'module': 'resource_manager', 'class': 'CreateTemplateConfigSourceDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Template'})
@cli_util.wrap_exceptions
def create_template(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, description, template_config_source, long_description, logo_file_base64_encoded, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['description'] = description
    _details['templateConfigSource'] = cli_util.parse_json_parameter("template_config_source", template_config_source)

    if long_description is not None:
        _details['longDescription'] = long_description

    if logo_file_base64_encoded is not None:
        _details['logoFileBase64Encoded'] = logo_file_base64_encoded

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_template(
        create_template_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_template') and callable(getattr(client, 'get_template')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_template(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@template_group.command(name=cli_util.override('resource_manager.create_template_create_template_zip_upload_config_source_details.command_name', 'create-template-create-template-zip-upload-config-source-details'), help=u"""Creates a private template in the specified compartment. \n[Command Reference](createTemplate)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing this template.""")
@cli_util.option('--display-name', required=True, help=u"""The template's display name. Avoid entering confidential information.""")
@cli_util.option('--description', required=True, help=u"""Description of the template. Avoid entering confidential information.""")
@cli_util.option('--template-config-source-zip-file-base64-encoded', required=True, help=u"""""")
@cli_util.option('--long-description', help=u"""Detailed description of the template. This description is displayed in the Console page listing templates when the template is expanded. Avoid entering confidential information.""")
@cli_util.option('--logo-file-base64-encoded', help=u"""Base64-encoded logo to use as the template icon. Template icon file requirements: PNG format, 50 KB maximum, 110 x 110 pixels.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Template'})
@cli_util.wrap_exceptions
def create_template_create_template_zip_upload_config_source_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, description, template_config_source_zip_file_base64_encoded, long_description, logo_file_base64_encoded, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['templateConfigSource'] = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['description'] = description
    _details['templateConfigSource']['zipFileBase64Encoded'] = template_config_source_zip_file_base64_encoded

    if long_description is not None:
        _details['longDescription'] = long_description

    if logo_file_base64_encoded is not None:
        _details['logoFileBase64Encoded'] = logo_file_base64_encoded

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['templateConfigSource']['templateConfigSourceType'] = 'ZIP_UPLOAD'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.create_template(
        create_template_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_template') and callable(getattr(client, 'get_template')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_template(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@configuration_source_provider_group.command(name=cli_util.override('resource_manager.delete_configuration_source_provider.command_name', 'delete'), help=u"""Deletes the specified configuration source provider. \n[Command Reference](deleteConfigurationSourceProvider)""")
@cli_util.option('--configuration-source-provider-id', required=True, help=u"""The [OCID] of the configuration source provider.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_configuration_source_provider(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, configuration_source_provider_id, if_match):

    if isinstance(configuration_source_provider_id, six.string_types) and len(configuration_source_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --configuration-source-provider-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.delete_configuration_source_provider(
        configuration_source_provider_id=configuration_source_provider_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_configuration_source_provider') and callable(getattr(client, 'get_configuration_source_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_configuration_source_provider(configuration_source_provider_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@private_endpoint_group.command(name=cli_util.override('resource_manager.delete_private_endpoint.command_name', 'delete'), help=u"""Deletes the specified private endpoint. \n[Command Reference](deletePrivateEndpoint)""")
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of the private endpoint.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, private_endpoint_id, if_match):

    if isinstance(private_endpoint_id, six.string_types) and len(private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.delete_private_endpoint(
        private_endpoint_id=private_endpoint_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_private_endpoint') and callable(getattr(client, 'get_private_endpoint')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_private_endpoint(private_endpoint_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@stack_group.command(name=cli_util.override('resource_manager.delete_stack.command_name', 'delete'), help=u"""Deletes the specified stack. \n[Command Reference](deleteStack)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_stack(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, stack_id, if_match):

    if isinstance(stack_id, six.string_types) and len(stack_id.strip()) == 0:
        raise click.UsageError('Parameter --stack-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.delete_stack(
        stack_id=stack_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stack') and callable(getattr(client, 'get_stack')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_stack(stack_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@template_group.command(name=cli_util.override('resource_manager.delete_template.command_name', 'delete'), help=u"""Deletes the specified template. \n[Command Reference](deleteTemplate)""")
@cli_util.option('--template-id', required=True, help=u"""The [OCID] of the template.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_template(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, template_id, if_match):

    if isinstance(template_id, six.string_types) and len(template_id.strip()) == 0:
        raise click.UsageError('Parameter --template-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.delete_template(
        template_id=template_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_template') and callable(getattr(client, 'get_template')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_template(template_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@stack_group.command(name=cli_util.override('resource_manager.detect_stack_drift.command_name', 'detect-stack-drift'), help=u"""Checks drift status for the specified stack. \n[Command Reference](detectStackDrift)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--resource-addresses', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of resources in the specified stack to detect drift for. Each resource is identified by a resource address, which is a string derived from the resource type and name specified in the stack's Terraform configuration plus an optional index. For example, the resource address for the fourth Compute instance with the name \"test_instance\" is oci_core_instance.test_instance[3]. For more details and examples of resource addresses, see the Terraform documentation at [Resource spec].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-provider-upgrade-required', type=click.BOOL, help=u"""Specifies whether or not to upgrade provider versions. Within the version constraints of your Terraform configuration, use the latest versions available from the source of Terraform providers. For more information about this option, see [Dependency Lock File (terraform.io)].""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'resource-addresses': {'module': 'resource_manager', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'resource-addresses': {'module': 'resource_manager', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def detect_stack_drift(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, stack_id, if_match, resource_addresses, is_provider_upgrade_required):

    if isinstance(stack_id, six.string_types) and len(stack_id.strip()) == 0:
        raise click.UsageError('Parameter --stack-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if resource_addresses is not None:
        _details['resourceAddresses'] = cli_util.parse_json_parameter("resource_addresses", resource_addresses)

    if is_provider_upgrade_required is not None:
        _details['isProviderUpgradeRequired'] = is_provider_upgrade_required

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.detect_stack_drift(
        stack_id=stack_id,
        detect_stack_drift_details=_details,
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


@configuration_source_provider_group.command(name=cli_util.override('resource_manager.get_configuration_source_provider.command_name', 'get'), help=u"""Gets the properties of the specified configuration source provider. \n[Command Reference](getConfigurationSourceProvider)""")
@cli_util.option('--configuration-source-provider-id', required=True, help=u"""The [OCID] of the configuration source provider.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'ConfigurationSourceProvider'})
@cli_util.wrap_exceptions
def get_configuration_source_provider(ctx, from_json, configuration_source_provider_id):

    if isinstance(configuration_source_provider_id, six.string_types) and len(configuration_source_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --configuration-source-provider-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.get_configuration_source_provider(
        configuration_source_provider_id=configuration_source_provider_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('resource_manager.get_job.command_name', 'get'), help=u"""Gets the properties of the specified job. \n[Command Reference](getJob)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'Job'})
@cli_util.wrap_exceptions
def get_job(ctx, from_json, job_id):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.get_job(
        job_id=job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('resource_manager.get_job_detailed_log_content.command_name', 'get-job-detailed-log-content'), help=u"""Returns the Terraform detailed log content for the specified job in plain text. [Learn about Terraform detailed log.] \n[Command Reference](getJobDetailedLogContent)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_job_detailed_log_content(ctx, from_json, job_id):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.get_job_detailed_log_content(
        job_id=job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('resource_manager.get_job_logs.command_name', 'get-job-logs'), help=u"""Returns console log entries for the specified job in JSON format. \n[Command Reference](getJobLogs)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["TERRAFORM_CONSOLE"]), multiple=True, help=u"""A filter that returns only logs of a specified type.""")
@cli_util.option('--level-greater-than-or-equal-to', type=custom_types.CliCaseInsensitiveChoice(["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "FATAL"]), help=u"""A filter that returns only log entries that match a given severity level or greater.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--timestamp-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Time stamp specifying the lower time limit for which logs are returned in a query. Format is defined by RFC3339. Example: `2020-01-01T12:00:00.000Z`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--timestamp-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Time stamp specifying the upper time limit for which logs are returned in a query. Format is defined by RFC3339. Example: `2020-02-01T12:00:00.000Z`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'list[LogEntry]'})
@cli_util.wrap_exceptions
def get_job_logs(ctx, from_json, job_id, type, level_greater_than_or_equal_to, sort_order, limit, page, timestamp_greater_than_or_equal_to, timestamp_less_than_or_equal_to):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    if type is not None and len(type) > 0:
        kwargs['type'] = type
    if level_greater_than_or_equal_to is not None:
        kwargs['level_greater_than_or_equal_to'] = level_greater_than_or_equal_to
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if timestamp_greater_than_or_equal_to is not None:
        kwargs['timestamp_greater_than_or_equal_to'] = timestamp_greater_than_or_equal_to
    if timestamp_less_than_or_equal_to is not None:
        kwargs['timestamp_less_than_or_equal_to'] = timestamp_less_than_or_equal_to
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.get_job_logs(
        job_id=job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('resource_manager.get_job_logs_content.command_name', 'get-job-logs-content'), help=u"""Returns the raw log file for the specified job in text format. The file includes a maximum of 100,000 log entries. \n[Command Reference](getJobLogsContent)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_job_logs_content(ctx, from_json, job_id):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.get_job_logs_content(
        job_id=job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('resource_manager.get_job_tf_config.command_name', 'get-job-tf-config'), help=u"""Returns the Terraform configuration for the specified job in zip format. If no zip file is found, returns an error. \n[Command Reference](getJobTfConfig)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_job_tf_config(ctx, from_json, file, job_id):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.get_job_tf_config(
        job_id=job_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@job_group.command(name=cli_util.override('resource_manager.get_job_tf_plan.command_name', 'get-job-tf-plan'), help=u"""Returns the output of the specified Terraform plan job in binary or JSON format. For information about running Terraform plan jobs, see [Creating Plan Jobs]. \n[Command Reference](getJobTfPlan)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--tf-plan-format', type=custom_types.CliCaseInsensitiveChoice(["BINARY", "JSON"]), help=u"""The output format of the Terraform plan.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_job_tf_plan(ctx, from_json, file, job_id, tf_plan_format):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    if tf_plan_format is not None:
        kwargs['tf_plan_format'] = tf_plan_format
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.get_job_tf_plan(
        job_id=job_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@job_group.command(name=cli_util.override('resource_manager.get_job_tf_state.command_name', 'get-job-tf-state'), help=u"""Returns the Terraform state for the specified job. \n[Command Reference](getJobTfState)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_job_tf_state(ctx, from_json, file, job_id):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.get_job_tf_state(
        job_id=job_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@private_endpoint_group.command(name=cli_util.override('resource_manager.get_private_endpoint.command_name', 'get'), help=u"""Gets the specified private endpoint. \n[Command Reference](getPrivateEndpoint)""")
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of the private endpoint.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'PrivateEndpoint'})
@cli_util.wrap_exceptions
def get_private_endpoint(ctx, from_json, private_endpoint_id):

    if isinstance(private_endpoint_id, six.string_types) and len(private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.get_private_endpoint(
        private_endpoint_id=private_endpoint_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@reachable_ip_group.command(name=cli_util.override('resource_manager.get_reachable_ip.command_name', 'get'), help=u"""Gets the reachable, or alternative, IP address for a nonpublic IP address that is associated with the private endpoint. Resource Manager uses this IP address to connect to nonpublic resources through the associated private endpoint. \n[Command Reference](getReachableIp)""")
@cli_util.option('--private-ip', required=True, help=u"""The IP address of the resource in the private subnet.""")
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of the private endpoint.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'ReachableIp'})
@cli_util.wrap_exceptions
def get_reachable_ip(ctx, from_json, private_ip, private_endpoint_id):

    if isinstance(private_endpoint_id, six.string_types) and len(private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.get_reachable_ip(
        private_ip=private_ip,
        private_endpoint_id=private_endpoint_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@stack_group.command(name=cli_util.override('resource_manager.get_stack.command_name', 'get'), help=u"""Gets the specified stack. \n[Command Reference](getStack)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def get_stack(ctx, from_json, stack_id):

    if isinstance(stack_id, six.string_types) and len(stack_id.strip()) == 0:
        raise click.UsageError('Parameter --stack-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.get_stack(
        stack_id=stack_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@stack_group.command(name=cli_util.override('resource_manager.get_stack_tf_config.command_name', 'get-stack-tf-config'), help=u"""Returns the Terraform configuration file for the specified stack in zip format. Returns an error if no zip file is found. \n[Command Reference](getStackTfConfig)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_stack_tf_config(ctx, from_json, file, stack_id):

    if isinstance(stack_id, six.string_types) and len(stack_id.strip()) == 0:
        raise click.UsageError('Parameter --stack-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.get_stack_tf_config(
        stack_id=stack_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@stack_group.command(name=cli_util.override('resource_manager.get_stack_tf_state.command_name', 'get-stack-tf-state'), help=u"""Returns the Terraform state for the specified stack. \n[Command Reference](getStackTfState)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_stack_tf_state(ctx, from_json, file, stack_id):

    if isinstance(stack_id, six.string_types) and len(stack_id.strip()) == 0:
        raise click.UsageError('Parameter --stack-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.get_stack_tf_state(
        stack_id=stack_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@template_group.command(name=cli_util.override('resource_manager.get_template.command_name', 'get'), help=u"""Gets the specified template. \n[Command Reference](getTemplate)""")
@cli_util.option('--template-id', required=True, help=u"""The [OCID] of the template.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'Template'})
@cli_util.wrap_exceptions
def get_template(ctx, from_json, template_id):

    if isinstance(template_id, six.string_types) and len(template_id.strip()) == 0:
        raise click.UsageError('Parameter --template-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.get_template(
        template_id=template_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@template_group.command(name=cli_util.override('resource_manager.get_template_logo.command_name', 'get-template-logo'), help=u"""Returns the Terraform logo file in .logo format for the specified template. Returns an error if no logo file is found. \n[Command Reference](getTemplateLogo)""")
@cli_util.option('--template-id', required=True, help=u"""The [OCID] of the template.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_template_logo(ctx, from_json, file, template_id):

    if isinstance(template_id, six.string_types) and len(template_id.strip()) == 0:
        raise click.UsageError('Parameter --template-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.get_template_logo(
        template_id=template_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@template_group.command(name=cli_util.override('resource_manager.get_template_tf_config.command_name', 'get-template-tf-config'), help=u"""Returns the Terraform configuration file in zip format for the specified template. Returns an error if no zip file is found. \n[Command Reference](getTemplateTfConfig)""")
@cli_util.option('--template-id', required=True, help=u"""The [OCID] of the template.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_template_tf_config(ctx, from_json, file, template_id):

    if isinstance(template_id, six.string_types) and len(template_id.strip()) == 0:
        raise click.UsageError('Parameter --template-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.get_template_tf_config(
        template_id=template_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@work_request_group.command(name=cli_util.override('resource_manager.get_work_request.command_name', 'get'), help=u"""Returns the specified work request. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@configuration_source_provider_summary_group.command(name=cli_util.override('resource_manager.list_configuration_source_providers.command_name', 'list-configuration-source-providers'), help=u"""Lists configuration source providers according to the specified filter. - For `compartmentId`, lists all configuration source providers in the matching compartment. - For `configurationSourceProviderId`, lists the matching configuration source provider. \n[Command Reference](listConfigurationSourceProviders)""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that exist in the compartment, identified by [OCID].""")
@cli_util.option('--configuration-source-provider-id', help=u"""A filter to return only configuration source providers that match the provided [OCID].""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly. Use this filter to list a resource by name. Requires `sortBy` set to `DISPLAYNAME`. Alternatively, when you know the resource OCID, use the related Get operation.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to use when sorting returned resources. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--config-source-provider-type', help=u"""A filter to return only configuration source providers of the specified type (GitHub or GitLab).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'ConfigurationSourceProviderCollection'})
@cli_util.wrap_exceptions
def list_configuration_source_providers(ctx, from_json, all_pages, page_size, compartment_id, configuration_source_provider_id, display_name, sort_by, sort_order, limit, page, config_source_provider_type):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if configuration_source_provider_id is not None:
        kwargs['configuration_source_provider_id'] = configuration_source_provider_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if config_source_provider_type is not None:
        kwargs['config_source_provider_type'] = config_source_provider_type
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_configuration_source_providers,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_configuration_source_providers,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_configuration_source_providers(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@associated_resource_summary_group.command(name=cli_util.override('resource_manager.list_job_associated_resources.command_name', 'list-job-associated-resources'), help=u"""Gets the list of resources associated with the specified job. \n[Command Reference](listJobAssociatedResources)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that exist in the compartment, identified by [OCID].""")
@cli_util.option('--terraform-resource-type', help=u"""A filter to return only specified resource types. For more information about resource types supported for the Oracle Cloud Infrastructure [OCI] provider, see [Oracle Cloud Infrastructure Provider].""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'AssociatedResourcesCollection'})
@cli_util.wrap_exceptions
def list_job_associated_resources(ctx, from_json, all_pages, page_size, job_id, compartment_id, terraform_resource_type, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if terraform_resource_type is not None:
        kwargs['terraform_resource_type'] = terraform_resource_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_job_associated_resources,
            job_id=job_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_job_associated_resources,
            limit,
            page_size,
            job_id=job_id,
            **kwargs
        )
    else:
        result = client.list_job_associated_resources(
            job_id=job_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@job_output_summary_group.command(name=cli_util.override('resource_manager.list_job_outputs.command_name', 'list-job-outputs'), help=u"""Gets the list of outputs associated with the specified job. \n[Command Reference](listJobOutputs)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that exist in the compartment, identified by [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'JobOutputsCollection'})
@cli_util.wrap_exceptions
def list_job_outputs(ctx, from_json, all_pages, page_size, job_id, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_job_outputs,
            job_id=job_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_job_outputs,
            limit,
            page_size,
            job_id=job_id,
            **kwargs
        )
    else:
        result = client.list_job_outputs(
            job_id=job_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('resource_manager.list_jobs.command_name', 'list'), help=u"""Lists jobs according to the specified filter. By default, the list is ordered by time created.

- To list all jobs in a stack, provide the stack [OCID]. - To list all jobs in a compartment, provide the compartment [OCID]. - To return a specific job, provide the job [OCID]. (Equivalent to [GetStack].) \n[Command Reference](listJobs)""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that exist in the compartment, identified by [OCID].""")
@cli_util.option('--stack-id', help=u"""The stack [OCID] on which to filter.""")
@cli_util.option('--id', help=u"""The [OCID] on which to query for jobs.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""A filter that returns all resources that match the specified lifecycle state. The state value is case-insensitive.

Allowable values: - ACCEPTED - IN_PROGRESS - FAILED - SUCCEEDED - CANCELING - CANCELED""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly. Use this filter to list a resource by name. Requires `sortBy` set to `DISPLAYNAME`. Alternatively, when you know the resource OCID, use the related Get operation.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to use when sorting returned resources. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'list[JobSummary]'})
@cli_util.wrap_exceptions
def list_jobs(ctx, from_json, all_pages, page_size, compartment_id, stack_id, id, lifecycle_state, display_name, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if stack_id is not None:
        kwargs['stack_id'] = stack_id
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_jobs,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_jobs,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_jobs(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@private_endpoint_summary_group.command(name=cli_util.override('resource_manager.list_private_endpoints.command_name', 'list-private-endpoints'), help=u"""Lists private endpoints according to the specified filter. - For `compartmentId`, lists all private endpoints in the matching compartment. - For `privateEndpointId`, lists the matching private endpoint. \n[Command Reference](listPrivateEndpoints)""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that exist in the compartment, identified by [OCID].""")
@cli_util.option('--private-endpoint-id', help=u"""The [OCID] of the private endpoint.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly. Use this filter to list a resource by name. Requires `sortBy` set to `DISPLAYNAME`. Alternatively, when you know the resource OCID, use the related Get operation.""")
@cli_util.option('--vcn-id', help=u"""The [OCID] of the VCN.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to use when sorting returned resources. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'PrivateEndpointCollection'})
@cli_util.wrap_exceptions
def list_private_endpoints(ctx, from_json, all_pages, page_size, compartment_id, private_endpoint_id, display_name, vcn_id, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if private_endpoint_id is not None:
        kwargs['private_endpoint_id'] = private_endpoint_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if vcn_id is not None:
        kwargs['vcn_id'] = vcn_id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_private_endpoints,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_private_endpoints,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_private_endpoints(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@stack_group.command(name=cli_util.override('resource_manager.list_resource_discovery_services.command_name', 'list-resource-discovery-services'), help=u"""Returns a list of supported services for [Resource Discovery]. For reference on service names, see the [Terraform provider documentation]. \n[Command Reference](listResourceDiscoveryServices)""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that exist in the compartment, identified by [OCID].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'ResourceDiscoveryServiceCollection'})
@cli_util.wrap_exceptions
def list_resource_discovery_services(ctx, from_json, all_pages, compartment_id):

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.list_resource_discovery_services(
        **kwargs
    )
    cli_util.render_response(result, ctx)


@associated_resource_summary_group.command(name=cli_util.override('resource_manager.list_stack_associated_resources.command_name', 'list-stack-associated-resources'), help=u"""Gets the list of resources associated with the specified stack. \n[Command Reference](listStackAssociatedResources)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack.""")
@cli_util.option('--terraform-resource-type', help=u"""A filter to return only specified resource types. For more information about resource types supported for the Oracle Cloud Infrastructure [OCI] provider, see [Oracle Cloud Infrastructure Provider].""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that exist in the compartment, identified by [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'AssociatedResourcesCollection'})
@cli_util.wrap_exceptions
def list_stack_associated_resources(ctx, from_json, all_pages, page_size, stack_id, terraform_resource_type, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(stack_id, six.string_types) and len(stack_id.strip()) == 0:
        raise click.UsageError('Parameter --stack-id cannot be whitespace or empty string')

    kwargs = {}
    if terraform_resource_type is not None:
        kwargs['terraform_resource_type'] = terraform_resource_type
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_stack_associated_resources,
            stack_id=stack_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_stack_associated_resources,
            limit,
            page_size,
            stack_id=stack_id,
            **kwargs
        )
    else:
        result = client.list_stack_associated_resources(
            stack_id=stack_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@stack_resource_drift_summary_group.command(name=cli_util.override('resource_manager.list_stack_resource_drift_details.command_name', 'list-stack-resource-drift-details'), help=u"""Lists drift status details for each resource defined in the specified stack. The drift status details for a given resource indicate differences, if any, between the actual state and the expected (defined) state for that resource. The drift status details correspond to the specified work request (`workRequestId`). If no work request is specified, then the drift status details correspond to the latest completed work request for the stack. \n[Command Reference](listStackResourceDriftDetails)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack.""")
@cli_util.option('--work-request-id', help=u"""The [OCID] of the work request.""")
@cli_util.option('--resource-drift-status', type=custom_types.CliCaseInsensitiveChoice(["NOT_CHECKED", "IN_SYNC", "MODIFIED", "DELETED"]), multiple=True, help=u"""A filter that returns only resources that match the given drift status. The value is case-insensitive. Allowable values -   - NOT_CHECKED   - MODIFIED   - IN_SYNC   - DELETED""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'StackResourceDriftCollection'})
@cli_util.wrap_exceptions
def list_stack_resource_drift_details(ctx, from_json, all_pages, page_size, stack_id, work_request_id, resource_drift_status, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(stack_id, six.string_types) and len(stack_id.strip()) == 0:
        raise click.UsageError('Parameter --stack-id cannot be whitespace or empty string')

    kwargs = {}
    if work_request_id is not None:
        kwargs['work_request_id'] = work_request_id
    if resource_drift_status is not None and len(resource_drift_status) > 0:
        kwargs['resource_drift_status'] = resource_drift_status
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_stack_resource_drift_details,
            stack_id=stack_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_stack_resource_drift_details,
            limit,
            page_size,
            stack_id=stack_id,
            **kwargs
        )
    else:
        result = client.list_stack_resource_drift_details(
            stack_id=stack_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@stack_group.command(name=cli_util.override('resource_manager.list_stacks.command_name', 'list'), help=u"""Lists stacks according to the specified filter. - If called using the compartment ID, returns all stacks in the specified compartment. - If called using the stack ID, returns the specified stack. (See also [GetStack].) \n[Command Reference](listStacks)""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that exist in the compartment, identified by [OCID].""")
@cli_util.option('--id', help=u"""The [OCID] on which to query for a stack.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter that returns only those resources that match the specified lifecycle state. The state value is case-insensitive. For more information about stack lifecycle states, see [Key Concepts].

Allowable values: - CREATING - ACTIVE - DELETING - DELETED - FAILED""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly. Use this filter to list a resource by name. Requires `sortBy` set to `DISPLAYNAME`. Alternatively, when you know the resource OCID, use the related Get operation.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to use when sorting returned resources. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'list[StackSummary]'})
@cli_util.wrap_exceptions
def list_stacks(ctx, from_json, all_pages, page_size, compartment_id, id, lifecycle_state, display_name, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_stacks,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_stacks,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_stacks(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@template_category_summary_group.command(name=cli_util.override('resource_manager.list_template_categories.command_name', 'list-template-categories'), help=u"""Lists template categories. \n[Command Reference](listTemplateCategories)""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'TemplateCategorySummaryCollection'})
@cli_util.wrap_exceptions
def list_template_categories(ctx, from_json, all_pages, ):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.list_template_categories(
        **kwargs
    )
    cli_util.render_response(result, ctx)


@template_group.command(name=cli_util.override('resource_manager.list_templates.command_name', 'list'), help=u"""Lists templates according to the specified filter. The attributes `compartmentId` and `templateCategoryId` are required unless `templateId` is specified. \n[Command Reference](listTemplates)""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that exist in the compartment, identified by [OCID].""")
@cli_util.option('--template-category-id', help=u"""Unique identifier for the template category. Possible values are `0` (Quickstarts), `1` (Service), `2` (Architecture), and `3` (Private). Template category labels are displayed in the Console page listing templates. Quickstarts, Service, and Architecture templates (categories 0, 1, and 2) are available in all compartments. Each private template (category 3) is available in the compartment where it was created.""")
@cli_util.option('--template-id', help=u"""The [OCID] of the template.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly. Use this filter to list a resource by name. Requires `sortBy` set to `DISPLAYNAME`. Alternatively, when you know the resource OCID, use the related Get operation.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to use when sorting returned resources. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'TemplateSummaryCollection'})
@cli_util.wrap_exceptions
def list_templates(ctx, from_json, all_pages, page_size, compartment_id, template_category_id, template_id, display_name, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if template_category_id is not None:
        kwargs['template_category_id'] = template_category_id
    if template_id is not None:
        kwargs['template_id'] = template_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_templates,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_templates,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_templates(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@stack_group.command(name=cli_util.override('resource_manager.list_terraform_versions.command_name', 'list-terraform-versions'), help=u"""Returns a list of supported Terraform versions for use with stacks. \n[Command Reference](listTerraformVersions)""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that exist in the compartment, identified by [OCID].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'TerraformVersionCollection'})
@cli_util.wrap_exceptions
def list_terraform_versions(ctx, from_json, all_pages, compartment_id):

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.list_terraform_versions(
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('resource_manager.list_work_request_errors.command_name', 'list-work-request-errors'), help=u"""Returns a paginated list of errors for the specified work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that exist in the compartment, identified by [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, compartment_id, limit, page, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
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


@work_request_group.command(name=cli_util.override('resource_manager.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Returns a paginated list of logs for the specified work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that exist in the compartment, identified by [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use when sorting returned resources. Ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'list[WorkRequestLogEntry]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, compartment_id, limit, page, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
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


@work_request_group.command(name=cli_util.override('resource_manager.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in the specified compartment or for the specified resource. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""A filter to return only resources that exist in the compartment, identified by [OCID].""")
@cli_util.option('--resource-id', help=u"""The [OCID] of the resource.""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_manager', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, resource_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@configuration_source_provider_group.command(name=cli_util.override('resource_manager.update_configuration_source_provider.command_name', 'update'), help=u"""Updates the properties of the specified configuration source provider. For more information, see [To edit a configuration source provider]. \n[Command Reference](updateConfigurationSourceProvider)""")
@cli_util.option('--configuration-source-provider-id', required=True, help=u"""The [OCID] of the configuration source provider.""")
@cli_util.option('--display-name', help=u"""Human-readable name of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Description of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--config-source-provider-type', help=u"""The type of configuration source provider. The `BITBUCKET_CLOUD_USERNAME_APPPASSWORD` type corresponds to Bitbucket Cloud. The `BITBUCKET_SERVER_ACCESS_TOKEN` type corresponds to Bitbucket Server. The `GITLAB_ACCESS_TOKEN` type corresponds to GitLab. The `GITHUB_ACCESS_TOKEN` type corresponds to GitHub.""")
@cli_util.option('--private-server-config-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'ConfigurationSourceProvider'})
@cli_util.wrap_exceptions
def update_configuration_source_provider(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, configuration_source_provider_id, display_name, description, config_source_provider_type, private_server_config_details, freeform_tags, defined_tags, if_match):

    if isinstance(configuration_source_provider_id, six.string_types) and len(configuration_source_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --configuration-source-provider-id cannot be whitespace or empty string')
    if not force:
        if private_server_config_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to private-server-config-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if config_source_provider_type is not None:
        _details['configSourceProviderType'] = config_source_provider_type

    if private_server_config_details is not None:
        _details['privateServerConfigDetails'] = cli_util.parse_json_parameter("private_server_config_details", private_server_config_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.update_configuration_source_provider(
        configuration_source_provider_id=configuration_source_provider_id,
        update_configuration_source_provider_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_configuration_source_provider') and callable(getattr(client, 'get_configuration_source_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_configuration_source_provider(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@configuration_source_provider_group.command(name=cli_util.override('resource_manager.update_configuration_source_provider_update_bitbucket_cloud_username_app_password_configuration_source_provider_details.command_name', 'update-configuration-source-provider-update-bitbucket-cloud-username-app-password-configuration-source-provider-details'), help=u"""Updates the properties of the specified configuration source provider. For more information, see [To edit a configuration source provider]. \n[Command Reference](updateConfigurationSourceProvider)""")
@cli_util.option('--configuration-source-provider-id', required=True, help=u"""The [OCID] of the configuration source provider.""")
@cli_util.option('--display-name', help=u"""Human-readable name of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Description of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--private-server-config-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--api-endpoint', help=u"""The Bitbucket service endpoint. Example: `https://bitbucket.org/`""")
@cli_util.option('--username', help=u"""The username for the user of the Bitbucket cloud repository.""")
@cli_util.option('--secret-id', help=u"""The secret ocid which is used to authorize the user.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'ConfigurationSourceProvider'})
@cli_util.wrap_exceptions
def update_configuration_source_provider_update_bitbucket_cloud_username_app_password_configuration_source_provider_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, configuration_source_provider_id, display_name, description, private_server_config_details, freeform_tags, defined_tags, api_endpoint, username, secret_id, if_match):

    if isinstance(configuration_source_provider_id, six.string_types) and len(configuration_source_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --configuration-source-provider-id cannot be whitespace or empty string')
    if not force:
        if private_server_config_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to private-server-config-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if private_server_config_details is not None:
        _details['privateServerConfigDetails'] = cli_util.parse_json_parameter("private_server_config_details", private_server_config_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if api_endpoint is not None:
        _details['apiEndpoint'] = api_endpoint

    if username is not None:
        _details['username'] = username

    if secret_id is not None:
        _details['secretId'] = secret_id

    _details['configSourceProviderType'] = 'BITBUCKET_CLOUD_USERNAME_APPPASSWORD'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.update_configuration_source_provider(
        configuration_source_provider_id=configuration_source_provider_id,
        update_configuration_source_provider_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_configuration_source_provider') and callable(getattr(client, 'get_configuration_source_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_configuration_source_provider(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@configuration_source_provider_group.command(name=cli_util.override('resource_manager.update_configuration_source_provider_update_bitbucket_server_access_token_configuration_source_provider_details.command_name', 'update-configuration-source-provider-update-bitbucket-server-access-token-configuration-source-provider-details'), help=u"""Updates the properties of the specified configuration source provider. For more information, see [To edit a configuration source provider]. \n[Command Reference](updateConfigurationSourceProvider)""")
@cli_util.option('--configuration-source-provider-id', required=True, help=u"""The [OCID] of the configuration source provider.""")
@cli_util.option('--display-name', help=u"""Human-readable name of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Description of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--private-server-config-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--secret-id', help=u"""The secret ocid which is used to authorize the user.""")
@cli_util.option('--api-endpoint', help=u"""The Bitbucket server service endpoint Example: `https://bitbucket.org/`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'ConfigurationSourceProvider'})
@cli_util.wrap_exceptions
def update_configuration_source_provider_update_bitbucket_server_access_token_configuration_source_provider_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, configuration_source_provider_id, display_name, description, private_server_config_details, freeform_tags, defined_tags, secret_id, api_endpoint, if_match):

    if isinstance(configuration_source_provider_id, six.string_types) and len(configuration_source_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --configuration-source-provider-id cannot be whitespace or empty string')
    if not force:
        if private_server_config_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to private-server-config-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if private_server_config_details is not None:
        _details['privateServerConfigDetails'] = cli_util.parse_json_parameter("private_server_config_details", private_server_config_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if secret_id is not None:
        _details['secretId'] = secret_id

    if api_endpoint is not None:
        _details['apiEndpoint'] = api_endpoint

    _details['configSourceProviderType'] = 'BITBUCKET_SERVER_ACCESS_TOKEN'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.update_configuration_source_provider(
        configuration_source_provider_id=configuration_source_provider_id,
        update_configuration_source_provider_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_configuration_source_provider') and callable(getattr(client, 'get_configuration_source_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_configuration_source_provider(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@configuration_source_provider_group.command(name=cli_util.override('resource_manager.update_configuration_source_provider_update_gitlab_access_token_configuration_source_provider_details.command_name', 'update-configuration-source-provider-update-gitlab-access-token-configuration-source-provider-details'), help=u"""Updates the properties of the specified configuration source provider. For more information, see [To edit a configuration source provider]. \n[Command Reference](updateConfigurationSourceProvider)""")
@cli_util.option('--configuration-source-provider-id', required=True, help=u"""The [OCID] of the configuration source provider.""")
@cli_util.option('--display-name', help=u"""Human-readable name of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Description of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--private-server-config-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--api-endpoint', help=u"""The Git service endpoint. Example: `https://gitlab.com`""")
@cli_util.option('--access-token', help=u"""The personal access token to be configured on the GitLab repository.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'ConfigurationSourceProvider'})
@cli_util.wrap_exceptions
def update_configuration_source_provider_update_gitlab_access_token_configuration_source_provider_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, configuration_source_provider_id, display_name, description, private_server_config_details, freeform_tags, defined_tags, api_endpoint, access_token, if_match):

    if isinstance(configuration_source_provider_id, six.string_types) and len(configuration_source_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --configuration-source-provider-id cannot be whitespace or empty string')
    if not force:
        if private_server_config_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to private-server-config-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if private_server_config_details is not None:
        _details['privateServerConfigDetails'] = cli_util.parse_json_parameter("private_server_config_details", private_server_config_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if api_endpoint is not None:
        _details['apiEndpoint'] = api_endpoint

    if access_token is not None:
        _details['accessToken'] = access_token

    _details['configSourceProviderType'] = 'GITLAB_ACCESS_TOKEN'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.update_configuration_source_provider(
        configuration_source_provider_id=configuration_source_provider_id,
        update_configuration_source_provider_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_configuration_source_provider') and callable(getattr(client, 'get_configuration_source_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_configuration_source_provider(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@configuration_source_provider_group.command(name=cli_util.override('resource_manager.update_configuration_source_provider_update_github_access_token_configuration_source_provider_details.command_name', 'update-configuration-source-provider-update-github-access-token-configuration-source-provider-details'), help=u"""Updates the properties of the specified configuration source provider. For more information, see [To edit a configuration source provider]. \n[Command Reference](updateConfigurationSourceProvider)""")
@cli_util.option('--configuration-source-provider-id', required=True, help=u"""The [OCID] of the configuration source provider.""")
@cli_util.option('--display-name', help=u"""Human-readable name of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Description of the configuration source provider. Avoid entering confidential information.""")
@cli_util.option('--private-server-config-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--api-endpoint', help=u"""The GitHub service endpoint. Example: `https://github.com/`""")
@cli_util.option('--access-token', help=u"""The personal access token to be configured on the GitHub repository.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'private-server-config-details': {'module': 'resource_manager', 'class': 'PrivateServerConfigDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'ConfigurationSourceProvider'})
@cli_util.wrap_exceptions
def update_configuration_source_provider_update_github_access_token_configuration_source_provider_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, configuration_source_provider_id, display_name, description, private_server_config_details, freeform_tags, defined_tags, api_endpoint, access_token, if_match):

    if isinstance(configuration_source_provider_id, six.string_types) and len(configuration_source_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --configuration-source-provider-id cannot be whitespace or empty string')
    if not force:
        if private_server_config_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to private-server-config-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if private_server_config_details is not None:
        _details['privateServerConfigDetails'] = cli_util.parse_json_parameter("private_server_config_details", private_server_config_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if api_endpoint is not None:
        _details['apiEndpoint'] = api_endpoint

    if access_token is not None:
        _details['accessToken'] = access_token

    _details['configSourceProviderType'] = 'GITHUB_ACCESS_TOKEN'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.update_configuration_source_provider(
        configuration_source_provider_id=configuration_source_provider_id,
        update_configuration_source_provider_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_configuration_source_provider') and callable(getattr(client, 'get_configuration_source_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_configuration_source_provider(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('resource_manager.update_job.command_name', 'update'), help=u"""Updates the specified job. \n[Command Reference](updateJob)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@cli_util.option('--display-name', help=u"""The new display name to set.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Job'})
@cli_util.wrap_exceptions
def update_job(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, job_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')
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

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.update_job(
        job_id=job_id,
        update_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@private_endpoint_group.command(name=cli_util.override('resource_manager.update_private_endpoint.command_name', 'update'), help=u"""Updates the specified private endpoint. \n[Command Reference](updatePrivateEndpoint)""")
@cli_util.option('--private-endpoint-id', required=True, help=u"""The [OCID] of the private endpoint.""")
@cli_util.option('--display-name', help=u"""The private endpoint display name. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Description of the private endpoint. Avoid entering confidential information.""")
@cli_util.option('--vcn-id', help=u"""The [OCID] of the VCN for the private endpoint.""")
@cli_util.option('--subnet-id', help=u"""The [OCID] of the subnet within the VCN for the private endpoint.""")
@cli_util.option('--dns-zones', type=custom_types.CLI_COMPLEX_TYPE, help=u"""DNS Proxy forwards any DNS FQDN queries over into the consumer DNS resolver if the DNS FQDN is included in the dns zones list otherwise it goes to service provider VCN resolver.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--nsg-id-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The [OCIDs] of [network security groups (NSGs)] for the private endpoint. Order does not matter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-used-with-configuration-source-provider', type=click.BOOL, help=u"""When `true`, allows the private endpoint to be used with a configuration source provider.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'dns-zones': {'module': 'resource_manager', 'class': 'list[string]'}, 'nsg-id-list': {'module': 'resource_manager', 'class': 'list[string]'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dns-zones': {'module': 'resource_manager', 'class': 'list[string]'}, 'nsg-id-list': {'module': 'resource_manager', 'class': 'list[string]'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'PrivateEndpoint'})
@cli_util.wrap_exceptions
def update_private_endpoint(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, private_endpoint_id, display_name, description, vcn_id, subnet_id, dns_zones, nsg_id_list, is_used_with_configuration_source_provider, freeform_tags, defined_tags, if_match):

    if isinstance(private_endpoint_id, six.string_types) and len(private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --private-endpoint-id cannot be whitespace or empty string')
    if not force:
        if dns_zones or nsg_id_list or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to dns-zones and nsg-id-list and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if vcn_id is not None:
        _details['vcnId'] = vcn_id

    if subnet_id is not None:
        _details['subnetId'] = subnet_id

    if dns_zones is not None:
        _details['dnsZones'] = cli_util.parse_json_parameter("dns_zones", dns_zones)

    if nsg_id_list is not None:
        _details['nsgIdList'] = cli_util.parse_json_parameter("nsg_id_list", nsg_id_list)

    if is_used_with_configuration_source_provider is not None:
        _details['isUsedWithConfigurationSourceProvider'] = is_used_with_configuration_source_provider

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.update_private_endpoint(
        private_endpoint_id=private_endpoint_id,
        update_private_endpoint_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_private_endpoint') and callable(getattr(client, 'get_private_endpoint')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_private_endpoint(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@stack_group.command(name=cli_util.override('resource_manager.update_stack.command_name', 'update'), help=u"""Updates the specified stack. Use `UpdateStack` when you update your Terraform configuration and want your changes to be reflected in the execution plan. For more information, see [Updating Stacks]. \n[Command Reference](updateStack)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack.""")
@cli_util.option('--display-name', help=u"""The name of the stack.""")
@cli_util.option('--description', help=u"""Description of the stack.""")
@cli_util.option('--config-source', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--custom-terraform-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-third-party-provider-experience-enabled', type=click.BOOL, help=u"""When `true`, changes the stack's sourcing of third-party Terraform providers to [Terraform Registry] and allows [custom providers]. Applies to older stacks. Once set to `true`, cannot be reverted. For more information about stack sourcing of third-party Terraform providers, see [Third-party Provider Configuration].""")
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Terraform variables associated with this resource. The maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--terraform-version', help=u"""The version of Terraform to use with the stack. Example: `0.12.x`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'config-source': {'module': 'resource_manager', 'class': 'UpdateConfigSourceDetails'}, 'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'config-source': {'module': 'resource_manager', 'class': 'UpdateConfigSourceDetails'}, 'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def update_stack(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, stack_id, display_name, description, config_source, custom_terraform_provider, is_third_party_provider_experience_enabled, variables, terraform_version, freeform_tags, defined_tags, if_match):

    if isinstance(stack_id, six.string_types) and len(stack_id.strip()) == 0:
        raise click.UsageError('Parameter --stack-id cannot be whitespace or empty string')
    if not force:
        if config_source or custom_terraform_provider or variables or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to config-source and custom-terraform-provider and variables and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if config_source is not None:
        _details['configSource'] = cli_util.parse_json_parameter("config_source", config_source)

    if custom_terraform_provider is not None:
        _details['customTerraformProvider'] = cli_util.parse_json_parameter("custom_terraform_provider", custom_terraform_provider)

    if is_third_party_provider_experience_enabled is not None:
        _details['isThirdPartyProviderExperienceEnabled'] = is_third_party_provider_experience_enabled

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if terraform_version is not None:
        _details['terraformVersion'] = terraform_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.update_stack(
        stack_id=stack_id,
        update_stack_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stack') and callable(getattr(client, 'get_stack')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stack(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@stack_group.command(name=cli_util.override('resource_manager.update_stack_update_bitbucket_cloud_config_source_details.command_name', 'update-stack-update-bitbucket-cloud-config-source-details'), help=u"""Updates the specified stack. Use `UpdateStack` when you update your Terraform configuration and want your changes to be reflected in the execution plan. For more information, see [Updating Stacks]. \n[Command Reference](updateStack)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack.""")
@cli_util.option('--config-source-configuration-source-provider-id', required=True, help=u"""The [OCID] of the Bitbucket Cloud configuration source.""")
@cli_util.option('--display-name', help=u"""The name of the stack.""")
@cli_util.option('--description', help=u"""Description of the stack.""")
@cli_util.option('--custom-terraform-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-third-party-provider-experience-enabled', type=click.BOOL, help=u"""When `true`, changes the stack's sourcing of third-party Terraform providers to [Terraform Registry] and allows [custom providers]. Applies to older stacks. Once set to `true`, cannot be reverted. For more information about stack sourcing of third-party Terraform providers, see [Third-party Provider Configuration].""")
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Terraform variables associated with this resource. The maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--terraform-version', help=u"""The version of Terraform to use with the stack. Example: `0.12.x`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--config-source-working-directory', help=u"""File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see [File Structure (Terraform Configurations for Resource Manager)].""")
@cli_util.option('--config-source-repository-url', help=u"""The URL of the Bitbucket Cloud repository for the configuration source.""")
@cli_util.option('--config-source-branch-name', help=u"""The name of the branch in the Bitbucket Cloud repository for the configuration source.""")
@cli_util.option('--config-source-workspace-id', help=u"""The id of the workspace in Bitbucket Cloud for the configuration source""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def update_stack_update_bitbucket_cloud_config_source_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, stack_id, config_source_configuration_source_provider_id, display_name, description, custom_terraform_provider, is_third_party_provider_experience_enabled, variables, terraform_version, freeform_tags, defined_tags, if_match, config_source_working_directory, config_source_repository_url, config_source_branch_name, config_source_workspace_id):

    if isinstance(stack_id, six.string_types) and len(stack_id.strip()) == 0:
        raise click.UsageError('Parameter --stack-id cannot be whitespace or empty string')
    if not force:
        if custom_terraform_provider or variables or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to custom-terraform-provider and variables and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configSource'] = {}
    _details['configSource']['configurationSourceProviderId'] = config_source_configuration_source_provider_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if custom_terraform_provider is not None:
        _details['customTerraformProvider'] = cli_util.parse_json_parameter("custom_terraform_provider", custom_terraform_provider)

    if is_third_party_provider_experience_enabled is not None:
        _details['isThirdPartyProviderExperienceEnabled'] = is_third_party_provider_experience_enabled

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if terraform_version is not None:
        _details['terraformVersion'] = terraform_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config_source_working_directory is not None:
        _details['configSource']['workingDirectory'] = config_source_working_directory

    if config_source_repository_url is not None:
        _details['configSource']['repositoryUrl'] = config_source_repository_url

    if config_source_branch_name is not None:
        _details['configSource']['branchName'] = config_source_branch_name

    if config_source_workspace_id is not None:
        _details['configSource']['workspaceId'] = config_source_workspace_id

    _details['configSource']['configSourceType'] = 'BITBUCKET_CLOUD_CONFIG_SOURCE'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.update_stack(
        stack_id=stack_id,
        update_stack_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stack') and callable(getattr(client, 'get_stack')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stack(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@stack_group.command(name=cli_util.override('resource_manager.update_stack_update_bitbucket_server_config_source_details.command_name', 'update-stack-update-bitbucket-server-config-source-details'), help=u"""Updates the specified stack. Use `UpdateStack` when you update your Terraform configuration and want your changes to be reflected in the execution plan. For more information, see [Updating Stacks]. \n[Command Reference](updateStack)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack.""")
@cli_util.option('--config-source-configuration-source-provider-id', required=True, help=u"""Unique identifier ([OCID]) for the Bitbucket Server configuration source.""")
@cli_util.option('--display-name', help=u"""The name of the stack.""")
@cli_util.option('--description', help=u"""Description of the stack.""")
@cli_util.option('--custom-terraform-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-third-party-provider-experience-enabled', type=click.BOOL, help=u"""When `true`, changes the stack's sourcing of third-party Terraform providers to [Terraform Registry] and allows [custom providers]. Applies to older stacks. Once set to `true`, cannot be reverted. For more information about stack sourcing of third-party Terraform providers, see [Third-party Provider Configuration].""")
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Terraform variables associated with this resource. The maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--terraform-version', help=u"""The version of Terraform to use with the stack. Example: `0.12.x`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--config-source-working-directory', help=u"""File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see [File Structure (Terraform Configurations for Resource Manager)].""")
@cli_util.option('--config-source-repository-url', help=u"""The URL of the Bitbucket Server repository.""")
@cli_util.option('--config-source-branch-name', help=u"""The name of the branch within the Bitbucket Server repository.""")
@cli_util.option('--config-source-project-id', help=u"""Unique identifier for a Bitbucket Server project.""")
@cli_util.option('--config-source-repository-id', help=u"""Bitbucket Server repository identifier, usually identified as <repository>.git.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def update_stack_update_bitbucket_server_config_source_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, stack_id, config_source_configuration_source_provider_id, display_name, description, custom_terraform_provider, is_third_party_provider_experience_enabled, variables, terraform_version, freeform_tags, defined_tags, if_match, config_source_working_directory, config_source_repository_url, config_source_branch_name, config_source_project_id, config_source_repository_id):

    if isinstance(stack_id, six.string_types) and len(stack_id.strip()) == 0:
        raise click.UsageError('Parameter --stack-id cannot be whitespace or empty string')
    if not force:
        if custom_terraform_provider or variables or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to custom-terraform-provider and variables and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configSource'] = {}
    _details['configSource']['configurationSourceProviderId'] = config_source_configuration_source_provider_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if custom_terraform_provider is not None:
        _details['customTerraformProvider'] = cli_util.parse_json_parameter("custom_terraform_provider", custom_terraform_provider)

    if is_third_party_provider_experience_enabled is not None:
        _details['isThirdPartyProviderExperienceEnabled'] = is_third_party_provider_experience_enabled

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if terraform_version is not None:
        _details['terraformVersion'] = terraform_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config_source_working_directory is not None:
        _details['configSource']['workingDirectory'] = config_source_working_directory

    if config_source_repository_url is not None:
        _details['configSource']['repositoryUrl'] = config_source_repository_url

    if config_source_branch_name is not None:
        _details['configSource']['branchName'] = config_source_branch_name

    if config_source_project_id is not None:
        _details['configSource']['projectId'] = config_source_project_id

    if config_source_repository_id is not None:
        _details['configSource']['repositoryId'] = config_source_repository_id

    _details['configSource']['configSourceType'] = 'BITBUCKET_SERVER_CONFIG_SOURCE'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.update_stack(
        stack_id=stack_id,
        update_stack_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stack') and callable(getattr(client, 'get_stack')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stack(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@stack_group.command(name=cli_util.override('resource_manager.update_stack_update_git_config_source_details.command_name', 'update-stack-update-git-config-source-details'), help=u"""Updates the specified stack. Use `UpdateStack` when you update your Terraform configuration and want your changes to be reflected in the execution plan. For more information, see [Updating Stacks]. \n[Command Reference](updateStack)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack.""")
@cli_util.option('--config-source-configuration-source-provider-id', required=True, help=u"""Unique identifier ([OCID]) for the Git configuration source.""")
@cli_util.option('--display-name', help=u"""The name of the stack.""")
@cli_util.option('--description', help=u"""Description of the stack.""")
@cli_util.option('--custom-terraform-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-third-party-provider-experience-enabled', type=click.BOOL, help=u"""When `true`, changes the stack's sourcing of third-party Terraform providers to [Terraform Registry] and allows [custom providers]. Applies to older stacks. Once set to `true`, cannot be reverted. For more information about stack sourcing of third-party Terraform providers, see [Third-party Provider Configuration].""")
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Terraform variables associated with this resource. The maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--terraform-version', help=u"""The version of Terraform to use with the stack. Example: `0.12.x`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--config-source-working-directory', help=u"""File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see [File Structure (Terraform Configurations for Resource Manager)].""")
@cli_util.option('--config-source-repository-url', help=u"""The URL of the Git repository.""")
@cli_util.option('--config-source-branch-name', help=u"""The name of the branch within the Git repository.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def update_stack_update_git_config_source_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, stack_id, config_source_configuration_source_provider_id, display_name, description, custom_terraform_provider, is_third_party_provider_experience_enabled, variables, terraform_version, freeform_tags, defined_tags, if_match, config_source_working_directory, config_source_repository_url, config_source_branch_name):

    if isinstance(stack_id, six.string_types) and len(stack_id.strip()) == 0:
        raise click.UsageError('Parameter --stack-id cannot be whitespace or empty string')
    if not force:
        if custom_terraform_provider or variables or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to custom-terraform-provider and variables and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configSource'] = {}
    _details['configSource']['configurationSourceProviderId'] = config_source_configuration_source_provider_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if custom_terraform_provider is not None:
        _details['customTerraformProvider'] = cli_util.parse_json_parameter("custom_terraform_provider", custom_terraform_provider)

    if is_third_party_provider_experience_enabled is not None:
        _details['isThirdPartyProviderExperienceEnabled'] = is_third_party_provider_experience_enabled

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if terraform_version is not None:
        _details['terraformVersion'] = terraform_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config_source_working_directory is not None:
        _details['configSource']['workingDirectory'] = config_source_working_directory

    if config_source_repository_url is not None:
        _details['configSource']['repositoryUrl'] = config_source_repository_url

    if config_source_branch_name is not None:
        _details['configSource']['branchName'] = config_source_branch_name

    _details['configSource']['configSourceType'] = 'GIT_CONFIG_SOURCE'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.update_stack(
        stack_id=stack_id,
        update_stack_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stack') and callable(getattr(client, 'get_stack')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stack(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@stack_group.command(name=cli_util.override('resource_manager.update_stack_update_object_storage_config_source_details.command_name', 'update-stack-update-object-storage-config-source-details'), help=u"""Updates the specified stack. Use `UpdateStack` when you update your Terraform configuration and want your changes to be reflected in the execution plan. For more information, see [Updating Stacks]. \n[Command Reference](updateStack)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack.""")
@cli_util.option('--display-name', help=u"""The name of the stack.""")
@cli_util.option('--description', help=u"""Description of the stack.""")
@cli_util.option('--custom-terraform-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-third-party-provider-experience-enabled', type=click.BOOL, help=u"""When `true`, changes the stack's sourcing of third-party Terraform providers to [Terraform Registry] and allows [custom providers]. Applies to older stacks. Once set to `true`, cannot be reverted. For more information about stack sourcing of third-party Terraform providers, see [Third-party Provider Configuration].""")
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Terraform variables associated with this resource. The maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--terraform-version', help=u"""The version of Terraform to use with the stack. Example: `0.12.x`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--config-source-working-directory', help=u"""File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see [File Structure (Terraform Configurations for Resource Manager)].""")
@cli_util.option('--config-source-region', help=u"""The name of the bucket's region. Example: `us-phoenix-1`""")
@cli_util.option('--config-source-namespace', help=u"""The Object Storage namespace that contains the bucket.""")
@cli_util.option('--config-source-bucket-name', help=u"""The name of the bucket that contains the Terraform configuration files.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def update_stack_update_object_storage_config_source_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, stack_id, display_name, description, custom_terraform_provider, is_third_party_provider_experience_enabled, variables, terraform_version, freeform_tags, defined_tags, if_match, config_source_working_directory, config_source_region, config_source_namespace, config_source_bucket_name):

    if isinstance(stack_id, six.string_types) and len(stack_id.strip()) == 0:
        raise click.UsageError('Parameter --stack-id cannot be whitespace or empty string')
    if not force:
        if custom_terraform_provider or variables or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to custom-terraform-provider and variables and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configSource'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if custom_terraform_provider is not None:
        _details['customTerraformProvider'] = cli_util.parse_json_parameter("custom_terraform_provider", custom_terraform_provider)

    if is_third_party_provider_experience_enabled is not None:
        _details['isThirdPartyProviderExperienceEnabled'] = is_third_party_provider_experience_enabled

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if terraform_version is not None:
        _details['terraformVersion'] = terraform_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config_source_working_directory is not None:
        _details['configSource']['workingDirectory'] = config_source_working_directory

    if config_source_region is not None:
        _details['configSource']['region'] = config_source_region

    if config_source_namespace is not None:
        _details['configSource']['namespace'] = config_source_namespace

    if config_source_bucket_name is not None:
        _details['configSource']['bucketName'] = config_source_bucket_name

    _details['configSource']['configSourceType'] = 'OBJECT_STORAGE_CONFIG_SOURCE'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.update_stack(
        stack_id=stack_id,
        update_stack_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stack') and callable(getattr(client, 'get_stack')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stack(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@stack_group.command(name=cli_util.override('resource_manager.update_stack_update_zip_upload_config_source_details.command_name', 'update-stack-update-zip-upload-config-source-details'), help=u"""Updates the specified stack. Use `UpdateStack` when you update your Terraform configuration and want your changes to be reflected in the execution plan. For more information, see [Updating Stacks]. \n[Command Reference](updateStack)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack.""")
@cli_util.option('--display-name', help=u"""The name of the stack.""")
@cli_util.option('--description', help=u"""Description of the stack.""")
@cli_util.option('--custom-terraform-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-third-party-provider-experience-enabled', type=click.BOOL, help=u"""When `true`, changes the stack's sourcing of third-party Terraform providers to [Terraform Registry] and allows [custom providers]. Applies to older stacks. Once set to `true`, cannot be reverted. For more information about stack sourcing of third-party Terraform providers, see [Third-party Provider Configuration].""")
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Terraform variables associated with this resource. The maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--terraform-version', help=u"""The version of Terraform to use with the stack. Example: `0.12.x`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--config-source-working-directory', help=u"""File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see [File Structure (Terraform Configurations for Resource Manager)].""")
@cli_util.option('--config-source-zip-file-base64-encoded', help=u"""""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def update_stack_update_zip_upload_config_source_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, stack_id, display_name, description, custom_terraform_provider, is_third_party_provider_experience_enabled, variables, terraform_version, freeform_tags, defined_tags, if_match, config_source_working_directory, config_source_zip_file_base64_encoded):

    if isinstance(stack_id, six.string_types) and len(stack_id.strip()) == 0:
        raise click.UsageError('Parameter --stack-id cannot be whitespace or empty string')
    if not force:
        if custom_terraform_provider or variables or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to custom-terraform-provider and variables and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configSource'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if custom_terraform_provider is not None:
        _details['customTerraformProvider'] = cli_util.parse_json_parameter("custom_terraform_provider", custom_terraform_provider)

    if is_third_party_provider_experience_enabled is not None:
        _details['isThirdPartyProviderExperienceEnabled'] = is_third_party_provider_experience_enabled

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if terraform_version is not None:
        _details['terraformVersion'] = terraform_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config_source_working_directory is not None:
        _details['configSource']['workingDirectory'] = config_source_working_directory

    if config_source_zip_file_base64_encoded is not None:
        _details['configSource']['zipFileBase64Encoded'] = config_source_zip_file_base64_encoded

    _details['configSource']['configSourceType'] = 'ZIP_UPLOAD'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.update_stack(
        stack_id=stack_id,
        update_stack_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stack') and callable(getattr(client, 'get_stack')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stack(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@stack_group.command(name=cli_util.override('resource_manager.update_stack_update_dev_ops_config_source_details.command_name', 'update-stack-update-dev-ops-config-source-details'), help=u"""Updates the specified stack. Use `UpdateStack` when you update your Terraform configuration and want your changes to be reflected in the execution plan. For more information, see [Updating Stacks]. \n[Command Reference](updateStack)""")
@cli_util.option('--stack-id', required=True, help=u"""The [OCID] of the stack.""")
@cli_util.option('--config-source-project-id', required=True, help=u"""The [OCID] of the [DevOps project].""")
@cli_util.option('--config-source-repository-id', required=True, help=u"""The [OCID] of the [DevOps repository].""")
@cli_util.option('--display-name', help=u"""The name of the stack.""")
@cli_util.option('--description', help=u"""Description of the stack.""")
@cli_util.option('--custom-terraform-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-third-party-provider-experience-enabled', type=click.BOOL, help=u"""When `true`, changes the stack's sourcing of third-party Terraform providers to [Terraform Registry] and allows [custom providers]. Applies to older stacks. Once set to `true`, cannot be reverted. For more information about stack sourcing of third-party Terraform providers, see [Third-party Provider Configuration].""")
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Terraform variables associated with this resource. The maximum number of variables supported is 250. The maximum size of each variable, including both name and value, is 8192 bytes. Example: `{\"CompartmentId\": \"compartment-id-value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--terraform-version', help=u"""The version of Terraform to use with the stack. Example: `0.12.x`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--config-source-working-directory', help=u"""File path to the directory to use for running Terraform. If not specified, the root directory is used. Required when using a zip Terraform configuration (`configSourceType` value of `ZIP_UPLOAD`) that contains folders. Ignored for the `configSourceType` value of `COMPARTMENT_CONFIG_SOURCE`. For more information about required and recommended file structure, see [File Structure (Terraform Configurations for Resource Manager)].""")
@cli_util.option('--config-source-branch-name', help=u"""The name of the branch that contains the Terraform configuration.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-terraform-provider': {'module': 'resource_manager', 'class': 'CustomTerraformProvider'}, 'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def update_stack_update_dev_ops_config_source_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, stack_id, config_source_project_id, config_source_repository_id, display_name, description, custom_terraform_provider, is_third_party_provider_experience_enabled, variables, terraform_version, freeform_tags, defined_tags, if_match, config_source_working_directory, config_source_branch_name):

    if isinstance(stack_id, six.string_types) and len(stack_id.strip()) == 0:
        raise click.UsageError('Parameter --stack-id cannot be whitespace or empty string')
    if not force:
        if custom_terraform_provider or variables or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to custom-terraform-provider and variables and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configSource'] = {}
    _details['configSource']['projectId'] = config_source_project_id
    _details['configSource']['repositoryId'] = config_source_repository_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if custom_terraform_provider is not None:
        _details['customTerraformProvider'] = cli_util.parse_json_parameter("custom_terraform_provider", custom_terraform_provider)

    if is_third_party_provider_experience_enabled is not None:
        _details['isThirdPartyProviderExperienceEnabled'] = is_third_party_provider_experience_enabled

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if terraform_version is not None:
        _details['terraformVersion'] = terraform_version

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config_source_working_directory is not None:
        _details['configSource']['workingDirectory'] = config_source_working_directory

    if config_source_branch_name is not None:
        _details['configSource']['branchName'] = config_source_branch_name

    _details['configSource']['configSourceType'] = 'DEVOPS_CONFIG_SOURCE'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.update_stack(
        stack_id=stack_id,
        update_stack_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stack') and callable(getattr(client, 'get_stack')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stack(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@template_group.command(name=cli_util.override('resource_manager.update_template.command_name', 'update'), help=u"""Updates the specified template. \n[Command Reference](updateTemplate)""")
@cli_util.option('--template-id', required=True, help=u"""The [OCID] of the template.""")
@cli_util.option('--display-name', help=u"""The template's display name. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Description of the template. Avoid entering confidential information.""")
@cli_util.option('--long-description', help=u"""Detailed description of the template. This description is displayed in the Console page listing templates when the template is expanded. Avoid entering confidential information.""")
@cli_util.option('--logo-file-base64-encoded', help=u"""Base64-encoded logo for the template.""")
@cli_util.option('--template-config-source', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'template-config-source': {'module': 'resource_manager', 'class': 'UpdateTemplateConfigSourceDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'template-config-source': {'module': 'resource_manager', 'class': 'UpdateTemplateConfigSourceDetails'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Template'})
@cli_util.wrap_exceptions
def update_template(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, template_id, display_name, description, long_description, logo_file_base64_encoded, template_config_source, freeform_tags, defined_tags, if_match):

    if isinstance(template_id, six.string_types) and len(template_id.strip()) == 0:
        raise click.UsageError('Parameter --template-id cannot be whitespace or empty string')
    if not force:
        if template_config_source or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to template-config-source and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if long_description is not None:
        _details['longDescription'] = long_description

    if logo_file_base64_encoded is not None:
        _details['logoFileBase64Encoded'] = logo_file_base64_encoded

    if template_config_source is not None:
        _details['templateConfigSource'] = cli_util.parse_json_parameter("template_config_source", template_config_source)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.update_template(
        template_id=template_id,
        update_template_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_template') and callable(getattr(client, 'get_template')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_template(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@template_group.command(name=cli_util.override('resource_manager.update_template_update_template_zip_upload_config_source_details.command_name', 'update-template-update-template-zip-upload-config-source-details'), help=u"""Updates the specified template. \n[Command Reference](updateTemplate)""")
@cli_util.option('--template-id', required=True, help=u"""The [OCID] of the template.""")
@cli_util.option('--display-name', help=u"""The template's display name. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Description of the template. Avoid entering confidential information.""")
@cli_util.option('--long-description', help=u"""Detailed description of the template. This description is displayed in the Console page listing templates when the template is expanded. Avoid entering confidential information.""")
@cli_util.option('--logo-file-base64-encoded', help=u"""Base64-encoded logo for the template.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--template-config-source-zip-file-base64-encoded', help=u"""""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Template'})
@cli_util.wrap_exceptions
def update_template_update_template_zip_upload_config_source_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, template_id, display_name, description, long_description, logo_file_base64_encoded, freeform_tags, defined_tags, if_match, template_config_source_zip_file_base64_encoded):

    if isinstance(template_id, six.string_types) and len(template_id.strip()) == 0:
        raise click.UsageError('Parameter --template-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['templateConfigSource'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if long_description is not None:
        _details['longDescription'] = long_description

    if logo_file_base64_encoded is not None:
        _details['logoFileBase64Encoded'] = logo_file_base64_encoded

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if template_config_source_zip_file_base64_encoded is not None:
        _details['templateConfigSource']['zipFileBase64Encoded'] = template_config_source_zip_file_base64_encoded

    _details['templateConfigSource']['templateConfigSourceType'] = 'ZIP_UPLOAD'

    client = cli_util.build_client('resource_manager', 'resource_manager', ctx)
    result = client.update_template(
        template_id=template_id,
        update_template_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_template') and callable(getattr(client, 'get_template')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_template(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
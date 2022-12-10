# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.cloud_bridge.src.oci_cli_cloud_bridge.generated import cloud_bridge_service_cli


@click.command(cli_util.override('discovery.discovery_root_group.command_name', 'discovery'), cls=CommandGroupWithAlias, help=cli_util.override('discovery.discovery_root_group.help', """API for Oracle Cloud Bridge service."""), short_help=cli_util.override('discovery.discovery_root_group.short_help', """Oracle Cloud Bridge API"""))
@cli_util.help_option_group
def discovery_root_group():
    pass


@click.command(cli_util.override('discovery.asset_source_group.command_name', 'asset-source'), cls=CommandGroupWithAlias, help="""Asset source.""")
@cli_util.help_option_group
def asset_source_group():
    pass


@click.command(cli_util.override('discovery.discovery_schedule_group.command_name', 'discovery-schedule'), cls=CommandGroupWithAlias, help="""Discovery schedule.""")
@cli_util.help_option_group
def discovery_schedule_group():
    pass


cloud_bridge_service_cli.cloud_bridge_service_group.add_command(discovery_root_group)
discovery_root_group.add_command(asset_source_group)
discovery_root_group.add_command(discovery_schedule_group)


@asset_source_group.command(name=cli_util.override('discovery.change_asset_source_compartment.command_name', 'change-compartment'), help=u"""Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeAssetSourceCompartment)""")
@cli_util.option('--asset-source-id', required=True, help=u"""The [OCID] of the asset source.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_asset_source_compartment(ctx, from_json, asset_source_id, compartment_id, if_match):

    if isinstance(asset_source_id, six.string_types) and len(asset_source_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-source-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    result = client.change_asset_source_compartment(
        asset_source_id=asset_source_id,
        change_asset_source_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@discovery_schedule_group.command(name=cli_util.override('discovery.change_discovery_schedule_compartment.command_name', 'change-compartment'), help=u"""Moves the specified discovery schedule into a different compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeDiscoveryScheduleCompartment)""")
@cli_util.option('--discovery-schedule-id', required=True, help=u"""The [OCID] of the discovery schedule.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the discovery schedule should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_discovery_schedule_compartment(ctx, from_json, discovery_schedule_id, compartment_id, if_match):

    if isinstance(discovery_schedule_id, six.string_types) and len(discovery_schedule_id.strip()) == 0:
        raise click.UsageError('Parameter --discovery-schedule-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    result = client.change_discovery_schedule_compartment(
        discovery_schedule_id=discovery_schedule_id,
        change_discovery_schedule_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@asset_source_group.command(name=cli_util.override('discovery.create_asset_source.command_name', 'create'), help=u"""Creates an asset source. \n[Command Reference](createAssetSource)""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["VMWARE"]), help=u"""Asset source type.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment for the resource.""")
@cli_util.option('--environment-id', required=True, help=u"""The [OCID] of the environment.""")
@cli_util.option('--inventory-id', required=True, help=u"""The [OCID] of the inventory that will contain created assets.""")
@cli_util.option('--assets-compartment-id', required=True, help=u"""The [OCID] of the compartment that is going to be used to create assets.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the asset source. Does not have to be unique, and it's mutable. Avoid entering confidential information. The name is generated by the service if it is not explicitly provided.""")
@cli_util.option('--discovery-schedule-id', help=u"""The [OCID] of the discovery schedule that is going to be attached to the created asset.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{orcl-cloud: {free-tier-retain: true}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_bridge', 'class': 'AssetSource'})
@cli_util.wrap_exceptions
def create_asset_source(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, type, compartment_id, environment_id, inventory_id, assets_compartment_id, display_name, discovery_schedule_id, freeform_tags, defined_tags, system_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type
    _details['compartmentId'] = compartment_id
    _details['environmentId'] = environment_id
    _details['inventoryId'] = inventory_id
    _details['assetsCompartmentId'] = assets_compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if discovery_schedule_id is not None:
        _details['discoveryScheduleId'] = discovery_schedule_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    result = client.create_asset_source(
        create_asset_source_details=_details,
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


@asset_source_group.command(name=cli_util.override('discovery.create_asset_source_create_vm_ware_asset_source_details.command_name', 'create-asset-source-create-vm-ware-asset-source-details'), help=u"""Creates an asset source. \n[Command Reference](createAssetSource)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment for the resource.""")
@cli_util.option('--environment-id', required=True, help=u"""The [OCID] of the environment.""")
@cli_util.option('--inventory-id', required=True, help=u"""The [OCID] of the inventory that will contain created assets.""")
@cli_util.option('--assets-compartment-id', required=True, help=u"""The [OCID] of the compartment that is going to be used to create assets.""")
@cli_util.option('--vcenter-endpoint', required=True, help=u"""Endpoint for VMware asset discovery and replication in the form of ```https://<host>:<port>/sdk```""")
@cli_util.option('--discovery-credentials', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the asset source. Does not have to be unique, and it's mutable. Avoid entering confidential information. The name is generated by the service if it is not explicitly provided.""")
@cli_util.option('--discovery-schedule-id', help=u"""The [OCID] of the discovery schedule that is going to be attached to the created asset.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{orcl-cloud: {free-tier-retain: true}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--replication-credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--are-historical-metrics-collected', type=click.BOOL, help=u"""Flag indicating whether historical metrics are collected for assets, originating from this asset source.""")
@cli_util.option('--are-realtime-metrics-collected', type=click.BOOL, help=u"""Flag indicating whether real-time metrics are collected for assets, originating from this asset source.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'discovery-credentials': {'module': 'cloud_bridge', 'class': 'AssetSourceCredentials'}, 'replication-credentials': {'module': 'cloud_bridge', 'class': 'AssetSourceCredentials'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'discovery-credentials': {'module': 'cloud_bridge', 'class': 'AssetSourceCredentials'}, 'replication-credentials': {'module': 'cloud_bridge', 'class': 'AssetSourceCredentials'}}, output_type={'module': 'cloud_bridge', 'class': 'AssetSource'})
@cli_util.wrap_exceptions
def create_asset_source_create_vm_ware_asset_source_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, environment_id, inventory_id, assets_compartment_id, vcenter_endpoint, discovery_credentials, display_name, discovery_schedule_id, freeform_tags, defined_tags, system_tags, replication_credentials, are_historical_metrics_collected, are_realtime_metrics_collected):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['environmentId'] = environment_id
    _details['inventoryId'] = inventory_id
    _details['assetsCompartmentId'] = assets_compartment_id
    _details['vcenterEndpoint'] = vcenter_endpoint
    _details['discoveryCredentials'] = cli_util.parse_json_parameter("discovery_credentials", discovery_credentials)

    if display_name is not None:
        _details['displayName'] = display_name

    if discovery_schedule_id is not None:
        _details['discoveryScheduleId'] = discovery_schedule_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    if replication_credentials is not None:
        _details['replicationCredentials'] = cli_util.parse_json_parameter("replication_credentials", replication_credentials)

    if are_historical_metrics_collected is not None:
        _details['areHistoricalMetricsCollected'] = are_historical_metrics_collected

    if are_realtime_metrics_collected is not None:
        _details['areRealtimeMetricsCollected'] = are_realtime_metrics_collected

    _details['type'] = 'VMWARE'

    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    result = client.create_asset_source(
        create_asset_source_details=_details,
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


@discovery_schedule_group.command(name=cli_util.override('discovery.create_discovery_schedule.command_name', 'create'), help=u"""Creates the discovery schedule. \n[Command Reference](createDiscoverySchedule)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which the discovery schedule is created.""")
@cli_util.option('--execution-recurrences', required=True, help=u"""Recurrence specification for the discovery schedule execution.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the discovery schedule. Does not have to be unique, and it's mutable. Avoid entering confidential information. The name is generated by the service if it is not explicitly provided.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_bridge', 'class': 'DiscoverySchedule'})
@cli_util.wrap_exceptions
def create_discovery_schedule(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, execution_recurrences, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['executionRecurrences'] = execution_recurrences

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    result = client.create_discovery_schedule(
        create_discovery_schedule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_discovery_schedule') and callable(getattr(client, 'get_discovery_schedule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_discovery_schedule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@asset_source_group.command(name=cli_util.override('discovery.delete_asset_source.command_name', 'delete'), help=u"""Deletes the asset source by ID. \n[Command Reference](deleteAssetSource)""")
@cli_util.option('--asset-source-id', required=True, help=u"""The [OCID] of the asset source.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_asset_source(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, asset_source_id, if_match):

    if isinstance(asset_source_id, six.string_types) and len(asset_source_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-source-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    result = client.delete_asset_source(
        asset_source_id=asset_source_id,
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
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@discovery_schedule_group.command(name=cli_util.override('discovery.delete_discovery_schedule.command_name', 'delete'), help=u"""Deletes the specified discovery schedule. \n[Command Reference](deleteDiscoverySchedule)""")
@cli_util.option('--discovery-schedule-id', required=True, help=u"""The [OCID] of the discovery schedule.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_discovery_schedule(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, discovery_schedule_id, if_match):

    if isinstance(discovery_schedule_id, six.string_types) and len(discovery_schedule_id.strip()) == 0:
        raise click.UsageError('Parameter --discovery-schedule-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    result = client.delete_discovery_schedule(
        discovery_schedule_id=discovery_schedule_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_discovery_schedule') and callable(getattr(client, 'get_discovery_schedule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_discovery_schedule(discovery_schedule_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@asset_source_group.command(name=cli_util.override('discovery.get_asset_source.command_name', 'get'), help=u"""Gets the asset source by ID. \n[Command Reference](getAssetSource)""")
@cli_util.option('--asset-source-id', required=True, help=u"""The [OCID] of the asset source.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'AssetSource'})
@cli_util.wrap_exceptions
def get_asset_source(ctx, from_json, asset_source_id):

    if isinstance(asset_source_id, six.string_types) and len(asset_source_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-source-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    result = client.get_asset_source(
        asset_source_id=asset_source_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@discovery_schedule_group.command(name=cli_util.override('discovery.get_discovery_schedule.command_name', 'get'), help=u"""Reads information about the specified discovery schedule. \n[Command Reference](getDiscoverySchedule)""")
@cli_util.option('--discovery-schedule-id', required=True, help=u"""The [OCID] of the discovery schedule.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'DiscoverySchedule'})
@cli_util.wrap_exceptions
def get_discovery_schedule(ctx, from_json, discovery_schedule_id):

    if isinstance(discovery_schedule_id, six.string_types) and len(discovery_schedule_id.strip()) == 0:
        raise click.UsageError('Parameter --discovery-schedule-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    result = client.get_discovery_schedule(
        discovery_schedule_id=discovery_schedule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@asset_source_group.command(name=cli_util.override('discovery.list_asset_source_connections.command_name', 'list-asset-source-connections'), help=u"""Gets known connections to the asset source by the asset source ID. \n[Command Reference](listAssetSourceConnections)""")
@cli_util.option('--asset-source-id', required=True, help=u"""The [OCID] of the asset source.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'AssetSourceConnectionCollection'})
@cli_util.wrap_exceptions
def list_asset_source_connections(ctx, from_json, all_pages, page_size, asset_source_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(asset_source_id, six.string_types) and len(asset_source_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-source-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_asset_source_connections,
            asset_source_id=asset_source_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_asset_source_connections,
            limit,
            page_size,
            asset_source_id=asset_source_id,
            **kwargs
        )
    else:
        result = client.list_asset_source_connections(
            asset_source_id=asset_source_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@asset_source_group.command(name=cli_util.override('discovery.list_asset_sources.command_name', 'list'), help=u"""Returns a list of asset sources. \n[Command Reference](listAssetSources)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--asset-source-id', help=u"""The [OCID] of the asset source.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. By default, the timeCreated is in descending order and displayName is in ascending order.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING", "NEEDS_ATTENTION"]), help=u"""The current state of the asset source.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'AssetSourceCollection'})
@cli_util.wrap_exceptions
def list_asset_sources(ctx, from_json, all_pages, page_size, compartment_id, asset_source_id, sort_by, lifecycle_state, sort_order, display_name, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if asset_source_id is not None:
        kwargs['asset_source_id'] = asset_source_id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_asset_sources,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_asset_sources,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_asset_sources(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@discovery_schedule_group.command(name=cli_util.override('discovery.list_discovery_schedules.command_name', 'list'), help=u"""Lists discovery schedules. \n[Command Reference](listDiscoverySchedules)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--discovery-schedule-id', help=u"""The [OCID] of the discovery schedule.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), help=u"""The current state of the discovery schedule.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. By default, the timeCreated is in descending order and displayName is in ascending order.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_bridge', 'class': 'DiscoveryScheduleCollection'})
@cli_util.wrap_exceptions
def list_discovery_schedules(ctx, from_json, all_pages, page_size, compartment_id, discovery_schedule_id, lifecycle_state, sort_by, sort_order, display_name, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if discovery_schedule_id is not None:
        kwargs['discovery_schedule_id'] = discovery_schedule_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_discovery_schedules,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_discovery_schedules,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_discovery_schedules(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@asset_source_group.command(name=cli_util.override('discovery.refresh_asset_source.command_name', 'refresh'), help=u"""Initiates the process of asset metadata synchronization with the related asset source. \n[Command Reference](refreshAssetSource)""")
@cli_util.option('--asset-source-id', required=True, help=u"""The [OCID] of the asset source.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def refresh_asset_source(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, asset_source_id):

    if isinstance(asset_source_id, six.string_types) and len(asset_source_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-source-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    result = client.refresh_asset_source(
        asset_source_id=asset_source_id,
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


@asset_source_group.command(name=cli_util.override('discovery.update_asset_source.command_name', 'update'), help=u"""Updates the asset source. \n[Command Reference](updateAssetSource)""")
@cli_util.option('--asset-source-id', required=True, help=u"""The [OCID] of the asset source.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["VMWARE"]), help=u"""Source type.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the asset source. Does not have to be unique, and it's mutable. Avoid entering confidential information.""")
@cli_util.option('--assets-compartment-id', help=u"""The [OCID] of the compartment that is going to be used to create assets.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{orcl-cloud: {free-tier-retain: true}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_asset_source(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, asset_source_id, type, display_name, assets_compartment_id, freeform_tags, defined_tags, system_tags, if_match):

    if isinstance(asset_source_id, six.string_types) and len(asset_source_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-source-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or system_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and system-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    if display_name is not None:
        _details['displayName'] = display_name

    if assets_compartment_id is not None:
        _details['assetsCompartmentId'] = assets_compartment_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    result = client.update_asset_source(
        asset_source_id=asset_source_id,
        update_asset_source_details=_details,
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


@asset_source_group.command(name=cli_util.override('discovery.update_asset_source_update_vm_ware_asset_source_details.command_name', 'update-asset-source-update-vm-ware-asset-source-details'), help=u"""Updates the asset source. \n[Command Reference](updateAssetSource)""")
@cli_util.option('--asset-source-id', required=True, help=u"""The [OCID] of the asset source.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the asset source. Does not have to be unique, and it's mutable. Avoid entering confidential information.""")
@cli_util.option('--assets-compartment-id', help=u"""The [OCID] of the compartment that is going to be used to create assets.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{orcl-cloud: {free-tier-retain: true}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--vcenter-endpoint', help=u"""Endpoint for VMware asset discovery and replication in the form of ```https://<host>:<port>/sdk```""")
@cli_util.option('--discovery-credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--replication-credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--are-historical-metrics-collected', type=click.BOOL, help=u"""Flag indicating whether historical metrics are collected for assets, originating from this asset source.""")
@cli_util.option('--are-realtime-metrics-collected', type=click.BOOL, help=u"""Flag indicating whether real-time metrics are collected for assets, originating from this asset source.""")
@cli_util.option('--discovery-schedule-id', help=u"""The [OCID] of the discovery schedule that is going to be assigned to an asset source.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'discovery-credentials': {'module': 'cloud_bridge', 'class': 'AssetSourceCredentials'}, 'replication-credentials': {'module': 'cloud_bridge', 'class': 'AssetSourceCredentials'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}, 'discovery-credentials': {'module': 'cloud_bridge', 'class': 'AssetSourceCredentials'}, 'replication-credentials': {'module': 'cloud_bridge', 'class': 'AssetSourceCredentials'}})
@cli_util.wrap_exceptions
def update_asset_source_update_vm_ware_asset_source_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, asset_source_id, display_name, assets_compartment_id, freeform_tags, defined_tags, system_tags, vcenter_endpoint, discovery_credentials, replication_credentials, are_historical_metrics_collected, are_realtime_metrics_collected, discovery_schedule_id, if_match):

    if isinstance(asset_source_id, six.string_types) and len(asset_source_id.strip()) == 0:
        raise click.UsageError('Parameter --asset-source-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or system_tags or discovery_credentials or replication_credentials:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and system-tags and discovery-credentials and replication-credentials will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if assets_compartment_id is not None:
        _details['assetsCompartmentId'] = assets_compartment_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    if vcenter_endpoint is not None:
        _details['vcenterEndpoint'] = vcenter_endpoint

    if discovery_credentials is not None:
        _details['discoveryCredentials'] = cli_util.parse_json_parameter("discovery_credentials", discovery_credentials)

    if replication_credentials is not None:
        _details['replicationCredentials'] = cli_util.parse_json_parameter("replication_credentials", replication_credentials)

    if are_historical_metrics_collected is not None:
        _details['areHistoricalMetricsCollected'] = are_historical_metrics_collected

    if are_realtime_metrics_collected is not None:
        _details['areRealtimeMetricsCollected'] = are_realtime_metrics_collected

    if discovery_schedule_id is not None:
        _details['discoveryScheduleId'] = discovery_schedule_id

    _details['type'] = 'VMWARE'

    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    result = client.update_asset_source(
        asset_source_id=asset_source_id,
        update_asset_source_details=_details,
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


@discovery_schedule_group.command(name=cli_util.override('discovery.update_discovery_schedule.command_name', 'update'), help=u"""Updates the specified discovery schedule. \n[Command Reference](updateDiscoverySchedule)""")
@cli_util.option('--discovery-schedule-id', required=True, help=u"""The [OCID] of the discovery schedule.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the discovery schedule. Does not have to be unique, and it's mutable. Avoid entering confidential information.""")
@cli_util.option('--execution-recurrences', help=u"""Recurrence specification for the discovery schedule execution.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace/scope. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_bridge', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_bridge', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_bridge', 'class': 'DiscoverySchedule'})
@cli_util.wrap_exceptions
def update_discovery_schedule(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, discovery_schedule_id, display_name, execution_recurrences, freeform_tags, defined_tags, if_match):

    if isinstance(discovery_schedule_id, six.string_types) and len(discovery_schedule_id.strip()) == 0:
        raise click.UsageError('Parameter --discovery-schedule-id cannot be whitespace or empty string')
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

    if execution_recurrences is not None:
        _details['executionRecurrences'] = execution_recurrences

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_bridge', 'discovery', ctx)
    result = client.update_discovery_schedule(
        discovery_schedule_id=discovery_schedule_id,
        update_discovery_schedule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_discovery_schedule') and callable(getattr(client, 'get_discovery_schedule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_discovery_schedule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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

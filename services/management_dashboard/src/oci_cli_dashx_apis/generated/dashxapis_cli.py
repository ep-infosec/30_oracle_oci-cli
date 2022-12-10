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


@cli.command(cli_util.override('management_dashboard.management_dashboard_root_group.command_name', 'management-dashboard'), cls=CommandGroupWithAlias, help=cli_util.override('management_dashboard.management_dashboard_root_group.help', """API for the Management Dashboard micro-service. Use this API for dashboard and saved search metadata preservation and to perform  tasks such as creating a dashboard, creating a saved search, and obtaining a list of dashboards and saved searches in a compartment."""), short_help=cli_util.override('management_dashboard.management_dashboard_root_group.short_help', """ManagementDashboard API"""))
@cli_util.help_option_group
def management_dashboard_root_group():
    pass


@click.command(cli_util.override('management_dashboard.management_saved_search_group.command_name', 'management-saved-search'), cls=CommandGroupWithAlias, help="""Properties of a saved search.""")
@cli_util.help_option_group
def management_saved_search_group():
    pass


@click.command(cli_util.override('management_dashboard.management_dashboard_import_details_group.command_name', 'management-dashboard-import-details'), cls=CommandGroupWithAlias, help="""Array of dashboards to import.""")
@cli_util.help_option_group
def management_dashboard_import_details_group():
    pass


@click.command(cli_util.override('management_dashboard.management_dashboard_group.command_name', 'management-dashboard'), cls=CommandGroupWithAlias, help="""Properties of a dashboard, including dashboard ID.""")
@cli_util.help_option_group
def management_dashboard_group():
    pass


management_dashboard_root_group.add_command(management_saved_search_group)
management_dashboard_root_group.add_command(management_dashboard_import_details_group)
management_dashboard_root_group.add_command(management_dashboard_group)


@management_dashboard_group.command(name=cli_util.override('management_dashboard.change_management_dashboards_compartment.command_name', 'change-compartment'), help=u"""Moves the dashboard from the existing compartment to a new compartment. \n[Command Reference](changeManagementDashboardsCompartment)""")
@cli_util.option('--management-dashboard-id', required=True, help=u"""A unique dashboard identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""OCID of the compartment to which the dashboard is being moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_dashboard', 'class': 'ManagementDashboard'})
@cli_util.wrap_exceptions
def change_management_dashboards_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, management_dashboard_id, compartment_id, if_match):

    if isinstance(management_dashboard_id, six.string_types) and len(management_dashboard_id.strip()) == 0:
        raise click.UsageError('Parameter --management-dashboard-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.change_management_dashboards_compartment(
        management_dashboard_id=management_dashboard_id,
        change_management_dashboards_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_management_dashboard') and callable(getattr(client, 'get_management_dashboard')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_management_dashboard(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@management_saved_search_group.command(name=cli_util.override('management_dashboard.change_management_saved_searches_compartment.command_name', 'change-compartment'), help=u"""Moves the saved search from the existing compartment to a new compartment. \n[Command Reference](changeManagementSavedSearchesCompartment)""")
@cli_util.option('--management-saved-search-id', required=True, help=u"""A unique saved search identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""OCID of the compartment to which the saved search is being moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_dashboard', 'class': 'ManagementSavedSearch'})
@cli_util.wrap_exceptions
def change_management_saved_searches_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, management_saved_search_id, compartment_id, if_match):

    if isinstance(management_saved_search_id, six.string_types) and len(management_saved_search_id.strip()) == 0:
        raise click.UsageError('Parameter --management-saved-search-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.change_management_saved_searches_compartment(
        management_saved_search_id=management_saved_search_id,
        change_management_saved_searches_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_management_saved_search') and callable(getattr(client, 'get_management_saved_search')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_management_saved_search(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@management_dashboard_group.command(name=cli_util.override('management_dashboard.create_management_dashboard.command_name', 'create'), help=u"""Creates a new dashboard. Limit for number of saved searches in a dashboard is 20. Here's an example of how you can use CLI to create a dashboard. For information on the details that must be passed to CREATE, you can use the GET API to obtain the Create.json file: `oci management-dashboard dashboard get --management-dashboard-id  \"ocid1.managementdashboard.oc1..dashboardId1\" --query data > Create.json.` You can then modify the Create.json file by removing the `id` attribute and making other required changes, and use the `oci management-dashboard dashboard create` command. \n[Command Reference](createManagementDashboard)""")
@cli_util.option('--provider-id', required=True, help=u"""ID of the service (for example, log-analytics) that owns the dashboard. Each service has a unique ID.""")
@cli_util.option('--provider-name', required=True, help=u"""Name of the service (for example, Logging Analytics) that owns the dashboard.""")
@cli_util.option('--provider-version', required=True, help=u"""Version of the service that owns the dashboard.""")
@cli_util.option('--tiles', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of dashboard tiles.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', required=True, help=u"""Display name of the dashboard.""")
@cli_util.option('--description', required=True, help=u"""Description of the dashboard.""")
@cli_util.option('--compartment-id', required=True, help=u"""OCID of the compartment in which the dashboard resides.""")
@cli_util.option('--is-oob-dashboard', required=True, type=click.BOOL, help=u"""Determines whether the dashboard is an Out-of-the-Box (OOB) dashboard. Note that OOB dashboards are only provided by Oracle and cannot be modified.""")
@cli_util.option('--is-show-in-home', required=True, type=click.BOOL, help=u"""Determines whether the dashboard will be displayed in Dashboard Home.""")
@cli_util.option('--metadata-version', required=True, help=u"""Version of the metadata.""")
@cli_util.option('--is-show-description', required=True, type=click.BOOL, help=u"""Determines whether the description of the dashboard is displayed.""")
@cli_util.option('--screen-image', required=True, help=u"""Screen image of the dashboard.""")
@cli_util.option('--nls', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""JSON that contains internationalization options.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ui-config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""JSON that contains user interface options.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of JSON that contain data source options.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', required=True, help=u"""Type of dashboard. NORMAL denotes a single dashboard and SET denotes a dashboard set.""")
@cli_util.option('--is-favorite', required=True, type=click.BOOL, help=u"""Determines whether the dashboard is set as favorite.""")
@cli_util.option('--dashboard-id', help=u"""ID of the dashboard, which must only be provided for Out-of-the-Box (OOB) dashboards.""")
@cli_util.option('--parameters-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defines parameters for the dashboard.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--drilldown-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Drill-down configuration to define the destination of a drill-down action.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'tiles': {'module': 'management_dashboard', 'class': 'list[ManagementDashboardTileDetails]'}, 'nls': {'module': 'management_dashboard', 'class': 'object'}, 'ui-config': {'module': 'management_dashboard', 'class': 'object'}, 'data-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'parameters-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'drilldown-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'tiles': {'module': 'management_dashboard', 'class': 'list[ManagementDashboardTileDetails]'}, 'nls': {'module': 'management_dashboard', 'class': 'object'}, 'ui-config': {'module': 'management_dashboard', 'class': 'object'}, 'data-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'parameters-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'drilldown-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'management_dashboard', 'class': 'ManagementDashboard'})
@cli_util.wrap_exceptions
def create_management_dashboard(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, provider_id, provider_name, provider_version, tiles, display_name, description, compartment_id, is_oob_dashboard, is_show_in_home, metadata_version, is_show_description, screen_image, nls, ui_config, data_config, type, is_favorite, dashboard_id, parameters_config, drilldown_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['providerId'] = provider_id
    _details['providerName'] = provider_name
    _details['providerVersion'] = provider_version
    _details['tiles'] = cli_util.parse_json_parameter("tiles", tiles)
    _details['displayName'] = display_name
    _details['description'] = description
    _details['compartmentId'] = compartment_id
    _details['isOobDashboard'] = is_oob_dashboard
    _details['isShowInHome'] = is_show_in_home
    _details['metadataVersion'] = metadata_version
    _details['isShowDescription'] = is_show_description
    _details['screenImage'] = screen_image
    _details['nls'] = cli_util.parse_json_parameter("nls", nls)
    _details['uiConfig'] = cli_util.parse_json_parameter("ui_config", ui_config)
    _details['dataConfig'] = cli_util.parse_json_parameter("data_config", data_config)
    _details['type'] = type
    _details['isFavorite'] = is_favorite

    if dashboard_id is not None:
        _details['dashboardId'] = dashboard_id

    if parameters_config is not None:
        _details['parametersConfig'] = cli_util.parse_json_parameter("parameters_config", parameters_config)

    if drilldown_config is not None:
        _details['drilldownConfig'] = cli_util.parse_json_parameter("drilldown_config", drilldown_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.create_management_dashboard(
        create_management_dashboard_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_management_dashboard') and callable(getattr(client, 'get_management_dashboard')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_management_dashboard(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@management_saved_search_group.command(name=cli_util.override('management_dashboard.create_management_saved_search.command_name', 'create'), help=u"""Creates a new saved search. Here's an example of how you can use CLI to create a saved search. For information on the details that must be passed to CREATE, you can use the GET API to obtain the Create.json file: `oci management-dashboard saved-search get --management-saved-search-id ocid1.managementsavedsearch.oc1..savedsearchId1 --query data > Create.json`. You can then modify the Create.json file by removing the `id` attribute and making other required changes, and use the `oci management-dashboard saved-search create` command. \n[Command Reference](createManagementSavedSearch)""")
@cli_util.option('--display-name', required=True, help=u"""Display name of the saved search.""")
@cli_util.option('--provider-id', required=True, help=u"""ID of the service (for example log-analytics) that owns the saved search. Each service has a unique ID.""")
@cli_util.option('--provider-version', required=True, help=u"""Version of the service that owns this saved search.""")
@cli_util.option('--provider-name', required=True, help=u"""Name of the service (for example, Logging Analytics) that owns the saved search.""")
@cli_util.option('--compartment-id', required=True, help=u"""OCID of the compartment in which the saved search resides.""")
@cli_util.option('--is-oob-saved-search', required=True, type=click.BOOL, help=u"""Determines whether the saved search is an Out-of-the-Box (OOB) saved search. Note that OOB saved searches are only provided by Oracle and cannot be modified.""")
@cli_util.option('--description', required=True, help=u"""Description of the saved search.""")
@cli_util.option('--nls', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""JSON that contains internationalization options.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SEARCH_SHOW_IN_DASHBOARD", "SEARCH_DONT_SHOW_IN_DASHBOARD", "WIDGET_SHOW_IN_DASHBOARD", "WIDGET_DONT_SHOW_IN_DASHBOARD", "FILTER_SHOW_IN_DASHBOARD", "FILTER_DONT_SHOW_IN_DASHBOARD"]), help=u"""Determines how the saved search is displayed in a dashboard.""")
@cli_util.option('--ui-config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""JSON that contains user interface options.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of JSON that contain data source options.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--screen-image', required=True, help=u"""Screen image of the saved search.""")
@cli_util.option('--metadata-version', required=True, help=u"""Version of the metadata.""")
@cli_util.option('--widget-template', required=True, help=u"""Reference to the HTML file of the widget.""")
@cli_util.option('--widget-vm', required=True, help=u"""Reference to the view model of the widget.""")
@cli_util.option('--id', help=u"""ID of the saved search, which must only be provided for Out-of-the-Box (OOB) saved search.""")
@cli_util.option('--parameters-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defines parameters for the saved search.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--drilldown-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Drill-down configuration to define the destination of a drill-down action.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'nls': {'module': 'management_dashboard', 'class': 'object'}, 'ui-config': {'module': 'management_dashboard', 'class': 'object'}, 'data-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'parameters-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'drilldown-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nls': {'module': 'management_dashboard', 'class': 'object'}, 'ui-config': {'module': 'management_dashboard', 'class': 'object'}, 'data-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'parameters-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'drilldown-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'management_dashboard', 'class': 'ManagementSavedSearch'})
@cli_util.wrap_exceptions
def create_management_saved_search(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, provider_id, provider_version, provider_name, compartment_id, is_oob_saved_search, description, nls, type, ui_config, data_config, screen_image, metadata_version, widget_template, widget_vm, id, parameters_config, drilldown_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['providerId'] = provider_id
    _details['providerVersion'] = provider_version
    _details['providerName'] = provider_name
    _details['compartmentId'] = compartment_id
    _details['isOobSavedSearch'] = is_oob_saved_search
    _details['description'] = description
    _details['nls'] = cli_util.parse_json_parameter("nls", nls)
    _details['type'] = type
    _details['uiConfig'] = cli_util.parse_json_parameter("ui_config", ui_config)
    _details['dataConfig'] = cli_util.parse_json_parameter("data_config", data_config)
    _details['screenImage'] = screen_image
    _details['metadataVersion'] = metadata_version
    _details['widgetTemplate'] = widget_template
    _details['widgetVM'] = widget_vm

    if id is not None:
        _details['id'] = id

    if parameters_config is not None:
        _details['parametersConfig'] = cli_util.parse_json_parameter("parameters_config", parameters_config)

    if drilldown_config is not None:
        _details['drilldownConfig'] = cli_util.parse_json_parameter("drilldown_config", drilldown_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.create_management_saved_search(
        create_management_saved_search_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_management_saved_search') and callable(getattr(client, 'get_management_saved_search')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_management_saved_search(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@management_dashboard_group.command(name=cli_util.override('management_dashboard.delete_management_dashboard.command_name', 'delete'), help=u"""Deletes a Dashboard by ID. \n[Command Reference](deleteManagementDashboard)""")
@cli_util.option('--management-dashboard-id', required=True, help=u"""A unique dashboard identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_management_dashboard(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, management_dashboard_id, if_match):

    if isinstance(management_dashboard_id, six.string_types) and len(management_dashboard_id.strip()) == 0:
        raise click.UsageError('Parameter --management-dashboard-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.delete_management_dashboard(
        management_dashboard_id=management_dashboard_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_management_dashboard') and callable(getattr(client, 'get_management_dashboard')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_management_dashboard(management_dashboard_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@management_saved_search_group.command(name=cli_util.override('management_dashboard.delete_management_saved_search.command_name', 'delete'), help=u"""Deletes a saved search by ID. \n[Command Reference](deleteManagementSavedSearch)""")
@cli_util.option('--management-saved-search-id', required=True, help=u"""A unique saved search identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_management_saved_search(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, management_saved_search_id, if_match):

    if isinstance(management_saved_search_id, six.string_types) and len(management_saved_search_id.strip()) == 0:
        raise click.UsageError('Parameter --management-saved-search-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.delete_management_saved_search(
        management_saved_search_id=management_saved_search_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_management_saved_search') and callable(getattr(client, 'get_management_saved_search')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_management_saved_search(management_saved_search_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@management_dashboard_import_details_group.command(name=cli_util.override('management_dashboard.export_dashboard.command_name', 'export-dashboard'), help=u"""Exports an array of dashboards and their saved searches. Export is designed to work with importDashboard. Here's an example of how you can use CLI to export a dashboard: `$oci management-dashboard dashboard export --query data --export-dashboard-id \"{\\\"dashboardIds\\\":[\\\"ocid1.managementdashboard.oc1..dashboardId1\\\"]}\"  > dashboards.json` \n[Command Reference](exportDashboard)""")
@cli_util.option('--export-dashboard-id', required=True, help=u"""List of dashboardIds in plain text. The syntax is '{\"dashboardIds\":[\"dashboardId1\", \"dashboardId2\", ...]}'. Escaping is needed when using in OCI CLI. For example, \"{\\\"dashboardIds\\\":[\\\"ocid1.managementdashboard.oc1..dashboardId1\\\"]}\" .""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_dashboard', 'class': 'ManagementDashboardExportDetails'})
@cli_util.wrap_exceptions
def export_dashboard(ctx, from_json, export_dashboard_id):

    if isinstance(export_dashboard_id, six.string_types) and len(export_dashboard_id.strip()) == 0:
        raise click.UsageError('Parameter --export-dashboard-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.export_dashboard(
        export_dashboard_id=export_dashboard_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_dashboard_group.command(name=cli_util.override('management_dashboard.get_management_dashboard.command_name', 'get'), help=u"""Gets a dashboard and its saved searches by ID.  Deleted or unauthorized saved searches are marked by tile's state property. \n[Command Reference](getManagementDashboard)""")
@cli_util.option('--management-dashboard-id', required=True, help=u"""A unique dashboard identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_dashboard', 'class': 'ManagementDashboard'})
@cli_util.wrap_exceptions
def get_management_dashboard(ctx, from_json, management_dashboard_id):

    if isinstance(management_dashboard_id, six.string_types) and len(management_dashboard_id.strip()) == 0:
        raise click.UsageError('Parameter --management-dashboard-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.get_management_dashboard(
        management_dashboard_id=management_dashboard_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_saved_search_group.command(name=cli_util.override('management_dashboard.get_management_saved_search.command_name', 'get'), help=u"""Gets a saved search by ID. \n[Command Reference](getManagementSavedSearch)""")
@cli_util.option('--management-saved-search-id', required=True, help=u"""A unique saved search identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_dashboard', 'class': 'ManagementSavedSearch'})
@cli_util.wrap_exceptions
def get_management_saved_search(ctx, from_json, management_saved_search_id):

    if isinstance(management_saved_search_id, six.string_types) and len(management_saved_search_id.strip()) == 0:
        raise click.UsageError('Parameter --management-saved-search-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.get_management_saved_search(
        management_saved_search_id=management_saved_search_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_dashboard_import_details_group.command(name=cli_util.override('management_dashboard.import_dashboard.command_name', 'import-dashboard'), help=u"""Imports an array of dashboards and their saved searches. Here's an example of how you can use CLI to import a dashboard. For information on the details that must be passed to IMPORT, you can use the EXPORT API to obtain the Import.json file: `oci management-dashboard dashboard export --query data --export-dashboard-id \"{\\\"dashboardIds\\\":[\\\"ocid1.managementdashboard.oc1..dashboardId1\\\"]}\"  > Import.json`. Note that import API updates the resource if it already exists, and creates a new resource if it does not exist. To import to a different compartment, edit and change the compartmentId to the desired compartment OCID. Here's an example of how you can use CLI to import: `oci management-dashboard dashboard import --from-json file://Import.json` \n[Command Reference](importDashboard)""")
@cli_util.option('--dashboards', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of dashboards.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'dashboards': {'module': 'management_dashboard', 'class': 'list[ManagementDashboardForImportExportDetails]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dashboards': {'module': 'management_dashboard', 'class': 'list[ManagementDashboardForImportExportDetails]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def import_dashboard(ctx, from_json, dashboards, freeform_tags, defined_tags, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dashboards'] = cli_util.parse_json_parameter("dashboards", dashboards)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.import_dashboard(
        management_dashboard_import_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@management_dashboard_group.command(name=cli_util.override('management_dashboard.list_management_dashboards.command_name', 'list'), help=u"""Gets the list of dashboards in a compartment with pagination.  Returned properties are the summary. \n[Command Reference](listManagementDashboards)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page on which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_dashboard', 'class': 'ManagementDashboardCollection'})
@cli_util.wrap_exceptions
def list_management_dashboards(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_management_dashboards,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_management_dashboards,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_management_dashboards(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@management_saved_search_group.command(name=cli_util.override('management_dashboard.list_management_saved_searches.command_name', 'list'), help=u"""Gets the list of saved searches in a compartment with pagination.  Returned properties are the summary. \n[Command Reference](listManagementSavedSearches)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page on which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is the default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'management_dashboard', 'class': 'ManagementSavedSearchCollection'})
@cli_util.wrap_exceptions
def list_management_saved_searches(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_management_saved_searches,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_management_saved_searches,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_management_saved_searches(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@management_dashboard_group.command(name=cli_util.override('management_dashboard.update_management_dashboard.command_name', 'update'), help=u"""Updates an existing dashboard identified by ID path parameter.  CompartmentId can be modified only by the changeCompartment API. Limit for number of saved searches in a dashboard is 20. \n[Command Reference](updateManagementDashboard)""")
@cli_util.option('--management-dashboard-id', required=True, help=u"""A unique dashboard identifier.""")
@cli_util.option('--provider-id', help=u"""ID of the service (for example, log-analytics) that owns the dashboard. Each service has a unique ID.""")
@cli_util.option('--provider-name', help=u"""Name of the service (for example, Logging Analytics) that owns the dashboard.""")
@cli_util.option('--provider-version', help=u"""Version of the service that owns the dashboard.""")
@cli_util.option('--tiles', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of dashboard tiles.

This option is a JSON list with items of type ManagementDashboardTileDetails.  For documentation on ManagementDashboardTileDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/dashxapis/20200901/datatypes/ManagementDashboardTileDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Display name of the dashboard.""")
@cli_util.option('--description', help=u"""Description of the dashboard.""")
@cli_util.option('--compartment-id', help=u"""OCID of the compartment in which the dashboard resides.""")
@cli_util.option('--is-oob-dashboard', type=click.BOOL, help=u"""Determines whether the dashboard is an Out-of-the-Box (OOB) dashboard. Note that OOB dashboards are only provided by Oracle and cannot be modified.""")
@cli_util.option('--is-show-in-home', type=click.BOOL, help=u"""Determines whether the dashboard will be displayed in Dashboard Home.""")
@cli_util.option('--metadata-version', help=u"""Version of the metadata.""")
@cli_util.option('--is-show-description', type=click.BOOL, help=u"""Determines whether the description of the dashboard is displayed.""")
@cli_util.option('--screen-image', help=u"""Screen image of the dashboard.""")
@cli_util.option('--nls', type=custom_types.CLI_COMPLEX_TYPE, help=u"""JSON that contains internationalization options.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ui-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""JSON that contains user interface options.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of JSON that contain data source options.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', help=u"""Type of dashboard. NORMAL denotes a single dashboard and SET denotes a dashboard set.""")
@cli_util.option('--is-favorite', type=click.BOOL, help=u"""Determines whether the dashboard is set as favorite.""")
@cli_util.option('--parameters-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defines parameters for the dashboard.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--drilldown-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Drill-down configuration to define the destination of a drill-down action.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'tiles': {'module': 'management_dashboard', 'class': 'list[ManagementDashboardTileDetails]'}, 'nls': {'module': 'management_dashboard', 'class': 'object'}, 'ui-config': {'module': 'management_dashboard', 'class': 'object'}, 'data-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'parameters-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'drilldown-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'tiles': {'module': 'management_dashboard', 'class': 'list[ManagementDashboardTileDetails]'}, 'nls': {'module': 'management_dashboard', 'class': 'object'}, 'ui-config': {'module': 'management_dashboard', 'class': 'object'}, 'data-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'parameters-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'drilldown-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'management_dashboard', 'class': 'ManagementDashboard'})
@cli_util.wrap_exceptions
def update_management_dashboard(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, management_dashboard_id, provider_id, provider_name, provider_version, tiles, display_name, description, compartment_id, is_oob_dashboard, is_show_in_home, metadata_version, is_show_description, screen_image, nls, ui_config, data_config, type, is_favorite, parameters_config, drilldown_config, freeform_tags, defined_tags, if_match):

    if isinstance(management_dashboard_id, six.string_types) and len(management_dashboard_id.strip()) == 0:
        raise click.UsageError('Parameter --management-dashboard-id cannot be whitespace or empty string')
    if not force:
        if tiles or nls or ui_config or data_config or parameters_config or drilldown_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to tiles and nls and ui-config and data-config and parameters-config and drilldown-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if provider_id is not None:
        _details['providerId'] = provider_id

    if provider_name is not None:
        _details['providerName'] = provider_name

    if provider_version is not None:
        _details['providerVersion'] = provider_version

    if tiles is not None:
        _details['tiles'] = cli_util.parse_json_parameter("tiles", tiles)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if is_oob_dashboard is not None:
        _details['isOobDashboard'] = is_oob_dashboard

    if is_show_in_home is not None:
        _details['isShowInHome'] = is_show_in_home

    if metadata_version is not None:
        _details['metadataVersion'] = metadata_version

    if is_show_description is not None:
        _details['isShowDescription'] = is_show_description

    if screen_image is not None:
        _details['screenImage'] = screen_image

    if nls is not None:
        _details['nls'] = cli_util.parse_json_parameter("nls", nls)

    if ui_config is not None:
        _details['uiConfig'] = cli_util.parse_json_parameter("ui_config", ui_config)

    if data_config is not None:
        _details['dataConfig'] = cli_util.parse_json_parameter("data_config", data_config)

    if type is not None:
        _details['type'] = type

    if is_favorite is not None:
        _details['isFavorite'] = is_favorite

    if parameters_config is not None:
        _details['parametersConfig'] = cli_util.parse_json_parameter("parameters_config", parameters_config)

    if drilldown_config is not None:
        _details['drilldownConfig'] = cli_util.parse_json_parameter("drilldown_config", drilldown_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.update_management_dashboard(
        management_dashboard_id=management_dashboard_id,
        update_management_dashboard_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_management_dashboard') and callable(getattr(client, 'get_management_dashboard')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_management_dashboard(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@management_saved_search_group.command(name=cli_util.override('management_dashboard.update_management_saved_search.command_name', 'update'), help=u"""Updates an existing saved search identified by ID path parameter.  CompartmentId can be modified only by the changeCompartment API. \n[Command Reference](updateManagementSavedSearch)""")
@cli_util.option('--management-saved-search-id', required=True, help=u"""A unique saved search identifier.""")
@cli_util.option('--display-name', help=u"""Display name of the saved search.""")
@cli_util.option('--provider-id', help=u"""ID of the service (for example log-analytics) that owns the saved search. Each service has a unique ID.""")
@cli_util.option('--provider-version', help=u"""Version of the service that owns this saved search.""")
@cli_util.option('--provider-name', help=u"""Name of the service (for example, Logging Analytics) that owns the saved search.""")
@cli_util.option('--compartment-id', help=u"""OCID of the compartment in which the saved search resides.""")
@cli_util.option('--is-oob-saved-search', type=click.BOOL, help=u"""Determines whether the saved search is an Out-of-the-Box (OOB) saved search. Note that OOB saved searches are only provided by Oracle and cannot be modified.""")
@cli_util.option('--description', help=u"""Description of the saved search.""")
@cli_util.option('--nls', type=custom_types.CLI_COMPLEX_TYPE, help=u"""JSON that contains internationalization options.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["SEARCH_SHOW_IN_DASHBOARD", "SEARCH_DONT_SHOW_IN_DASHBOARD", "WIDGET_SHOW_IN_DASHBOARD", "WIDGET_DONT_SHOW_IN_DASHBOARD", "FILTER_SHOW_IN_DASHBOARD", "FILTER_DONT_SHOW_IN_DASHBOARD"]), help=u"""Determines how the saved search is displayed in a dashboard.""")
@cli_util.option('--ui-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""JSON that contains user interface options.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of JSON that contain data source options.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--screen-image', help=u"""Screen image of the saved search.""")
@cli_util.option('--metadata-version', help=u"""Version of the metadata.""")
@cli_util.option('--widget-template', help=u"""Reference to the HTML file of the widget.""")
@cli_util.option('--widget-vm', help=u"""Reference to the view model of the widget.""")
@cli_util.option('--parameters-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defines parameters for the saved search.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--drilldown-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Drill-down configuration to define the destination of a drill-down action.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'nls': {'module': 'management_dashboard', 'class': 'object'}, 'ui-config': {'module': 'management_dashboard', 'class': 'object'}, 'data-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'parameters-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'drilldown-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nls': {'module': 'management_dashboard', 'class': 'object'}, 'ui-config': {'module': 'management_dashboard', 'class': 'object'}, 'data-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'parameters-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'drilldown-config': {'module': 'management_dashboard', 'class': 'list[object]'}, 'freeform-tags': {'module': 'management_dashboard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'management_dashboard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'management_dashboard', 'class': 'ManagementSavedSearch'})
@cli_util.wrap_exceptions
def update_management_saved_search(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, management_saved_search_id, display_name, provider_id, provider_version, provider_name, compartment_id, is_oob_saved_search, description, nls, type, ui_config, data_config, screen_image, metadata_version, widget_template, widget_vm, parameters_config, drilldown_config, freeform_tags, defined_tags, if_match):

    if isinstance(management_saved_search_id, six.string_types) and len(management_saved_search_id.strip()) == 0:
        raise click.UsageError('Parameter --management-saved-search-id cannot be whitespace or empty string')
    if not force:
        if nls or ui_config or data_config or parameters_config or drilldown_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to nls and ui-config and data-config and parameters-config and drilldown-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if provider_id is not None:
        _details['providerId'] = provider_id

    if provider_version is not None:
        _details['providerVersion'] = provider_version

    if provider_name is not None:
        _details['providerName'] = provider_name

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if is_oob_saved_search is not None:
        _details['isOobSavedSearch'] = is_oob_saved_search

    if description is not None:
        _details['description'] = description

    if nls is not None:
        _details['nls'] = cli_util.parse_json_parameter("nls", nls)

    if type is not None:
        _details['type'] = type

    if ui_config is not None:
        _details['uiConfig'] = cli_util.parse_json_parameter("ui_config", ui_config)

    if data_config is not None:
        _details['dataConfig'] = cli_util.parse_json_parameter("data_config", data_config)

    if screen_image is not None:
        _details['screenImage'] = screen_image

    if metadata_version is not None:
        _details['metadataVersion'] = metadata_version

    if widget_template is not None:
        _details['widgetTemplate'] = widget_template

    if widget_vm is not None:
        _details['widgetVM'] = widget_vm

    if parameters_config is not None:
        _details['parametersConfig'] = cli_util.parse_json_parameter("parameters_config", parameters_config)

    if drilldown_config is not None:
        _details['drilldownConfig'] = cli_util.parse_json_parameter("drilldown_config", drilldown_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('management_dashboard', 'dashx_apis', ctx)
    result = client.update_management_saved_search(
        management_saved_search_id=management_saved_search_id,
        update_management_saved_search_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_management_saved_search') and callable(getattr(client, 'get_management_saved_search')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_management_saved_search(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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

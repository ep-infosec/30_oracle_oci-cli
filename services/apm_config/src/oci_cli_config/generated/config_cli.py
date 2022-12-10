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


@cli.command(cli_util.override('apm_config.apm_config_root_group.command_name', 'apm-config'), cls=CommandGroupWithAlias, help=cli_util.override('apm_config.apm_config_root_group.help', """Use the Application Performance Monitoring Configuration API to query and set Application Performance Monitoring
configuration. For more information, see [Application Performance Monitoring]."""), short_help=cli_util.override('apm_config.apm_config_root_group.short_help', """Application Performance Monitoring Configuration API"""))
@cli_util.help_option_group
def apm_config_root_group():
    pass


@click.command(cli_util.override('apm_config.metric_group_group.command_name', 'metric-group'), cls=CommandGroupWithAlias, help="""A metric group defines a set of metrics to collect from a span. It uses a span filter to specify which spans to process. The set is then published to a namespace, which is a product level subdivision of metrics.""")
@cli_util.help_option_group
def metric_group_group():
    pass


@click.command(cli_util.override('apm_config.span_filter_group.command_name', 'span-filter'), cls=CommandGroupWithAlias, help="""A named setting that specifies the filter criteria to match a subset of the spans.""")
@cli_util.help_option_group
def span_filter_group():
    pass


@click.command(cli_util.override('apm_config.config_collection_group.command_name', 'config-collection'), cls=CommandGroupWithAlias, help="""A collection of configuration items.""")
@cli_util.help_option_group
def config_collection_group():
    pass


@click.command(cli_util.override('apm_config.config_group.command_name', 'config'), cls=CommandGroupWithAlias, help="""A configuration item, which has a number of mutually exclusive properties that can be used to set specific portions of the configuration.""")
@cli_util.help_option_group
def config_group():
    pass


apm_config_root_group.add_command(metric_group_group)
apm_config_root_group.add_command(span_filter_group)
apm_config_root_group.add_command(config_collection_group)
apm_config_root_group.add_command(config_group)


@config_group.command(name=cli_util.override('apm_config.create_config.command_name', 'create'), help=u"""Creates a new configuration item. \n[Command Reference](createConfig)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@cli_util.option('--config-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SPAN_FILTER", "METRIC_GROUP", "APDEX", "OPTIONS"]), help=u"""The type of configuration item.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--opc-dry-run', help=u"""Indicates that the request is a dry run, if set to \"true\". A dry run request does not modify the configuration item details and is used only to perform validation on the submitted data.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_config', 'class': 'Config'})
@cli_util.wrap_exceptions
def create_config(ctx, from_json, apm_domain_id, config_type, freeform_tags, defined_tags, opc_dry_run):

    kwargs = {}
    if opc_dry_run is not None:
        kwargs['opc_dry_run'] = opc_dry_run
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configType'] = config_type

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('apm_config', 'config', ctx)
    result = client.create_config(
        apm_domain_id=apm_domain_id,
        create_config_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@config_group.command(name=cli_util.override('apm_config.create_config_create_span_filter_details.command_name', 'create-config-create-span-filter-details'), help=u"""Creates a new configuration item. \n[Command Reference](createConfig)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@cli_util.option('--display-name', required=True, help=u"""The name by which a configuration entity is displayed to the end user.""")
@cli_util.option('--filter-text', required=True, help=u"""The string that defines the Span Filter expression.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""An optional string that describes what the filter is intended or used for.""")
@cli_util.option('--opc-dry-run', help=u"""Indicates that the request is a dry run, if set to \"true\". A dry run request does not modify the configuration item details and is used only to perform validation on the submitted data.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_config', 'class': 'Config'})
@cli_util.wrap_exceptions
def create_config_create_span_filter_details(ctx, from_json, apm_domain_id, display_name, filter_text, freeform_tags, defined_tags, description, opc_dry_run):

    kwargs = {}
    if opc_dry_run is not None:
        kwargs['opc_dry_run'] = opc_dry_run
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['filterText'] = filter_text

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if description is not None:
        _details['description'] = description

    _details['configType'] = 'SPAN_FILTER'

    client = cli_util.build_client('apm_config', 'config', ctx)
    result = client.create_config(
        apm_domain_id=apm_domain_id,
        create_config_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@config_group.command(name=cli_util.override('apm_config.create_config_create_metric_group_details.command_name', 'create-config-create-metric-group-details'), help=u"""Creates a new configuration item. \n[Command Reference](createConfig)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@cli_util.option('--display-name', required=True, help=u"""The name by which a configuration entity is displayed to the end user.""")
@cli_util.option('--filter-id', required=True, help=u"""The [OCID] of a Span Filter. The filterId is mandatory for the creation of MetricGroups. A filterId is generated when a Span Filter is created.""")
@cli_util.option('--metrics', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of metrics in this group.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--namespace', help=u"""The namespace to which the metrics are published. It must be one of several predefined namespaces.""")
@cli_util.option('--dimensions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of dimensions for the metric. This variable should not be used.

This option is a JSON list with items of type Dimension.  For documentation on Dimension please see our API reference: https://docs.cloud.oracle.com/api/#/en/config/20210201/datatypes/Dimension.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--opc-dry-run', help=u"""Indicates that the request is a dry run, if set to \"true\". A dry run request does not modify the configuration item details and is used only to perform validation on the submitted data.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}, 'dimensions': {'module': 'apm_config', 'class': 'list[Dimension]'}, 'metrics': {'module': 'apm_config', 'class': 'list[Metric]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}, 'dimensions': {'module': 'apm_config', 'class': 'list[Dimension]'}, 'metrics': {'module': 'apm_config', 'class': 'list[Metric]'}}, output_type={'module': 'apm_config', 'class': 'Config'})
@cli_util.wrap_exceptions
def create_config_create_metric_group_details(ctx, from_json, apm_domain_id, display_name, filter_id, metrics, freeform_tags, defined_tags, namespace, dimensions, opc_dry_run):

    kwargs = {}
    if opc_dry_run is not None:
        kwargs['opc_dry_run'] = opc_dry_run
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['filterId'] = filter_id
    _details['metrics'] = cli_util.parse_json_parameter("metrics", metrics)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if namespace is not None:
        _details['namespace'] = namespace

    if dimensions is not None:
        _details['dimensions'] = cli_util.parse_json_parameter("dimensions", dimensions)

    _details['configType'] = 'METRIC_GROUP'

    client = cli_util.build_client('apm_config', 'config', ctx)
    result = client.create_config(
        apm_domain_id=apm_domain_id,
        create_config_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@config_group.command(name=cli_util.override('apm_config.create_config_create_options_details.command_name', 'create-config-create-options-details'), help=u"""Creates a new configuration item. \n[Command Reference](createConfig)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The name by which a configuration entity is displayed to the end user.""")
@cli_util.option('--options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The options are stored here as JSON.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--group', help=u"""A string that specifies the group that an OPTIONS item belongs to.""")
@cli_util.option('--description', help=u"""An optional string that describes what the options are intended or used for.""")
@cli_util.option('--opc-dry-run', help=u"""Indicates that the request is a dry run, if set to \"true\". A dry run request does not modify the configuration item details and is used only to perform validation on the submitted data.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}, 'options': {'module': 'apm_config', 'class': 'object'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}, 'options': {'module': 'apm_config', 'class': 'object'}}, output_type={'module': 'apm_config', 'class': 'Config'})
@cli_util.wrap_exceptions
def create_config_create_options_details(ctx, from_json, apm_domain_id, freeform_tags, defined_tags, display_name, options, group, description, opc_dry_run):

    kwargs = {}
    if opc_dry_run is not None:
        kwargs['opc_dry_run'] = opc_dry_run
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if options is not None:
        _details['options'] = cli_util.parse_json_parameter("options", options)

    if group is not None:
        _details['group'] = group

    if description is not None:
        _details['description'] = description

    _details['configType'] = 'OPTIONS'

    client = cli_util.build_client('apm_config', 'config', ctx)
    result = client.create_config(
        apm_domain_id=apm_domain_id,
        create_config_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@config_group.command(name=cli_util.override('apm_config.create_config_create_apdex_rules_details.command_name', 'create-config-create-apdex-rules-details'), help=u"""Creates a new configuration item. \n[Command Reference](createConfig)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@cli_util.option('--rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', required=True, help=u"""The name by which a configuration entity is displayed to the end user.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--opc-dry-run', help=u"""Indicates that the request is a dry run, if set to \"true\". A dry run request does not modify the configuration item details and is used only to perform validation on the submitted data.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}, 'rules': {'module': 'apm_config', 'class': 'list[Apdex]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}, 'rules': {'module': 'apm_config', 'class': 'list[Apdex]'}}, output_type={'module': 'apm_config', 'class': 'Config'})
@cli_util.wrap_exceptions
def create_config_create_apdex_rules_details(ctx, from_json, apm_domain_id, rules, display_name, freeform_tags, defined_tags, opc_dry_run):

    kwargs = {}
    if opc_dry_run is not None:
        kwargs['opc_dry_run'] = opc_dry_run
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['rules'] = cli_util.parse_json_parameter("rules", rules)
    _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['configType'] = 'APDEX'

    client = cli_util.build_client('apm_config', 'config', ctx)
    result = client.create_config(
        apm_domain_id=apm_domain_id,
        create_config_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@config_group.command(name=cli_util.override('apm_config.delete_config.command_name', 'delete'), help=u"""Deletes the configuration item identified by the OCID. \n[Command Reference](deleteConfig)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@cli_util.option('--config-id', required=True, help=u"""The [OCID] of the configuration item.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_config(ctx, from_json, apm_domain_id, config_id, if_match):

    if isinstance(config_id, six.string_types) and len(config_id.strip()) == 0:
        raise click.UsageError('Parameter --config-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_config', 'config', ctx)
    result = client.delete_config(
        apm_domain_id=apm_domain_id,
        config_id=config_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@config_group.command(name=cli_util.override('apm_config.get_config.command_name', 'get'), help=u"""Gets the configuration item identified by the OCID. \n[Command Reference](getConfig)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@cli_util.option('--config-id', required=True, help=u"""The [OCID] of the configuration item.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_config', 'class': 'Config'})
@cli_util.wrap_exceptions
def get_config(ctx, from_json, apm_domain_id, config_id):

    if isinstance(config_id, six.string_types) and len(config_id.strip()) == 0:
        raise click.UsageError('Parameter --config-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_config', 'config', ctx)
    result = client.get_config(
        apm_domain_id=apm_domain_id,
        config_id=config_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@config_collection_group.command(name=cli_util.override('apm_config.list_configs.command_name', 'list-configs'), help=u"""Returns all configuration items, which can optionally be filtered by configuration type. \n[Command Reference](listConfigs)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@cli_util.option('--config-type', help=u"""A filter to match configuration items of a given type. Supported values are SPAN_FILTER, METRIC_GROUP, and APDEX.""")
@cli_util.option('--display-name', help=u"""A filter to return resources that match the given display name.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The maximum number of results per page, or items to return in a paginated \"List\" call. For information on how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The displayName sort order is case-sensitive.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "timeCreated", "timeUpdated"]), help=u"""The field to sort by. You can provide one \"sortBy\" value. The default order for displayName, timeCreated and timeUpdated is ascending. The displayName sort by is case-sensitive.""")
@cli_util.option('--options-group', help=u"""A filter to return OPTIONS resources that match the given group.""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tag-equals': {'module': 'apm_config', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'apm_config', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'apm_config', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'apm_config', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tag-equals': {'module': 'apm_config', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'apm_config', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'apm_config', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'apm_config', 'class': 'list[string]'}}, output_type={'module': 'apm_config', 'class': 'ConfigCollection'})
@cli_util.wrap_exceptions
def list_configs(ctx, from_json, all_pages, page_size, apm_domain_id, config_type, display_name, limit, page, sort_order, sort_by, options_group, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if config_type is not None:
        kwargs['config_type'] = config_type
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
    if options_group is not None:
        kwargs['options_group'] = options_group
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_config', 'config', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_configs,
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_configs,
            limit,
            page_size,
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    else:
        result = client.list_configs(
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@metric_group_group.command(name=cli_util.override('apm_config.retrieve_namespace_metrics.command_name', 'retrieve-namespace-metrics'), help=u"""Returns all metrics associated with the specified namespace. \n[Command Reference](retrieveNamespaceMetrics)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@cli_util.option('--name', required=True, help=u"""Name of the namespace.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_config', 'class': 'NamespaceMetricCollection'})
@cli_util.wrap_exceptions
def retrieve_namespace_metrics(ctx, from_json, apm_domain_id, name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name

    client = cli_util.build_client('apm_config', 'config', ctx)
    result = client.retrieve_namespace_metrics(
        apm_domain_id=apm_domain_id,
        retrieve_namespace_metrics_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@metric_group_group.command(name=cli_util.override('apm_config.retrieve_namespaces.command_name', 'retrieve-namespaces'), help=u"""Returns all namespaces available in APM. \n[Command Reference](retrieveNamespaces)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_config', 'class': 'NamespaceCollection'})
@cli_util.wrap_exceptions
def retrieve_namespaces(ctx, from_json, apm_domain_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_config', 'config', ctx)
    result = client.retrieve_namespaces(
        apm_domain_id=apm_domain_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@config_group.command(name=cli_util.override('apm_config.update_config.command_name', 'update'), help=u"""Updates the details of the configuration item identified by the OCID. \n[Command Reference](updateConfig)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@cli_util.option('--config-id', required=True, help=u"""The [OCID] of the configuration item.""")
@cli_util.option('--config-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SPAN_FILTER", "METRIC_GROUP", "APDEX", "OPTIONS"]), help=u"""The type of configuration item.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--opc-dry-run', help=u"""Indicates that the request is a dry run, if set to \"true\". A dry run request does not modify the configuration item details and is used only to perform validation on the submitted data.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_config', 'class': 'Config'})
@cli_util.wrap_exceptions
def update_config(ctx, from_json, force, apm_domain_id, config_id, config_type, freeform_tags, defined_tags, if_match, opc_dry_run):

    if isinstance(config_id, six.string_types) and len(config_id.strip()) == 0:
        raise click.UsageError('Parameter --config-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if opc_dry_run is not None:
        kwargs['opc_dry_run'] = opc_dry_run
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configType'] = config_type

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('apm_config', 'config', ctx)
    result = client.update_config(
        apm_domain_id=apm_domain_id,
        config_id=config_id,
        update_config_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@config_group.command(name=cli_util.override('apm_config.update_config_update_metric_group_details.command_name', 'update-config-update-metric-group-details'), help=u"""Updates the details of the configuration item identified by the OCID. \n[Command Reference](updateConfig)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@cli_util.option('--config-id', required=True, help=u"""The [OCID] of the configuration item.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The name by which a configuration entity is displayed to the end user.""")
@cli_util.option('--filter-id', help=u"""The [OCID] of a Span Filter. The filterId is mandatory for the creation of MetricGroups. A filterId is generated when a Span Filter is created.""")
@cli_util.option('--namespace', help=u"""The namespace to which the metrics are published. It must be one of several predefined namespaces.""")
@cli_util.option('--dimensions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of dimensions for the metric. This variable should not be used.

This option is a JSON list with items of type Dimension.  For documentation on Dimension please see our API reference: https://docs.cloud.oracle.com/api/#/en/config/20210201/datatypes/Dimension.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metrics', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of metrics in this group.

This option is a JSON list with items of type Metric.  For documentation on Metric please see our API reference: https://docs.cloud.oracle.com/api/#/en/config/20210201/datatypes/Metric.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--opc-dry-run', help=u"""Indicates that the request is a dry run, if set to \"true\". A dry run request does not modify the configuration item details and is used only to perform validation on the submitted data.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}, 'dimensions': {'module': 'apm_config', 'class': 'list[Dimension]'}, 'metrics': {'module': 'apm_config', 'class': 'list[Metric]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}, 'dimensions': {'module': 'apm_config', 'class': 'list[Dimension]'}, 'metrics': {'module': 'apm_config', 'class': 'list[Metric]'}}, output_type={'module': 'apm_config', 'class': 'Config'})
@cli_util.wrap_exceptions
def update_config_update_metric_group_details(ctx, from_json, force, apm_domain_id, config_id, freeform_tags, defined_tags, display_name, filter_id, namespace, dimensions, metrics, if_match, opc_dry_run):

    if isinstance(config_id, six.string_types) and len(config_id.strip()) == 0:
        raise click.UsageError('Parameter --config-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or dimensions or metrics:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and dimensions and metrics will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if opc_dry_run is not None:
        kwargs['opc_dry_run'] = opc_dry_run
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if filter_id is not None:
        _details['filterId'] = filter_id

    if namespace is not None:
        _details['namespace'] = namespace

    if dimensions is not None:
        _details['dimensions'] = cli_util.parse_json_parameter("dimensions", dimensions)

    if metrics is not None:
        _details['metrics'] = cli_util.parse_json_parameter("metrics", metrics)

    _details['configType'] = 'METRIC_GROUP'

    client = cli_util.build_client('apm_config', 'config', ctx)
    result = client.update_config(
        apm_domain_id=apm_domain_id,
        config_id=config_id,
        update_config_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@config_group.command(name=cli_util.override('apm_config.update_config_update_apdex_rules_details.command_name', 'update-config-update-apdex-rules-details'), help=u"""Updates the details of the configuration item identified by the OCID. \n[Command Reference](updateConfig)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@cli_util.option('--config-id', required=True, help=u"""The [OCID] of the configuration item.""")
@cli_util.option('--rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The name by which a configuration entity is displayed to the end user.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--opc-dry-run', help=u"""Indicates that the request is a dry run, if set to \"true\". A dry run request does not modify the configuration item details and is used only to perform validation on the submitted data.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}, 'rules': {'module': 'apm_config', 'class': 'list[Apdex]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}, 'rules': {'module': 'apm_config', 'class': 'list[Apdex]'}}, output_type={'module': 'apm_config', 'class': 'Config'})
@cli_util.wrap_exceptions
def update_config_update_apdex_rules_details(ctx, from_json, force, apm_domain_id, config_id, rules, freeform_tags, defined_tags, display_name, if_match, opc_dry_run):

    if isinstance(config_id, six.string_types) and len(config_id.strip()) == 0:
        raise click.UsageError('Parameter --config-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or rules:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if opc_dry_run is not None:
        kwargs['opc_dry_run'] = opc_dry_run
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['rules'] = cli_util.parse_json_parameter("rules", rules)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    _details['configType'] = 'APDEX'

    client = cli_util.build_client('apm_config', 'config', ctx)
    result = client.update_config(
        apm_domain_id=apm_domain_id,
        config_id=config_id,
        update_config_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@config_group.command(name=cli_util.override('apm_config.update_config_update_span_filter_details.command_name', 'update-config-update-span-filter-details'), help=u"""Updates the details of the configuration item identified by the OCID. \n[Command Reference](updateConfig)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@cli_util.option('--config-id', required=True, help=u"""The [OCID] of the configuration item.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The name by which a configuration entity is displayed to the end user.""")
@cli_util.option('--filter-text', help=u"""The string that defines the Span Filter expression.""")
@cli_util.option('--description', help=u"""An optional string that describes what the filter is intended or used for.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--opc-dry-run', help=u"""Indicates that the request is a dry run, if set to \"true\". A dry run request does not modify the configuration item details and is used only to perform validation on the submitted data.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_config', 'class': 'Config'})
@cli_util.wrap_exceptions
def update_config_update_span_filter_details(ctx, from_json, force, apm_domain_id, config_id, freeform_tags, defined_tags, display_name, filter_text, description, if_match, opc_dry_run):

    if isinstance(config_id, six.string_types) and len(config_id.strip()) == 0:
        raise click.UsageError('Parameter --config-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if opc_dry_run is not None:
        kwargs['opc_dry_run'] = opc_dry_run
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if filter_text is not None:
        _details['filterText'] = filter_text

    if description is not None:
        _details['description'] = description

    _details['configType'] = 'SPAN_FILTER'

    client = cli_util.build_client('apm_config', 'config', ctx)
    result = client.update_config(
        apm_domain_id=apm_domain_id,
        config_id=config_id,
        update_config_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@config_group.command(name=cli_util.override('apm_config.update_config_update_options_details.command_name', 'update-config-update-options-details'), help=u"""Updates the details of the configuration item identified by the OCID. \n[Command Reference](updateConfig)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@cli_util.option('--config-id', required=True, help=u"""The [OCID] of the configuration item.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The name by which a configuration entity is displayed to the end user.""")
@cli_util.option('--options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The options are stored here as JSON.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--group', help=u"""A string that specifies the group that an OPTIONS item belongs to.""")
@cli_util.option('--description', help=u"""An optional string that describes what the options are intended or used for.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--opc-dry-run', help=u"""Indicates that the request is a dry run, if set to \"true\". A dry run request does not modify the configuration item details and is used only to perform validation on the submitted data.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}, 'options': {'module': 'apm_config', 'class': 'object'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'apm_config', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_config', 'class': 'dict(str, dict(str, object))'}, 'options': {'module': 'apm_config', 'class': 'object'}}, output_type={'module': 'apm_config', 'class': 'Config'})
@cli_util.wrap_exceptions
def update_config_update_options_details(ctx, from_json, force, apm_domain_id, config_id, freeform_tags, defined_tags, display_name, options, group, description, if_match, opc_dry_run):

    if isinstance(config_id, six.string_types) and len(config_id.strip()) == 0:
        raise click.UsageError('Parameter --config-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or options:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and options will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if opc_dry_run is not None:
        kwargs['opc_dry_run'] = opc_dry_run
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if options is not None:
        _details['options'] = cli_util.parse_json_parameter("options", options)

    if group is not None:
        _details['group'] = group

    if description is not None:
        _details['description'] = description

    _details['configType'] = 'OPTIONS'

    client = cli_util.build_client('apm_config', 'config', ctx)
    result = client.update_config(
        apm_domain_id=apm_domain_id,
        config_id=config_id,
        update_config_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@span_filter_group.command(name=cli_util.override('apm_config.validate_span_filter_pattern.command_name', 'validate-span-filter-pattern'), help=u"""Validates the Span Filter pattern (filterText) for syntactic correctness. Returns 204 on success, 422 when validation fails. \n[Command Reference](validateSpanFilterPattern)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID the request is intended for.""")
@cli_util.option('--filter-text', required=True, help=u"""The string that defines the Span Filter expression.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def validate_span_filter_pattern(ctx, from_json, apm_domain_id, filter_text):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['filterText'] = filter_text

    client = cli_util.build_client('apm_config', 'config', ctx)
    result = client.validate_span_filter_pattern(
        apm_domain_id=apm_domain_id,
        validate_span_filter_pattern_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
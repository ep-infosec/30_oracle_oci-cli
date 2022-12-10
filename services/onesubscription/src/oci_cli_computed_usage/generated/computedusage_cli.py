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
from services.onesubscription.src.oci_cli_onesubscription.generated import onesubscription_service_cli


@click.command(cli_util.override('computed_usage.computed_usage_root_group.command_name', 'computed-usage'), cls=CommandGroupWithAlias, help=cli_util.override('computed_usage.computed_usage_root_group.help', """OneSubscription APIs"""), short_help=cli_util.override('computed_usage.computed_usage_root_group.short_help', """OneSubscription APIs"""))
@cli_util.help_option_group
def computed_usage_root_group():
    pass


@click.command(cli_util.override('computed_usage.aggregated_computed_usage_summary_group.command_name', 'aggregated-computed-usage-summary'), cls=CommandGroupWithAlias, help="""Subscribed Service Contract details""")
@cli_util.help_option_group
def aggregated_computed_usage_summary_group():
    pass


@click.command(cli_util.override('computed_usage.computed_usage_group.command_name', 'computed-usage'), cls=CommandGroupWithAlias, help="""Computed Usage Summary object""")
@cli_util.help_option_group
def computed_usage_group():
    pass


onesubscription_service_cli.onesubscription_service_group.add_command(computed_usage_root_group)
computed_usage_root_group.add_command(aggregated_computed_usage_summary_group)
computed_usage_root_group.add_command(computed_usage_group)


@computed_usage_group.command(name=cli_util.override('computed_usage.get_computed_usage.command_name', 'get'), help=u"""This is an API which returns Computed Usage corresponding to the id passed \n[Command Reference](getComputedUsage)""")
@cli_util.option('--computed-usage-id', required=True, help=u"""The Computed Usage Id""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the root compartment.""")
@cli_util.option('--fields', multiple=True, help=u"""Partial response refers to an optimization technique offered by the RESTful web APIs to return only the information (fields) required by the client. This parameter is used to control what fields to return.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'onesubscription', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'onesubscription', 'class': 'list[string]'}}, output_type={'module': 'onesubscription', 'class': 'ComputedUsage'})
@cli_util.wrap_exceptions
def get_computed_usage(ctx, from_json, computed_usage_id, compartment_id, fields):

    if isinstance(computed_usage_id, six.string_types) and len(computed_usage_id.strip()) == 0:
        raise click.UsageError('Parameter --computed-usage-id cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('onesubscription', 'computed_usage', ctx)
    result = client.get_computed_usage(
        computed_usage_id=computed_usage_id,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@aggregated_computed_usage_summary_group.command(name=cli_util.override('computed_usage.list_aggregated_computed_usages.command_name', 'list-aggregated-computed-usages'), help=u"""This is a collection API which returns a list of aggregated computed usage details (there can be multiple Parent Products under a given SubID each of which is represented under Subscription Service Line # in SPM). \n[Command Reference](listAggregatedComputedUsages)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the root compartment.""")
@cli_util.option('--subscription-id', required=True, help=u"""Subscription Id is an identifier associated to the service used for filter the Computed Usage in SPM.""")
@cli_util.option('--time-from', required=True, type=custom_types.CLI_DATETIME, help=u"""Initial date to filter Computed Usage data in SPM. In the case of non aggregated data the time period between of fromDate and toDate , expressed in RFC 3339 timestamp format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-to', required=True, type=custom_types.CLI_DATETIME, help=u"""Final date to filter Computed Usage data in SPM, expressed in RFC 3339 timestamp format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--parent-product', help=u"""Product part number for subscribed service line, called parent product.""")
@cli_util.option('--grouping', type=custom_types.CliCaseInsensitiveChoice(["HOURLY", "DAILY", "MONTHLY", "NONE"]), help=u"""Grouping criteria to use for aggregate the computed Usage, either hourly (`HOURLY`), daily (`DAILY`), monthly(`MONTHLY`) or none (`NONE`) to not follow a grouping criteria by date.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number aggregatedComputedUsages of items to return within the Subscription \"List\" call, this counts the overall count across all items Example: `500`""")
@cli_util.option('--page', help=u"""The value of the 'opc-next-page' response header from the previous \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'onesubscription', 'class': 'list[AggregatedComputedUsageSummary]'})
@cli_util.wrap_exceptions
def list_aggregated_computed_usages(ctx, from_json, all_pages, page_size, compartment_id, subscription_id, time_from, time_to, parent_product, grouping, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if parent_product is not None:
        kwargs['parent_product'] = parent_product
    if grouping is not None:
        kwargs['grouping'] = grouping
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('onesubscription', 'computed_usage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_aggregated_computed_usages,
            compartment_id=compartment_id,
            subscription_id=subscription_id,
            time_from=time_from,
            time_to=time_to,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_aggregated_computed_usages,
            limit,
            page_size,
            compartment_id=compartment_id,
            subscription_id=subscription_id,
            time_from=time_from,
            time_to=time_to,
            **kwargs
        )
    else:
        result = client.list_aggregated_computed_usages(
            compartment_id=compartment_id,
            subscription_id=subscription_id,
            time_from=time_from,
            time_to=time_to,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@computed_usage_group.command(name=cli_util.override('computed_usage.list_computed_usages.command_name', 'list'), help=u"""This is a collection API which returns a list of Computed Usages for given filters. \n[Command Reference](listComputedUsages)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the root compartment.""")
@cli_util.option('--subscription-id', required=True, help=u"""Subscription Id is an identifier associated to the service used for filter the Computed Usage in SPM.""")
@cli_util.option('--time-from', required=True, type=custom_types.CLI_DATETIME, help=u"""Initial date to filter Computed Usage data in SPM. In the case of non aggregated data the time period between of fromDate and toDate , expressed in RFC 3339 timestamp format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-to', required=True, type=custom_types.CLI_DATETIME, help=u"""Final date to filter Computed Usage data in SPM, expressed in RFC 3339 timestamp format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--parent-product', help=u"""Product part number for subscribed service line, called parent product.""")
@cli_util.option('--computed-product', help=u"""Product part number for Computed Usage .""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call. Default: (`50`)

Example: '500'""")
@cli_util.option('--page', help=u"""The value of the 'opc-next-page' response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending ('ASC') or descending ('DESC').""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeOfArrival", "timeMeteredOn"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'onesubscription', 'class': 'list[ComputedUsageSummary]'})
@cli_util.wrap_exceptions
def list_computed_usages(ctx, from_json, all_pages, page_size, compartment_id, subscription_id, time_from, time_to, parent_product, computed_product, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if parent_product is not None:
        kwargs['parent_product'] = parent_product
    if computed_product is not None:
        kwargs['computed_product'] = computed_product
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('onesubscription', 'computed_usage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_computed_usages,
            compartment_id=compartment_id,
            subscription_id=subscription_id,
            time_from=time_from,
            time_to=time_to,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_computed_usages,
            limit,
            page_size,
            compartment_id=compartment_id,
            subscription_id=subscription_id,
            time_from=time_from,
            time_to=time_to,
            **kwargs
        )
    else:
        result = client.list_computed_usages(
            compartment_id=compartment_id,
            subscription_id=subscription_id,
            time_from=time_from,
            time_to=time_to,
            **kwargs
        )
    cli_util.render_response(result, ctx)
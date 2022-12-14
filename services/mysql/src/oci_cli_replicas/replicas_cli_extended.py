# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.mysql.src.oci_cli_replicas.generated import replicas_cli
from services.mysql.src.oci_cli_mysql.generated import mysql_service_cli

# oci mysql replicas replica -> oci mysql replica
mysql_service_cli.mysql_service_group.commands.pop(replicas_cli.replicas_root_group.name)
mysql_service_cli.mysql_service_group.add_command(replicas_cli.replica_group)

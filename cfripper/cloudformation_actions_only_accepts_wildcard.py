CLOUDFORMATION_ACTIONS_ONLY_ACCEPTS_WILDCARD = [
    "batch:CancelJob",
    "batch:DescribeComputeEnvironments",
    "batch:DescribeJobDefinitions",
    "batch:DescribeJobQueues",
    "batch:DescribeJobs",
    "batch:ListJobs",
    "batch:TerminateJob",
    "cloudformation:CreateStackSet",
    "cloudformation:CreateUploadBucket",
    "cloudformation:DeregisterType",
    "cloudformation:DescribeAccountLimits",
    "cloudformation:DescribeStackDriftDetectionStatus",
    "cloudformation:DescribeType",
    "cloudformation:DescribeTypeRegistration",
    "cloudformation:EstimateTemplateCost",
    "cloudformation:ListExports",
    "cloudformation:ListImports",
    "cloudformation:ListStacks",
    "cloudformation:ListTypeRegistrations",
    "cloudformation:ListTypeVersions",
    "cloudformation:ListTypes",
    "cloudformation:RegisterType",
    "cloudformation:SetTypeDefaultVersion",
    "cloudformation:ValidateTemplate",
    "cloudwatch:DeleteAnomalyDetector",
    "cloudwatch:DescribeAlarmsForMetric",
    "cloudwatch:DescribeAnomalyDetectors",
    "cloudwatch:DescribeInsightRules",
    "cloudwatch:GetMetricData",
    "cloudwatch:GetMetricStatistics",
    "cloudwatch:GetMetricWidgetImage",
    "cloudwatch:ListDashboards",
    "cloudwatch:ListMetrics",
    "cloudwatch:PutAnomalyDetector",
    "cloudwatch:PutMetricData",
    "dynamodb:ListTables",
    "ec2:AcceptReservedInstancesExchangeQuote",
    "ec2:AdvertiseByoipCidr",
    "ec2:AllocateAddress",
    "ec2:AssignIpv6Addresses",
    "ec2:AssignPrivateIpAddresses",
    "ec2:AssociateAddress",
    "ec2:AssociateDhcpOptions",
    "ec2:AssociateRouteTable",
    "ec2:AssociateSubnetCidrBlock",
    "ec2:AssociateVpcCidrBlock",
    "ec2:AttachInternetGateway",
    "ec2:AttachNetworkInterface",
    "ec2:AttachVpnGateway",
    "ec2:BundleInstance",
    "ec2:CancelBundleTask",
    "ec2:CancelConversionTask",
    "ec2:CancelExportTask",
    "ec2:CancelImportTask",
    "ec2:CancelReservedInstancesListing",
    "ec2:CancelSpotFleetRequests",
    "ec2:CancelSpotInstanceRequests",
    "ec2:ConfirmProductInstance",
    "ec2:CopyFpgaImage",
    "ec2:CopyImage",
    "ec2:CreateCustomerGateway",
    "ec2:CreateDefaultSubnet",
    "ec2:CreateDefaultVpc",
    "ec2:CreateImage",
    "ec2:CreateNetworkInterface",  # It shouldn't be here AWS Support Case: 7344470691
    "ec2:CreateNetworkAclEntry",
    "ec2:CreateReservedInstancesListing",
    "ec2:CreateRouteTable",
    "ec2:CreateSpotDatafeedSubscription",
    "ec2:CreateVpcEndpointConnectionNotification",
    "ec2:CreateVpnConnectionRoute",
    "ec2:CreateVpnGateway",
    "ec2:DeleteEgressOnlyInternetGateway",
    "ec2:DeleteFleets",
    "ec2:DeleteFpgaImage",
    "ec2:DeleteKeyPair",
    "ec2:DeleteNatGateway",
    "ec2:DeleteNetworkInterface",
    "ec2:DeleteNetworkInterfacePermission",
    "ec2:DeletePlacementGroup",
    "ec2:DeleteSpotDatafeedSubscription",
    "ec2:DeleteSubnet",
    "ec2:DeleteVpc",
    "ec2:DeleteVpcEndpointConnectionNotifications",
    "ec2:DeleteVpnConnection",
    "ec2:DeleteVpnConnectionRoute",
    "ec2:DeleteVpnGateway",
    "ec2:DeprovisionByoipCidr",
    "ec2:DeregisterImage",
    "ec2:DeregisterInstanceEventNotificationAttributes",
    "ec2:DescribeAccountAttributes",
    "ec2:DescribeAddresses",
    "ec2:DescribeAggregateIdFormat",
    "ec2:DescribeAvailabilityZones",
    "ec2:DescribeBundleTasks",
    "ec2:DescribeByoipCidrs",
    "ec2:DescribeCapacityReservations",
    "ec2:DescribeClassicLinkInstances",
    "ec2:DescribeClientVpnAuthorizationRules",
    "ec2:DescribeClientVpnConnections",
    "ec2:DescribeClientVpnEndpoints",
    "ec2:DescribeClientVpnRoutes",
    "ec2:DescribeClientVpnTargetNetworks",
    "ec2:DescribeCoipPools",
    "ec2:DescribeConversionTasks",
    "ec2:DescribeCustomerGateways",
    "ec2:DescribeDhcpOptions",
    "ec2:DescribeEgressOnlyInternetGateways",
    "ec2:DescribeElasticGpus",
    "ec2:DescribeExportImageTasks",
    "ec2:DescribeExportTasks",
    "ec2:DescribeFastSnapshotRestores",
    "ec2:DescribeFleetHistory",
    "ec2:DescribeFleetInstances",
    "ec2:DescribeFleets",
    "ec2:DescribeFlowLogs",
    "ec2:DescribeFpgaImageAttribute",
    "ec2:DescribeFpgaImages",
    "ec2:DescribeHostReservationOfferings",
    "ec2:DescribeHostReservations",
    "ec2:DescribeHosts",
    "ec2:DescribeIamInstanceProfileAssociations",
    "ec2:DescribeIdFormat",
    "ec2:DescribeIdentityIdFormat",
    "ec2:DescribeImageAttribute",
    "ec2:DescribeImages",
    "ec2:DescribeImportImageTasks",
    "ec2:DescribeImportSnapshotTasks",
    "ec2:DescribeInstanceAttribute",
    "ec2:DescribeInstanceCreditSpecifications",
    "ec2:DescribeInstanceEventNotificationAttributes",
    "ec2:DescribeInstanceStatus",
    "ec2:DescribeInstanceTypeOfferings",
    "ec2:DescribeInstanceTypes",
    "ec2:DescribeInstances",
    "ec2:DescribeInternetGateways",
    "ec2:DescribeKeyPairs",
    "ec2:DescribeLaunchTemplateVersions",
    "ec2:DescribeLaunchTemplates",
    "ec2:DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations",
    "ec2:DescribeLocalGatewayRouteTableVpcAssociations",
    "ec2:DescribeLocalGatewayRouteTables",
    "ec2:DescribeLocalGatewayVirtualInterfaceGroups",
    "ec2:DescribeLocalGatewayVirtualInterfaces",
    "ec2:DescribeLocalGateways",
    "ec2:DescribeManagedPrefixLists",
    "ec2:DescribeMovingAddresses",
    "ec2:DescribeNatGateways",
    "ec2:DescribeNetworkAcls",
    "ec2:DescribeNetworkInterfaceAttribute",
    "ec2:DescribeNetworkInterfacePermissions",
    "ec2:DescribeNetworkInterfaces",
    "ec2:DescribePlacementGroups",
    "ec2:DescribePrefixLists",
    "ec2:DescribePrincipalIdFormat",
    "ec2:DescribePublicIpv4Pools",
    "ec2:DescribeRegions",
    "ec2:DescribeReservedInstances",
    "ec2:DescribeReservedInstancesListings",
    "ec2:DescribeReservedInstancesModifications",
    "ec2:DescribeReservedInstancesOfferings",
    "ec2:DescribeRouteTables",
    "ec2:DescribeScheduledInstanceAvailability",
    "ec2:DescribeScheduledInstances",
    "ec2:DescribeSecurityGroupReferences",
    "ec2:DescribeSecurityGroups",
    "ec2:DescribeSnapshotAttribute",
    "ec2:DescribeSnapshots",
    "ec2:DescribeSpotDatafeedSubscription",
    "ec2:DescribeSpotFleetInstances",
    "ec2:DescribeSpotFleetRequestHistory",
    "ec2:DescribeSpotFleetRequests",
    "ec2:DescribeSpotInstanceRequests",
    "ec2:DescribeSpotPriceHistory",
    "ec2:DescribeStaleSecurityGroups",
    "ec2:DescribeSubnets",
    "ec2:DescribeTags",
    "ec2:DescribeTrafficMirrorFilters",
    "ec2:DescribeTrafficMirrorSessions",
    "ec2:DescribeTrafficMirrorTargets",
    "ec2:DescribeTransitGatewayAttachments",
    "ec2:DescribeTransitGatewayMulticastDomains",
    "ec2:DescribeTransitGatewayPeeringAttachments",
    "ec2:DescribeTransitGatewayRouteTables",
    "ec2:DescribeTransitGatewayVpcAttachments",
    "ec2:DescribeTransitGateways",
    "ec2:DescribeVolumeAttribute",
    "ec2:DescribeVolumeStatus",
    "ec2:DescribeVolumes",
    "ec2:DescribeVolumesModifications",
    "ec2:DescribeVpcAttribute",
    "ec2:DescribeVpcClassicLink",
    "ec2:DescribeVpcClassicLinkDnsSupport",
    "ec2:DescribeVpcEndpointConnectionNotifications",
    "ec2:DescribeVpcEndpointConnections",
    "ec2:DescribeVpcEndpointServiceConfigurations",
    "ec2:DescribeVpcEndpointServicePermissions",
    "ec2:DescribeVpcEndpointServices",
    "ec2:DescribeVpcEndpoints",
    "ec2:DescribeVpcPeeringConnections",
    "ec2:DescribeVpcs",
    "ec2:DescribeVpnConnections",
    "ec2:DescribeVpnGateways",
    "ec2:DetachInternetGateway",
    "ec2:DetachNetworkInterface",
    "ec2:DetachVpnGateway",
    "ec2:DisableEbsEncryptionByDefault",
    "ec2:DisableVgwRoutePropagation",
    "ec2:DisableVpcClassicLinkDnsSupport",
    "ec2:DisassociateAddress",
    "ec2:DisassociateRouteTable",
    "ec2:DisassociateSubnetCidrBlock",
    "ec2:DisassociateVpcCidrBlock",
    "ec2:EnableEbsEncryptionByDefault",
    "ec2:EnableVgwRoutePropagation",
    "ec2:EnableVolumeIO",
    "ec2:EnableVpcClassicLinkDnsSupport",
    "ec2:ExportClientVpnClientCertificateRevocationList",
    "ec2:ExportClientVpnClientConfiguration",
    "ec2:ExportImage",
    "ec2:ExportTransitGatewayRoutes",
    "ec2:GetCapacityReservationUsage",
    "ec2:GetCoipPoolUsage",
    "ec2:GetConsoleOutput",
    "ec2:GetDefaultCreditSpecification",
    "ec2:GetEbsDefaultKmsKeyId",
    "ec2:GetEbsEncryptionByDefault",
    "ec2:GetHostReservationPurchasePreview",
    "ec2:GetLaunchTemplateData",
    "ec2:GetManagedPrefixListAssociations",
    "ec2:GetManagedPrefixListEntries",
    "ec2:GetPasswordData",
    "ec2:GetReservedInstancesExchangeQuote",
    "ec2:GetTransitGatewayAttachmentPropagations",
    "ec2:GetTransitGatewayMulticastDomainAssociations",
    "ec2:GetTransitGatewayRouteTableAssociations",
    "ec2:GetTransitGatewayRouteTablePropagations",
    "ec2:ImportImage",
    "ec2:ImportInstance",
    "ec2:ImportKeyPair",
    "ec2:ImportSnapshot",
    "ec2:ImportVolume",
    "ec2:ModifyDefaultCreditSpecification",
    "ec2:ModifyEbsDefaultKmsKeyId",
    "ec2:ModifyFleet",
    "ec2:ModifyFpgaImageAttribute",
    "ec2:ModifyHosts",
    "ec2:ModifyIdFormat",
    "ec2:ModifyIdentityIdFormat",
    "ec2:ModifyImageAttribute",
    "ec2:ModifyInstanceAttribute",
    "ec2:ModifyInstanceCapacityReservationAttributes",
    "ec2:ModifyInstanceMetadataOptions",
    "ec2:ModifyInstancePlacement",
    "ec2:ModifyNetworkInterfaceAttribute",
    "ec2:ModifyReservedInstances",
    "ec2:ModifySpotFleetRequest",
    "ec2:ModifySubnetAttribute",
    "ec2:ModifyVolume",
    "ec2:ModifyVolumeAttribute",
    "ec2:ModifyVpcAttribute",
    "ec2:ModifyVpcEndpointConnectionNotification",
    "ec2:ModifyVpcPeeringConnectionOptions",
    "ec2:ModifyVpcTenancy",
    "ec2:ModifyVpnTunnelCertificate",
    "ec2:MonitorInstances",
    "ec2:MoveAddressToVpc",
    "ec2:ProvisionByoipCidr",
    "ec2:PurchaseHostReservation",
    "ec2:PurchaseReservedInstancesOffering",
    "ec2:PurchaseScheduledInstances",
    "ec2:RegisterImage",
    "ec2:RegisterInstanceEventNotificationAttributes",
    "ec2:ReleaseAddress",
    "ec2:ReleaseHosts",
    "ec2:ReplaceNetworkAclAssociation",
    "ec2:ReplaceNetworkAclEntry",
    "ec2:ReplaceRouteTableAssociation",
    "ec2:ReportInstanceStatus",
    "ec2:RequestSpotFleet",
    "ec2:RequestSpotInstances",
    "ec2:ResetEbsDefaultKmsKeyId",
    "ec2:ResetFpgaImageAttribute",
    "ec2:ResetImageAttribute",
    "ec2:ResetInstanceAttribute",
    "ec2:ResetNetworkInterfaceAttribute",
    "ec2:ResetSnapshotAttribute",
    "ec2:RestoreAddressToClassic",
    "ec2:RunScheduledInstances",
    "ec2:SearchLocalGatewayRoutes",
    "ec2:SearchTransitGatewayMulticastGroups",
    "ec2:SearchTransitGatewayRoutes",
    "ec2:UnassignIpv6Addresses",
    "ec2:UnassignPrivateIpAddresses",
    "ec2:UnmonitorInstances",
    "ec2:WithdrawByoipCidr",
    "ecr:GetAuthorizationToken",
    "ecs:CreateCapacityProvider",
    "ecs:CreateCluster",
    "ecs:CreateTaskSet",
    "ecs:DeleteAccountSetting",
    "ecs:DeregisterTaskDefinition",
    "ecs:DescribeTaskDefinition",
    "ecs:DiscoverPollEndpoint",
    "ecs:ListAccountSettings",
    "ecs:ListClusters",
    "ecs:ListServices",
    "ecs:ListTaskDefinitionFamilies",
    "ecs:ListTaskDefinitions",
    "ecs:PutAccountSetting",
    "ecs:PutAccountSettingDefault",
    "elasticbeanstalk:CheckDNSAvailability",
    "elasticbeanstalk:CreateStorageLocation",
    "elasticbeanstalk:DescribeAccountAttributes",
    "elasticbeanstalk:ListPlatformBranches",
    "elasticache:DescribeCacheEngineVersions",
    "elasticache:DescribeEngineDefaultParameters",
    "elasticache:DescribeEvents",
    "elasticache:DescribeReservedCacheNodesOfferings",
    "elasticache:DescribeServiceUpdates",
    "elasticache:RevokeCacheSecurityGroupIngress",
    "elasticloadbalancing:DescribeAccountLimits",
    "elasticloadbalancing:DescribeListenerCertificates",
    "elasticloadbalancing:DescribeListeners",
    "elasticloadbalancing:DescribeLoadBalancerAttributes",
    "elasticloadbalancing:DescribeLoadBalancerPolicies",
    "elasticloadbalancing:DescribeLoadBalancerPolicyTypes",
    "elasticloadbalancing:DescribeLoadBalancers",
    "elasticloadbalancing:DescribeRules",
    "elasticloadbalancing:DescribeSSLPolicies",
    "elasticloadbalancing:DescribeTags",
    "elasticloadbalancing:DescribeTargetGroupAttributes",
    "elasticloadbalancing:DescribeTargetGroups",
    "elasticloadbalancing:DescribeTargetHealth",
    "elasticloadbalancing:SetWebAcl",
    "es:AcceptInboundCrossClusterSearchConnection",
    "es:CreateElasticsearchServiceRole",
    "es:DeleteElasticsearchServiceRole",
    "es:DeleteInboundCrossClusterSearchConnection",
    "es:DeleteOutboundCrossClusterSearchConnection",
    "es:DescribeElasticsearchInstanceTypeLimits",
    "es:DescribeInboundCrossClusterSearchConnections",
    "es:DescribeOutboundCrossClusterSearchConnections",
    "es:DescribeReservedElasticsearchInstanceOfferings",
    "es:DescribeReservedElasticsearchInstances",
    "es:ListDomainNames",
    "es:ListElasticsearchInstanceTypeDetails",
    "es:ListElasticsearchInstanceTypes",
    "es:ListElasticsearchVersions",
    "es:PurchaseReservedElasticsearchInstanceOffering",
    "es:RejectInboundCrossClusterSearchConnection",
    "events:ListEventBuses",
    "events:ListEventSources",
    "events:ListPartnerEventSources",
    "events:ListRuleNamesByTarget",
    "events:ListRules",
    "events:PutPartnerEvents",
    "events:PutPermission",
    "events:RemovePermission",
    "events:TestEventPattern",
    "events:UntagResource",
    "iam:CreateAccountAlias",
    "iam:DeleteAccountAlias",
    "iam:DeleteAccountPasswordPolicy",
    "iam:GenerateCredentialReport",
    "iam:GenerateServiceLastAccessedDetails",
    "iam:GetAccountAuthorizationDetails",
    "iam:GetAccountPasswordPolicy",
    "iam:GetAccountSummary",
    "iam:GetContextKeysForCustomPolicy",
    "iam:GetCredentialReport",
    "iam:GetOrganizationsAccessReport",
    "iam:GetServiceLastAccessedDetails",
    "iam:GetServiceLastAccessedDetailsWithEntities",
    "iam:ListAccountAliases",
    "iam:ListGroups",
    "iam:ListOpenIDConnectProviders",
    "iam:ListPolicies",
    "iam:ListPoliciesGrantingServiceAccess",
    "iam:ListRoles",
    "iam:ListSAMLProviders",
    "iam:ListServerCertificates",
    "iam:ListUsers",
    "iam:ListVirtualMFADevices",
    "iam:SetSecurityTokenServicePreferences",
    "iam:SimulateCustomPolicy",
    "iam:UpdateAccountPasswordPolicy",
    "iot:CreateCertificateFromCsr",
    "iot:CreateKeysAndCertificate",
    "iot:CreatePolicy",
    "iot:DeleteRegistrationCode",
    "iot:DescribeEndpoint",
    "iot:GetLoggingOptions",
    "iot:GetRegistrationCode",
    "iot:ListCACertificates",
    "iot:ListCertificates",
    "iot:ListCertificatesByCA",
    "iot:ListOutgoingCertificates",
    "iot:ListPolicies",
    "iot:ListThingTypes",
    "iot:ListThings",
    "iot:ListTopicRules",
    "iot:RegisterCACertificate",
    "iot:RegisterCertificate",
    "lambda:CreateEventSourceMapping",
    "lambda:GetAccountSettings",
    "lambda:ListEventSourceMappings",
    "lambda:ListFunctions",
    "lambda:ListLayerVersions",
    "lambda:ListLayers",
    "rds:CancelExportTask",
    "rds:CreateDBProxy",
    "rds:DescribeAccountAttributes",
    "rds:DescribeCertificates",
    "rds:DescribeDBClusterEndpoints",
    "rds:DescribeDBClusterSnapshots",
    "rds:DescribeDBInstanceAutomatedBackups",
    "rds:DescribeDBInstances",
    "rds:DescribeEngineDefaultClusterParameters",
    "rds:DescribeEngineDefaultParameters",
    "rds:DescribeEventCategories",
    "rds:DescribeEvents",
    "rds:DescribeExportTasks",
    "rds:DescribeGlobalClusters",
    "rds:DescribeOrderableDBInstanceOptions",
    "rds:DescribeReservedDBInstancesOfferings",
    "rds:DescribeSourceRegions",
    "rds:StartExportTask",
    "route53:CreateHostedZone",
    "route53:CreateReusableDelegationSet",
    "route53:CreateTrafficPolicy",
    "route53:CreateTrafficPolicyInstance",
    "route53:CreateTrafficPolicyVersion",
    "route53:CreateVPCAssociationAuthorization",
    "route53:DeleteHostedZone",
    "route53:DeleteReusableDelegationSet",
    "route53:DeleteTrafficPolicy",
    "route53:DeleteTrafficPolicyInstance",
    "route53:DeleteVPCAssociationAuthorization",
    "route53:GetAccountLimit",
    "route53:GetChange",
    "route53:GetCheckerIpRanges",
    "route53:GetHealthCheckCount",
    "route53:GetHostedZone",
    "route53:GetHostedZoneCount",
    "route53:GetHostedZoneLimit",
    "route53:GetReusableDelegationSet",
    "route53:GetReusableDelegationSetLimit",
    "route53:GetTrafficPolicy",
    "route53:GetTrafficPolicyInstance",
    "route53:GetTrafficPolicyInstanceCount",
    "route53:ListHealthChecks",
    "route53:ListHostedZones",
    "route53:ListHostedZonesByName",
    "route53:ListReusableDelegationSets",
    "route53:ListTrafficPolicies",
    "route53:ListTrafficPolicyInstances",
    "route53:ListTrafficPolicyInstancesByHostedZone",
    "route53:ListTrafficPolicyInstancesByPolicy",
    "route53:ListTrafficPolicyVersions",
    "route53:UpdateHostedZoneComment",
    "route53:UpdateTrafficPolicyComment",
    "route53:UpdateTrafficPolicyInstance",
    "route53domains:CheckDomainAvailability",
    "route53domains:DeleteTagsForDomain",
    "route53domains:DisableDomainAutoRenew",
    "route53domains:DisableDomainTransferLock",
    "route53domains:EnableDomainAutoRenew",
    "route53domains:EnableDomainTransferLock",
    "route53domains:GetContactReachabilityStatus",
    "route53domains:GetDomainDetail",
    "route53domains:GetDomainSuggestions",
    "route53domains:GetOperationDetail",
    "route53domains:ListDomains",
    "route53domains:ListOperations",
    "route53domains:ListTagsForDomain",
    "route53domains:RegisterDomain",
    "route53domains:RenewDomain",
    "route53domains:ResendContactReachabilityEmail",
    "route53domains:RetrieveDomainAuthCode",
    "route53domains:TransferDomain",
    "route53domains:UpdateDomainContact",
    "route53domains:UpdateDomainContactPrivacy",
    "route53domains:UpdateDomainNameservers",
    "route53domains:UpdateTagsForDomain",
    "route53domains:ViewBilling",
    "s3:CreateJob",
    "s3:GetAccessPoint",
    "s3:GetAccountPublicAccessBlock",
    "s3:ListAccessPoints",
    "s3:ListAllMyBuckets",
    "s3:ListJobs",
    "s3:PutAccountPublicAccessBlock",
    "sns:CheckIfPhoneNumberIsOptedOut",
    "sns:CreatePlatformApplication",
    "sns:CreatePlatformEndpoint",
    "sns:DeleteEndpoint",
    "sns:DeletePlatformApplication",
    "sns:GetEndpointAttributes",
    "sns:GetPlatformApplicationAttributes",
    "sns:GetSMSAttributes",
    "sns:GetSubscriptionAttributes",
    "sns:ListEndpointsByPlatformApplication",
    "sns:ListPhoneNumbersOptedOut",
    "sns:ListPlatformApplications",
    "sns:ListSubscriptions",
    "sns:ListTopics",
    "sns:OptInPhoneNumber",
    "sns:SetEndpointAttributes",
    "sns:SetPlatformApplicationAttributes",
    "sns:SetSMSAttributes",
    "sns:SetSubscriptionAttributes",
    "sns:Unsubscribe",
    "xray:BatchGetTraces",
    "xray:GetEncryptionConfig",
    "xray:GetGroups",
    "xray:GetInsight",
    "xray:GetInsightEvents",
    "xray:GetInsightImpactGraph",
    "xray:GetInsightSummaries",
    "xray:GetSamplingRules",
    "xray:GetSamplingStatisticSummaries",
    "xray:GetSamplingTargets",
    "xray:GetServiceGraph",
    "xray:GetTimeSeriesServiceStatistics",
    "xray:GetTraceGraph",
    "xray:GetTraceSummaries",
    "xray:PutEncryptionConfig",
    "xray:PutTelemetryRecords",
    "xray:PutTraceSegments",
    "xray:PutTraceSegments",
    "xray:PutTraceSegments",
]

"""
Copyright 2018-2019 Skyscanner Ltd

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
from cfripper.rules.cloudformation_authentication import *  # noqa
from cfripper.rules.cross_account_trust import *  # noqa
from cfripper.rules.ebs_volume_has_sse import *  # noqa
from cfripper.rules.hardcoded_RDS_password import *  # noqa
from cfripper.rules.iam_managed_policy_wildcard_action import *  # noqa
from cfripper.rules.iam_roles import *  # noqa
from cfripper.rules.kms_key_wildcard_principal import *  # noqa
from cfripper.rules.managed_policy_on_user import *  # noqa
from cfripper.rules.policy_on_user import *  # noqa
from cfripper.rules.privilege_escalation import *  # noqa
from cfripper.rules.s3_bucked_policy import *  # noqa
from cfripper.rules.s3_public_access import *  # noqa
from cfripper.rules.security_group import *  # noqa
from cfripper.rules.sns_topic_policy_not_principal import *  # noqa
from cfripper.rules.sqs_queue_policy import *  # noqa
from cfripper.rules.wildcard_principals import *  # noqa

DEFAULT_RULES = {
    "IAMRolesOverprivilegedRule": IAMRolesOverprivilegedRule,
    "SecurityGroupOpenToWorldRule": SecurityGroupOpenToWorldRule,
    "S3BucketPublicReadWriteAclRule": S3BucketPublicReadWriteAclRule,
    "SecurityGroupIngressOpenToWorld": SecurityGroupIngressOpenToWorld,
    "ManagedPolicyOnUserRule": ManagedPolicyOnUserRule,
    "PolicyOnUserRule": PolicyOnUserRule,
    "SNSTopicPolicyNotPrincipalRule": SNSTopicPolicyNotPrincipalRule,
    "SQSQueuePolicyNotPrincipalRule": SQSQueuePolicyNotPrincipalRule,
    "S3BucketPolicyPrincipalRule": S3BucketPolicyPrincipalRule,
    "EBSVolumeHasSSERule": EBSVolumeHasSSERule,
    "PrivilegeEscalationRule": PrivilegeEscalationRule,
    "CrossAccountTrustRule": CrossAccountTrustRule,
    "S3BucketPublicReadAclAndListStatementRule": S3BucketPublicReadAclAndListStatementRule,
    "SQSQueuePolicyPublicRule": SQSQueuePolicyPublicRule,
    "S3CrossAccountTrustRule": S3CrossAccountTrustRule,
    "HardcodedRDSPasswordRule": HardcodedRDSPasswordRule,
    "KMSKeyWildcardPrincipal": KMSKeyWildcardPrincipal,
    "FullWildcardPrincipal": FullWildcardPrincipalRule,
    "PartialWildcardPrincipal": PartialWildcardPrincipalRule,
}

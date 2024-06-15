from os import environ as env
from typing import Optional

from boto3.session import Session


class AwsSession(Session):
    def __init__(
        self,
        aws_secret_access_key: Optional[str] = None,
        botocore_session: Optional[Session] = None,
        profile_name: Optional[str] = None,
    ) -> None:
        super().__init__(
            aws_secret_access_key=aws_secret_access_key,
            botocore_session=botocore_session,
            profile_name=profile_name,
        )

        self.resource = self.resource(
            service_name="s3",
            region_name="us-east-1",
            use_ssl=False,
            verify=False,
        )


s3 = AwsSession(aws_secret_access_key=env.get("AWS_SECRET_ACCESS_KEY", ""))

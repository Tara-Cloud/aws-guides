#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_static_website.cdk_static_website_stack import CdkStaticWebsiteStack


app = cdk.App()
CdkStaticWebsiteStack(app, "cdk-static-website")

app.synth()

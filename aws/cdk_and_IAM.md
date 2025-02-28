### permissions around CDK

#### my issue
- I added S3 bucket policy for limiting bucket policy to update itself. (adding role)
- And then deploy it by aws cdk with the added role, but it failed.
- This is why the role used for deployment by cdk is cdk execution role, which is created by cdk bootstrap.
- So, I should have added permission for S3 bucket policy to cdk execution role.

#### What permissions should we apply?
##### white list (allowing list)
- anti pattern
- It's hard to recognize what permissions cloudFormation needs when deploying.

##### set guard rails
- many companies take this way.
- developer can do everything except for the actions banned. 

##### Allowing creation of IAM Roles without privilege escalation
- more flexible and make development fast, etc...
- the CDK will automatically create roles and provision them with least-privilege permissions
- It's a very hard to try to replace these roles created automatically with manually created ones.
- To avoid privilege escalation, there are altanative ways, "Permissions Boundary" and "SCP"
- By attaching a Permissions Boundary to the developer’s Roles you are limiting both the actions the developer can perform directly, as well as the actions that can be performed by any Roles they create. SCPs allow you to restrict actions for every user and role in an AWS account
  

###### my hypothesis
- Basically, to avoid easy privilege excalation, the IAM roles to execute cloudformation (deploy) is created automatically?


##### my summary
・It's better to allow CDK to create role because it create roles with the least privileges.  
・If your company won't allow to create such roles in order to prevent privilege escalation, you can use Permission Boundaries.

### reference
https://github.com/aws/aws-cdk/wiki/Security-And-Safety-Dev-Guide
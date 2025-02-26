### permissions around CDK

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
## AWS ECR
### how to login (using authorization token)
get password with "get-login-password" command like below

``` shell
aws ecr get-login-password --region region-xxx
```
pass the token to docker cli

``` shell
aws ecr get-login-password --region region-xxx | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com
```
#### appendix
 - To use --password-stdin option prevent the password from remaining in the shell and its history.


reference
1: https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html
2: https://docs.docker.com/reference/cli/docker/login/
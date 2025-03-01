import pulumi
from pulumi_digitalocean import do

# Create a DigitalOcean resource (Domain)
domain = do.Domain("my-domain",
    name='my-domain.io')

# Export the name of the domain
pulumi.export('domain_name',  domain.name)

# Python Docker client

## About

Some testing code to play with Docker Python API before trying to work it into Dagster

## References

* Portainer   https://docs.portainer.io/api/examples
* Docker API:  https://docs.docker.com/engine/api/
* Docker docs for create:  https://docs.docker.com/engine/api/v1.41/#tag/Container/operation/ContainerCreate 

``` 
Error: Database is uninitialized and superuser password is not specified.
       You must specify POSTGRES_PASSWORD to a non-empty value for the
       superuser. For example, "-e POSTGRES_PASSWORD=password" on "docker run".
       You may also use "POSTGRES_HOST_AUTH_METHOD=trust" to allow all
       connections without a password. This is *not* recommended.
       See PostgreSQL documentation about "trust":
       https://www.postgresql.org/docs/current/auth-trust.html
```
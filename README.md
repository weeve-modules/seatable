# SeaTable

|                |                                       |
| -------------- | ------------------------------------- |
| Name           | SeaTable                           |
| Version        | v1.0.0                                |
| DockerHub | [weevenetwork/seatable](https://hub.docker.com/r/weevenetwork/seatable) |
| authors        | Jakub Grzelak                    |

- [SeaTable](#seatable)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

Write single or batch of data to a selected SeaTable base and table. **IMPORTANT: Make sure that data labels match column names in the selected SeaTable table.**

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                 | Environment Variables     | type     | Description                                              |
| -------------------- | ------------------------- | -------- | -------------------------------------------------------- |
| API Token    | API_TOKEN         | string  | API token to a selected SeaTable base.            |
| Data Table    | TABLE         | string  | Table in SeaTable where data will be written.            |


### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)  |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
seatable-api
```

## Input

Input to this module is:

* JSON body single object, example:

```json
{
   "temperature": 12,
   "device": "Konin-1"
}
```

* batch of JSON body objects, example:

```json
[
    {
        "temperature": 12,
        "device": "Konin-1"
    },
    {
        "temperature": 15,
        "device": "Konin-1"
    }
]
```

## Output

New records written to a selected TABLE in SeaTable.

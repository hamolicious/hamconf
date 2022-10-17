
## Data Types

| Datatype | Representation |
| -------- | -------------- |
| integer | int |
| floating point  | float |
| string | str |
| boolean | bool |
| json | json |
| array | arr |

## Comments
You can use comments (`//`) anywhere in the file
```
single_value [float] = 3.14 // comment on the line
// comment alone on a line
```

## Arrays
To create an array of any type, use the syntax:
```
single_value [float] = 3.14
some_array [arr float] = [0.1, 0.2, 0.3]
```

## Environment Variables
You can read environment variables from the config file and convert their type
```
float_contents_of_env_var [float] = ${SOME_ENV_VAR}
```


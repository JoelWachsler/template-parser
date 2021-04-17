# Template parser

Simple Jinja2 wrapper written in Python for parsing configuration files.

## Example usage

The following example assumes there is a file in the current directory named hello.txt.j2 with the following content
```
Hello {{ variable }}
```

To parse the configuration, first build the image and tag it
```bash
docker build . -t template-parser
```

Then run it
```bash
docker run \
  # This file should be parsed
  -e TEMPLATE_FILE=hello.txt.j2 \
  # With this variable substituted
  -e T_MY_VARIABLE=world! \
  -v $PWD/hello.txt.j2:/root/hello.txt.j2 \
  --rm template-parser 
```

The following text should be printed to stdout
```bash
Hello world!
```

For more more Jinja2 templating, then please refer to their documenation [here](https://jinja.palletsprojects.com/en/2.11.x/).
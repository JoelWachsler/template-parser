import os
from jinja2 import Template
from pathlib import Path

# Assuming all variables to capture starts with this prefix.
# These variables will be available in the template with- and without the prefix.
VARIABLE_PREFIX = 'T_'

def main():
    template_file = Path(os.environ.get('TEMPLATE_FILE'))
    if not template_file.exists():
        raise Exception(f'{template_file} does not exist!')

    template = Template(template_file.read_text())
    variables = {}
    for env_key in os.environ:
        if env_key.startswith(VARIABLE_PREFIX):
            env_value = os.environ.get(env_key)
            # Add both variants - the user should decide which one to use
            variables[env_key.removeprefix(VARIABLE_PREFIX)] = env_value
            variables[env_key] = env_value
    print(template.render(variables))

if __name__ == "__main__":
    main()

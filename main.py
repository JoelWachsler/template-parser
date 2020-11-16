from jinja2 import Template
from pathlib import Path
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description='Parses a jinja2 template file')
    parser.add_argument('template_file', help='Template file to parse')
    parser.add_argument('-e', nargs=2, action='append', help='Variable to pass to the template')
    args = parser.parse_args()

    template_file = Path(args.template_file)
    if not template_file.exists():
        raise Exception(f'{template_file} does not exist!')

    template = Template(template_file.read_text())
    print(template.render(dict(args.e)))

if __name__ == "__main__":
    main()

import tomllib


class DocumentConfig:

    def __init__(self, file: str):
        with open(file, "rb") as f:
            self.config = tomllib.load(f)

    def get_margin(self, side: str):
        return self.config['document']['margins'][side]

    def get_cell(self, cell_type: str):
        return self.config['document']['cells'][cell_type]

    def get_style(self, style_type: str):
        return self.config['document']['styles'][style_type]


if __name__ == '__main__':
    d = DocumentConfig('./config.toml')
    print(d.get_margin('line_end'))
    print(d.get_cell('standard'))
    print(d.get_style('name'))

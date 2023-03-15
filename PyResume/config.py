import tomllib
from fpdf import FPDF
from fortmatting import get_contact_info

with open("config.toml", "rb") as f:
    config = tomllib.load(f)


class Resume(FPDF):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.set_margins(config['document']['page']['margin'], config['document']['page']['margin'],
                         config['document']['page']['margin'])
        self.add_page()

    def jump_y(self, distance: float):
        self.set_y(self.get_y() + distance)

    def jump_x(self, distance: float):
        self.set_x(self.get_x() + distance)

    def divider_line(self):
        self.jump_y(1)
        self.line(20, self.get_y(), config['document']['page']['line_end'], self.get_y())
        self.jump_y(1)

    def write_name(self, person: dict):
        self.set_font(**config['document']['styles']['name'])
        self.cell(h=14, txt=person['name'], **config['document']['cells']['standard'])

    def write_contact(self, person: dict):
        self.set_font(**config['document']['styles']['body'])
        self.cell(h=8, txt=get_contact_info(person), **config['document']['cells']['standard'])

    def write_section_title(self, title: str):
        self.set_font(**config['document']['styles']['title'])
        self.cell(h=8, txt=title, **config['document']['cells']['standard'])
        self.divider_line()

    def write_body(self, text: str):
        self.set_font(**config['document']['styles']['body'])
        self.multi_cell(h=6, txt=text, **config['document']['cells']['multi'])

    def write_two_column_body(self, info: dict):
        self.set_font(**config['document']['styles']['emphasis'])
        self.cell(h=6, txt=info['name'], **config['document']['cells']['left'])
        self.cell(h=6, txt=info['years'], **config['document']['cells']['right'])
        self.set_font(**config['document']['styles']['body'])
        self.multi_cell(h=6, txt=f'{info["accomplishment"]}', **config['document']['cells']['multi'])
        self.jump_y(4)

    def write_list_body(self, string: str):
        self.set_font(**config['document']['styles']['body'])
        self.multi_cell(h=8, txt=f'{string}', **config['document']['cells']['multi'])

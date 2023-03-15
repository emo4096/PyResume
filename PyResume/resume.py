from fpdf import FPDF

from configuration import DocumentConfig
from fortmatting import get_contact_info


class Resume(FPDF):
    def __init__(self, config: DocumentConfig):
        super().__init__()
        self.config = config
        self.set_margins(self.config.get_margin('margin'), self.config.get_margin('margin'),
                         self.config.get_margin('margin'))
        self.add_page()

    def jump_y(self, distance: float):
        self.set_y(self.get_y() + distance)

    def jump_x(self, distance: float):
        self.set_x(self.get_x() + distance)

    def divider_line(self):
        self.jump_y(1)
        self.line(20, self.get_y(), self.config.get_margin('line_end'), self.get_y())
        self.jump_y(1)

    def write_name(self, person: dict):
        self.set_font(**self.config.get_style('name'))
        self.cell(h=14, txt=person['name'], **self.config.get_cell('standard'))

    def write_contact(self, person: dict):
        self.set_font(**self.config.get_style('body'))
        self.cell(h=8, txt=get_contact_info(person), **self.config.get_cell('standard'))

    def write_section_title(self, title: str):
        self.set_font(**self.config.get_style('title'))
        self.cell(h=8, txt=title, **self.config.get_cell('standard'))
        self.divider_line()

    def write_body(self, text: str):
        self.set_font(**self.config.get_style('body'))
        self.multi_cell(h=6, txt=text, **self.config.get_cell('multi'))

    def write_two_column_body(self, info: dict):
        self.set_font(**self.config.get_style('emphasis'))
        self.cell(h=6, txt=info['name'], **self.config.get_cell('left'))
        self.cell(h=6, txt=info['years'], **self.config.get_cell('right'))
        self.set_font(**self.config.get_style('body'))
        self.multi_cell(h=6, txt=f'{info["accomplishment"]}', **self.config.get_cell('multi'))
        self.jump_y(4)

    def write_list_body(self, string: str):
        self.set_font(**self.config.get_style('body'))
        self.multi_cell(h=8, txt=f'{string}', **self.config.get_cell('multi'))

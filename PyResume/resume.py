from fpdf import FPDF
from fortmatting import get_contact_info

MARGIN = 20

LINE_END = 190

BORDER = 0

CELL_ARGS = {'w': 0,
             'border': BORDER,
             'align': 'L'}

LEFT_COLUMN_CELL_ARGS = {'w': 120,
                         'border': BORDER,
                         'align': 'L'}

RIGHT_COLUMN_CELL_ARGS = {'w': 50,
                          'border': BORDER,
                          'align': 'R'}

NAME_STYLE = {'family': 'Times',
              'style': 'B',
              'size': 28}

BODY_STYLE = {'family': 'Times',
              'style': '',
              'size': 12}

TITLE_STYLE = {'family': 'Times',
               'style': 'B',
               'size': 18}

EMPHASIS_STYLE = {'family': 'Times',
                  'style': 'B',
                  'size': 12}


class Resume(FPDF):
    def __init__(self):
        super().__init__()
        self.set_margins(MARGIN, MARGIN, MARGIN)
        self.add_page()

    def jump_y(self, distance: float):
        self.set_y(self.get_y() + distance)

    def jump_x(self, distance: float):
        self.set_x(self.get_x() + distance)

    def divider_line(self):
        self.jump_y(1)
        self.line(20, self.get_y(), LINE_END, self.get_y())
        self.jump_y(1)

    def write_name(self, person: dict):
        self.set_font(**NAME_STYLE)
        self.cell(h=14, txt=person['name'], ln=1, **CELL_ARGS)

    def write_contact(self, person: dict):
        self.set_font(**BODY_STYLE)
        self.cell(h=8, txt=get_contact_info(person), ln=1, **CELL_ARGS)

    def write_section_title(self, title: str):
        self.set_font(**TITLE_STYLE)
        self.cell(h=8, txt=title, ln=1, **CELL_ARGS)
        self.divider_line()

    def write_body(self, text: str):
        self.set_font(**BODY_STYLE)
        self.multi_cell(h=6, txt=text, **CELL_ARGS)

    def write_two_column_body(self, info: dict):
        self.set_font(**EMPHASIS_STYLE)
        self.cell(h=6, txt=info['name'], ln=0, **LEFT_COLUMN_CELL_ARGS)
        self.cell(h=6, txt=info['years'], ln=1, **RIGHT_COLUMN_CELL_ARGS)
        self.set_font(**BODY_STYLE)
        self.multi_cell(h=6, txt=f'{info["accomplishment"]}', **CELL_ARGS)
        self.jump_y(4)

    def write_list_body(self, string: str):
        self.set_font(**BODY_STYLE)
        self.multi_cell(h=8, txt=f'{string}', **CELL_ARGS)

from config import Resume
import tomllib

PERSON = {"name": "Shaq O'Neal",
          "location": "Los Angeles, CA",
          "phone": "(123) - 456 - 7890",
          "email": "diesel@shaqattack.com"}

SUMMARY = '    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

EDUCATION = [{'name': 'Louisiana State University',
              'accomplishment': '- B.S. Computer Science',
              'years': 'Fall 1989 - Spring 1992'},

             {'name': 'Cole High School',
              'accomplishment': '- High School Diploma',
              'years': 'Fall 1985 - Spring 1989'}]

EXPERIENCE = [{'name': 'Self-employed - Recording Artist',
               'accomplishment': '- Released numerous studio albums.\n'
                                 '- Performed multiple worldwide tours.\n'
                                 '- Possibly the top baketball playing rapper of all time.',
               'years': '1993 - Present'},

              {'name': 'Orlando Magic - NBA Center',
               'accomplishment': '- Won lots of games with the franchise.\n'
                                 '- Garnered attention around the league in first season.\n'
                                 '- Dunked on just about every big in the league.',
               'years': '1992 - 1996'}]

SKILLS = ('- Excel\n'
          '- Python\n'
          '- Fantasy football\n'
          '- Conflict resolution\n'
          '- Drone piloting\n'
          '- Underwater basket weaving')

with open("config.toml", "rb") as f:
    config = tomllib.load(f)


document = Resume(config)

document.write_name(PERSON)
document.write_contact(PERSON)
document.jump_y(2)

document.write_section_title('Summary')
document.write_body(SUMMARY)
document.jump_y(2)

document.write_section_title('Education')
for school in EDUCATION:
    document.write_two_column_body(school)
document.jump_y(2)

document.write_section_title('Experience')
for job in EXPERIENCE:
    document.write_two_column_body(job)
document.jump_y(2)

document.write_section_title('Skills')
document.write_list_body(SKILLS)

document.output('../output/test_resume.pdf')

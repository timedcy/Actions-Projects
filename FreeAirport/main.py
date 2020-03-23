import datetime

from jinja2 import FileSystemLoader,Environment

from providers import test


def generate_md(source, date, ssr_link):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('base.md')
    with open('README.md', 'w+', encoding='utf-8') as fout:
        md_content = template.render(source=source, date=date, ssr_link=ssr_link)
        fout.write(md_content)




if __name__ == "__main__":
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    generate_md("ssr", date=date, ssr_link=test.thessr())

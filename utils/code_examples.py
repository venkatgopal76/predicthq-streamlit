from pathlib import Path
from typing import Iterable

def get_code_example(filename):
    # Render the readme as markdown using st.markdown.
    txt = Path(f"docs/code_examples/{filename}.md").read_text()
    # st.markdown(txt)
    return txt

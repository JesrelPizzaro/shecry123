# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import inspect
import textwrap
import streamlit as st

def show_code(func):
    """Show the source code of a given Python function."""
    show_code_checkbox = st.sidebar.checkbox("Show code", True)
    if show_code_checkbox:
        # Show the code of the function.
        st.markdown("## Code")
        source_lines, _ = inspect.getsourcelines(func)
        code = textwrap.dedent("".join(source_lines[1:]))
        st.code(code)

# Example usage:
def my_function():
    print("This is a sample function.")
    # Other code here...

if __name__ == "__main__":
    show_code(my_function)

LAB 7 - FUZZING FOR INPUT VALIDATION BUGS

IMPORTANT:
The supplied handout refers to processor.py and test_processor.py, but those source files were not included in the material provided. These files are a self-contained replacement exercise, not the lecturer's original assigned implementation. Confirm with your instructor whether this replacement is acceptable.

FILES:
- processor_buggy.py : intentionally buggy starter for demonstrating the initial application run
- processor.py       : fixed application to submit
- test_processor.py  : Hypothesis property-based tests to submit

RUN ON MAC / LINUX:
1. Open Terminal in this folder.
2. Create/activate a virtual environment if desired:
   python3 -m venv .venv
   source .venv/bin/activate
3. Install dependencies:
   python -m pip install hypothesis pytest
4. Demonstrate the original buggy app:
   python processor_buggy.py
5. To show failing fuzz tests against the buggy version, temporarily rename processor.py to processor_fixed.py, copy processor_buggy.py to processor.py, then run:
   python -m pytest -q test_processor.py
   (Expect failures; capture the terminal output.)
6. Restore the fixed processor.py supplied in this folder.
7. Run the fixed application:
   python processor.py
8. Run the tests:
   python -m pytest -q test_processor.py
   (All tests should pass.)

SUBMISSION:
Upload processor.py as the fixed application script and test_processor.py as the updated test code. Create a PDF containing genuine screenshots of the original run, failing tests, fixed application run, and passing tests.

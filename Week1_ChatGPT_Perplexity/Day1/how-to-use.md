# 1) Create & activate venv
python -m venv venv
# Windows: .\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 2) Install the stack
pip install -r requirements.txt

# 3) Sanity check your environment
python test_setup.py
# (This will also write test_plot_environment.html in your working dir)

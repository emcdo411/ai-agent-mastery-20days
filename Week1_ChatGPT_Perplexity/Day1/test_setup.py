"""
AI Model Mastery — Day 1 sanity check

Run:
    python test_setup.py
"""
import sys

def section(title: str):
    print("\n" + "="*80)
    print(title)
    print("="*80)

errors = []

# Python version
section("🧪 Python Version")
print(sys.version)

# Import checks + versions
section("🧪 Library Imports")
try:
    import pandas as pd
    import numpy as np
    import sklearn
    import plotly
    import fastapi
    import pydantic
    print("pandas:", pd.__version__)
    print("numpy:", np.__version__)
    print("scikit-learn:", sklearn.__version__)
    print("plotly:", plotly.__version__)
    print("fastapi:", fastapi.__version__)
    print("pydantic:", pydantic.__version__)
except Exception as e:
    errors.append(("imports", str(e)))

# Tiny ML fit/predict
section("🧪 Tiny scikit-learn model")
try:
    from sklearn.linear_model import LinearRegression
    import numpy as np

    X = np.array([[1.0],[2.0],[3.0],[4.0]])
    y = np.array([2.0, 4.1, 6.1, 8.2])
    model = LinearRegression().fit(X, y)
    pred = model.predict([[5.0]])[0]
    print("LinearRegression coef:", round(float(model.coef_[0]), 4))
    print("Prediction for x=5:", round(float(pred), 3))
except Exception as e:
    errors.append(("sklearn", str(e)))

# FastAPI app construct
section("🧪 FastAPI construct")
try:
    from fastapi import FastAPI
    app = FastAPI()

    @app.get("/health")
    def health():
        return {"status": "ok"}
    print("FastAPI app created with /health route ✅")
    print("Tip: run 'uvicorn app:app --reload' once you have an app.py")
except Exception as e:
    errors.append(("fastapi", str(e)))

# Plotly render
section("🧪 Plotly render (HTML)")
try:
    import plotly.express as px
    import pandas as pd
    df = pd.DataFrame({"x":[1,2,3,4], "y":[1,4,9,16]})
    fig = px.line(df, x="x", y="y", title="Environment Test Plot")
    out = "test_plot_environment.html"
    fig.write_html(out, include_plotlyjs="cdn")
    print(f"Wrote {out} ✅  (open in a browser)")
except Exception as e:
    errors.append(("plotly", str(e)))

# Summary
section("✅ Summary")
if not errors:
    print("Environment OK — all checks passed.")
else:
    print("Environment checks completed with issues:")
    for name, msg in errors:
        print(f" - {name}: {msg}")
    print("\nFix the above and re-run:  python test_setup.py")

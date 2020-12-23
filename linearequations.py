{"metadata":{"language_info":{"name":"python","version":"3.7.8","mimetype":"text/x-python","codemirror_mode":{"name":"ipython","version":3},"pygments_lexer":"ipython3","nbconvert_exporter":"python","file_extension":".py"},"kernelspec":{"name":"python3","display_name":"Python 3","language":"python"}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"code","source":"jupyter nbconvert --to script 'linearequations.py'\nf = open(\"nov09.txt\", \"r\")\nf.readline()\nf.readline()\n\nb = []\nwhile True:\n    try:\n        line = f.readline()\n        for a in line.split(\" \"):\n            b.append(float(a))\n    except (EOFError, ValueError):\n        break\nprint(\"COEFFICIENTS:\")\nprint(b)\nprint(\"---------------------------\")\n\nc = []\nwhile True:\n    try:\n        line = f.readline()\n        for a in line.split(\" \"):\n            c.append(float(a))\n    except (EOFError, ValueError):\n        break\nprint(\"RIGHT-HAND SIDE VALUES:\")        \nprint(c)\nprint(\"---------------------------\")\n\n\nimport numpy as np \nx = np.array([b[0:4], b[4:8], b[8:12], b[12:16]])\ny = np.array(c)\n\nz = np.linalg.solve(x,y)\nprint(\"SOLUTION:\")\nprint(z)\n","metadata":{},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"","metadata":{},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"","metadata":{},"execution_count":null,"outputs":[]}]}
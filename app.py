body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 40px;
    background-color: #f4f6f9;
    color: #333;
}

.container {
    max-width: 900px;
    margin: auto;
    background: white;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
}

h1 {
    color: #2c3e50;
    border-bottom: 2px solid #ecf0f1;
    padding-bottom: 15px;
}

h2 {
    color: #2980b9;
    margin-top: 30px;
}

h3 {
    color: #34495e;
}

p,
li {
    line-height: 1.6;
    font-size: 15px;
}

/* ✅ UPDATED: dynamic matrix grid (IMPORTANT CHANGE ONLY) */
.matrix-grid {
    display: grid;
    gap: 12px;
    margin: 20px 0;
}

/* input styling unchanged */
.matrix-grid input {
    width: 90px;
    height: 45px;
    text-align: center;
    font-size: 16px;
    border: 1px solid #bdc3c7;
    border-radius: 6px;
    background-color: #fafafa;
}

.matrix-grid input:focus {
    border-color: #3498db;
    outline: none;
    background-color: white;
}

button {
    padding: 12px 25px;
    font-size: 16px;
    font-weight: bold;
    background-color: #2ecc71;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    transition: background 0.2s;
}

button:hover {
    background-color: #27ae60;
}

.error {
    color: #721c24;
    background-color: #f8d7da;
    border-left: 5px solid #dc3545;
    padding: 15px;
    border-radius: 6px;
    margin-top: 20px;
}

.results-section {
    margin-top: 35px;
    background: #f8f9fa;
    padding: 25px;
    border-radius: 8px;
    border: 1px solid #e9ecef;
}

.example-box {
    padding: 20px;
    border-radius: 8px;
    margin-top: 20px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.02);
}

.ex1 {
    background: #fef9e7;
    border-left: 5px solid #f39c12;
}

.ex2 {
    background: #eaf2f8;
    border-left: 5px solid #2980b9;
}

.math-step {
    background: rgba(255,255,255,0.6);
    padding: 10px;
    border-radius: 4px;
    margin: 8px 0;
}

.step-heading {
    font-weight: bold;
    color: #2c3e50;
    margin-top: 15px;
    border-bottom: 1px dashed #ccc;
    padding-bottom: 4px;
}

.answer-box {
    background-color: #ebf5fb;
    border: 3px solid #2980b9;
    padding: 20px;
    border-radius: 8px;
    margin-top: 20px;
}

.apps-box {
    background-color: #f2f4f4;
    border-left: 5px solid #7f8c8d;
    padding: 15px;
    border-radius: 6px;
    margin-top: 15px;
}

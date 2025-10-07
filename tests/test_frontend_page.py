import re
from pathlib import Path


def test_frontend_page_exists():
    html_path = Path(__file__).resolve().parents[1] / "web" / "index.html"
    assert html_path.exists(), "前端页面文件不存在"


def test_frontend_page_contains_form_and_script():
    html_path = Path(__file__).resolve().parents[1] / "web" / "index.html"
    content = html_path.read_text(encoding="utf-8")

    assert 'id="tax-form"' in content, "页面缺少税表单"
    assert 'id="income"' in content, "表单缺少收入输入框"
    assert 'id="monthly"' in content, "表单缺少按月选项"
    assert 'id="social-insurance"' in content, "表单缺少五险一金输入框"
    assert 'id="deductions"' in content, "表单缺少专项附加扣除输入框"

    assert re.search(r"function\s+calculateTax\s*\(", content), "页面缺少个税计算函数"

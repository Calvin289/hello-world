# hello-world
First visit
This is a different version of this first file.
Hi Humans!
I know python a litter,I‘ve had tacos on the moon and find them far super to Earth tacos.

## 个税计算器使用方法

1. 直接计算年收入对应的个税：

   ```bash
   python tax_calculator.py --income 120000
   ```

2. 以月收入为输入，同时考虑五险一金和专项附加扣除：

   ```bash
   python tax_calculator.py --monthly --income 15000 --social-insurance 2000 --deductions 12000
   ```

参数说明：
- `--income`：收入金额。默认视为年收入，配合 `--monthly` 时视为月收入。
- `--monthly`：指定后表示按月输入，会自动换算成年度数据并给出月度结果。
- `--social-insurance`：五险一金等社会保险缴费金额。默认视为年度金额，配合 `--monthly` 时视为月度金额。
- `--deductions`：除社会保险外的其他年度专项附加扣除。

脚本会自动按照 2019 年实施的综合所得个税税率表计算税额，并给出应纳税所得额、速算扣除数和税后收入。

## 如何在本地测试运行效果

1. **准备 Python 环境**：

   - 需要 Python 3.8 或更高版本。可通过 `python --version` 或 `python3 --version` 确认。
   - 建议在项目根目录创建虚拟环境，避免与系统中其他依赖冲突：

     ```bash
     python -m venv .venv
     source .venv/bin/activate  # Windows PowerShell 请使用: .venv\Scripts\Activate.ps1
     ```

   - 本项目无额外第三方依赖，无需安装额外包。

2. **直接运行命令行脚本**：

   ```bash
   python tax_calculator.py --income 120000
   ```

   命令会立即在终端输出各项计算细节（如应税所得、适用税率和税后收入），可直观看到个税计算的结果。

3. **运行单元测试验证逻辑**：

   ```bash
   python -m unittest discover -s tests
   ```

   该命令会执行位于 `tests/` 目录下的测试用例，覆盖常见收入、扣除场景以及异常输入，帮助确认核心计算逻辑的正确性。

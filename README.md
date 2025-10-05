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

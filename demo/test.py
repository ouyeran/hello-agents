import re


test = """
Finish[2025年苹果最新手机是iPhone 17系列（包括iPhone 17、iPhone 17 Pro、iPhone 17 Pro Max）以及全新推出的iPhone Air。主要卖点包括：
- 起步存储容量提升至256GB；
- 提供五种配色：黑色、薰衣草紫色、青雾蓝色、鼠尾草绿等；
- 搭载A19芯片，采用第三代3纳米工艺；
- 配备迄今最出色的显示屏，支持最高120Hz ProMotion自适应刷新率，并采用超瓷晶面板2保护；
- iPhone 17为史上最薄设计；
- 初期AI功能未完全上线，需等待后续iOS更新；
- Pro和Pro Max版本分别配备6.3英寸与6.9英寸屏幕，采用横向大矩阵相机模组设计。]
"""

final_answer = re.match(r".*Finish\[(.*)\]", test, re.DOTALL)
result = final_answer.group(1)
print(f"🎉 最终答案: {result}")
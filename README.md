# ImageTextConverter
即开即用的批量图片转文字脚本

# 图片文字识别项目

该项目使用 EasyOCR 库对图片中的文字进行识别，并将识别出的文字保存到 `.txt` 文件中。支持中文（简体）和英文的文字识别。

## 功能

- 自动读取指定文件夹中的所有图片文件。
- 使用 OCR 技术提取图片中的文字。
- 识别结果将以 `.txt` 格式保存，文件名与原图片文件名相同。
- 处理过程中会显示每个文件的处理进度。

## 环境要求

- Python 3.8 或更高版本。
- 安装以下依赖库：`easyocr`、`Pillow`。

## 安装和使用

### 1. 克隆项目

```bash
git clone https://github.com/your-username/ocr-project.git
cd ocr-project
```

### 2. 创建虚拟环境（可选）

为了避免库冲突，建议使用虚拟环境：

```bash
python -m venv venv
source venv/bin/activate  # 在 Windows 上使用 venv\Scripts\activate
```

### 3. 安装依赖

使用 `requirements.txt` 安装所需的库：

```bash
pip install -r requirements.txt
```

### 4. 运行项目

运行脚本并输入包含图片的文件夹路径：

```bash
python main.py
```

程序会处理文件夹中的所有图片文件，并将每个文件的识别结果保存为 `.txt` 文件。

### 5. 输出

每个 `.txt` 文件将包含从对应图片中提取的文字。处理过程中，程序会打印当前处理的文件及其进度。

## 依赖

- easyocr: 用于 OCR 文字识别。
- Pillow: 用于处理图片文件。

## 示例

```bash
Processing the 1/5 file: image1.png
Processing the 2/5 file: image2.jpg
...
```

## 常见问题

- **识别结果乱码**：确保选择了正确的语言模型（如中文简体 `ch_sim`），并确保图片清晰。
- **权限问题**：确保程序有权限读取图片文件和写入 `.txt` 文件。




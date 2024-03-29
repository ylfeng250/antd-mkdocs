import re
import os
import shutil

# 提取 md 文件


def extract_md_file(src, dst):
    try:
        with open(src, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(content)
    except:
        print(f"Error extr")

# 提取 ts 文件


def extract_ts_file(src, dst):
    try:
        with open(src, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(dst, 'w', encoding='utf-8') as f:
            f.write('## interface\n\n')
            f.write('```tsx\n')
            f.write(content)
            f.write('```\n')
    except Exception as e:
        print(f"Error extracting {src}: {e}")

# 提取 demo 文件


def extract_demo_file(demo_name, src_tsx, src_md, dst):
    try:
        with open(src_tsx, 'r', encoding='utf-8') as f:
            tsx_content = f.read()
        with open(src_md, 'r', encoding='utf-8') as f:
            md_content = f.read()
        with open(dst, 'a', encoding='utf-8') as f:
            f.write('\n')
            f.write(f'## {demo_name[:-4]} demo')
            f.write('\n')
            f.write(f'>/demo/{demo_name}')
            f.write('\n')
            f.write(remove_language_tags(md_content))
            f.write('```tsx\n')
            f.write(tsx_content)
            f.write('```\n')
    except FileNotFoundError:
        print(f'File not found: {src_tsx} or {src_md}')

# 删除空目录


def delete_empty_directories(path):
    for root, dirs, files in os.walk(path, topdown=False):
        if not os.listdir(root):
            os.rmdir(root)
            print(f"Deleted directory: {root}")

# 删除 tag


def remove_language_tags(s):
    s = re.sub(r'## zh-CN', '', s)
    s = re.sub(r'## en-US', '', s)
    return s


def main():
    components_dir = '../components'  # 实际目录位置
    md_dir = 'md'
    shutil.rmtree(md_dir)
    for component_name in os.listdir(components_dir):
        component_dir = os.path.join(components_dir, component_name)
        if not os.path.isdir(component_dir):
            continue

        index_zh_CN_md = os.path.join(component_dir, 'index.zh-CN.md')
        antd_md_dir = os.path.join(md_dir)
        os.makedirs(antd_md_dir, exist_ok=True)
        api_md = os.path.join(antd_md_dir, f'{component_name}.md')
        extract_md_file(index_zh_CN_md, api_md)

        interface_ts = os.path.join(component_dir, 'interface.ts')
        if os.path.exists(interface_ts):
            extract_ts_file(interface_ts, api_md)

        demo_dir = os.path.join(component_dir, 'demo')
        if os.path.isdir(demo_dir):
            for demo_name in os.listdir(demo_dir):
                if demo_name.endswith('.tsx'):
                    demo_tsx = os.path.join(demo_dir, demo_name)
                    demo_md = os.path.join(demo_dir, demo_name[:-4] + '.md')
                    # demo_dst = os.path.join(
                    #     md_dir, component_name, f'demo-{demo_name[:-4]}.md')
                    # 直接在 api_md 后面追加 demo
                    extract_demo_file(demo_name, demo_tsx, demo_md, api_md)

    delete_empty_directories(md_dir)


if __name__ == '__main__':
    main()

## zh-CN

使用 `height` 属性则切换为虚拟滚动。

## en-US

Use virtual list through `height` prop.
```tsx
import React from 'react';
import { Tooltip, Tree } from 'antd';
import type { TreeDataNode } from 'antd';

const dig = (path = '0', level = 3) => {
  const list = [];
  for (let i = 0; i < 10; i += 1) {
    const key = `${path}-${i}`;
    const treeNode: TreeDataNode = {
      title: key,
      key,
    };

    if (level > 0) {
      treeNode.children = dig(key, level - 1);
    }

    list.push(treeNode);
  }
  return list;
};

const treeData = dig();

const MemoTooltip = Tooltip || React.memo(Tooltip);

const App: React.FC = () => (
  <Tree
    treeData={treeData}
    height={233}
    defaultExpandAll
    titleRender={(item) => <MemoTooltip title={item.title as any}>{item.title as any}</MemoTooltip>}
  />
);

export default App;
```

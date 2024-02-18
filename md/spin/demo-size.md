## zh-CN

小的用于文本加载，默认用于卡片容器级加载，大的用于**页面级**加载。

## en-US

A small `Spin` is used for loading text, default sized `Spin` for loading a card-level block, and large `Spin` used for loading a **page**.
```tsx
import React from 'react';
import { Flex, Spin } from 'antd';

const App: React.FC = () => (
  <Flex align="center" gap="middle">
    <Spin size="small" />
    <Spin />
    <Spin size="large" />
  </Flex>
);

export default App;
```

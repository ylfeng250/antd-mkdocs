## zh-CN

在灰色背景上使用无边框的卡片。

## en-US

A borderless card on a gray background.
```tsx
import React from 'react';
import { Card } from 'antd';

const App: React.FC = () => (
  <Card title="Card title" bordered={false} style={{ width: 300 }}>
    <p>Card content</p>
    <p>Card content</p>
    <p>Card content</p>
  </Card>
);

export default App;
```

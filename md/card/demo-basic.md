## zh-CN

包含标题、内容、操作区域。

## en-US

A basic card containing a title, content and an extra corner content. Supports two sizes: `default` and `small`.
```tsx
import React from 'react';
import { Card, Space } from 'antd';

const App: React.FC = () => (
  <Space direction="vertical" size={16}>
    <Card title="Default size card" extra={<a href="#">More</a>} style={{ width: 300 }}>
      <p>Card content</p>
      <p>Card content</p>
      <p>Card content</p>
    </Card>
    <Card size="small" title="Small size card" extra={<a href="#">More</a>} style={{ width: 300 }}>
      <p>Card content</p>
      <p>Card content</p>
      <p>Card content</p>
    </Card>
  </Space>
);

export default App;
```

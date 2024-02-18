## zh-CN

设置鼠标放在状态点上时显示的文字。

## en-US

The badge will display `title` when hovered over, instead of `count`.
```tsx
import React from 'react';
import { Avatar, Badge, Space } from 'antd';

const App: React.FC = () => (
  <Space size="large">
    <Badge count={5} title="Custom hover text">
      <Avatar shape="square" size="large" />
    </Badge>
    <Badge count={-5} title="Negative">
      <Avatar shape="square" size="large" />
    </Badge>
  </Space>
);

export default App;
```

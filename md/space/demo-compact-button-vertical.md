## zh-CN

垂直方向的紧凑布局，目前仅支持 Button 组合。

## en-US

Vertical Mode for Space.Compact, support Button only.
```tsx
import React from 'react';
import { Button, Space } from 'antd';

const App: React.FC = () => (
  <Space>
    <Space.Compact direction="vertical">
      <Button>Button 1</Button>
      <Button>Button 2</Button>
      <Button>Button 3</Button>
    </Space.Compact>
    <Space.Compact direction="vertical">
      <Button type="dashed">Button 1</Button>
      <Button type="dashed">Button 2</Button>
      <Button type="dashed">Button 3</Button>
    </Space.Compact>
    <Space.Compact direction="vertical">
      <Button type="primary">Button 1</Button>
      <Button type="primary">Button 2</Button>
      <Button type="primary">Button 3</Button>
    </Space.Compact>
  </Space>
);

export default App;
```

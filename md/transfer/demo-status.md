## zh-CN

使用 `status` 为 Transfer 添加状态，可选 `error` 或者 `warning`。

## en-US

Add status to Transfer with `status`, which could be `error` or `warning`.
```tsx
import React from 'react';
import { Space, Transfer } from 'antd';

const App: React.FC = () => (
  <Space direction="vertical">
    <Transfer status="error" />
    <Transfer status="warning" showSearch />
  </Space>
);

export default App;
```

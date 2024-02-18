## zh-CN

共有四种样式 `success`、`info`、`warning`、`error`。

## en-US

There are 4 types of Alert: `success`, `info`, `warning`, `error`.
```tsx
import React from 'react';
import { Alert, Space } from 'antd';

const App: React.FC = () => (
  <Space direction="vertical" style={{ width: '100%' }}>
    <Alert message="Success Text" type="success" />
    <Alert message="Info Text" type="info" />
    <Alert message="Warning Text" type="warning" />
    <Alert message="Error Text" type="error" />
  </Space>
);

export default App;
```

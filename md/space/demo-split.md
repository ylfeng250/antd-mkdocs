## zh-CN

相邻组件分隔符。

## en-US

Crowded components split.
```tsx
import React from 'react';
import { Divider, Space, Typography } from 'antd';

const App: React.FC = () => (
  <Space split={<Divider type="vertical" />}>
    <Typography.Link>Link</Typography.Link>
    <Typography.Link>Link</Typography.Link>
    <Typography.Link>Link</Typography.Link>
  </Space>
);

export default App;
```
